---
title: "CageHome3D"
description: "A 3D printer that folds flush to enable efficient storage"
project_name: "CageHome3D"
repository: "https://raw.githubusercontent.com/chunyinkwong/infill-journal/refs/heads/main/README.md"
---
Made by: @chunyinkwong // https://github.com/chunyinkwong/

Repository link: https://github.com/chunyinkwong/infill-journal

Total hours so far: 20

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
