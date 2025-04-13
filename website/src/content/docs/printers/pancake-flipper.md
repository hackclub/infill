---
title: "Pancake Flipper"
description: "Upside-down toolchanger printer with belted Z axis"
project_name: "PancakeFlipper"
repository: "https://raw.githubusercontent.com/tmshader/pancake-flipper/refs/heads/main/JOURNAL.md"
---
# Pancake Flipper
An upside-down toolchanger printer with belted Z axis

**Made by:** @tmshader ([GitHub](https://github.com/tmshader)) <br>
**Repository:** [https://github.com/tmshader/pancake-flipper](https://github.com/tmshader/pancake-flipper) <br>
**Total hours so far:** 44

- [x] I have a 3D printer or will be getting one before March 21st

<br>

## Log

### Day 0 -  Big research day
*(2025. 03. 06.)* <br>
*Hours: 10*

Started planning out the printer (a bit late for Infill tbh 😅). Done a lot of
research today and some CAD work.

The current plan is the following:
- Upside-down design
- Fits into filament box (200 x 200 x 70)
- 2 extruders with toolchanger
  - mechanical or electrical toolchanger <- to be decided, but mechanical is
    preferred
- 2020 and 1020 aluminium extrusions for structural rigidity and stability
- 3 linear rails for precise motion on all axes
- 1 belt for X and Y axes and 1 belt for Z axis
- Positron-style XY kinematics
- Positron hotend
- Eddy current bed leveling
- BTT SKR Pico v1.0 controller
- Rasberry Pi Zero 2 W main board
- Integrated power supply
- Enclosure
  - Fitting into the same filament box is preferred, but might not be possible
  - Not 100% planned out yet
  - Might not be included in final design

<br>

### Day 1 - First mockup of mechanical components
*(2025. 03. 07.)* <br>
*Hours: 5*

Found models for the linear rails, steppers and extrusions. After putting
together a quick model I realised that the 1020 extrusion option is not viable
for this printer, so I'm going to be using all 2020 extrusions.

Working on the placement of the Z stepper and the two extruder steppers. Tough
problem. I need to make it fit into the filament box, but also have 5 steppers,
2 control boards and a power supply in the foot of the printer. I'll continue
working on it tomorrow, it's gonna be a fun problem to solve.

<br>

### Day 2 - Iterate, iterate, iterate
*(2025. 03. 08.)* <br>
*Hours: 9*

Switched to two 1030 extrusions for the Y and Z axis as they are flatter but
also fit my original idea, which the 1020 extrusion did not.

Changed out the linear rails for 3 different types instead of using the same
type for all axes. This makes the printer stronger and more precise.

I'm having a hard time designing the Z axis belt stepper and the two extruder
steppers. It is hard to fit them all into the base, so I'm trying to put the
extruder steppers on the Z axis but that also introduces problems.

<br>

### Day 3 - Bye bye Z belt
*(2025. 03. 09.)* <br>
*Hours: 10*

I spent the whole day researching printers, searching for parts and trying out
different configurations for the Z axis belt. Sadly the solutions I came up with
were either too expensive or did not fit into the volume that I want for the
printer.

Because of this I'm switching to a lead screw for the Z axis.

---

**<p align="center">RIP<br>Z axis belt<br>(2025 - 2025)</p>**

---

<br>

### Day 4 - Powersupply and motion system shenanigans
*(2025. 03. 10.)* <br>
*Hours: 6*

I chose the powersupply to be included in the printer. I picked a 300W 24V one
so I have enough headroom even for the two hotends. It will possibly require
a little modification to fit the printer, but not something that cannot be done
with tools anyone building a 3D printer should have.

I split the Y axis extrusion into two 100mm parts so that the cables can pass
through the 50mm gap left between them. The cables are for the power supply and
one extruder and it's hotend.

I started planning out the specifics of the hotend and the toolchanger and I
think I'm going to have just the one part cooling fan and attach the hotend to
that somehow. I do need to have two toolhead PCBs because that way I can
pre-heat the hotend before changing and the downtime will be way lower. The part
cooling fan will have it's own wire and PCB which will contain any components
that are required on the toolhead but not specific to the hotend, such as bed
leveling sensors or possible LEDs.

I'm currently designing the belt path and the tensioner for it. It's quite fun
routing and modeling the belt and picking out the different bearings, pulleys
and idlers.

<br>

### Day 5 - Belt, idler, pulley... belt, idler, pulley...
*(2025. 03. 11.)* <br>
*Hours: 4*

The belt path for the printer has been adjusted and tweaked and I think it is
now close to done. I might have to make slight adjustments once I get to the
modeling part of the planning phase, but for now I'm satisfied with how it looks
and behaves.

I changed and modified the position of most pulleys and idlers. This way the
assembly should be easier and less parts are needed, which makes the printer
cheaper in return.