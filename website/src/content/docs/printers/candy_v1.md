---
title: "Candy-V1"
description: "A 4-axis 3D printer"
project_name: "Candy-V1"
repository: "https://raw.githubusercontent.com/Outdatedcandy92/CandyV1/refs/heads/main/candy_v1.md"
---
# Candy V1
Made by: @outdatedcandy92

Repository: [https://github.com/Outdatedcandy92/CandyV1](https://github.com/Outdatedcandy92/CandyV1)

### Total Hours: 56

- ✅I have a 3D printer or will be getting one before March 21st

---


Things To Do:

- [x] Order Parts
- [ ] Mechanical Filament runout sensor
- [ ] Part Cooler Design
- [x] X-axis motor mount
- [x] PTEF Tube
- [ ] Build Failure (opencv?)
- [x] Y-axis tensioner 
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

### Time Spent: 6 Hours
## Day 12 (March 27th)

### Update:
I orderded all the parts, and they should be arriving in the next 3 weeks.



## Day 13-21 (Apr 1st - Apr 9th)
Over the past 2 weeks almost 90% of my stuff has arrived and I have started the build process.
The main frame of my printer was completed this week, I made a few minor changes from my orignial frame design like changing the orientation of the bottom 2020 extrusions and how they connect to each other. Instead of one end of a 2020 extrusion going into the side of another 2020 extrusion, they both now connect to a 20x20mm block, so the overall footprint of the bottom frame is now 490x490mm instead of the previous 490x450mm.
![Image](https://hc-cdn.hel1.your-objectstorage.com/s/v3/719c5d4ba1eb05d2082b18788b33f3c761d566cf_image.png)

For the vertical part of my frame I had a few design prototype, the first prototype was where my smooth rod was attached to the corner bracket of the bottom and vertical 2020 extrusion.
![Image](https://hc-cdn.hel1.your-objectstorage.com/s/v3/94c1b77004b54978e7840ce50080848ec38dda9c_20250406_133310.jpg)
![Image](https://hc-cdn.hel1.your-objectstorage.com/s/v3/b969f9580cb1a9e5dd1ca2cef322348cb458d6b9_20250406_210339.jpg)
The second prototype changed the location of the smooth rods and moved them to inside the frame instead of on the frame.
![Image](https://hc-cdn.hel1.your-objectstorage.com/s/v3/eef63a4949be86229bc8fa97b55f2d39029abd5b_20250408_221733.jpg)


Since my printed doesn't have heatplate, I used 2 of 2mm wood boards glued together as the base which connects the y-carriage to the build plate, In theory this should work just fine as I am only gonna print PLA on it and it has a textured PEI sheet which should be sticky enough for the PLA without heat.
[Image]


#### Diy AMS System
For my AMS system my plan was to use 28BYJ48 5V motors to extrude the filament, but unfortunately that did not work as expected, the motor was running slow and filament wasn't being gripped properly by the 3D printed gears.
![Image](https://hc-cdn.hel1.your-objectstorage.com/s/v3/55a4e7331eb15a2d620d683c12ef264d17fad1a2_20250406_210518.jpg)

Going forward I think I'll buy metal gears and nema 14 or nema 17 motors to push the filament.

### Time Spent: 8 Hours

## Day 22 (10th Apr)
Most of today was spent on prototypes for the Y-axis smooth rod holders. I had a couple iterations of prototypes for this design and for now ended up with this.
![Image]

However this keeps the smooth rods centred which is a problem because our tool head is not exactly centred on our printer, to solve this problem I plan on moving the smooth rods a bit forward later on.

### Time Spent: 2 Hours

## Day 23-24 (12th-13th Apr)

- Worked on Z-Axis Motor Mounts

*will include updated images in next commit*

#### Notes: Over the past few week I've been very busy and did not have time to write my updates properly in this journal. I was however maintaining an actual physical journal which tracked my progress. Below is basically the tl;dr of my journal.

# Day 25 -  Day 27 (18th Apr - 20th Apr)

I started working on designing the Y-axis belt tensioner for my printer.
	- Version 1 of this was failure. I had very tight tolerances for the design and the supports messed it up.
I printed Y-axis tensioner without supports in a different orientation and it worked properly.

Also modeled Y-axis motor mount and Y-carriage belt mount.
	- Version 1 of the motor mount was also a fail, I made it into a box like design and completely forgot about how I would actually put the motor inside it.
	- Version 2 split the mount into 2 different parts which would now screw onto the motor
	- Y-carriage mount worked first try, but I might redesign it in the future
Finished designing Z-axis belt tensioner
	- Had a few failed prototype of the thumb screw for tightening it. Decided to just use a long M4 screw 
	- I heat welded an open GT2 belt into a closed loop for the Z-axis, but it not that strong and loop snapped under tensioner

Designed and printer holder for the Y-axis smooth rods.

Printed a mount for the extruder to the linear rail block. 
	- Version 1 failed because I forgot to countersink the holes for the screws, which blocked the extruder motor from fitting in.
	- Version 2 failed because I forgor to take into account the lengths of the screw and I made it too thin.
	- Version 3 worked but one of the screws got stuck in the mgn block and is literally impossible to take out

Printed a fan mount for the V6 hotend which acted like a part cooler and hotend cooler at the same time. This will most likely get updated later into an actually good part coolder, but for now I used this as its easy to take off and put back.

Printed out the top and bottom holders for the Z-axis smooth rods

Designed a temporary mount for the X-axis to the lead screw nut
	- Made V1 5mm thick which did not work because the screws at 12mm (they need atleast 6mm thick block to screw in without hitting the back of the extrusion)
	- V2 was made 6mm thick

Designed a mount for LM8UU bearings to the X-axis
	- Version 1 failed because the holes on it were not big into to fit a zip tie through
	- Version 2 worked with increased hole width


# Day 28 - Day 30 (30th Apr - 2nd May)
The single Z-axis motor with synced lead screw using a belt idea was very difficult to actually implement for me, so I decided to upgrade my printer to dual Z-axis motors.

Designed a new mount for the extruder which has holes on the side to allow for the GT2 belt to loop into.

Designed a motor mount bracket for the X-axis motor
	- Version 1 was a fail, it was suppose to use the bottoms screws of the nema motor but the threads were pretty deep on the motor so it just did not screw at all.
	- Version 2 was redesigned to use the top screw holes for securing the motors, but again I designed it like a box with no way to actually put the motor inside in the first place
	- Version 3 split the design into two different parts (top and bottom). Top screws into the motor and bottom screws onto the lead screw nut.

# Day 31 (3rd May)

Printed belt tensioner block for X axis
	- Version 1 had some problems. The block was not tall/thick enough on the bottom of the idler edges were touching the tensioner block holder, which cause friction and rough movement.
	- Version 2 fixed this issue, but I still think I could improve its design in later version

I also setup Kiauh on my Raspberry pi 4 and flashed Klipper on my SKR board
	- I had some issue with flash Klipper onto the board. I was using a 64gb SD card which the board cannot accept. I partitioned it down to 512 mb which worked. I spent so much time on figuring this out.
	- Installed mainsail on Raspberry pi. I was able to see the printer in mainsail but could not control the motors. Had a UART error for no reason which I spent hours troubleshooting but did not find a solution

# Day 32 (4th May)

So the UART error I was facing just resolved itself!?

I added some temporary endstops just to test the printer (used glue dots to stick the endstops).
	- All axis were moving properly
	- The temporary endstops were doing their job properly
	- The extruder motor was motor was not working, turned out I had the wrong pin definition in my config

**Problem**: The Z-axis's lowest position was apparently not low enough for the toolhead to actually touch the bed. As a temporary solution I placed a cardboard box under the build plate to increase the bed height. I plan on redesigning the lead screw position later.


# Day 33 (10th May)

Major Printer Redesign!!!
	- Redesigned the Z-axis. I moved the Z-axis motors down to get more Z Travel
	- Also planning on moving the Y-Axis up a bit and then fitting the PSU and Controller under it.
	- Redesigned the toolhead mount, It now just uses one single part which screws directly into the MGN block.
	- The x-axis motor mounts and tensioner were also redesigned and a bit more optimized now.
	- Designed an actual mount for Z axis endstop.
	- New Z-axis lead screw guide/top holder design
	- Pushed the Y-Axis 30mm up
		- Version 1 of the smooth rod holder did not work. Tolerances were too tight.
		- Motor holder worked perfectly

# Day 34 (11th May)


Updated some designed and printed a lot of drag chains
	- Fixed the Y-axis smooth rods tolerances
	- Designed a mount for Y-axis endstop
	- Redesigned the toolhead motor mount to have another hole in which I could screw in the drag chain holder. 
	- Printed a LOT of drag chains for cable management (took prob about 6-8 hours)

# Day 35 (16th May)

I tested the printer over the past few days, but it was mostly a fail. I had a pretty bad print the first time which was clumpy and stringy (I think I had the wrong extruder settings) and the print detached from the bed midway. Did some more testing, but since I did not buy a bed leveling probe I had to manually level it. which caused a lot of issues and the nozzle ended up scrapping the PEI sheets multiple times while testing. I decided its not worth it to manually level and ordered a BLTouch sensor.

I also designed a new version of the drag chain mount for the X to Z axis adapter, This version screws onto the X axis motor.

Also redesigned the drag chain mount for the bottom Z axis mount, V1 actually had the wrong side of the clip so the chain could not be attached. The updated version makes it such that both sides can be used to clip in.
