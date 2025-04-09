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
- Klipper run on a Raspberry Pi 4B
- Enclosed in a polycarb shell (1/8 inch thick?)
- FAST!!! Possibly a sub 7 or sub 6 benchy!
- Phaetus Rapido Hotend
- Sherpa Mini extruder

## Toolhead
For the toolhead, I started off with the aesthetic of the Apogee toolhead for the Ender 3 (https://www.orbiterprojects.com/apogee-ender-3-v2/), but since it doesn't support linear rails (Ender 3 uses v-wheels) or the Sherpa Mini, that was really all I could use.
- Fan shroud to house all three fans (CFD optimized) and built from scratch to fit the Sherpa mini (3 hrs)
![image](https://github.com/user-attachments/assets/7493b16f-a735-429f-90a0-f32249da1e3c)

- Rapido hotend mount + linear block mount + BLTouch holder mount (6 hrs)
  I integrated all the mounts into one to save weight -> print faster!
![image](https://github.com/user-attachments/assets/7b46b22d-0484-464a-bb28-7a0598df8fba)

![image](https://github.com/user-attachments/assets/4fce721d-af8b-4e2e-aee1-25a7bd769c94)

- BLTouch mount (Had to be built from scratch to fit the Sherpa Mini) (1 hr)
![image](https://github.com/user-attachments/assets/633c3ad5-eae2-4f4e-bf5d-8f6ea63f5215)

- Final assembly (with an accelerometer)
  Klipper needs accelerometer readings for input shaping (make printer go wheee), so I managed to (barely) add one in 
![image](https://github.com/user-attachments/assets/2f236289-0eb3-480c-9b90-cd85538516bd)

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

## Motor improvements
### Z Axis
On further thought, I wanna make sure the Z axis stepper I use is enough to go fast. 

I'm gonna first try to estimate the weight of the bed assembly.
- 1515 extrusions are approximately 0.503 kg/m
- 100mm = 0.1m (why am I writing this)
- 3*(0.503 * 0.1) = 150.9 grams
- 3D printed parts are approximately 62.931 grams in ABS

![image](https://github.com/user-attachments/assets/9949a95c-9beb-4d12-9dfb-3b7bec61192a)

- Add an extra 25 grams for screws, ball screw nut, springs
- Approximate weight for bed = **642 grams**

Now, using physics (crazy), we can calculate the minimum amount of torque we need to move the bed in my setup, along with some RPM numbers
- Let's convert the values to load: F = m⋅g = 0.642kg⋅9.81m/s = 6.296N
- Using some cool formulas, calculate the idealized torque: T = (6.296⋅0.008)/2pi = 6.283/0.05037 = 0.00802N
- Convert to g/cm, usually used in torque curves -> 81.74 g/cm

Friction exists. So, we should probably account for 100-120 g/cm of torque. 

I'm going to experiment with a different stepper, this one: https://www.aliexpress.us/item/2251832776347337.html?gatewayAdapt=glo2usa4itemAdapt 

Unfortunately, there is no torque curve, so I need to find the estimated RPM output for 120 g/cm of torque.
- Max RPM is likely between 250–350 RPM at 0.0196 Nm (200 g·cm)
- Might reach 400–500 RPM at 0.0098 Nm (100 g·cm)
- For 200 g·cm → Max RPM ≈ 300 RPM
- For 100 g·cm → Max RPM ≈ 450–500 RPM
- Linear speed (mm/s) = RPM × Lead (mm) / 60
- Estimated linear speed = 10-16.7 mm/s

Alright, so for a Z axis, this is really fast, so I switched the motor out! 

### Gantry
Now, for the gantry, here's the torque curve for the stepper I'm using:

![image](https://github.com/user-attachments/assets/05d45417-a912-4be4-8cea-fc632299be13)

On recommendation, here's some other torque charts I'm considering:

Kraken:

![image](https://github.com/user-attachments/assets/0900c6aa-ffd3-4473-ac68-42436d3f88cc)

Wantai NEMA17:

![image](https://github.com/user-attachments/assets/dfc120f8-e7fd-40c0-afbd-b982f66a00e9)

Based on an estimated 0.8 amp average supply to the stepper motor, and assuming the weight of the toolhead and torque needed, I found that the Wantai NEMA17 had the best max RPM output compared to the others (including another variant)

Model here:

![image](https://github.com/user-attachments/assets/8654e7d8-7829-451d-bf28-87603526c9fc)

The cool thing is that, since it's a NEMA17, it's a drop in replacement! And even cheaper than the StepperOnline one I was using earlier!

## Vibrations
I got a lot of ideas from here: https://www.youtube.com/watch?v=y08v6PY_7ak&t=789s 
I still need some way to decrease vibration from the flat extrusions to the ground.

I designed these quick mounts for more surface area to stick on the bottom of the printer:

![image](https://github.com/user-attachments/assets/6f20e79a-5a11-4414-aa68-229c2ecc96d7)

Then, I did some research into different vibration dampening materials:
- Sorbothane: This seems to be the best solution, a form of rubber that has high vibration absorption
- Rubber: A little bit too unorthodox for my liking, doesn't work great with concrete
- TPU: This doesn't really work because I want to maintain the rigidity of the surface mount
- Concrete Paver: This will happen, but since it's not part of the printer, I don't have to worry about it (yet)

To be really sure, I found some quantitative data. Apparently, there's something called damping coefficients (read an article here: https://www.sciencedirect.com/topics/engineering/damping-coefficient) that can help me find a good material.
I also read through this paper: https://asmedigitalcollection.asme.org/astm-ebooks/book/1813/chapter-abstract/27849243/The-Relationship-of-Traditional-Damping-Measures?redirectedFrom=PDF (didn't really help, but really interesting)
- Sorbothane is about 0.5 (absorbs close to 50%)
- TPU is anywhere from 0.05 to 0.5, but usually around 0.15-0.2 (I need consistency, so this isn't great)
- Rubber is close to 0.2 (again, a little unorthodox, and not great damping)
We have a clear winner!

Since Sorbothane seems to work the best, I found some cheap sheets of it here: https://www.isolateit.com/products/sorbothane-strip-36-91-4cm-x-2-5-1cm-1-strip?variant=37396536819873&country=US&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&srsltid=AfmBOorRawhGNcH6DOdEWkVSQgJC5gtM31SIxVORnRBf-TZJYa7PYxjfMyw&gQT=1

Yay! Vibration-free printing!

## Bom 
This took the most amount of time, being a brokie. (15 hrs)
https://docs.google.com/spreadsheets/d/19cffJtxG1fblSYRPSsD5pqwqxI_k1R2xgWYntvwAhY0/edit?usp=sharing 
