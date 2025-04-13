---
title: "Candy-V1"
description: "A 4-axis 3D printer"
project_name: "Candy-V1"
repository: "https://raw.githubusercontent.com/Outdatedcandy92/CandyV1/refs/heads/main/candy_v1.md"
---
# Candy V1
Made by: @outdatedcandy92

Repository: [https://github.com/Outdatedcandy92/CandyV1](https://github.com/Outdatedcandy92/CandyV1)

### Total Hours: 40

- ✅I have a 3D printer or will be getting one before March 21st

---


Things To Do:

- [ ] Order Parts
- [ ] Mechanical Filament runout sensor
- [ ] Part Cooler Design
- [ ] X-axis motor mount
- [ ] PTEF Tube
- [ ] Build Failure (opencv?)
- [ ] Y-axis tensioner 
- [ ] PCB (Oled display and Buttons)
- [ ] Software UI
- [ ] Nozzle Cleaner
- [ ] AMS (BY28J-48 motors)
 

# Desired Specifications
- >= 250mm^3 Build Volume
- Raspberry Pi 4 Host
- Running OctoPrint+Klipper
- Timelapse Feature
- Tangle Detection
- Build Failure Detection
- 2 Color AMS System
- Up to 0.1mm Resolution

 

## Day 1 (3rd Feb, 2025)

Did preliminary research on polar printers and how they work

- Want something like this by Joshua [https://www.youtube.com/watch?v=VEgwnhLHy3g](https://www.youtube.com/watch?v=VEgwnhLHy3g)
- Instead of the tool head moving on the X-Axis I'm thinking of the moving the whole bed if possible???
- Did a little bit of researching about 3D printer parts

I want this thing to be able to fit on my shelf/desk, build volume doesn’t really matter i just want to make it

### Time Elapsed: 1 Hrs

## Day 2 & 3 (4th-5th Feb, 2025)

- Created a project timeline and set up deadlines
- worked on formatting this markdown file and writing a description for this project

I was thinking about how printing with a rotational bed would work, like how much should i rotate to get to a set coordinate on a Cartesian plane.

- Studied about polar coordinates and how they really work.
- Turns out its very easy to convert Cartesian coordinates to polar ones.

Below is the maths for how it works for a point (x,y) on a Cartesian plane. 

1. Find linear position (r) of the bed by using Pythagoras theorem
    
    [![\\ r^{2}=\sqrt{x^{2}+y^{2}}](https://latex.codecogs.com/svg.latex?%5C%5C%20r%5E%7B2%7D%3D%5Csqrt%7Bx%5E%7B2%7D%2By%5E%7B2%7D%7D)](#_)    

    

2. Find angle of the bed (θ) using trigonometry (use Sin/Cos/Tan based on the quadrant of the coordinates). here we assume its in the 1st quadrant
    
    [![\\ \theta = \cot(\frac{y}{x})](https://latex.codecogs.com/svg.latex?%5C%5C%20%5Ctheta%20%3D%20%5Ccot(%5Cfrac%7By%7D%7Bx%7D))](#_)

    

Polar coordinates are (r,θ)

- I still have no idea what parts I'm gonna use

### Time Elapsed: 2 Hrs

## Day 4-6 (8th-10th March, 2025)

 ### March break grind starts!!

##### March 8th
I decided to scrap my previous idea of a polar printer, while it is a cool idea I feel like it wouldn't really be that functional.
So now instead of building a polar printer I'm thinking of making a Cartesian style printer with a build volume of at least 300x300x300mm. This idea seems more functional and feels like something I would actually use on a daily basis. I currently own a Bambu A1 mini so having a bigger build volume is really something I want.

##### March 9th-10th
I spent majority of my time on picking out the parts i wanted. It was really hard to get stuff under the budget. After a lot of considerations I decided to get rid of the heatbed 
as I'll only be printing in PLA, which saved me about $60CAD. Getting rid of the heatbed helped me stay under the buget and gave me a little extra wiggle room for adding more parts.

I also decided to rethink about how many gantry was gonna be. My original idea was something like an H-Bot design but after some thinking I decided to scrap that idea because then the toolhead would be heavy and since im moving on smooth rods this might cause some issue, I did some more research and came across the cross-styled gantry but again it had the same problem of having a overall heavy toolhead. After a lot of consideration and research I decided to go with a corexy design, this would make the belt system a lot more complex but allow for a lighter and balanced printhead.

Over the past 3 days I've worked on my parts list and BOM and I've almost finished my BOM (just have a few misc parts and wires left)
[BOM](https://docs.google.com/spreadsheets/d/10UROUA1rVFZyfdf39kwov9C5ffhGzZl1vPd_-cW53OE/edit?usp=sharing)


### Time Spent:  8 hours


## Day 7 (11th March 2025)

Started working on the design of the print today. I started by building out the frame and then placing all the rods and lead screws. After some considerations and looking at the design I decided to opt for only 1 lead screw instead of two, since my bed wont be that heavy.

![Image](https://github.com/user-attachments/assets/2bc5e786-8dab-40bb-9ab5-2a88fcd0478e)

### Time Spent: 3 Hours

## Day 8 (12th March 2025)

Well... I redesigned my printer... again..

After some thinking and considerations I decide to change up my movement style and just go for a standard bed-slinger design. The previous corexy was a good design but making it with a 300x300mm bed was really becoming a problem. I had to cheap out on stuff and remove some features I wanted. With a bedslinger I was able to reduce the overall cost, which allowed me to fit better stuff within the budget, like linear rails for my x and z axis. 

I worked on the 3D model of this new design today, layed out the frame, the rails, the bed. I'm aiming that I can work on connecting them all together tommorow, and then finally start working on the toolhead on 14th.

![Image](https://github.com/user-attachments/assets/4c334025-5592-4327-b8f5-b87abf8fcd32)
I also spent some time on updating my old BOM.

### Time Spent: 6 Hours



## Day 9 (March 13th 2025)

Well it turns out I totally forgot about my Y-Carriage when making the BOM which I realised today when working on the 3D model. So today I spent all of my time on researching what different types of Y-Carriage systems I could use, researching on if I should use linear rails, or smooth rods, or even wheels. After some research I landed on my original idea of using 2 smooth rods but this time I decided to use SC8UU bearings. 
Because I am not using a heatbed I ran into a bit of a problem. How do I mount my build plate on the Y-Carriage? This was a really big problem as a lot of the suggestions were to use either 3-4mm Aluminium plates or Acrylic Sheets, but both of these had their issues. Firstly Aluminium plates were super expensive and then secondly both the Aluminium and Acrylic sheet did not have holes in them, drilling holes myself was not possible as I do not have the proper tools to do such task. After a lot of more searching and surfing I landed on MDF board. I found a cheap 2pc set of 2mm MDF board on aliexpress, which I think is perfect for my project as its cheap, its light, and I can drill into it.

Since I was well under the budget I decided to add magnetic sheet with my build plate
Here is an image of the updated BOM
![Image](https://github.com/user-attachments/assets/c548b1af-a310-4402-955f-9d387d04a661)


I also worked a bit on my sketches for the printer.

### Time Spent: 5 Hours

## Day 10 (March 14th 2025)


Today I worked on my 3D design of the printer overall, added the new Y-Carriage, mounted it with bearings, added smooth rods. All the basic parts are laid out now except for the toolhead which I also started working on, my plan is to go for afterburner type design.
I also changed up my extruder and hotend components, the updated components are the E3D V6 hotend and Titan Extruder

Here are some screenshots of todays work-
![Image](https://github.com/user-attachments/assets/0f1a8d6f-9905-47f4-8e64-20a0b83c7fdc)
![Image](https://github.com/user-attachments/assets/92a059f6-a2b8-4219-829c-7699cfbd06e5)

![Image](https://github.com/user-attachments/assets/128f7f1c-c26c-4855-b977-7521660d3b1e)

### Time Spent: 3 Hours

## Day 11 (March 15-25th)
Had a really busy week so I didn't get a lot of time to work on my logs. Over the past 2 weeks I've worked upon improving and finalizing my design.
Changes I've made-
- Switched out the z axis linear rails to 8mm Smooth rods with LM8UU bearings
- Now added MGN12H rail for the x-axis instead of MGN9H
- Changed the x-axis rail mounting. It is now mounted on top of the aluminium extrusion instead of on its side.
- Added mounts for my y-axis motor and idler
- Made custom pillow blocks for Z-axis Lead Screws and Smooth Rods using 608ZZ bearings
- Designed the toolhead mount for X axis
- Placed X-axis motor and idler (still need to create mounts)
- Worked on BOM
	- Switched from SKR V3 TO V2 (Budget Constraints)
	- Instead of using 4 Nema 17HS4401S I'm now using 3 of those and 1 Nema 17 20mm for my Direct Drive Extruder.
	- Switched to LM8UU from LM8UUU (Size Constraint)
	- Refined my BOM overall. Tried to find lower prices

#### The Plan:
I'm planning on buying the parts soon, and then continue on improving the design till the parts arrive. Right now I have an Idea of using some BY28J-48 Stepper Motors for creating and AMS type system, According to my research if I convert it into a bipolar it would be able to produce enough torque to push and pull the filament. Speaking of filament, I'm planning on adding a mechanical filament runout sensor using one of the micro switches I'm buying for the endstops.


3D Model-
![Image](https://github.com/user-attachments/assets/5ad5988c-e98f-4c5f-a250-8dab14d97939)



