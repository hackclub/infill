---
title: "Storm"
description: "My first 3D printer. Cheap, uses usb c, large, fast (180mm/s), easy to use, accurate, and cool looking (hopefully all of that!"
project_name: "Storm"
repository: "https://raw.githubusercontent.com/the-X-alien/Storm/refs/heads/main/JOURNAL.md"
---
Made by: @the-X-alien // Dhiaan Dave
Repository link: https://github.com/the-X-alien/Storm/
Total hours so far: 36

- [] I have a 3D printer or will be getting one before March 21st (printing legion pls save me)

---
### Status: Design Complete

---
### Goals:

- Beat the A1 at everything
- Cartesian bedslinger (like the Bambu Lab A1)
- 300×300×450mm build volume
- 500–700mm/s, sub-5min Benchy, high quality
- Screen, WiFi, Quiet
- Under $350 including shipping/taxes

---
### Day 1 - Feb 28 2026 - 2 Hours
I thought that Campfire SJ would be a good place to start making my printer because I was an org and not a participant.

But the second I opened the Infill website, I was lost by all the terms like Gantry, Toolhead, and Extrusions. 

But after googling and asking various AI chatbots, I learned that the Gantry is the frame system that allows movement, the toolhead is the part that encompasses the hotend and extruder, and extrusions are metal parts that make up the frame of a printer.

But I was still lost on how to actually make the 3D printer.

After watching a few YouTube videos on how to assemble the frame of a Cartesian 3D printer, I learned that the frame is built of a square base made from metal extrusions, and then there are two extrusions attached vertically on each side with one extrusion connecting them, allowing X Y and Z movement.

One video that really helped me was this one video on how the Bambu Lab A1 works, because it is also a Cartesian printer: https://www.youtube.com/watch?v=f94CnlQ0eq4

I understood the frame completely, but now I was lost on how to make things like the toolhead.

<img width="1240" height="820" alt="image" src="https://github.com/user-attachments/assets/8e75f1ee-b2e3-4fc5-a71a-6963a64ac9bc" />

And right then, Alex (@alexren) pulled up to the event and I asked him for help.

He explained to me how he made his tool head by modeling the inside with the dimensions of the hotend, and how he added magnets to make the hotend hotswapable.
He also recommended that I look at other 3D printers to see what they did for their toolhead and other parts.

So I viewed printers like PandA and Nighthawk and saw their toolhead design.

And now I need to pick a hotend and an extruder so I can model my toolhead.

---
### Day 2 - Mar 3 2026 - 5 Hours

I spent some more time researching what parts I am actually using to build the 3D printer.

(to come up with this list, I had to read alot of reddit, watch many youtube videos, and I had to ask many questions to Claude and Grok)

So, I had to decide what kind of Aluminum extrusions to use.

I needed the frame to be both sturdy and impact resistant.

So, I had a large base made up of 4x 350mm 4040 Extrusions to spread vibration impact,

Then 2x 2040 Extrusions for the Z axis movement,

And the cross bar uptop will be a 2020 extrusion.

To connect them, I will be using cornerplates.

The extruder will be a Orbiter V2.5 which is the evolution of the V2.0 which is the standard lightweight direct-drive extruder for fast bedslingers

And the hotend will be a Trianglelab TZ V6 2.0 Hotend which is considered to be a budget A1 hotend, because it prints 30–45 mm³/s on PLA with a 0.6 mm nozzle compared to the A1's 20–25 mm³/s speed, and it has a bi-metal heatbreak, copper block, fast heating, and it is CHT-compatible nozzle options. It is also super  lightweight, reliable, and it will work with with most V6-style mounts. (V6 style mount to keep in mind when im cadding the toolhead)

For the nozzle, I'll go with any generic no name 0.4 mm hardened steel CHT-style (3-hole/high-flow) nozzle because 0.4mm is the industry standard for a balance of speed and quality for nice printers like the A1, A1 Mini, and Ender 3.

For cooling, I will get Dual 5015 blower fans with high static pressure (24V) because the nozzle and hotend are going to run hot, and so this powerful combination should cool it down.

For leveling, im using the Klicky probe, which is better than the CR Touch and the BL Touch in everysingle way of acuracy, weight, noise.

---
### Day 3 - Mar 4 2026 - 6 Hours (I didn't think research would take this long :heavysob:)

Made some modifications to the above parts list after reading more on Reddit

Aparently since the Klicky probe needs to dock, it's not ideal for bedslingers, and designed for other printers.
So instead, I am switching to the BTT Eddy, because it is super fast and scans the entire bed in one go, making my printing time faster.

Aparently CHT nozzles are a pain to clean if they get a clog and are annoying, and you might just have to throw them away altogether.
So I'll start with a basic standard hardened steel 0.4mm V6 nozzle because I'm a beginner and I want the printer to work before I start trying anything crazy.

