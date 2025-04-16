---
title: "Ducc it"
description: "Can't afford a printer? Ducc it, build one. Cheap CoreXY printer!"
project_name: "Ducc it"
repository: "https://raw.githubusercontent.com/Dongathan-Jong/Ducc-it/refs/heads/main/Duccbook.md"
---
# Ducc-it

Made by: @Dongathan-Jong  
Repository link: https://github.com/Dongathan-Jong/Ducc-it  
Total hours so far: 113

BOM: [here](https://docs.google.com/spreadsheets/d/1qOZgMDn6hGFZKtvJTQ3WRMCq_ESmatV1Npfq33ltyqs/edit?usp=sharing)

This is a custom made 3d printer for Hack Club's Infill YSWS! Currently, the printer's features are: 
- 160x160x160mm Print Volume
- Cantilever Design
- Auto Ejecting prints
- Fits under $300 USD
- At least 100mm/s printing
- Klipper support

As someone who has used Autodesk's Tinkercad their whole life, I have realised that CADing models on that software may not be the best idea. I have used this YSWS as an opportunity to learn Fusion 360 along with the electronic workings of a 3D printer. 


### Day 1 - 2/15/2025 - 12:02 PM (1 Hr)

I want to lay some ground rules down for what this printer can do:

- 100mmx100mmx100mm build size
- At least 100mm/s printing
- Fit under $300 USD (under Hack Club's infill budget)
- The printer is rigid enough to produce good quality prints

Going to try and sort out the BOM today

### Day 1 - 2/15/2025 - 1:37 PM (1 Hr)

Worked on my bom, added steppers, aluminum rails, and linear rails.

### Day 1 - 2/15/2025 - 10:36 PM (6 Hrs)

Just did a super long work session ~6h, added a ton of things to the bom! Lead screw, motor bracket, coupler, build plate, linear bearings, and linear rods! Turns out Aliexpress is really my best friend...

I did a ton of work on the CAD, doing pretty good with the cad so far: 

<img src="https://github.com/user-attachments/assets/dc74fda4-12da-4dd2-87e0-a16a4c2017e8"
     alt="Day 1 cad progress"/>

I struggled quite a lot as im pretty new to fusion, but all seems to be good! 

### Day 2 - 2/16/2025 - 10:08 AM (1 Hr)

I thought this through, and I will restart this. I realised that with my current progress, I have barely made a dent in my CAD and have already blown through half the budget. I think the current progress is amazing, but even using the cheapest parts I can find, I don't think I can hit my desired $300 budget. I think a bedslinger would be cheaper? Something like the bambu A1, where the z axis is supported on both sides. 

Here is the current BOM:
| Part    | Quantity |Cost | link| 
| -------- | ------- |-----|--- |
| Nema17 Stepper Motor  | 4   |  $30.25 | [here](https://www.amazon.ca/Nema17-Stepper-Motor-Efficient-Versatile/dp/B0D1VJ9HHY/) |
| MGN12C Linear rail + block (200mm) | 3     | $33.04 | [here](https://www.aliexpress.com/item/1005004908405311.html?spm=a2g0o.productlist.main.5.18baRdNzRdNzEJ&algo_pvid=984f007a-bd47-4df8-b3d0-9a4284b02dd2&algo_exp_id=984f007a-bd47-4df8-b3d0-9a4284b02dd2-2&pdp_ext_f=%7B%22order%22%3A%221196%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%2116.98%2114.94%21%21%21123.06%21108.29%21%40210312d517396392457402387ec167%2112000031182888806%21sea%21CA%213877050385%21X&curPageLogUid=7DN3afI5w5cV&utparam-url=scene%3Asearch%7Cquery_from%3A) |
| 2020 Aluminum extrusions (8 in)  | 8   | $24.44| [here](https://www.fazstore.ca/product/20qe2020/) |
| 2020 Aluminum extrusions (10 in)  | 4   | $10| [here](https://www.fazstore.ca/product/20qe2020/) |
| T10 lead screw (2mm pitch 8mm lead), 200mm | 1 | $9.68 | [here](https://www.aliexpress.com/item/1005007527129800.html?spm=a2g0o.productlist.main.3.1f785bb2rdPq43&algo_pvid=8db134ff-b4a9-4886-b487-1b8b9926f626&algo_exp_id=8db134ff-b4a9-4886-b487-1b8b9926f626-1&pdp_ext_f=%7B%22order%22%3A%2232%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%2123.22%2111.61%21%21%21168.29%2184.14%21%402101eac917396682670056992ea43c%2112000041161391631%21sea%21CA%213877050385%21X&curPageLogUid=zbjTZQFVbNkb&utparam-url=scene%3Asearch%7Cquery_from%3A) |
| Nema17 stepper motor bracket | 3 | $8.06 | [here](https://www.aliexpress.com/item/32969153656.html?spm=a2g0o.productlist.main.1.6c9d51881LCX3R&algo_pvid=049047e0-21c5-4621-b87e-6b6a0072a954&algo_exp_id=049047e0-21c5-4621-b87e-6b6a0072a954-0&pdp_ext_f=%7B%22order%22%3A%22300%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%213.56%213.56%21%21%213.56%213.56%21%402101ec1f17396700195143971ebdcc%2112000033258477529%21sea%21CA%213877050385%21X&curPageLogUid=lv3F4OFtXTsR&utparam-url=scene%3Asearch%7Cquery_from%3A) |
| 5mm to 10mm shaft coupler | 1 | $1.23 | [here](https://www.aliexpress.com/item/1005006333159653.html?spm=a2g0o.productlist.main.1.34496063NZgLYD&algo_pvid=2287ec14-fccb-470b-868b-888cadd1918a&algo_exp_id=2287ec14-fccb-470b-868b-888cadd1918a-0&pdp_ext_f=%7B%22order%22%3A%224%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%211.29%211.23%21%21%211.29%211.23%21%402103247417396706153453151ebf7e%2112000036793940850%21sea%21CA%213877050385%21X&curPageLogUid=pVlg3RGF0ifG&utparam-url=scene%3Asearch%7Cquery_from%3A) |
| 110mm x 120mm build plate (PEI + PET) | 1 | $12.91 | [here](https://www.aliexpress.com/item/1005007660929112.html?spm=a2g0o.productlist.main.3.5d5d4206vu0LN1&algo_pvid=47f21b8f-3be0-4f76-b123-32e8c521ad49&algo_exp_id=47f21b8f-3be0-4f76-b123-32e8c521ad49-1&pdp_ext_f=%7B%22order%22%3A%2212%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%2122.89%2110.99%21%21%2122.89%2110.99%21%402101efeb17396730356818220e08d9%2112000041696428342%21sea%21CA%213877050385%21X&curPageLogUid=F0i5iEvz9Lrj&utparam-url=scene%3Asearch%7Cquery_from%3A) |
| LM8UU linear bearings | 10 | $4.94 | [here](https://www.aliexpress.com/item/1005004108098706.html?spm=a2g0o.productlist.main.3.2aed44adoYtxdQ&algo_pvid=61f54303-4417-42a7-9d8a-e7266e451976&algo_exp_id=61f54303-4417-42a7-9d8a-e7266e451976-1&pdp_ext_f=%7B%22order%22%3A%22691%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%218.74%218.65%21%21%218.74%218.65%21%402103205117396732653087993e5d27%2112000028059680071%21sea%21CA%213877050385%21X&curPageLogUid=8OENk0EMMLbw&utparam-url=scene%3Asearch%7Cquery_from%3A) |
| 8mm linear rods | 2 | $4.99 | [here](https://www.aliexpress.com/item/1005006293171727.html?spm=a2g0o.productlist.main.3.474d2f59k0yrhO&algo_pvid=8c974eb5-c1d1-4c9a-acdb-27f8d2245784&algo_exp_id=8c974eb5-c1d1-4c9a-acdb-27f8d2245784-1&pdp_ext_f=%7B%22order%22%3A%223884%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%217.11%213.98%21%21%217.11%213.98%21%402101c5ac17396768963603218ed2cf%2112000036638889805%21sea%21CA%213877050385%21X&curPageLogUid=e8iNtRMiNKKF&utparam-url=scene%3Asearch%7Cquery_from%3A) | 

The total comes to ~ $139, which excluding electronics and such doesn't sound so feasable. 

### Day 2 - 2/16/2025 - 11:01 PM (6 Hrs) 

I did a bit of work here and there throughout the day, came out to ~ 6 hours. I worked on achieving a cheaper frame, and eneded up settling with a cantilever design, similar to the Bambu A1 mini. Here is the progress for today! 

<img src="https://github.com/user-attachments/assets/b288cdf1-0d52-48ea-b8a0-5dd2686a3132"
     alt="Day 2 cad progress"/>

I'll get to updating the BOM soon, maybe tomorrow.

### Day 3 - 2/24/2025 - 4:53 PM (10 Hrs)

Wow... School really put everything to a halt. I updated the BOM and put everything on a spreadsheet, making these tables in markdown SUCK, [here](https://docs.google.com/spreadsheets/d/1qOZgMDn6hGFZKtvJTQ3WRMCq_ESmatV1Npfq33ltyqs/edit?usp=sharing) is the link to that.

I have worked a little more on the CAD, hope to get the mechanics and everything finished by the end of the week, then finish the electronics in the week after. Will be pretty inactive on this project though, going to Scraypard!

Here is the CAD progress:
<img src="https://github.com/user-attachments/assets/18ab51fa-7a8f-4070-ad20-3bb4b8cdb752"
     alt="Day 3 cad progress"/>

### Day 4, 5, 6, 7 - 3/1/2025 to 3/17/2025 (~35 Hrs)

School, Scrapyard, HQ, everythings been putting this on the backburner, but I am finally here to continue on the writeup! I did quite a lot of work in between my trips to hq fulfilling hackpad, texas for scrapyard, and others, and have finished the hotend assembly, updating the spreadsheet with everything needed, and have everything done except for the electronics and fan shroud (and the feet but thats not high priority). 

I need to figure out how to make a good looking fan shroud since I'm pretty new to fusion, definitely will figure that out soon. As per now, I have quite a lot of stuff figured out, this is basically the final stretch!

<img src="https://github.com/user-attachments/assets/b7593ea6-c7cc-43a7-bef1-3798d3698031"
     alt="Day 4-7 cad progress"/>

### Day 8 - 3/21/2025 - 11:39 PM (7 Hours)

Finally had some time to work on this, worked ~ 7 hours today figuring out electronics, PSU, what I am going to use since I have zero experience with what I am using. The popular choice was to go with a SKR Mini E3 V3, a 350W Creality power supply, and a RPI3 I have laying around. I also added a roll of Polymaker Carbon Reinforced filament, as the brace for the X axis won't be able to support the weight with normal PLA. This suprisingly took SO long because I watched so many YouTube videos on whats good and what isn't.

I updated the bom, added some GT2 parts, belts, pulleys, etc. The total right now is a little over $290 USD, but I added around $2 to each part, since customs may be an issue. 

<img src="https://github.com/user-attachments/assets/e77a89f3-8840-4f13-8c97-0db9c4bc47a3"
     alt="Day 8 cad progress"/>

I think I am going to just strap all the electronics under the bed, and create mounts as I go, since I cannot find the right CAD models for the parts. Also, for the self-ejecting part, I plan to use a servo to sweep the bed, but that will also need to be further researched into. 

As of now, I am marking this printer as completed until I recieve the parts to fabricate!

### Day 9, 10, 11, 12 - 4/1/2025 to 4/4/2025 (12 Hours)

My parts arrived! Super stoked to to start building, but was sad to find out I actually got scammed from the SKR vendor on Aliexpress. I got a refund but it will be a little while until I can actually get the next one I ordered. 

<img src="https://github.com/user-attachments/assets/41039fc4-cada-46c5-bc69-6f472f0705e0"
     alt="All my parts came!"/>

I got quite a lot done today (4/2/2025), finished building all the axes without attaching them to the 2020 extrusions.

<img src="https://github.com/user-attachments/assets/4fd99bc2-3416-4d70-aa20-805d263a4947"
     alt="Axes built"/>

Built the 2020 extrusion base and attached everything together!

<img src="https://github.com/user-attachments/assets/340130ce-0e56-45e0-9dc3-6ac6001b07ae"
     alt="Attached stuff together!"/>

Thats all for now, signing off!

### Day 13 - 4/8/2025 (4 Hours)

Today I realised I bought a MGN12H rail instead of the MGN12C rail... That meant that I had to redesign the WHOLE hotend to fit the proper block. I spent WAY too long redoing this, and haven't even gotten to the fan duct. 

<img src="https://github.com/user-attachments/assets/1048c0a8-7d65-42ea-871a-1a5587edfafd"
     alt="Created new hotend"/>

I also realised my linear rail vertical was SUPER unstable, so I reinforced it with 2020 extrusion 90 degree mounts I created myself on Tinkercad.

<img src="https://github.com/user-attachments/assets/57fe77d1-ee2f-47d0-9552-4bbef96d2f96"
     alt="Fixed stabilization"/>

### Day 14 - 4/10/2025 (3 Hours)

I finished the hotend!

<img src="https://github.com/user-attachments/assets/1bf88ba2-7ad8-4324-a558-c2107f1b9034"
     alt="Fixed stabilization"/>

This took SO much longer than expected, I think I made the holes for the heatset a little bit too small, so the plastic would find it's way seeping into the heatset which made screwing everything together SO difficult. I ended up using a drill but its all together. I also belted the X axis, so that axis is good to go! 

I need to do a little more research on how I plan to organize these cables because currently its a massive rats nest. 

### Day 15 - 4/11/2025 (4 Hours)

The bed carriage is on now! I had to redesign this because I bought a 180x180 bed compared to the 160x160 I planned for, I did it in fusion and printed it out. Once I put the heatsets in and tried to screw it in, I actually had some problem with it being really stiff and not moving around at all, but everything was solved when I untightened the rod holders and retightened them at a better place. So far, everything looks amazing! 

<img src="https://github.com/user-attachments/assets/96ca4b57-4331-4ed6-b58a-882922f1f14e"
     alt="Fixed stabilization"/>

For now, I am just waiting on the mobo to come, so I can start wiring everything together! Can't wait.

### Day 16 & 17 - 4/12/2025 - 4/13/2025 ( ~ 14 Hours)


Welp, it's been a LONG 2 days. After the last entry in this journal, I started testing the motors with an arduino, and found the Z axis's unstable motion SUCKED the toolhead moved all over the place when the Z axis was going up or down, and it was because of the joint of the aluminum exutrsions with the base. I went through quite a few iterations of how to fix it, but I ended up with this design that finally worked (made it stable enough). I'm kinda sad I ran out of black filament and had to start using blue, since the all black would've been so cool. 

<img src="https://github.com/user-attachments/assets/3a11cf3d-6564-4eec-a44b-3655e4832918"
     alt="Fixed stabilization"/>

Along with that, I designed the belt idler for the Y axis, with it working amazing. I belted the bed on as well.

<img src="https://github.com/user-attachments/assets/a4c30162-e298-412b-b658-f1748310c98d"
     alt="Fixed stabilization"/>

Finally, I extended the cables to the fans since they were only 20cm long and weren't long enough to reach the mobo. It took me a while to do this suprisingly but it's all done! 

<img src="https://github.com/user-attachments/assets/c1b7f062-0f21-499c-8444-95aa422e866d"
     alt="Fixed stabilization"/>

This also means that I hit the 100 hour mark making my printer! It's been a crazy ride so far. 

### Day 18 - 4/14/2025 (11 Hours)

I'm actually writing this on the 16th of April... That day was way too long. When I finished my bed, I was so excited, and I hooked all the electronics up, and when I went to move the motors, and the shakiness in the bed was so bad. I made the stupid decision to rip it out... and restart it. I had some extra 2020 extrusion and POM wheels laying around, so I decided to completely redesign the bed. Here it was before: 

<img src="https://github.com/user-attachments/assets/c6b38d78-964a-40f8-96f2-c4b0745b109e"
     alt="Fixed stabilization"/>

And here it was ripped out: 

<img src="https://github.com/user-attachments/assets/ed8f9860-0474-43dc-917e-e9edda4aab44"
     alt="Fixed stabilization"/>

Here is the new carriage! 

<img src="https://github.com/user-attachments/assets/dbba9ee7-3e0c-46c2-bf42-8ef86fafd050"
     alt="Fixed stabilization"/>

I've learned not to trust linear rods and SC8UU bearings anymore :) and now love how stable the bed is! Everything works great and looks amazing. 
