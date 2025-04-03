---
title: "Nighthawk"
description: "A budget friendly, accurate and enclosed Core-XY printer with a large bed"
project_name: "Nighthawk"
repository: "https://raw.githubusercontent.com/yashsethu/nighthawk/refs/heads/main/logbook.md"
---
# Nighthawk 
Nighthawk is a budget, beginner friendly core-xy printer inspired by the Voron 0.2! Ideally, the goal is for it to be as fast as possible!

CAD: https://cad.onshape.com/documents/9f6081b42dd620e3b70b8ed4/w/61d0d2c4dd2d5a6a0ed231f5/e/00db797bbb767489537577aa?renderMode=0&uiState=67ee31a8cbe352034e171d82
Note: I couldn't find a CAD for 150mm stepper, so 200mm is in the CAD. Yes, I know it will hit the x/y axis.

## Planning
Desired specifications:
- 150x150x150 build volume
- Core-xy design, with linear rails for all axes and lead screws for z-axis screws
- Custom (not just configured) DragonBurner toolhead (Orbiter v2, Phaetus Dragonfly BMS, CRTouch)
- Klipper run on a Raspberry Pi 4B
- Enclosed in a polycarb shell (1/8 inch thick?)
- FAST!!! Possibly a sub 7 or sub 6 benchy!

## Toolhead
The Dragon Burner is a really popular toolhead, so a great start, but it doesn't support BLTouch or CRTouch and has some issues in supporting the Orbit v2.0 and Phaetus Dragonfly BMS. So, I completely redesigned it. Also, the original STL files provided open-source were cursed, so I had to do some more redesigns. 
Final toolhead:
![image](https://github.com/user-attachments/assets/4a7f108b-63d5-4f36-8368-5d615c173ced)

- Added BLTouch support + CRTouch (whatever turns out to be cheaper) (6 hrs)
![image](https://github.com/user-attachments/assets/b808a4fd-db37-428a-b518-96da17380741)

- Added Phaetus Dragonfly BMS support (the configuration from Dragon Burner was a little scuffed, had to redesign) + Orbiter v2.0 support (the original burner had some cursed intersected parts) (6 hrs)
![image](https://github.com/user-attachments/assets/0678162d-62e9-488a-9fc6-9f06567c1b44)

## Gantry
For the gantry, I'm going to copy the basic config and geometry of the Voron gantry, but change up spacing + mounts to fit my toolhead and remove legacy Voron attachmnents like support for the tophat and weirdly shaped (IMO) x/y axis endstops. (5 hrs)
![image](https://github.com/user-attachments/assets/1bee0fc3-490e-4f85-9b37-064485aadf3c)

Changes:
- Redesigned the cursed toolhead mount that has this part that inexplicably intersects with the cowl (It might be a support? Idk, but took some digging to delete it (2 hrs)
- Deleted legacy x/y endstop mounts (See final assembly for new mounts) (30 min)
- Changed spacing/mounting stuff, removed tophat support, removed polycarbonate mounts, etc. (3 hrs)

## Z-Axis
This is still heavily inspired by the v0.2 (It's such a good printer), but it has been almost completely redesigned compared to legacy.
![image](https://github.com/user-attachments/assets/557f1e79-0397-48e8-9bbf-03bd7d31b402)

Changes:
- Completely redesigned all bed mounts (From build plate to extrustions), needs to be more filament-efficient and less blocky looking (2 hrs)
![image](https://github.com/user-attachments/assets/02fe16ed-926a-40e9-a522-681f534479db)

- Moved ball screw stepper next to bottom-most extrusion (Instead of mounted underneath) to save the extra two extusions and +1/4 ft height increase (30 min)
![image](https://github.com/user-attachments/assets/4de5d8cd-29fa-4c1b-9911-b79e3463fc15)

- Made a mounting plate for the ball screw stepper (30 min)
![image](https://github.com/user-attachments/assets/6357a97a-c544-4060-b830-6da8d91044fd)

- New mounting plate for the ball screw and nut to the bed (spacing changed, also ugly geometry replaced) (2 hrs)
![image](https://github.com/user-attachments/assets/ba5ed8d7-0c78-4ba5-9fb4-04e6a28ba45c)

## Frame
I wanted to keep it simple here, 15mm extrusions with a very simple architecture. The v.02 was too complicated with the tophat and skirts so yeet they go! Then, I remade it so I wouldn't have to hold everything together with 3d printed parts. (3 hrs)
![image](https://github.com/user-attachments/assets/ec3bfd3c-25a0-4ecb-8a03-405cacc6d4c2)

Changes:
- Screw the tophat! If I really want it later, I'll make it but I'm too lazy to copy it and too broke to buy more extrusions
- No skirts! I moved the stepper so I have more space now!
- No 3d printed stuff holding aluminum together! Iron sharpens iron as extrusions screw into extrusions

## Electronics
My computer will crash if I load any more assemblies, so here's the plan:
- Mount a giant piece of polycarb onto the back of the 2 extrusions supporting the Z axis
- Stick the PSU, RPi, SKR Pico, Buck converter, and whatever else I need on there. (Stick the psu as close to ground as possible)
- Check BOM for electronics details, but I already have most of what I need other than the PSU and Pico

## Bom 
This took the most amount of time, being a brokie. (15 hrs)
https://docs.google.com/spreadsheets/d/19cffJtxG1fblSYRPSsD5pqwqxI_k1R2xgWYntvwAhY0/edit?usp=sharing 
