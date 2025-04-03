---
title: "Daedelus"
description: "CoreXY with swapable toolhead"
project_name: "Daedelus"
repository: "https://raw.githubusercontent.com/meowkewok/Daedelus/refs/heads/main/JOURNAL.md"
---
# Daedelus

Made by: @Meowkewok  
Repository link: https://github.com/meowkewok/Daedelus  
Total hours so far: 27.5   

- [x] I have a 3D printer or will be getting one before March 21st

Daedelus was a Greek inventor, builder, and tinkerer, hence the name.  
I started this project with a coreXY design, but I flew too high, hence the name/designation Daedelus (Icharus) for the first variant.

## Link to CAD: https://a360.co/3XCGgpZ

## New Design Goals:
- [ ] Under $300 (USD)
- [x] 310mm3 Build Volume
- [x] Cartesian Bedslinger
- [x] Cool design
- [ ] Touchscreen UI
- [ ] Klipper w/ RPi?

## BOM
I just decided to make a spreadsheet using Google Sheets, it was easier. LINK: https://docs.google.com/spreadsheets/d/1hZlX8M_wxNlEcmAArnw9ARre6T5sTla1MoFUZHyh3DU/edit?usp=sharing

## Log
|Date |Task |Time |Notes|
|-----|-----|-----|-----|
|2/21/2025|Set up Repo, ideas, design goals, began BOM, began CAD|4 Hours|Thanks to my brain for finally deciding what to make|
|2/23/2025|CAD, Research|3 hours||
|2/26/2025|Bit more BOM|30 mins|Buying cheap parts from China|
|2/27/2025|Bit more BOM, some research|1 Hour||
|2/28/2025|Tons of CAD!|3 Hours|Finished the XY gantry!, started Z axis/frame|
|3/6/2025|More CAD! Also made a belt routing pic|2 Hour|Worked on frame|
|3/10/2025|BOM|1.5 Hours|Got it down a tad, have more to do...|
|3/15/2025|CAD, Research, BOM|1.5 Hours|Started Redesign|
|3/16/2025|CAD, BOM|3 Hours|Finished XY axis|
|3/17/2025|BOM, CAD|2.5 Hours|Started toolhead mount|
|3/25/2025|CAD|1 Hour|almost done!|
|3/26/2025|CAD|30 mins||
|3/27/2025|CAD, Logo|2 Hours|Yay logo, also almost done again!|
|3/30/2025|CAD, BOM|2 Hours|I think im done!|

