---
title: "Nu"
description: "A polar, 5 axis 3d printer"
project_name: "Nu"
repository: "https://raw.githubusercontent.com/Magicninja7/Nu/refs/heads/main/LOG.md"
---

# Nu
Nu, a 5-axis 3d printer

Design inspired by this video: [https://www.youtube.com/watch?v=VEgwnhLHy3g&ab_channel=JoshuaBird](https://www.youtube.com/watch?v=VEgwnhLHy3g&ab_channel=JoshuaBird)

**Author:** @Magic (slack), [@Magicninja7](https://github.com/Magicninja7) (github)  
**Repository:** [https://github.com/Magicninja7/Nu/](https://github.com/Magicninja7/Nu/edit/main/README.md)  
**Total Time Spent:** 10 hour

# Project specifics
 - no set largness yet, but printbed is 200mm in diamater, and ill build around it
 - circular printbed + cantilevered design
 - 5 axis:
   - c axis of printbed
   - x, z axis of dual-arm system
   - b axis of nozzle

# Goals
 - actually create it
 - make it fairly around the 300$ mark
 - make the firmware work (reprap)

# Todo
- todo

# Log
**Day 0**
  - 20 - 26 febuary 2025
  - RESEARCH
  - approx. 10 hours
i mainly use reprap forum, yt videos about mechanical features, learning about advantages of certain designs over other (ex ball screw, vs normal, or belt vs gears)
i also am actively analysing every word in this excellent guide: [drdflo](https://www.drdflo.com/pages/Guides/How-to-Build-a-3D-Printer/FFF.html). 
I have finalised all design, choices, drew some more complex ones on paper, and am starting to create a BOM.
Basically:
 - circular heated printbed 200mm in diamater
 - 220mm, 10mm [sliding rods for printbed](https://www.aliexpress.com/item/33036180370.html)
 - using gears, and this [nema 17 motor](https://www.aliexpress.com/item/1005005742670433.html?spm=a2g0o.detail.pcDetailTopMoreOtherSeller.2.76f5nfoNnfoNWn&gps-id=pcDetailTopMoreOtherSeller&scm=1007.40050.354490.0&scm_id=1007.40050.354490.0&scm-url=1007.40050.354490.0&pvid=1afe711d-2e0e-4bf4-9af2-c8a5c796746a&_t=gps-id:pcDetailTopMoreOtherSeller,scm-url:1007.40050.354490.0,pvid:1afe711d-2e0e-4bf4-9af2-c8a5c796746a,tpp_buckets:668%232846%238110%231995&isseo=y&pdp_ext_f=%7B%22order%22%3A%22162%22%2C%22eval%22%3A%221%22%2C%22sceneId%22%3A%2230050%22%7D&pdp_npi=4%40dis%21PLN%2142.79%2123.40%21%21%2110.59%215.79%21%40%2112000034182321935%21rec%21PL%21%21ABXZ&utparam-url=scene%3ApcDetailTopMoreOtherSeller%7Cquery_from%3A), ill rotate the printbed along c axis


**Day 1**
March 1st
scrap the recent printbed design, a better one would be screws a interacting with rotatable straightener(?), which holds the printbed. this doesn't work bc it'd be too complicated, maybe impossible, to make the printbed stable.
My current is still a work in progress. I'm considering slicing sides of printbed, and putting on the slicing gear teeth. they will lean on the rods (the straightener will still be there), so the printbed will be stable, while moving in 2 axis.
other design, which idk If is possible, is putting the printbed directly on the rods, so it lays on them (still with the straightener. this would ensure better stability and be safer (the spinning screws wouldn't be so in the open).
also, started making the dual-arm system in fusion.