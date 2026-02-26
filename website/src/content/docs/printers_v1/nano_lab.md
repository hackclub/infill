---
title: "NanoLab"
description: "A enclosed, small and thus hopefully portable 3D printer that allows printing high quality models with a whole bunch of different materials"
project_name: "NanoLab"
repository: "https://raw.githubusercontent.com/Illuminum2/NanoLab/refs/heads/main/JOURNAL.md"
---
# NanoLab

Made by: @Iluminum2  
Repo link: [https://github.com/Illuminum2/NanoLab](https://github.com/Illuminum2/NanoLab)  
Total hours so far: 51.5
- [x] I have a 3D printer

## Idea
A small and thus hopefully portable 3D printer that allows printing high quality models with a whole bunch of different materials, including ABS and ASA

## Design
###  Goals
- Cost(lower than ~300€ grant + Own Parts)
- Quality(Best quality achievable within the budget)
- Sacrifice speed for points above

### Build Volume
- 100(length)x100(width)x100-150(height) mm

### Printable materials
- PLA
- PETG
- TPU
- ABS
- ASA

### Printer size
- To be determined, as small as possible
- Electronics contained in chassis, only exception can be PSU

### Chassis
- Clear(gray) aluminum extrusion
- Sizes to be determined
- Blind joints
- Optionally angle brackets as well(if budget allows, probably unnecessary)
- Electronics and print head at bottom, print bed above, upside down printing
- Tinted translucent plastic cover(resin cast/print)
- Printed bottom cover

### Motion platform
- CoreXY system
- Dual linear rail y-axis mounted on extrusion
- Mono linear rail x-axis mounted on y-axis linear rails, maybe aluminum extrusion support, but better would be CF plate reinforcement
- Dual or mono linear rail z-axis on one extrusion(bed only mounted on one side)
- 3d printed belt housing mounted on extrusion and linear rails
- AB drives mounted on backside of aluminum square, gear ratio to be determined
- Fiberglass core GT2 belts for XY mechanism, routed in extrusion if possible
- Fiberglass or steel core GT2 belts for z-axis

### Print head
- Bowden extruder with PTFE Bowden tubes
- 45° mounted hot end for improved space efficiency or Positron 90° hot end

## Day 1 (Mar 14) 4.5h
I did general research, found a lot of useful guides and videos, and outlined the basic design idea. I also made a few sketches in my notebook to get a better idea of how everything should come together.

## Day 2 (Mar 15) 8h
I did a lot more research, made a few more sketches, and tore down my 3D printers print head to get a better understanding of it. I also took a look at the [Positron LT](https://github.com/Audiotronix/Positron_LT) 3D model (a fork of the [Positron V3](https://github.com/Positron3D/Positron)). After a lot of consideration, I think I am going to go for a Bowden extruder setup and a 45° mounted hot end, but if the budget allows I want to get a Positron 90° bent hot end, but those are over 70$.

## Day 3 (Mar 16) 8.5h
Today I did even more research on a whole bunch of areas, but mainly the tool head. After considering designing my own Proton-like 90° bent nozzle, I figured that it would be too complex, expensive and time consuming, but I'll leave room for future upgrades in the design. I have most of the printer mapped out in sketches now, and I think I can start the CAD phase of this project soon. For the hotend, I plan to use a Deltaprintr Mini, even though it's fairly expensive and it's maximum operating temperature is only 270°, but I have a few modifications in mind to improve that. The hotend will be mounted at a 45° angle for better space efficiency, like I previously mentioned.

## Day 4 (Mar 17) 1.5h
I couldn't get much done today because we had 10 hours of school, but I found a few models of the hotend and the linear rails I want to use, and also started modeling the hotend mount. I also decided to attempt to use berd air cooling to try to keep my tool head as small as possible.

## Day 5 (Mar 18) 5h
I lost a few of my sketches because my brother managed to spill water over them, but it gave me the opportunity to reconsider a few design decisions I had made, and I decided to simplify everything. My toolhead should only carry the hot end + cooling fan as well as ducts for the part cooling, for which the air will be supplied by a tube(berd air cooling). I experimented a bit with a part cooling duct shape similar to some momentum curtain designs, but I have yet to simulate if my design actually has any advantages.

## Day 6 (Mar 19) 1h
I had 10 hous of school, and also have a math exam in two days, so I couldn't work on this for that long. I just started searching 3D models for some other components, and thought a bit about how I can organze the electronics.

## Day 7 (Mar 20) 1h
I did a bit of research on electronics and what main bord would be best for my use case in between the math studying.

## Day 8 (Mar 21) 2h
I had another 10 hour school day, but I did some research into steppet motors and also did some work on my CAD designs.

## Day 9 (Mar 22) 2h
So I was only able to start working on this after 9pm, so I didn't get as much done as I would have liked, but I looked at some more control boards, and I also fixed a weird scaling issue and remodeled part of my tool head because I realized that the model of the hotend I had used was slightly off.

## Day 10 (Mar 23) 5h
Today I got a lot of work done, mainly in 3D modeling, I also did some more sketches of components I need. Also I had to redesign my tool head yet again, for now I haven't added part cooling, but because I am going for berd air cooling I should be able to simply add that by modifying my toolhead cover. I also noticed that I probably have to file off 0.5-1 mm of a part of the nozzle, because it will be mounted at 45°, and could otherwise interfere with the layers.

## Day 11 (Mar 24) 1.5h
Had another 10 hour school day, and had to study for a test, so I wasn't able to do too much, but I added a small cover for the hot end, and started working on other parts as well. I also started restructuring my project in Onshape.

## Day 12 (Mar 25) 0.5h
Today I had another 10 hour school day today, and I also had to study for a test, so I was barely able to make any progress, just did little things here and there and also continued with restructuring all CAD files.

## Day 13 (Mar 26) 3h
Made decent progress, restructuring the project took quite a bit longer than I expected, and I also finally got the planar mate on the linear rails to work. Somehow did even more sketches, and decided that I am going to mount my MGN12H linear rail on a Makerbeam XL 15x15 using T slot nuts, so any twist in the linear rail caused by the manufacturing process does not affect the print quality(hopefully). It should also simplify the mounting to the Y axis. The only downside is that it is going to be slightly thicker.

## Day 14 (Mar 27) 3.5h
Got quite a bit of stuff done, finally pretty much finished the X axis(except for the belt clamps). Also watched a few videos about the Voron 2.4s belt routing, ideally I should be able to finish the Y axis tomorrow.

## Day 15 (Mar 28) 1h
Another 10 hour friday, I couldn't get alot of stuff done, but I realized that I can't use the motors that I wanted to use, so I looked around and did more research, so I can finally get the belts on the Y and X axis done.

## Day 16 (Mar 29) 2h
Well I had to do some other stuff today, so I couldn't work on this for as long as I would have liked, I selected my belts(2GT fiberglass 6mm) and pulleys/idlers. I decided to go for a Nema 17 stepper, even though they are pretty big, but I am going to use a gear reduction anyways, which means it doesn't matter that much(hard to explain why, will be visible in the final model).

## Day 17 (Mar 30) 1h
Had to start working on my Apex proposal as well as study for a test, so not too much progress again, but I got started modeling the motor bracket that is going to hold my steppers, I also need to make sure I keep tolerances in mind with the gears.

## Day 18 (Mar 31) 0.5h
Another 10h school day, and I also had to study for the test so I was barely able to get anything done, just worked on the motor mounting plate.
