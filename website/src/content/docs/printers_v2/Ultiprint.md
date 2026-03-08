---
title: "Ultiprint"
description: "CoreXY 3d printer with 3 point ABL and an enclosure"
project_name: "Ultiprint"
repository: "https://raw.githubusercontent.com/Icyconfusion/Ultiprint/refs/heads/main/journal.md"
---
Made by: @kyle.mason
Repository link: https://github.com/Icyconfusion/Ultiprint
Total hours so far: 20

- [x] I have a 3D printer or will be getting one before March 21st

**Log 1**
28/2/26
3 hours

Spent some time deciding on the specific of the project. I knew I wanted to make an enclosed 3d printer that could print any material I could realistically need e.g ABS, PC etc. I researched options for a print bed, as finding a size that wouldn't blow the budget will dictate design choices later e.g frame size. I decided on a 330x330mm print bed, so I can attach a 300mm heated bed, for a 300x300 print size. (https://www.aliexpress.com/item/1005004904564882.html?spm=a2g0o.productlist.main.31.4eeaivmUivmUxW&algo_pvid=ea0e96ed-2de0-4b82-a229-da8bdd76b634&algo_exp_id=ea0e96ed-2de0-4b82-a229-da8bdd76b634-30&pdp_ext_f=%7B%22order%22%3A%228%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21AUD%2163.15%2159.99%21%21%2144.20%2141.99%21%402101e07217722410840546160e312d%2112000030968139841%21sea%21AU%217347437705%21ABX%211%210%21n_tag%3A-29910%3Bd%3A6fbdfe4b%3Bm03_new_user%3A-29895&curPageLogUid=wlvp3Kg7l19g&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005004904564882%7C_p_origin_prod%3A). Given this, my frame will use 400mm aluminium profiles. So I started assembling the frame in Fusion using T slot and 90 degree brackets.

Then I thought about the enclosure. In my research, I found polycarbonate is often mounted to the profiles to form the enclosure, so that is most likely the route I will take.


**Log 2**
1/3/26
3 hours

Kept working on the assembly. Originally, I had planned to essentially make a cube out of profiles, though now i have moved the vertical posts down to create feet for the printer. Additionally, I researched materials for the enclosure, as polycarbonate seemed kind of expensive. I cam across ACM (Aluminium composite metal). This gives it a clean, metal look. For the top, bottom, and side panels, I will use ACM. But for the door, I will use polycarbonate to be able to see the print. The door will be mounted on hinges, and panels will be mounted using T nuts.

I also started working on the Z axis. To get 3 point Auto-bed levelling, I have one z motor in each corner. Each motor is connected to a leadscrew to drive the bed. I made the bracket to mount them to the T nuts. I now just need to add the mechansim for the nut block to attach to the bed. In research, I found that similar systems e.g ratrig use steel balls and rods in a coupling to mount the bed, so I might try that.

**Log 3**
2/3/26
4 hours

Redesigned the bracket for the Z axis motors to improve space, and added a holder for the support rods. Also modelled ACM panels for the sides. I have found a relatively cheap supplier (where I don't need to pay 100+ in shipping) for the ACM. 

Also made the entire X and Y axes. I will use linear rails for the motion, with MGN12H carriages. The extruder will be a mk8 extruder and mk8 hotend, in my own X carriage 3d printed design.

**Log 4**
3/3/26
2 hours
Had to move around some elements of the frame to give enough space for things like the extruder etc without hitting the ACM panels. Also started thinking about belts. Decided on a CoreXY system (orignally I considered a cartesian system), and made the brackets for the motors.

**Log 5**
5/5/26
3 hours
Tweaking the CoreXY system. It was hard to get the belts at the right height, especially given the cover on top. I tried to use pulleys for both belts on one pillar (stacked on top of each other) but this was getting quite hard. I did a bit of research and realised that I could just separate them into two, so that worked. I will work on that next log.

I also started designing the Z support for the bed, and edited the corner brackets again to include the smooth rods as supports.

**Log 6**
6/3/26
3 hours
Refined the CoreXY system. To do this, I also edited the extruder to include fasteners for securing the belts. Also designed the Z axis holders using leadscrew nuts, LM8UU and some metal dowels I had laying around. The CAD is now complete, time to move onto the electronics. For the motherboard, I will use a PCB motherboard I made for a blueprint 3d printer. This motherboard has the capabilities to support all the features of this printer. Also configured the firmware to this motherboard and my printer layout. Pretty simple as it is a pretty standard setup. Realised while I was writing this I forgot to model the door and hinge in the CAD, so once I do that, the project will be ready to go.

**Log 7**
8/3/26
2 hours
Finished the final few steps. Added a hole to hold the smooth rods, and modelled a handle for the polycarb door. Everything is now complete and ready to go.
