---
title: "Briefcase-printer"
description: "A bedslinger 3D printer disguised as a Briefcase"
project_name: "Briefcase Printer"
repository: "https://raw.githubusercontent.com/civilizayden/Briefcase-printer/refs/heads/main/JOURNAL.md"
---
Made by: @CiviliZayden
Repository link: https://github.com/civilizayden/Briefcase-printer
Total hours so far: 39

- [3/1/26] I have spent a couple of hours brainstorming what I wanted to do for Infill. I finally came up with this idea, and I have begun CAD work to get the idea into Fusion. I also started looking for parts and communicated with other Hack Clubbers to find out what would work, ultimately deciding that I can probably scrap an old MakerBot Replicator from my teacher for parts. (3 hours)
<img width="500" alt="image" src="https://github.com/user-attachments/assets/a524eb73-3797-4028-85d0-81ec3b08ea01" />  

- [3/3/26] I continued fiddling with the layout of the printer, and I think I have decided how I want it to go. I am laying out a footprint in Fusion and trying to make everything fit nicely. I have decided on linear rails for all axes and am now planning how to build it. (1 hour)
<img width="500" alt="image" src="https://github.com/user-attachments/assets/2f3b04ab-fa09-4a03-b98d-3e589f4ae78f" />
  

- [3/7/26] I worked on getting this into Fusion, figuring out spacing and rail sizes. Then Fusion crashed. I lost my work. At least I was writing down my measurements as I went so I could recreate what I had. Now I have a basic frame and am looking at what extruder to use. I am leaning toward the picolino. (2 hours)
<img width="500" alt="image" src="https://github.com/user-attachments/assets/65857724-db39-4e36-9dd5-520fd65470af" />
  

- [3/8/26] Today I sourced my 3D printers. I am getting some old MakerBot Replicator+ printers as well as a Replicator Z18 for free from my CAD teacher. I will also be designing the printer in class now instead of doing my classwork (approved by the teacher). Today I set up my document with the various components I would need, like the MGN12 rail/carriage and 2020 extrusion. I began setting up the Z-axis rail assembly as well. I will not be able to make too much progress until I have the printers in my possession and I can disassemble them to figure out what I have to work with. (1.5 hours)  

