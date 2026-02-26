---
title: "FoldPrinter"
description: "A very portable 3D printer that will (hopefully) fit inside a briefcase!"
project_name: "FoldPrinter"
repository: "https://raw.githubusercontent.com/BingleyPro/foldprinter/refs/heads/main/JOURNAL.md"
---
Made by: @Bingley
Repository link: https://github.com/BingleyPro/foldprinter
Total hours so far: 2

- [x] I have a 3D printer or will be getting one before March 21st

## March 2nd, 2025
**5:48pm**: Time to start planning. I have literally no idea where to start or what to do, so I betetr figure that out first.

**6:26pm**: Finished making a basic sketch:

![Day 1 Sketches](https://hc-cdn.hel1.your-objectstorage.com/s/v3/26b00b22c5196df01f748437b00c7f00c51b1056_day_1_sketches.png)

I realised my orginal thought process wasn't actually possible, but I made design #1, where the tall thingys move back and forth. I haven't seen this on a printer before, it's either the build plate moving (not really possible with the constraints) or the extruder moving two ways (again, not entirely possible, but a fold out thing could be possible but very difficult). I think I will stick with this design for now.

Design #2 just another quick idea to test my brain. This does have a moving build plate (conveyor belt!) but I don't think this is the best idea and it has a good chance of not working.

So far, I'm sticking with design #1.

**6:38pm**: Here are my current goals for this printer:
- To be portable enough to fit in a suitcase
- To be to survive being upside down and some jolting around (but not while printing!)
- To be able to easily plug in and power the print
- To be able to reliably fold and unfold the printer a million times
- To be able to print with millimeter precision
- To be easy enough for an end user to use.

And for some extra goals:
- Have an in-built battery (although, 3D printers take a lot of power so you wouldn't be able to run very long with this)
- Have a touch screen for controlling the printer
- Have a USB-A / micro-SD card slot for sending over designs
- Have in-built storage with a micro-SD card (actually, isn't this a requirement because the printer has to be actively reading this?)

Still have no idea really where to start but to do some research!

**6:48pm**: Started watching [https://www.youtube.com/watch?v=JdfztjEP_bI](https://www.youtube.com/watch?v=JdfztjEP_bI) to 1:53!

**7:59pm**: Ready to continue the above video and take notes! Going to watch it from the start again.
- FDM printer: lays down melted plastic
- look at cartisan/delta printers later
- First part: frame - usually made of aluminium extrustion, has guide rails for wheels
- Power supply - converts AC to DC to use for components
- Motherboard - sends info to motors to move the components
- Stepper motors - each axis has at least one, can move precisely instead of continously
- Tooth belts, lead screws, or both - converts movement of stepper motor to the movement of the axis
- Limits of axises can be controlled by limit switches, closed when stepper motors move to the end, provides zero reference point and stops parts falling off
- Y-axis movement, whole nozzle and x-axis gantry can be moved (what this printer will use!) or moving the bed back and forth (can't use)
- Beds have a heating element, prevents warping, helps print stick
- Extruder - collective amount of components that manage the filament extrustion
- Consists of stepper motor, toothed gear, and exturder arm that pushes the filament into the tooth gear so that as the gear turns the filament oves in and out, set tension right
- on direct drive, located on x axis, and guides filament into the hotend, that controls the melting
- some have extruder on side, and use a tube to put into hotend (bowden tube)
- the hotend has the nozzle, heat block, heat break, heat sticking
- the heat block transfers the heat from a heating element to the nozzle
- the heat sink must keep filament that hasnt reached the nzozle below melting temp
- the heat break connects hot and cold (heat block and sink) sides of the hotend and resricts the amount of heat transfer between the two
- a teflon lined hot end has a non-metallic lining that also helps prevent heat transfer into the filament too soon, cannot withstand large temps
- to print ABS etc. you need all metal hot end, higher temps can be used but eneds much better controlling
- heat block/nozzle temp is monitored by a thermistor, which info to the control board
- nozzle controls a temp controlled section of the hotend where the filament is rapidly heated before extruded
- the nozzle has precise hole
- nozzle features: material and hole diameter, most common material is brass (conducts heat very well)
- some filametns are more abrasive and increase wear on rbass nozzle
- nozzle like steel are better, but don't always transfer heat as well as brass
- a smaller nozzle hole allows higher detail, but longer print times
- fan that belows on hotend heat sink to keep it control and another fan inside power supply, may be one for control board, and park fan that cools filament as it comes out the nozzle
- display screen, touch or seperate controls, stop and start prints from seperate micro-SD card

**8:23pm**: And finished video! Learnt a lot more from that. Watching another video: https://www.youtube.com/watch?v=KZi3esvQ02w
- Filament fed by extruder, which consists of a stepper motor, a drive/hopped gear and an idler which pushes filament into hop gear (idle lever and bearing + adjustable spring)
- Hotend melts filament at right temp: nozzle, heater block, heat break, heat sink
- heat break mechnically supports heat block and nozzle while allowing as little heat as possible to creep into heatsink abrasive
- heater block and nozzle are heated by a heater cartridge and temp is read back by a temp sensor (normally thermistor)
- all metal hotends means no plastic parts touching the heated zone
- cartisean means aligned wiht XYZ axises
- hot end sits on a carriage
- driven by stepper motors that transfer power through belts or lead screws
- lead screws or threaded rods used for z axis which stay in palce when motors aren't power
- faster x/y axises are typically driven by timing belts
- each axis runs on a linear bearing
- main board or controller board: microcontroller, MCU, stepper drivers, MOSFETs for switching heaters and fans on/off, various inputs and outputs
- LCD screen
- Process g-code files: contains mvoe instructions, generated from slice

**8:39pm**: Finished video 2. I think I know a lot more about the components now, and feel a tiny bit confident now :D!
Anyway, this will be the last entry today.

**Time elapsed**: 5:48pm - 6:48pm, 7:59pm - 8:23pm, total: 1 hour, 24 minutes

## March 4th, 2025
**8:35pm**: Time to get to work again!

The hardest part of my printer is the folding mechanism, which will be very tricky to pull off, since the tall part of the frame have to both fold, and slide along guide rails (belts?). I think having a hinge will be very helpful, but I need some way to lock the frame in the state of being up, plus supporting the extruder's weight, and also locked when down. I looked a bit at CoreXY and Cartesian, and since I'm completely new to anything remotely related to this, I'm going for Cartesian, with seems to be simplier.

**8:59pm**: Idea time! The guide rails (or belts idk know what they called) will move a square, and then there will be a hinge connected to the tall frame part.

**9:11pm**: Have absolutely no idea what I'm doing.

**Time elapsed**: 8:35pm - 9:11pm, total: 36 minutes