Scratch the first thing, I'm going with a CR Touch because the the BTT Eddy is influenced by location and is aparently a pain to calibrate because it is super dependent on the magnetic field of the area.
<img width="352" height="792" alt="image" src="https://github.com/user-attachments/assets/451fb54d-27c4-403d-aa9a-bd238fc0f1fc" />

Wait scratch that again, (I'm sorry) I'm trying to make my printer as fast as possible so a light probe would help, and the Biqu Microprobe is recomeneded because it only weighs 6 grams!
<img width="355" height="587" alt="image" src="https://github.com/user-attachments/assets/55ece148-f39e-4f48-9e35-40dff47505da" />

(I should put a disclaimer that I might change any parts later if I get recommendations or I find a problem with them)

I guess I should start with the motherboard, so for the control board, I am going with the BTT SKR Mini E3 V3, because not only is it super popular, but its also super cheap. It also just makes things simple.
<img width="1409" height="956" alt="image" src="https://github.com/user-attachments/assets/53e2cba0-9552-4b38-b553-0a619aeddd3e" />

Then for the brain, I am using a BTT Pi V1.2.1, because it is designed for the exact motherboard, it can run Klipper, and its optimized for printing. It also has an SPI Port

So I can connect a TFT35 SPI touchscreen for Klipperscreen so I can control the printer without an external screen.
<img width="168" height="168" alt="image" src="https://github.com/user-attachments/assets/bb05352c-ba5b-4bbf-bd1d-b7d27eba63e8" />

For my motors, I am choosing the NEMA 17 Stepper Motors because they have high torque and good precision to have detailed 3D prints.
<img width="522" height="522" alt="image" src="https://github.com/user-attachments/assets/5492777f-fd98-4749-85e0-d0fd00f092e0" />

TO keep the thing running, my power supply will be a 24V 15A one, because all of my components take 24V to have more power.
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/87c9b1b3-fdf8-4ab1-a79e-5540587c41f6" />

For my heated base, I will be using a 310x310mm 24V 220W Aluminum Substrate Heated Bed, so my prints stick to the plate.
<img width="342" height="342" alt="image" src="https://github.com/user-attachments/assets/2a35054d-3fcc-4426-bbc4-bd0e77d0f4af" />

For the actual build plate, I will be using a 256x256mm PEI Textured buildplate because it is a good size so I can make most things, and the texture makes the print stick to the plate and also makes it easy to take off.
<img width="1000" height="1000" alt="image" src="https://github.com/user-attachments/assets/e82596f2-42fd-4914-b653-5e2094203dd5" />

I also added a 24V 4010 Cooling fan to cool the toolhead because its going to get pretty hot.
<img width="220" height="220" alt="image" src="https://github.com/user-attachments/assets/3d9723a1-6bff-4e6c-ab9c-5f2afd717100" />

I also added dual 24V 5015 Turbo Blowers to cool the plate and parts quickly.
<img width="800" height="800" alt="image" src="https://github.com/user-attachments/assets/e8a60b2e-77e4-4b87-a662-3bf5db9a7268" />

I got all the electronics down, but I still need to find the extrusions and rails/rods, and I might have to change some parts because the total is already around $280.

---
### Day 4 - Mar 7 2026 - 3 Hours
After looking at my parts and looking at the prices, I started to question if this is actually possible

And the math said no

So I had to build the entire thing for cheaper

So I started swapping expensive parts for cheaper ones

So this isn't finalized (if you haven't realised I'm updating this as I go), but

I'm switching the BTT SKR Mini E3 V3.0 to the MKS Robin Nano V3 because it has a better chip and more ram so its faster, but it has less support in places like Reddit.

I'm switching the Orbiter V2.5 to the Sherpa Mini cause the orbiter is super expensive, and the Sherpa Mini is just lighter which makes my printer fast, and since it weighs less, its easier to stop making my prints more accurate (yay! paying attention in science class paid off!)

I also switched the BTT Pi with a normal Raspberry Pi Zero 2 W because the BTT PI is just a waste of money

I'm also going to find a cheaper smaller touch screen

And for thing like the hotend and nozzle, I'm gonna use clones that are just as good as the original instead of paying more

Everything else is going to stay pretty much the same, but even with this new budget, I'm pretty cooked

So I was wondering, how do I further lower the cost,

So I read other journals of people who made 3D printers last year and their BOMs (of course I did realize that tarrifs changed the  prices by alot for things)

And in one journal, I read that someone got sponsored by Polymaker

And that got me think about all the videos about making 3D printers that are sponsored by PCBWay, Polymaker, and tons of other 3D printing companies

So I spent some time making a list of all the companies that are in the 3D printing field and have sponsored projects before, or are just a big name in the business

I'll post the full link of sponsors here later, because I don't want them to get spammed before I send in my request : 
<img width="119" height="704" alt="image" src="https://github.com/user-attachments/assets/f7b15bd0-5586-43ec-aea7-2142343780f3" />

Now, I've finally decided to start working on the formal BOM on a spreadsheet to actually see what parts I need to swap and where the money is going (right now I'm just doing it in my head)

