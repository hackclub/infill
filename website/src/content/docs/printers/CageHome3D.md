---
title: "CageHome3D"
description: "A 3D printer that folds flush to enable efficient storage"
project_name: "CageHome3D"
repository: "https://raw.githubusercontent.com/chunyinkwong/infill-journal/refs/heads/main/README.md"
---
Made by: @chunyinkwong // https://github.com/chunyinkwong/

Repository link: https://github.com/chunyinkwong/infill-journal

Total hours so far: 32

- [x] I have access to 3D printing facilities and am able to obtain printed models on or before March 21st.

## 26th February 2025

Research: 1 hour (brainstorming + printer type researching)

Brainstorming ideas, first draft idea selected: A foldable 3D printer that is able to be stored within an small apartment.

**Draft specifications**
-  Should fold flat so it can be stored nearly flush to the wall
-  Be easily unfoldable without any tools
-  Have a heated bed
-  Be able to print PLA
-  Moderate speed (50-150mm/s)

**TBD, in progress**

Printer type:
- CoreXY
  - **Pros**
    - Fast print speed
  - **Cons**
    - Has a belt which might be hard to tension after folding and unfolding
- Cantilever
  - **Pros**
    - Compact
  - **Cons**
    - Stability issues
- Rectilinear
 
## 5th March 2025

CAD: 1 hour

Installed Fusion360 and watched some tutorials on how to use CAD software

## 12th March 2025

Spent 2.5 hours trying to CAD a toolhead, realized that I have no clue that I am doing.

Probably should've started on the gantry and frame first. This plan only took 30 mins and it's more progress that I've made on the toolhead

**Frame plan**

Bed slinger 3D printer design

![pro drawing in paint](https://files.catbox.moe/vfhj1d.png)

- Part circled in red should have some joint that allows it to fold
- The top of the frame will move along the blue arrow
- Ensure it actually folds flat given that the user manually moves the hotend to the top and the bed to one side after power off
- When opened, it shoud be locked into place and a stopper or something that ensures it is square
    - Perhaps some spring locking mechanisms but I don't know how any of that would work
- To close it, probably will be some button or something to hold down
  - Probably should lock in place when shut as well
 
btw no clue how to design any of that in CAD brb gonna spend 6 hours later learning Fusion360

## 14th March 2025

Spent 3 hours learning Fusion360 again

# 22nd March 2025

Spent the last week learning CAD, took me 8 hours to make this (totally unrelated to the project, just to improve my CAD skills).

I think I am ready to actually design the things in CAD after a quick sketch of my ideas, hopefully a week is enough.

![cad animation](https://files.catbox.moe/ud7fq7.gif)

## 3rd April 2025

I got sick the last week, and had schoolwork, so didn't make progress. 3 days remain.

I made the BOM with around 4 hours of research. Got feedback in Slack and tried to improve it further.

Feedback gotten
- Belts were closed loops and not adjustable length (oops)
- Bed selected isn't a buildplate, so I either need magnets or a buildplate
- Choose a E3D V6 clone instead of the official one to save money (I was overbudget)

Realized that my original plan wouldn't exactly work.
Firstly, I couldn't find a part that I wanted. I searched up knife hinge, locking hinge, pivot hinge, 90 degree hinge, spring loaded hinge with button to unlock, etc but I couldn't get the part that I had in mind. Not sure what to search but I tried a long time.

Furthermore, I realized that if I have a rotating part, then that part would need to lock in place to avoid vibrations.

New plan: Make the Z axis removable with ease.
- Bed slinger design
  - Belt only; no lead screw so there are less parts connected to be base
  - Need to change the BOM, add a counterweight (decided on a Key-Bak, inspired by the Voron Switchwire) and remove the lead screw
-  To disassemble, remove 4 captive screws and unplug the extruder wires
  - Wires needs to have an external point to connect; a single action should disconnect the wires
  - Captive/thumb screws are used so it doesn't fall out and get lost. Also needs to be a thumb screw with a knob and knurling to make removal by hand easy.
-  Z axis assembly parts
  - X motor, belts, tensioner, pulley, etc (connected to the base with 2 captive screws)
  - Z motor, belts, tensioner, counterweight, pulley etc. (connected to the base with 2 captive screws)
  - Extruder, toolhead etc (connected to the base with wires)
  - Filament and stand (connected to the extruder, not related to base)
- Base assembly
  - Y motor, belt etc
  - Heated bed
  - PSU, electronics etc
  - Frame (as small of a footprint as possible)

3 days of nonstop CAD is about to come >:)

## 4th April 2025

Got started building the CAD for the printer. I tried to cheap out on aluminium extrusions (ouch those are expensive) by using 2020 extrusions. Taking a look at other printers, I noticed lots of printers used 2040 or 3060 extrusions for the base. I wondered why until I realised how large the PSU was. I don't want my printer to have a huge PSU sitting at the bottom, so I looked into other solutions.

I decided on using a USB-C PD 3.1 input. I already have a charger at home, and they are widely available (eg. Apple Macbook 140W USBC charger). Doing some research, I noticed that the PD specifications are 28V, 36V or 48V. As I own a 28V charger, I will go with that. More research shows that the maximum for the 28V spec is 140W. I don't want to buy a 48V 240W charger just for this printer (they're expensive).

