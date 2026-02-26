---
title: "AKPrinter (such a cringe name sob)"
description: "Prototype CoreXY printer that can self replicate (?) and will be USB-C powered (??)"
project_name: "AKPrinter"
repository: "https://raw.githubusercontent.com/hash-ak/AK-Printer/refs/heads/main/JOURNAL.md"
---
Made by: @Hash-AK
Repository link: https://github.com/Hash-AK/AK-Printer/
Total hours so far: 6:00 hour

- [x] I have access to a makerspace 3d printer, can't make infinite print with it tho

# Day 1 ( Feb 21 2025)
I will try to start to work on my 3d printer today.
Not done much yet, found some ressources to help me later (I'm so inexperienced 😭)

research : 15 minutes

# Day 2 ( Feb 22 2025)

I'm making a little plan for the printer, like constraint and things :

- I would want to make it USB-C powered ( like proposed in the guide, I don't think it would be _that_ hard

- It **NEED** to be printable by either an Ultimaker 3 or by a Qidi X-one 2

- It will be CoreXY because it look cooler and the afor mentionned printers I have access to are CoreXY, meaning I can study it irl

- I plan to make a custom PCB for a keybad at the front to manually control the extruder's movement and temperature (like the menu in the X-one 2 but physical)

- Print volume will be 180^3mm

- It's frame will be made of 2020 250mm V-slots aluminium extrusions (Black anodized if possible)

After talking a bit with perpelxity.ai, I'm starting to have a better plan about this. 

@Anicetus on the slack proposed me these motors : https://www.aliexpress.us/item/2255801033887365.html

Research : 1:45 hour


# Day 3 ( Feb 23 2025)

I'm still searching for what aluminium extrusions I will use. After searching on the web and asking in the slack (only one reply 😭), I think I will go with 2020. Not sure yet what slot type (V or T) yet.
So there's not much done yet but I'm sorta starting to see where I'm going. [this link](https://www.drdflo.com/pages/Guides/How-to-Build-a-3D-Printer/FFF.html) is realyl awesome tho, not supeer detailed but gives a really good overview.

Research : 20 min


# Day 4 ( Feb 26 2025)

Yesterday after asking in the slack and some reasearch I decided that I will use 2020 V-slot aluminium extrusions, 250 mm of lenght. After importing it and setting it all in FreeCAD (I lost so much time trying to resize them), I finnally have a _very rought_ idea of how to case is looking ![image of the aluminium extrusions in freecad](https://hc-cdn.hel1.your-objectstorage.com/s/v3/8481a678c763f07e890dcd723f270deac1fcd036_2025-02-26-110309_hyprshot.png)

I'm also searching on how to make the USB-C power. The main problem is that, from what I saw, USB-C PD (Power Delivery) can only go up to _100 watts_, which look pretty low for a printer. Maybe my printer will have a dual power system (either normal power, which more voltage, and USB-C when less power is required) ?

CAD time : 1:05 minutes
Research : 1 hour

# Day 5 (2 March 2025)

I added the extruder's motor (LBO Orbiter V2) and the extruder/hotend (TZ V2), added all that in my FreeCad project, then I gotta start making the printhead.

CAD + Research time : 1:30 
# Ressources I found
- https://www.instructables.com/How-to-Design-and-Build-a-3D-Printer/
- https://kingroon.com/blogs/3d-print-101/cartesian-vs-corexy
- https://reprap.org/wiki/Build_A_RepRap
- https://www.instructables.com/Complete-newbie-step-by-step-3D-printer-with-all-p/
- https://www.drdflo.com/pages/Guides/How-to-Build-a-3D-Printer/FFF.html
- https://www.geeky-gadgets.com/mondrian-customisable-reprap-3d-printer-07-12-2015/
- https://reprap.org/wiki/Choosing_a_Power_Supply_for_your_RepRap
