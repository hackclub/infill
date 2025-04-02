---
title: "Penguin"
description: "(Hopefully) The most accurate 3d printer you'll find for under $300."
project_name: "Penguin"
repository: "https://raw.githubusercontent.com/Lucas4680/Penguin/refs/heads/main/Devlog.md"
---
Total hours: 34

BOM: https://docs.google.com/spreadsheets/d/1BoM7iUl6QUpEB06v-WNWhYhMciubwFNZ1HohTmLiy30/edit?usp=sharing

2/13/25 - 2 hr (2 total)
Started Project, began researching basics on 3D printers, watched Youtube videos and builds

2/14/25 - 1 hr (3 total)
Continued basic research, began thinking about design requirements, studied other DIY 3D printers

2/15/25 - 3 hr (6 total)
Watched more YT videos on 3D printers, researched and created BOM for toolhead, began importing models to CAD. Time was spread out throughout the day

2/16/25 - 3 hr (9 total)
Finished draft of BOM, began cadding mounts etc to connect everything together (spent an hour trying to find a 3d model of carto. probe to no avail)

2/17/25 - 2 hr (11 total)
Continued working on toolhead, began thinking about frame and movement system
https://cdn.hackclubber.dev/slackcdn/6684845de0eb26d4113f0da41a8cba38.png
![image](https://github.com/user-attachments/assets/01c439c8-47d2-4a28-a76d-a75fc61e13b4)

2/18/25 - 1hr 30m (12.5 total)
Researched and worked on frame design. Spent wayyy to long creating a linear rail model.
![image](https://github.com/user-attachments/assets/51415975-1f88-4109-a288-6bb900b8a315)

2/19/25 - 30m (13 total)
Attached toolhead to rail, did some more research
![image](https://github.com/user-attachments/assets/dd9d3322-2139-4337-ae67-9933c461a7ff)

2/21/25 - 1hr (14 total)
Finished toolhead
![image](https://github.com/user-attachments/assets/dcb69451-0936-447d-97f5-feb8db14a2be)

2/23/25 - 2hr 30m (16.5 total)
Struggled to download and use autodesk cdf. When I finally began running simulations, they were all completely goofed. Notably:
![image](https://github.com/user-attachments/assets/d89c51e9-5a76-48d7-827b-083919ab9782)

3/4/25 - 1hr 30m (18 total)
Settled on frame designl, bedslinger. Began working on X axis mount and belt drive.
![image](https://github.com/user-attachments/assets/f56e778a-a176-4f15-a74f-409ac1c81624)

3/8/25 - 2hr 30m (20.5 total)
Locked in on CFD, created first two iterations of my first design, a 2 stream blower funnel.
V1:![image](https://github.com/user-attachments/assets/d6fb6bbf-abf5-4dd4-85ee-c999e6ce05dc)
V2:![image](https://github.com/user-attachments/assets/e30228c6-5c0f-4b0e-804d-912f68678d95)
Both completely missed the nozzle end ._.

3/9/25 - 3hr (23.5 total)
Finished second version of the double funnel, promising first results
![image](https://github.com/user-attachments/assets/1b03d269-07cb-4faf-bdef-5f28e6cfacef)
Finished the frame and brackets for all 3 axis. The printer's really starting to come together.
![image](https://github.com/user-attachments/assets/6395274d-2a62-40a7-8633-4aeda7ff58d1)

3/10/25 - 1hr (24.5 total)
Began researching for beds and electronics
Finished X and Z movement systems (specifically belt mounts)
Build volume is currently looking to be around 19 x 25 x 16 (xyz), which I'll definitely have to look into tomorrow. One way is to cut down the Y axis by 5, which brings the volume to a fairly square 19x20x16
![image](https://github.com/user-attachments/assets/5c39bbb9-b04c-459f-9aa3-76788edd1f90)

3/11/25 - 30m (25 total)
Did some random small work. Here's the current build volume roughly visualized (24x24x18)
![image](https://github.com/user-attachments/assets/faa6b673-a931-4536-a2d1-d3902bfdf0b8)

3/14/25 - 2hr 30m (27.5 total)
Finished up (almost) all of the 3D printer not including electronics
![image](https://github.com/user-attachments/assets/6704d89e-68c3-4db1-bcac-fb89180e9ae4)

3/15/25 - 1hr 30m (29 total)
Started the day with minimal knowledge on 3d printer electronics setups, ended with a solid grasp of components and how they work together. 

3/16/25 - 5hr (34 total)
Finished researching electronics and finalized parts needed. Went through the BOM and checked and counted up everything. The costs seemed to shoot up significantly after I actually tallied everything up, going from my expectation of ~250 to 350. I spent a lot of time switching and cutting parts to get this number down. One of which was replacing the cartographer probe with a BL Touch clone.
![image](https://github.com/user-attachments/assets/5101fd8c-3462-40ea-b3a2-6cf0d36dbb42)
Here's the full printer rendered  (ooh). ![image](https://github.com/user-attachments/assets/e2794985-d96e-49b5-ab51-7955f0b84594)

3/18/25 - 2hr (36 total)
Spent some time looking over the the BOM again. After trying to find cheaper alternatives for every part, I got the total down to around 330 total before tax. At this point, I had submitted for the grant and bought all the parts.

3/19-3/24 - 6hr (42 total)
Time was scattered throughout this period. By the end I had mostly finished redesigning the printer. (Ignore the glaring issues with bed movement, will figure it out next time)
![image](https://github.com/user-attachments/assets/6fb435ef-8757-42c5-b93a-a0ea940464a7)
![image](https://github.com/user-attachments/assets/5eae9fdd-d082-46ad-8116-a8c66709dbb7)

3/25 - 30m (42.5 total)
Continued redesign
![image](https://github.com/user-attachments/assets/90204df8-222e-492f-b25d-ed6ffe871bad)

3/26-3/28 - 2hr (44.5 total)
Fleshed out redesign and made some really cool renders. Check out renders tab! 
![image](https://github.com/user-attachments/assets/432cb989-e714-43c5-a17b-25090acd974c)

4/2/25 - 2hr 30m (47 total)
Finalized the redesign, made all the parts look nice with chamfers and fillets.
![image](https://github.com/user-attachments/assets/6f3944e6-0495-494b-adb0-ba702418a07b)
Most of the parts have arrived, but still waiting on a few.