- [3/9/26] I spent a lot of time the past few days in class and at home figuring out what I want to do. I found a RepRap project called FoldaRap that I will be taking inspiration from. I have found sources for most of my parts and have a design in mind for the heated bed. It will be 220x220 mm and will be connected as such: MGN12 linear rail -> MGN12C carriage -> y-axis carriage plate (either CNC'd or sourced from an existing printer) -> insulation stuck to heater stuck to aluminum plate with magnetic sheet adhered on top to hold the PEI build plate. I will be using linear rails for all of the axes and will have the x-axis fold up instead of the complicated y-axis folding mechanism I was previously envisioning. As I type this, I am designing the heated bed in CAD, as I am creating the individual components and then constraining them into an assembly in Fusion. (7 hours).
<img width="500" alt="image" src="https://github.com/user-attachments/assets/ea87669b-0068-473d-9052-c7347163dd37" />  
  
- [3/10/26] Today I basically finished the y-axis assembly. I also added to the BOM all of the parts I will need for the extruder. I spent a LOT of time researching how to connect belts and pulleys and such, and also spent a lot of time looking at extruders. I changed my mind from the picolino and am now going to use the ProtoXtruder, since there is better documentation and it is cheaper. I am hoping I have the budget for auto levelling, but it is not looking good. I will be right at the $350 budget if not over it. I will probably use my tickets for a Blueprint hardware grant. (5 hours)
<img width="500" alt="image" src="https://github.com/user-attachments/assets/7b9753d2-27ad-4d54-88bf-445d95a20a77" />


- [3/13/26] I have finished the Y-axis assembly. It will slide back and forth onto the briefcase wall for transportation. I have finalized my BOM and purchased the AliExpress components so that they get here on time. I still have not secured the salvage 3D printers, but I am hoping to get them this weekend. It took a while to make the y-axis assembly reasonably compact, but I think I did it. The main troubles were getting the stepper to go under the bed as it moved. This meant making the y axis carriage plate with enough space for the stepper while still letting the bed go on top of it. I also had to get the pulleys aligned with the belt tensioner on the 3D printed y axis carriage. This took a few hours of back and forth between different fusion workspaces and waiting for it to update so I could see if it worked. Speaking of the belt tensioner, I found a STEP model online someone developed, but I completely overhauled it, changing the side widths and attaching it to the y-axis carriage plate. I want to make this y-axis as compact as possible, so I want the carriage plate nearly touching the stepper. I was able to get the length down to 375mm, which is in my opinion still too long, as this length determines the height of the final briefcase. (6.5 hours)
- <img width="550" alt="image" src="https://github.com/user-attachments/assets/f97bdede-d234-4b1b-8ab7-46ff617fe64d" /> <img width="500" alt="image" src="https://github.com/user-attachments/assets/e2548a2d-5751-475c-9e96-2dc64b961c16" /> <img width="500" alt="image" src="https://github.com/user-attachments/assets/32a41e81-2bc4-4a26-b260-199f793b82af" />




- [3/15/26] I did not, in fact, finish the Y-axis assembly. Yesterday morning I recieved my 3D printers. There were no Z18s as I expected, however, there are 4 MakerBot Replicator (5th gen) printers and 2 MakerBot Replicator+ 3D printers. This means I might have to buy more parts for the Y-axis, but we will see. It will depend on the print volume I want.  
<img width="500" alt="image" src="https://github.com/user-attachments/assets/59ba0f16-8edb-4bd4-97ab-607ab6828e8f" />

I spent the ENTIRETY of today from when I woke up until I went to bed (aside from going to Church and eating lunch) disassembling one of each of the printers.  
<img width="500" alt="image" src="https://github.com/user-attachments/assets/2b521397-743e-4e02-ad36-c46364661ad1" /> <img width="500" alt="image" src="https://github.com/user-attachments/assets/6f3e56d5-1a26-42dc-b8b3-1ee22beab642" />  
I found out that the + model has both MGN9C and H linear rails/guides in its motion system. I took apart every screw, and I struggled with a few of the screws, in some cases having to drill them out or etch them with a dremel.  
<img width="500" alt="image" src="https://github.com/user-attachments/assets/a1d572cf-4040-4623-a11c-dd029610cd8a" />  
I am redesigning the Y-axis to use the MGN9H rails, since this will save me $36. I also found out that both of the printers use sensorless homing, which means I may need to buy some end switches for the filament runout sensors in my build. Additionally to the rails and screws, I salvaged 8 stepper motors, four fans, belts, idler pulleys, 2 hdmi cables, 2 power supplies for future projects, and a z axis lead screw brass thingy. (10 hours)  

- [3/16/26] I spent a while today going back to the Y-axis. Since I changed the design to use MGN9 rails instead of MGN12, I had to go back to the start of my Fusion timeline and fix all of the joints, relationships, sketch planes, extrusion distances, etc to work with the new rail size. Thank goodness for parametric modeling. There is a bright side to this, which is that I was able to reduce the size of the Y-axis from 374mm to 349mm, a whole 25mm! Progress was still slow because I was having to do this part on my Chromebook since I had a free 1st period today, giving me around 2 hours during school to work. I also made a sketch for the stepper mount for the Z-axis. (3 hours)  
<img width="193" height="26" alt="image" src="https://github.com/user-attachments/assets/41d26de7-f997-41c9-add9-0697a5e1d8bf" /> <img width="500" alt="image" src="https://github.com/user-attachments/assets/15d94a9c-f80d-4764-8f8b-5fcee9c7062b" /> <img width="500" alt="image" src="https://github.com/user-attachments/assets/d13e7698-ed31-4419-9808-f58de124dc65" /> <img width="500" alt="image" src="https://github.com/user-attachments/assets/c2108270-df2c-4bb0-8b80-97d195918259" /> <img width="500" alt="image" src="https://github.com/user-attachments/assets/e75da83c-3175-4d1f-9fdc-3746d7f3b438" />
  
