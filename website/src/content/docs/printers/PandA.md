---
title: "PandA"
description: "A printer designed for rapid prototyping on the go."
project_name: "PandA"
repository: "https://raw.githubusercontent.com/lolwutboi987/PandA-RPD/refs/heads/main/JOURNAL.md"
---
# PandA RPD 
 The Portable and Automated Rapid Protyping Device
 
 Made by @lolwutboi987
 Total Hours on CAD: 15
 Total Hours on BOM: 2
 Total hours on Git Repo: 2
## Goals
- Make it portable
- Make it very fast
- Make it reliable
- Make it cheap
- Make it make good prints
- Make it happen
## What the Heck is a PandA-RPD?
The PandA-RPD is a completely open-source, low cost printer with an emphasis on it's portability and ability to print parts in record time. This printer is designed for quick printing on the go, with every aspect of the printer optimized for maximum speed and minimal downtime.  Great for hackathons or making on the go!
![Untitled_2025-Mar-23_01-53-38AM-000_CustomizedView22018073743](https://github.com/user-attachments/assets/702e0df6-3828-41a6-ace2-b3a03b36b2d9)

## Features:
- All-Original CoreXZ kinematics for maximum print speed and acceleration, while tackling common z-axis artifacts caused by leadscrews and ballscrews.
- 300-Watt Ultralight AC Heated Bed for minimal downtime between print protyping.
- BigTreeTech Eddy Duo sensor for lightning-fast bed leveling
- BigTreeTech SKR MINI E3 V3 for silent, yet high performance operation.
- Driven by 3 42-48 Stepper motors, granting unprecedented torque and velocity in all directions.
- Dual 5020 blowers with optimized ducts allow for unprecedented cooling.
- 150X150mm build volume allows for Ample build volumes.
- Custom Carbon Fiber Y-Axis allows for acceleration values never seen on a bedsligner.
- Integrated custom resonance damping feet allow for printing on any surface and reduces translated shaking & vibrations.

## Bill of Materials:
https://docs.google.com/spreadsheets/d/1V79EK8Z-FFW_dK_e8KKpWufplBCfT9gk4kxhHtjUPYw/edit?usp=sharing

 # 3/18/25, Day 0: The brainstorm
 It was a boring tuesday afternoon. I had nothing to do, and was chatting with my group after the absolute chaos that was scrapyard silicon valley. I was chatting on discord about how it was funny that we brought a 3d printer to the hackathon, untill my friend mentions the infill channel. I browse through the channel, excited for another engineering related thing to do during the vex offseason. One problem: Where do I begin? With Scrapyard SV still on my mind, I think of my ender 3 that we brought and the numerous problems that arised when it came to taking a conventional 3d pritner with you on the go. I decided, Why not make a 3d printer designed for hackathons? (Or any situation that requires rapid protyping). Here's what would make a printer optimal in this scenario:

 - Optimized velocity for high speed printing.
 - Minized downtime to allow maximum throughput of prototyped parts.
 - Maximum convenience means reducing hassle with the printer, and increasing time for working/printing.
 - Portability means that said printer can be taken anywhere conveniently.
## Concluding Notes
And so the day ends. With a general idea of what my plans are for this project, I've got 13 days to make it work so i will begin to CAD tommorrow. 

# 3/19/25, Day 1: Cadding Framework
## Creating the file:
With profound experience with both, I am offered both OnShape and Fusion 360 for this project. As this will be a primarily top-down designed project, and online collaboration wont be an absolute requirement, I have chosen Fusion 360. 
## The frame:
Every good printer design starts with a frame. It lays the constraints and framework (hehe) for the motion systems and gives a general idea of the printer's design. For maximum compactibility, I have decided on a Cantilever frame.

![image](https://github.com/user-attachments/assets/9205c7f6-5371-4150-8917-4b5e247e0315)

The Z axis bar is removable, allowing for easy folding of the PandA.
## The Y axis
I have also been able to complete the Y axis. 

![image](https://github.com/user-attachments/assets/c8978fe5-faf1-4eff-a5c0-21da630e701a)

The Y axis incorporates a beefy 42-48 Stepper for maximum torque and velocity. The Bed frame and the Hotbed itself are both carbon fiber. Carbon fiber's Strength-to-weight ratio, stiffness, and relative price point makes it optimal for this situation. 

The Y axis slides upon a nice and extremely thick MGN15H carriage as it's undoubtedly the heaviest moving part on the printer. This size of rail means that wear and friction will be reduced. 

![image](https://github.com/user-attachments/assets/7baa51e6-7288-45c7-b4a5-43c3a1b1fd3f)

The beltpath is drawn in an indigo-blue.
You might be wondering, why would someone do such a beltpath? This is once again, to optimize form factor and simplicity. 

One might also wonder, Why the object circled in red exists. it's there to once again, guide the belt through the 4020 Extrusion without the need for a larger drive pulley which would otherwise, sacrifice torque and performance. 
## Concluding Notes
With the frame and Y-Axis done, I'm calling it a day and I'll pick up tomorrow. Ill likely take care of the XZ axis by tomorrow and start toolhead design too.
# 3/20/25, Day 2:X's O's and Z's
## The kinematics
As of 2025, I can't find any examples of a coreXZ cantilever printer in the wild, however it's similar to a COREXY cantilever. however things like belt passthrough and routing are a different story, especially considering the theoretical form factor contraints of this project.
## The XZ Joints
![Screenshot 2025-03-25 11 55 09 AM](https://github.com/user-attachments/assets/551012d0-5fe7-4816-b5e0-dc698d5ff755)
I've not only adjusted the colors of the parts to match their respecive materials, but following the above example in the image, It's highly similar to the kinematics of a corexy cantilever, just rotated 90. I still with it were that easy, as corexy and corexz systems function extremely differently and bracing can become complicated. 

I have decided the Z axis due to the extremely high and unbalanced load, needs to also be a nice, beefy mgn15H. The cantililever, I have decided while needs to be rigid, also needs to be light and compact, so I have decided to choose an MGN12H and back it with a 2010 extrusion. One thing I have absolutely learned designing printers is that you DO NOT CHEAP OUT ON RAILS. 
## Concluding Notes
For any of the printers i've had the pleasure of designing, beltpaths is probably the hardest thing to figure out, and i've spent several hours chipping away at this and I think this is done, for now I guess. Luckily, tommorrow is friday, which means I can come home straight from school and get straight to work, as long as I please. All that's left is toolhead, and cramming the electronics wherever. And also designing some more gimmicks. I also really need to fix the organization of the f360 file. 
# 3/21/25, Day 3: Finishing Strong
## Electronics
Everyone's Favorite (and most expensive 😭 ) part, Electronics! 

Seeing as my budget should ballpack 300 dollars, however I already have extrusions from another 3d printer I can sacrifice to the benchy gods, Along with F695 bearings, I think I have some pretty sweet "Splurgability" at hand. I feel like a kid in a candy store. 

### Motherboard 
Since this is meant to be a high performance, yet high convenience build, I think I can happily pick a decent, yet not completely overkill motherboard. ( Idk why yall are building an ender 3 but picking a BTT kraken for your builds :skull:) Not only that, it needs to be nice and compact. You know what fits that description? 

![image](https://github.com/user-attachments/assets/24c67c25-0fe0-42ea-9250-2ed9e34c41e4)

This cute little bugger! Its relatively cheap, and pretty much used as a direct replacement to every single ender 3 motherboard the lord hath created. With the sweet sweet taste of TMC 2209 Drivers, features like spreadcycle, stealthchop, and sensorless homing not only makes the life and performance of the motors exponentially better, but mine too, as I no longer have to worry about dealing with endstops. One down, a million left to go...

### AC🌩️DC
One big aspect of printers is to remember that 50% of the job is heating the filament and the bed, Since i want to mimize downtime, I need to find a way to heat the bed fast. One problem is, That a high wattage DC bed needs a big power supply, and a big power supply consumes a lot of space and therefore, would increase the footprint of the printer. One little revolution in 3d printing, is the uptick of 110VAC beds. Since the wall outlet it technically a power supply with a wattage of 1800, if I can pull direct AC power I can increase compactness and performance, while keeping cost relatively the same. Amazing! 

Only one problem though. I cant run the bed 100% full blast the entire time, or we would have a big, firey, smoky problem. Most printers use PWM to control a bed, however no printer motherboard can PWM 120VAC, unless you plan to use the board as a heater. Also, no clicky relay can cycle at 10HZ. the trick? Use something called a Solid-state-relay (SSR):

![image](https://github.com/user-attachments/assets/47897cf6-0072-4d41-a135-76c1a6325fb2)

Its essentialy a giant, fat mosfet that just so happens to be able to handle 120VAC without dying. Yipee.

That means, My DC power supply shouldn't need to be absolutely oversized. I have decided a basic 200 Watt LED driver PSU should be adequate, silent, and nice and compact since the LED driver can sustain it's peak wattage for it's entire lifetime. 

![image](https://github.com/user-attachments/assets/e3ec62d5-1a3e-4a1c-b2ee-ea81de4afcce)




## Enclosure

The enclosure is relatively simple, but has a couple constraints:


 - It has to have good ventilation
 - It has to actually fit whatever electonic components I want to put in them.
 - It has to be printable, and it cannot interfere with the operation of any of the printer's other components
 - It has to look good!

The enclosure I built includes a 70x15 axial fan which first, blows directly at the motherboard, And blows through the enclosure and blows at the SSR and power supply, then out the back vent:

![Screenshot 2025-03-25 12 46 32 PM](https://github.com/user-attachments/assets/1d9f91b8-d268-4051-8b8b-719d6c40665a)

Looks cool too

## Toohead

The toolhead may be considered as the centrepiece of the printer. It is the only part of the printer that technically prints. 

![Screenshot 2025-03-25 12 50 38 PM](https://github.com/user-attachments/assets/f9678a03-fcaa-40c0-a336-d40bc6c45cf6)

2 ducts, 2 quacks

### Cooling
You may have noticed how 80% of the toolhead is literally cooling ducts and blowers. What I have learned from printing PLA at high speeds, is that you need an INSANE amount of cooling. The toolhead incorporates 2 5020 Blowers and high flow ducts. Cooling is 100% integral when it comes to bridging, overhangs, and reducing elephant's foot. There also may or may not be plans to print even faster than it already does in the near future 😉.

![image](https://github.com/user-attachments/assets/3d53ac0f-7994-4b37-bc47-2ca11dbc47c8)

This multiplied by two and I should be able to cool whatever the heck I want.


### Extruder
The red thing on top is an HGX lite extruder. It has relatively good torque and is very light, but most importantly, They are CHEAP. I run one on my ender 3 and it works GREAT. With one LDO orbiter, you could buy 5 of these. The all-aluminum frame is also advantageous to reducing just how much the little nema-14 stepper will overheat under higher current running for more torque.

![image](https://github.com/user-attachments/assets/4484f2cc-6e5a-479e-bb5c-942f893c06ed)

At a dime a dozen, I still wonder why this isn't the number one extruder for budget high-performance printing.

### Hotend
Another thing to notice is the rather elongated looking hotend. While not as abnormaly long as the supervolcano on my ender 3, it is much lighter and yields similar if not better flowrates that a Phaetus, or a revo, at a fraction of the cost. This plus a CHT nozzle and a conversion might be the secret to mind-bogglingly high flowrates, without draining my budget.

![image](https://github.com/user-attachments/assets/163773ba-34d1-45f7-a1b3-b7acdd184bb3)

## Integrated Dampeners
Nowadays, pretty much any consumer available 3d printer is considered to be a "Desktop 3d Printer". Sure, they all fit on a table, or a desk, but all have one problem. Vibration. When the printer is actually printing at speeds beyond a snail's pace, They shake the table and often emit vibrations that use the giant table's surface as a resonating speaker to generate huge amounts of noise. Most printers try their best to counteract this with basic rubber cylinder shaped feet, but this often isnt enough, and makes the printer unstable. Since this printer is designed to print anywhere, It musn't be allowed to succumb to the effects of not having a 100000% perfect printing surface. 

![Screenshot 2025-03-25 2 47 49 PM](https://github.com/user-attachments/assets/1eb0bcc4-5827-42e2-8b10-c1fca462a38e)

On the outside, This looks like a conventional plastic block, with some rubber at the botton, but these are much more advanced than that. 

![Screenshot 2025-03-25 2 49 16 PM](https://github.com/user-attachments/assets/a2476012-04e6-4a32-8aae-b08e6841b170)

You might recognize the design! These take after the HULA vibration damping feet, however those are much more generalized and are designed to be a roughly one size fits all feet. These follow a similar design, but are revamped to do much, much more. They have much more travel space, and have reduced friction and are designed for the lighter, yet higher-frequency nature of the PandA. 

## Concluding Notes
And that concludes the CAD portion of PandA, for now... All that's left is to purchase parts and assemble the thing. I imagine things wont be perfect the first time round, so I'll find myself back here pretty soon....