## Detailed Log
3/6/2025  
Last time I was working, I finished the Z-Axis, however, I still need a frame...
![image](https://github.com/user-attachments/assets/ad0c2183-4e92-49cb-bfbe-74857ae6f1a0)  
Need to take a break, but here is progress (after 1 hour):
![image](https://github.com/user-attachments/assets/bf1df8d6-a668-471f-a1fd-dd65f7159161)  
Here is the belt routing pic (ik its a bit wonky):
![XY Axis Assemby v14](https://github.com/user-attachments/assets/6ac167ef-7925-4199-b3bf-ac91b8dc63a7)  

3/10/2025  
I get my cast off tomorrow!  
I realized that my BOM needs to be cut down, so I started work on that. OG: ~375, Now: N/A  

3/15/2025  
I made a realization that a coreXY just costs too much for this...  
Making new goals, and hopefully this time it will work out, and maybe I can make Daedelus (Icharus) in the future. I simply flew too high.
Started work on the CAD for it, looking real good so far, maybe even better than Icharus! I also started working on the BOM for this one, which hopefully will end better than last time.
![XZ Axis v3](https://github.com/user-attachments/assets/9472b425-5541-4f23-9779-f955bfda6945)  

3/16/2025  
Kept working, here is progress so far:  
![XYZ Axis v2](https://github.com/user-attachments/assets/2d936903-57cd-419b-9d47-a01d6e89f8ad)  
Continued working on the BOM, and already it is sooo much cheaper!  

3/27/2025  
Did more CAD and made a logo. ![image](https://github.com/user-attachments/assets/02262cd7-f29a-4057-8ae8-dca04caa174f)

3/30/2025  
I think this CAD model is done!
![XYZ Axis v23](https://github.com/user-attachments/assets/93d91f62-8c10-4a08-88d1-50bc8e97942e)  
Going to try to finish the BOM and submit it today!  

4/3/2025  
I wanted to explain some of the way this printer ended up how it is now. I started by designing a coreXY, and I even finished the CAD, but I realized that there was no chance it would be anywhere near $300, and I didn't really want to spend much of my own money. After a lot of thought, I decided that a way to make it more in-budget would be to redesign it with cheaper parts and as a cartesian, since it would use less parts. The goal for the coreXY was to have a hand-swappable toolhead, but I realized I may not have the budget to even do that on the cartesian. What I am thinking of doing now is designing the swappable toolhead as a "mod" so that I can get the extra $20 to make it (and possibly add a 4th axis?). This whole project is a huge upgrade to what I have now, because I have a printer with 100mm3 of print volume... I do however have access to a bunch of Prusa minis and MK3s at school to print parts on. I wanted to use linear rails because I want this to be as rigid as possible, for when I make a swappable toolhead. 


## OLD DESIGN INFO (Icharus)


### (OG) Design goals: 
- [x] CoreXY
- [x] 300 x 300 x 250 (at least) mm Build area
- [ ] Swappable toolhead (maybe magnets?)
- [ ] Very rigid
- [ ] Under $500
- [ ] Looks cool

### (OG) BOM
BOM Total: ~$375 (needs to be cut down)
|Parts |Quantity |Cost (per) |Link  |Total Cost| 
|------|------|------|------|------|
|Linear Rails + Carriages|5|$16 (less if on sale) |https://www.aliexpress.us/item/3256804722090559.html?gatewayAdapt=glo2usa|$80|
|Extruder Assembly|1|$0|Have on hand (from Ender 3)|$0|
|NEMA 17 Steppers|5|$40-$70|https://www.aliexpress.us/item/3256802068491329.html?spm=a2g0o.productlist.main.2.1478494c9Qbepi&algo_pvid=6fc5044f-9e02-450e-8a7f-6a22700f37b1&algo_exp_id=6fc5044f-9e02-450e-8a7f-6a22700f37b1-1&pdp_ext_f=%7B%22order%22%3A%2257%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%2117.73%2110.98%21%21%2117.73%2110.98%21%40%2112000030753573944%21sea%21US%210%21ABX&curPageLogUid=p9PesYSEpBL2&utparam-url=scene%3Asearch%7Cquery_from%3A|$40-70|
|Threaded rods|2|$5|https://www.aliexpress.us/item/2251832687660623.html?gatewayAdapt=glo2usa4itemAdapt|$10|
|BTT Octopus (Mainboard)|1|$45|https://www.aliexpress.us/item/3256806125317618.html?spm=a2g0o.productlist.main.1.21e37e1e146ILe&algo_pvid=4399267c-2518-489e-ab32-ce4d51bee648&algo_exp_id=4399267c-2518-489e-ab32-ce4d51bee648-0&pdp_ext_f=%7B%22order%22%3A%22492%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%21107.75%2131.14%21%21%21777.40%21224.64%21%402101e9ec17416126463746144e553b%2112000036739233884%21sea%21US%210%21ABX&curPageLogUid=deSITuVx9Wp1&utparam-url=scene%3Asearch%7Cquery_from%3A, https://biqu.equipment/products/bigtreetech-octopus-v1-1?variant=39749194023010|$45|
|T-Nuts for Extrusion|Lots|$1-5|https://www.aliexpress.us/item/2251832673603903.html?gatewayAdapt=glo2usa4itemAdapt|$15|
|Power Supply|1|$45|https://www.aliexpress.us/item/2255800177960035.html?spm=a2g0o.productlist.main.10.29e86cb2DFWhxp&algo_pvid=9d2211bd-d2ef-4c6d-9297-66f241ef53cf&algo_exp_id=9d2211bd-d2ef-4c6d-9297-66f241ef53cf-9&pdp_ext_f=%7B%22order%22%3A%22685%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%2110.17%2110.17%21%21%2110.17%2110.17%21%40%2112000036770193644%21sea%21US%210%21ABX&curPageLogUid=YLEhOH7fhbvM&utparam-url=scene%3Asearch%7Cquery_from%3A|$45|
|Aluminum Extrusion|TBD|<$10|https://www.aliexpress.us/item/3256802466647592.html?spm=a2g0o.productlist.main.19.2caf76d97ScVfD&algo_pvid=52473732-8ea2-4281-8b34-0b2e3da8b27b&algo_exp_id=52473732-8ea2-4281-8b34-0b2e3da8b27b-18&pdp_ext_f=%7B%22order%22%3A%22344%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%2118.17%2112.72%21%21%2118.17%2112.72%21%40%2112000031561558558%21sea%21US%210%21ABX&curPageLogUid=sGZAKhBiu0Wp&utparam-url=scene%3Asearch%7Cquery_from%3A|$60|
|GT2 Belt + Idlers + Pulley|2|$2|https://www.aliexpress.us/item/3256805425039875.html?spm=a2g0o.productlist.main.3.548d3d59kXrpbI&algo_pvid=c0ab7ab0-88ac-40f5-97aa-bff7d19877bb&algo_exp_id=c0ab7ab0-88ac-40f5-97aa-bff7d19877bb-2&pdp_ext_f=%7B%22order%22%3A%22445%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%213.36%210.99%21%21%2124.31%217.19%21%40%2112000033744518728%21sea%21US%210%21ABX&curPageLogUid=pYHM1GhRV0q2&utparam-url=scene%3Asearch%7Cquery_from%3A|$4|
|Lead Screw Coupler|2|$2.5|https://www.aliexpress.us/item/3256806935585490.html?spm=a2g0o.detail.pcDetailBottomMoreOtherSeller.2.43d1eXWheXWh7C&gps-id=pcDetailBottomMoreOtherSeller&scm=1007.40050.354490.0&scm_id=1007.40050.354490.0&scm-url=1007.40050.354490.0&pvid=4129a269-8bff-4c93-a41d-8f3881bd4cf1&_t=gps-id:pcDetailBottomMoreOtherSeller,scm-url:1007.40050.354490.0,pvid:4129a269-8bff-4c93-a41d-8f3881bd4cf1,tpp_buckets:668%232846%238110%231995&pdp_ext_f=%7B%22order%22%3A%221066%22%2C%22eval%22%3A%221%22%2C%22sceneId%22%3A%2230050%22%7D&pdp_npi=4%40dis%21USD%212.53%210.99%21%21%2118.30%217.21%21%40%2112000039472281805%21rec%21US%21%21ABX&utparam-url=scene%3ApcDetailBottomMoreOtherSeller%7Cquery_from%3A|$5|
|M3/M4/M5 bolts + nuts|1|$12|https://www.aliexpress.us/item/3256805690668398.html?spm=a2g0o.productlist.main.5.4f5f45cdHMQp8k&algo_pvid=24515cc1-e107-4679-920a-cb3ce2f612d6&algo_exp_id=24515cc1-e107-4679-920a-cb3ce2f612d6-4&pdp_ext_f=%7B%22order%22%3A%2289%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%217.50%214.00%21%21%2154.14%2128.89%21%402101c80017416473105057760e6a3c%2112000038240155004%21sea%21US%210%21ABX&curPageLogUid=TId63rXPS906&utparam-url=scene%3Asearch%7Cquery_from%3A||
|4x2 Magnets|1|$1|https://www.aliexpress.us/item/3256807003208737.html?spm=a2g0o.productlist.main.3.32e4605fVUjuoO&algo_pvid=6dfc16f6-4558-413d-b06d-d125a583f44b&algo_exp_id=6dfc16f6-4558-413d-b06d-d125a583f44b-2&pdp_ext_f=%7B%22order%22%3A%221662%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%213.14%210.99%21%21%2122.80%217.19%21%40%2112000039747098307%21sea%21US%210%21ABX&curPageLogUid=h6lus0tn7X4w&utparam-url=scene%3Asearch%7Cquery_from%3A|$1|
|Anti-Backlash nut|2|$1|https://www.aliexpress.us/item/3256804076887678.html?spm=a2g0o.productlist.main.2.7ee94e68xZUXwL&algo_pvid=e45c2e0f-f25d-4d53-9616-3a49d46dbe51&algo_exp_id=e45c2e0f-f25d-4d53-9616-3a49d46dbe51-15&pdp_ext_f=%7B%22order%22%3A%22439%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%212.61%210.99%21%21%212.61%210.99%21%402101c5ac17416551344413638e031d%2112000030764210616%21sea%21US%210%21ABX&curPageLogUid=fIaQOWl0snEx&utparam-url=scene%3Asearch%7Cquery_from%3A|$2|
|GT2 Idlers (6pcs)|1|$4|http://aliexpress.us/item/3256807371672860.html?spm=a2g0o.productlist.main.1.16e1fW2TfW2TM0&algo_pvid=523295ef-b74a-406d-8f16-ca7a10bc695f&algo_exp_id=523295ef-b74a-406d-8f16-ca7a10bc695f-0&pdp_ext_f=%7B%22order%22%3A%22112%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%211.85%210.99%21%21%2113.32%217.12%21%402103205217416479687076855e11e0%2112000041285813865%21sea%21US%210%21ABX&curPageLogUid=7huwqvAusaop&utparam-url=scene%3Asearch%7Cquery_from%3A|$4|
|plastic|all of it|like $20 per kilo|Obtain from school's makerspace?|


### (OG) Ideas for Attachments:
- 3d Extruder (obviously)
- Dremel/CNC head
- 4-Axis attachment - adds a 4th axis which can be attached to by various toolheads
- Laser (DANGER!)
- Pen plotter

### Credits:  
Thank you to:  
- Rabbi Hametz (RTH) for letting me use school printers and stuff
- Ryan Rich for giving me random ender 3 parts

### Fun stories:
- This printer is being designed with a broken finger (at the beginning at least. Its healed now!)
- Realized I had to redesign the printer half way through since I would never be able to make it affordable enough.
