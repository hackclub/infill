---
title: "MuonForge"
description: "A battery and direct electricity powered 3d printer with rechargeability"
project_name: "MuonForge"
repository: "https://raw.githubusercontent.com/asmahdi08/MuonForge/refs/heads/main/JOURNAL.md"
---

# Smoother
* title: "Smoother"
* description: "A smooth printing friend..."

Made by: @Mahdi
Repository link: [Click Here](https://github.com/asmahdi08/MuonForge/)
Total hours so far: 7

- I have access to some 3d printers, especially Bambu labs A1, P1S and some anycubic

Total time: 45+ hours 30 mins (Idk how accurate this is probably pretty close tho)

**Smoother** is a compact, budget-friendly 3D printer designed to stay under $300 while maintaining high functionality. It features a filament detection system to automatically pause printing when the filament runs out, ensuring smooth and uninterrupted prints. Built for efficiency and affordability, it’s ideal for makers looking for a reliable and cost-effective 3D printing solution.

### **Plan to achieve**
I ofter notices after 3D prints finish, thin plastic threads (stringing) often appear between gaps or travel paths. This ruins surface quality and usually requires manual post-processing. So I plan to build a system to auto smooth the printing, by automatically blows **precisely controlled hot air** at specific positions, we can do this thing to get smooth print.

 - ### **How it will be**
	 - **Glass Enclosure**:
		 - As shown by your blue outline, the printer is enclosed in a **glass case** to:
		-   Maintain internal temperature.
	    -   Prevent air disturbance.
	    -   Contain hot air application safely.
    - **Airflow System:**
		-   A series of **airflow nozzles** (shown in purple dots on the sides in your image) installed vertically on both sides of the printer frame.
	    -   These nozzles are controlled to release **hot air** in short bursts on specific layers or coordinates post-print.


## BOM (Bill Of Materials) & CAD Model

- Here is the full BOM - [*Click*](https://docs.google.com/spreadsheets/d/14x0yJbEj5C0rEIQlVVuA8SjHctHjPKWwfSs_GVw-i9w/edit?usp=sharing)
- Cad file in [autodesk](https://autode.sk/42gcF8B) , [OneShape](https://cad.onshape.com/documents/3349b807a03fe84f4fc0f3cb/w/b2111816dbf8ea3aa4b7eab1/e/ff7fe39f09c31c14beff4fb1?renderMode=0&uiState=67faccc9e9a02b4af7a81ac3)

## **Day - 1, ( 20/03/25 ) - Planning and breakdown idea**  

⏳ **Time Spent:** 4+ hours  

- Watched multiple YouTube videos on **how 3D printers work** and their components.  
- Read various articles to understand **FDM printing, mechanics, and common issues**.  
- Identified **filament detection** as a key problem to solve.  
- Goal: **Keep cost under $300** while ensuring quality.  
- Planned a **filament sensor** to pause printing when filament runs out.  
- Next: Research detection methods, sketch design, estimate costs.  


## **Day - 2, ( 21/03/25 ) - Findings and gather printer idea from exist one**  
⏳ **Time Spent:** 3+ hours  

Firstly I researched popular 3D printers to understand their features, components, and designs. I noted key aspects like print volume, filament types, quality, and ease of use. I organized my findings and explored technologies to make the idea happen. So lessgo on building....

## **Day - 3, ( 22/03/25 ) - Assembly frame structure**  
⏳ **Time Spent:** 2+ hours  

### Description
- Started to design the main skeleton of the printer. 
![enter image description here](https://hc-cdn.hel1.your-objectstorage.com/s/v3/ed0409a60188f5c5da7db810c223653faa43ac3f_printer_frame.jpg)





## **Day - 4, ( 23/03/25 ) - z axis assembly**  
⏳ **Time Spent:** 5+ hours  


### Description
- Designing printer Z-axis
![enter image description here](https://hc-cdn.hel1.your-objectstorage.com/s/v3/2666a5ebe5ff6f97031fc5bb7d67c1a0d3b6fb24_z-axis_assembly_l.jpg)


### Parts Breakdown ( z-axis left & z-axis right)


## **Day - 5, ( 24/03/25 ) - Z-axis limit switch & Y-axis assembly**  
⏳ **Time Spent:** 4+ hours  


### Description
- Firstly i started to design the printer Z-axis and then 
- Design the limit switch here
- After that started to design the Y-axis


- ### Z-axis
	- ![enter image description here](https://hc-cdn.hel1.your-objectstorage.com/s/v3/b83a77605363e3044e9f8b88a18ef1a08bf04c22_z-axis_limit_switch.jpg)
- ### Y-axis
	- ![enter image description here](https://hc-cdn.hel1.your-objectstorage.com/s/v3/58ca338517873cd2f39789f5a2744ebedb5a2786_y-axis_assembly.jpg)



## **Day - 6, ( 25/03/25 ) - X-axis assembly**  
⏳ **Time Spent:** 3+ hours  

### Description
- Designing printer X-axis 


![enter image description here](https://hc-cdn.hel1.your-objectstorage.com/s/v3/13194345b20d75f0a4a0257f49f91c0568a2a118_x-axis_assembly.jpg)


## **Day - 7, ( 26/03/25 ) - Feed & Cooling Assembly**  
⏳ **Time Spent:** 4 hours  

### Description
- Here i design the feed and then started to work in the main fun fact so it not miss the filament anymore
-   Added an IR sensor at the filament entry point to detect if the filament is missing.
-   If filament is missing during printing, the sensor triggers:
    -   Automatic pausing of the print
    -   An alert sound.
    -   A popup notification to your phone.


![enter image description here](https://hc-cdn.hel1.your-objectstorage.com/s/v3/03bef370048e771e5356670db30a400fc2fbd176_whatsapp_image_2025-03-31_at_4.28.09_pm.jpeg)



## **Day - 8, ( 27/03/25 ) - Control Panel, Power and Display**  
⏳ **Time Spent:** 3+ hours  



### Description
- For this i review many power supply for printer
- And which power supply will better for my printer. 
- And all basis thought it may good to go


## **Day - 9, ( 5/04/25 ) - Adding Auto Smoothing**  
⏳ **Time Spent:** 11+ hours  
- Today i hope to finish it full less goooo.
- Firstly i covered the printer with glass so the air works
- Making a door for the glass 
- Installing the frame and nozzle for the air flow

![enter image description here](https://files.edgestore.dev/iz2sept3369gmc0f/publicFiles/_public/d9443607-f6a6-46f3-8584-bd05eae0a13f.jpg)

## **Day - 10, ( 28/03/25 ) - Preparing Final BOM**  
⏳ **Time Spent:** 3+ hours  
> This is quite pain to find right goods based on budget and availability.
> I search on Alibaba and Aliexpress
> And got the items also but it will take a bunch of time so decided to make a purchase from local market. 


## **Day - 11, ( 29/03/25 ) - Readme and Reviewing**  
⏳ **Time Spent:** 1+ hours  
- I updated the readme Overall and correct some stuffs   