Researching for USB PD 3.1 sinks, they're tiny boards compared to the PSU. Really surprised they output 140W, considering the size of it.

Initially, I had 2 concerns.
1. Will I accidentally fry the mainboard (SKR mini E3) and components connected to it?
2. Will 140W be enough to heat a bed? (TriangleLAB 24V PRUSA i3 MK3 MK3S, which is 250x210mm)

To address the voltage issue on the mainboard, I looked into the [SKR mini E3 schematic](https://github.com/bigtreetech/BIGTREETECH-SKR-mini-E3/blob/master/hardware/BTT%20SKR%20MINI%20E3%20V3.0/Hardware/BTT%20E3%20SKR%20MINI%20V3.0_SCH.pdf). After consulting with someone who knows what they're doing, they told me to look at the VBB line after the DC input and the fuse. The components connected to the VBB line are
1. [MP1584EN](https://www.monolithicpower.com/en/documentview/productdocument/index/version/2/document_type/Datasheet/lang/en/sku/MP1584EN-LF-Z/document_id/204/), a DC-DC 5V converter, used to power the CPU and 5V output for the RPI, which is rated up to 28V.
2. [TMC2209](https://www.analog.com/en/products/tmc2209.html), the stepper motor driver, which is rated for up to 29V.
3. Extruder heater and bed heater. These are just resistors with no sensitive electronics, so they follow Ohm's law etc, so P = V^2/R, so they won't die or anything, just consume more power
4. Fan headers and LED headers. It should be fine to run a 24V fan on 28V, it's 17% over the rated voltage but it's just a motor. I don't plan to use the LED headers, but there are 28V LEDs available for purchase (unlike fans)

To adress the power issues, I did some research and came across a rough number of 0.4W per cm^2 of bed area. As I am using a 25x21 = 525cm^2 bed, it will draw around 210W of power, which the 140W won't be able to sustain. I wasn't planning to print ABS anyway, so perhaps I will resort to the gluestick method for printing PLA. However, I still want to buy the heated bed to see if it it's possible, eg I put a cardboard box over it to insulate it and it may reach 60C for PLA.

Additionally, revised my plans a little bit. This is because the stepper motors are connected to the top assembly, while the wires for them are connected to the base assembly. I will need to find a connector for the wires which are accessible from the top as I don't want to be flipping the thing over and disconnecting a USB from the RPI and the stepper motor from the mainboard. Therefore, the current action for disassembling the printer into 2 parts that can sit flush to a wall will be
1. Unscrew the 4 captive screws connecting the gantry to the frame
2. Unplug the 2 stepper motors
3. Unplug the wires leading to the extruder
4. Hopefully it's really easy to lift up the gantry from the frame, and doesn't require sliding around. However I looked at the captive screws and I don't think they unscrew enough to totally lift off the frame, so it may have to slide along the slot in the aluminum extrusions

CAD Progress so far:

![3d printer draft frame](https://files.catbox.moe/dcolft.png)

CAD TODO List:
- [ ] Top pulley connector (has 4 bearings for 2 belts and connects to the top of the printer)
- [ ] XZ axis connector (has 4 bearings, connects to the Z carriages and redirects the belts 90 degrees to the X axis)
- [ ] Y axis connector (connects Y motor to frame) 
- [ ] X, Y, and Z carriage endstops (should be just a cube or something, easy)
- [ ] XZ stepper motor mount (contains belt tensioner, stepper motors and the captive screws to mount the motors to the frame)
- [ ] Toolhead (connects Sherpa mini v3 to E3D V6 clone and the filament and the fans)