The link is: https://docs.google.com/spreadsheets/d/1btD1Bjle54Zft8ynW4hvl1bNV1Zsg6aF89J3ntGE-do/edit?usp=sharing

After checking the BOM from the one video, I watched earlier (https://www.youtube.com/watch?v=EX62plOF-So&list=PLyYZUiBHD1QjaYx7eCEW8zXvsgwEbAykY)

I learned that a site called Misumi has Extrusions for really cheap, so I'm getting all my extrusions from there

But, Aliexpress claims to be cheaper, but I'd have to have a talk with a seller

---
### Day 5 - Mar 9 2026 - 2 Hours
I started working on the BOM, and I planned out the full frame, and motion system

<img width="1896" height="575" alt="image" src="https://github.com/user-attachments/assets/5343cc77-f8c4-4969-8bda-a0c74d6b4bab" />

Now all thats left is the electronics

It was a bit challenging because I had to balance price, preformance, and shipping date for each part

I'm starting to wonder what sourcing parts was like before tarrifs and inflation

Because all the videos and articles I find are from years ago, when everything was cheap and you could make a high end 3D printer for $350

These days Extrusions are $60 alone

How did metal become so expensive?

But, since the Corner Plates were just too expensive, I'm going to try to just 3D print them

I realised, that I can probably print alot of the parts

I wonder if I can just print Extrusions . . .

Today we also had a group agreement to name all of our printers after real names, like Tim, David, John, Bruce, and I'm naming mine Bob.

It's going to be a play on Bob the Builder, so Bob the Printer

Tommorow, I plan on finishing the BOM and starting the toolhead design

Then on Thursday, I want to build the full CAD Assembly

And I hope that I can submit on friday, so I can order parts in time

---
### Day 6 - Mar 10 2026 - 2 Hours
Today I finshed the BOM, while keeping it under $350

But I had to make some sacrifices along the way ...

First, on a happier note, I discovered Amazon Haul after checking some other people's BOMs

And often, I found that for my parts, haul was cheaper!

For things like the endstops, the bearings, wire, etc

Anyways, one of the big changes I had to make was the extrusions

Since bigger extrusions cost more, I had to ditch the 4040s

So now, I was using 2040s for the base

2020s for the Z towers

And a 2020 for the crossbar

Other changes:

I went back to the BTT SKR E3 V3 Mini, because the other one doesn't have drivers for the motors with it, so its an additional cost

Next, instead of using a Nema17 Stepper Motor 17HS4401 for all the axes, I'm only using it for the Y axis

And for the Z and X axis, I am using two Nema 17 Stepper Motor 42HS34

Unfortunately, 300mm heated beds are really hard to find, but every site had tons of Ender 3 beds, so now my bed is 235mm

Then for the probe, I went with the absolute cheapest, the 3DTouch

Next, instead of buying a new touchscreen, I am using a ILI9341 2.8" SPI touchscreen that I have lying around

Finally, I switched all the linear rails to linear rods because they are so much more cheaper

I also emailed JLCMC for sponsorship because they have about half of the things I need, from the extrusions to the motors

---
### Day 7 - Mar 15 2026 - 6 Hours

Finally, I decided to address the Elephant in the room, the toolhead

I put this off the whole week because I had a bunch of schoolwork and a science olympaid tournament, but I mostly put it off because I am quite inexperienced at CAD and designing a whole toolhead looked scary

So finally facing it, I had to make the toolhead

And I started off by thinking of the most simple way to make it, which was to carve out each part from a block and then join all the blocks together so I can just insert all the parts

So I did that, but I had no idea how

I started off by figuring out how to import a part

And that looked simple, just press the import button

But, the immports are all in different tabs, so you have to make an Assembly and then insert the imports

But you can't create a sketch in an assembly, so then you had to make a part studio in the assembly's context

That wasn't the end though, you then had to use the transform function to copy the part to the part studio

And that was all to just get the part

To carve it, I initally thought I could just use the remove feature of the extrude function, but thats not how parts work

So I had to learn all about the "boolean" function, which can preform union, subtraction, and intersection operations

Merging, carving, or intersecting parts

So using that function, I had to select the part as the "tool" and then a block as the "target" and then it would carve the shape of the part into the block

So, following this video, I learned all the sections I had to make and I got started: https://www.youtube.com/watch?v=6OJSKmMlmZA

Hotend mount: 

<img width="1275" height="624" alt="image" src="https://github.com/user-attachments/assets/006d524b-d5e7-4e79-ad30-9ea991392c25" />

Fan holder:

<img width="595" height="454" alt="image" src="https://github.com/user-attachments/assets/29d15cee-7bea-412c-b636-e181febaa00c" />

3DTouch holder:

<img width="285" height="285" alt="image" src="https://github.com/user-attachments/assets/ebc849bf-489a-4d21-b58a-199ccff919ab" />

X Carriage:

<img width="613" height="581" alt="image" src="https://github.com/user-attachments/assets/8f9e35c3-1685-469f-9717-259209629fd4" />

Then I had to do something different for the fan ducts, because you can't just carve that

I had to use this video: https://youtu.be/o-jrtvJ98nE

<img width="576" height="318" alt="image" src="https://github.com/user-attachments/assets/a17a6ee9-b68d-401e-8bf1-369256cfbb9f" />

And the loft function to make the duct for the fan to slide into

Finally, I opened an Assemmbly and inserted all the parts and put it together

When it was done, it looked like this:

<img width="583" height="494" alt="image" src="https://github.com/user-attachments/assets/26daa92d-016e-4b35-823d-59a68c957502" />

<img width="559" height="456" alt="image" src="https://github.com/user-attachments/assets/ee19ac56-57a5-4c55-9a80-ac93f844ff44" />

Very Makeshift, but functional. (in theory)

---
### Day 8 - Mar 28 2026 - 2 Hours

I now had to address the other Elephant in the room, the actual whole assembly

And since my homework was light this weekend and Monday was a holiday, I was determined to finished by the end of the long weekend

So I had to think the entire thing through

How was I going to do this

I figured out that I would have the 2040s face up with the 40mm side up to mimic a 4040 extrusion

And I would connect everything with a 2020 corner bracket

I had to learn how to source parts, and usually, my best bet was GrabCAD because they had nice Step files of almost everything

By the end of the day, I had this:

<img width="883" height="719" alt="Screenshot 2026-03-28 164713" src="https://github.com/user-attachments/assets/4b660a09-18f1-4b3f-a255-5ce6d5f13295" />

Again, I'm not that good at CAD, so even this took me a while

---
### Day 9 - Mar 29 2026 - 4 Hours

Today I had to lock in

Since I'm still a beginner to 3D printers, I didn't know how to assemble the whole thing and the motion systems

So I referenced this youtube series a bunch of times, step by step to assemble it, and I also borrowed a bunch of the 3D parts they used for things like motor mounts, tensioners, and various other pieces: https://www.youtube.com/watch?v=EX62plOF-So&list=PLyYZUiBHD1QjaYx7eCEW8zXvsgwEbAykY

And by diving into various cad sites like GrabCAD, TraceParts, and Cult 3D, I found the parts I needed to assemble it

The hardest thing to find was the Y Carriage for an Ender 3 bed, because there wearn't that many and the ones that were there used the Ender 3's motion system and not rails

Luckily I found a good carriage and then for attaching to the bearings, I found a seperate block to fit onto the carriage

All the other parts were also a headache to find, but they were easier than this

For most of the parts that would attach to the extrusions, I took from the videos, but I often had to modify them or find a different one because my printer was different

I completed the entire process while doomscrolling, listening to music, playing fortnite, and eating

At the end, I had this: 

<img width="857" height="687" alt="Screenshot 2026-03-29 231630" src="https://github.com/user-attachments/assets/7d4583e1-f8d6-4cb5-b07d-50304cff3191" />

The entire Y and Z axis movements done, and the X carriage attached to the linear rods

---
### Day 10 - Mar 30 2026 - 4 Hours

A big one! Day 10 and the 30th of March!

Today was the day I finished!

I assembled the X movement, all the electronics, and double checked everything

For the X movement I initally made the spacing between the bearing holder on the carriage random, so the rods didn't fit right with the parts on the end

So I had to redesign the X carriage properly

Then I added all of the parts onto the toolhead like the extruder, hotend, fans, probe

Then I had to place all of the other electronics like the PSU, MCU, and the screen

So found holders for all those parts and a case for the screen, in which I fit the Raspberry Pi Zero 2W

After double checking, I forgot the T connector that connects the 2020 to the 2040 Z towers, but I quickly added it

The final assembly looks like this:

<img width="790" height="744" alt="image" src="https://github.com/user-attachments/assets/d6de303d-3b07-461a-a784-1a85d07b3f11" />

And the link to it is https://cad.onshape.com/documents/37467ea71eb1fca5838973f8/w/7266e1215341462849f7532b/e/d342240afd8f3da62d0e4bb2?renderMode=0&uiState=69cb56d9761461eae4a4866a

Now, I'm current writing the Journal and I'm done with that, so I just have to do the README

---







