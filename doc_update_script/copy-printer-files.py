import os
import yaml
import requests
import re
import sys
from urllib.parse import urlparse

# Directories
script_dir = os.path.dirname(os.path.realpath(__file__))
config_file = os.path.join(script_dir, 'config.yaml')
website_dir = os.path.join(script_dir, '../website/src/content/docs/printers')

# Make sure the website directory exists
os.makedirs(website_dir, exist_ok=True)

#rewrite relative image paths to reference the github cdn instead
#this implementation is somewhat hacky with using regex to parse markdown
def rewrite_image_urls(text, url):
    #parse the url and find the base path
    url_obj = urlparse(url)
    base_url = f"{url_obj.scheme}://{url_obj.netloc}"
    base_path = os.path.dirname(url_obj.path)

    def regex_callback(match):
        img_url = match.group(1) or match.group(2)
        img_url_obj = urlparse(img_url)
        #if this is already an absolute url, just return the original match
        if img_url_obj.netloc:
            return match.group(0)
        #otherwise join the path of the image to the base path and return it
        new_path = os.path.join(base_path, img_url_obj.path)
        new_url = base_url + new_path
        return match.group(0).replace(img_url, new_url, 1)

    #this regex matches the urls inside markdown images and html image tags
    urls_regex = r"!\[.+?]\(<?(.+?)>?\)|<img.+?src=['\"](.+?)['\"].*?>"
    return re.sub(urls_regex, regex_callback, text)

# Function to download a markdown file and create metadata within the file
def download_and_create_metadata(url, title, description, project_name, file_name):
    # If file_name is provided in the config, use it; otherwise, use the basename of the URL
    if file_name:
        filename = file_name
    else:
        filename = os.path.basename(url)

    file_path = os.path.join(website_dir, filename)

    # Download the markdown file
    print(f"Downloading {filename} from {url}...")
    response = requests.get(url)
    if response.status_code == 200:
        # Create metadata to prepend to the file
        metadata = f"""---
title: "{title}"
description: "{description}"
project_name: "{project_name}"
repository: "{url}"
---
"""
        text = metadata + response.text
        text = rewrite_image_urls(text, url)

        # Write metadata + markdown content to the file
        with open(file_path, "w") as f:
            f.write(text)
        print(f"Downloaded {filename} to {file_path} with metadata")

    else:
        print(f"Failed to download {filename} from {url}. Status code: {response.status_code}")

# Parse the config.yaml file
def parse_config(config_file):
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    
    # Iterate over each project in the YAML file
    for project_name, project_info in config.items():
        title = project_info.get('title')
        description = project_info.get('description')
        repository = project_info.get('repository')
        file_name = project_info.get('file_name', None)  # Default to None if not provided

        if not file_name.endswith('.md'):
            print(f"Skipping project {project_name} due to invalid file name")
            continue
        if title and description and repository:
            download_and_create_metadata(repository, title, description, project_name, file_name)
        else:
            print(f"Skipping project {project_name} due to missing required fields")

# Main function to execute the script
def main():
    if not os.path.isfile(config_file):
        print(f"Error: {config_file} not found.")
        return
    
    parse_config(config_file)
    print("Finished processing printer files.")

if __name__ == '__main__':
    main()
