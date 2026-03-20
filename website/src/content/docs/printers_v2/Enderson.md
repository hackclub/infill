---
title: "Enderson"
description: "A 240x240x240 Fast Core XY 3D Printer Build from Scratch with feature like Autobed leveling ,Filament run out & etc"
project_name: "Enderson"
repository: "https://raw.githubusercontent.com/smartlearningorbit-arch/Enderson/refs/heads/main/JOURNAL.md"
---
**Repository link:** https://github.com/smartlearningorbit-arch/Enderson <br/>
**Total hours so far:** 32.3 Hr <br/>

- [✓] I have a 3D printer or will be getting one before March 21st  

 [Time lapse 1.0](https://hackclub.enterprise.slack.com/files/U0ADJ8KJK53/F0AKVMX5065/whatsapp_video_2026-03-09_at_3.12.27_pm.mp4) <br/>
 [Time lapse 2.0](https://hackclub.slack.com/archives/C08B7LF58TX/p1773322538954319?thread_ts=1773073754.786359&cid=C08B7LF58TX)   <br/>



# Routing the Belt 
## After understanding the whole Core XY system I jump over the Belt routing part
<img width="881" height="474" alt="image" src="https://github.com/user-attachments/assets/48c319b3-c9fb-47df-948a-726932f7fdea" />  <br/>

While building we have to consider Some Things in our mind
- The belt should be Parallel
- First thing is belt alignment, belt should be straight and parallel to the frame. If it is tilted then it can wear out fast and cause inaccurate movement.
- Proper belt tension is very important. If belt is too loose then it cause skipping and inaccurate prints, and if too tight then it can damage the pulley or put extra load on motor.
- Make sure both side belt length is equal, otherwise motion will not be balanced and it can create shifting issue.
- Pulley alignment should be perfect. Motor pulley and idler pulley must be in same line, otherwise belt will rub and create friction.



------
------
------
# log - 1.2Hr
## Understanding the core XY system 
~ Source - https://www.youtube.com/watch?v=_ramiM3KHYE <br/>
<img width="465" height="503" alt="Screenshot 2026-03-10 010805" src="https://i.ytimg.com/vi/_ramiM3KHYE/maxresdefault.jpg" /> <br/>
~ Source - https://www.youtube.com/watch?v=NMfFirtB1D4 <br/>
<img width="465" height="503" alt="Screenshot 2026-03-10 010805" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqPvSZ777N-qrL990a2eXe2XZl7v_7SVLgMw&s" /> <br/>


## what I learn 
how it works <br/>
In a CoreXY system, two motors ( let Suppose A and B) work together to control movement of the TOOL head . <br/>

| Motor A   | Motor B   | Toolhead Movement |
|-----------|----------|-------------------|
| Forward   | Forward  | +X (Right)        |
| Backward  | Backward | -X (Left)         |
| Forward   | Backward | +Y (Forward)      |
| Backward  | Forward  | -Y (Backward)     |

Main Point
- Same direction → X movement  
- Opposite direction → Y movement  

Short Trick to understand 
- A + B (same) = X axis  
- A + B (opposite) = Y axis  

So after


----------------------------
----------------------------
----------------------------




# Date/log - Friday, 17 March, 2026  0.7 Hr
## Analyse the problem 
After taking to Alot Of People. I found there Is Majoy Problem :


## Motion System Missing (Fixed) [✓]
- No belt exist
- No pulleys setup
- Motors exist but don’t drive anything
- No working CoreXY mechanism {JUST A CAD}


## Z-Axis Weak Design VIA @1mon (Fixed) [✓]
- No guide rail and linear rod
- it is very weak design
- cause Bad print quality or non working printer


## Tool head (Fixed) [✓]
- Incorrect fan position 
- No cooling duct (Not maintain the air flow)
- No space for Bltouch
- Centre of mass not manage 


## Structure issue and some geometrical issue (Fixed) [✓]

---------------------
---------------------
---------------------

  
# Date/log - Tuesday, 10 March, 2026  1.7Hr
## Preparing BOM 
After The design completed I making the BOM <br/> 
If you are Indian Here is something crazy detail for you Help me know the component Are expensive in India Plus importing from outside The taxes Will rob you So here is the few website Where you find the Component add good price And I also contact Few Indian Hack Clubber Regardingly And they have good experience with these websites previously.
### This not Sponsored This is my personal recommendation After conducting a search 
- [NOVO3d](https://novo3d.in/)
- [ROBOkits](http://robokits.co.in/)
- [Robu](https://robu.in/)


-------------------------
-------------------------
-------------------------


# Date/log - Tuesday, 10  March, 2026      9 hr 
## Breaking news — I am no longer buying an Ender 3 for scrap parts.
After conducting a long long long research, I came to a simple conclusion:
It is not worth that much money. <br/> 
Today I woke up at 11 AM and got back to work.
(I know it is late but I slept at 4:45 AM.) <br/> 
First I started working on the BOM (Bill of Materials).
While calculating the cost I realized something important. <br/> 
Buying an Ender 3 for ₹6000 is expensive if I use an external MCU instead of the Ender 3 board v4.2.2. <br/> 
So I searched for second-hand printers, but most of them were: <br/> 
- fully worn out
- used for thousands of printing hours  <br/> 
 So it doesn't make sense to buy them.
Then I started thinking:
If I don't buy a 3D printer, how will I arrange the parts that need to be 3D printed?  <br/> 
Finally I decided I can get them printed from:
- #printing-legion-india
- or some other printing sources.  <br/> 
I will also try to reduce the number of 3D printed parts.
New plan for the structure:
- Use aluminum sheet for mounting parts
- Use acrylic for the body  <br/> 
Print the final outer case after the printer is working, so it doesn't affect the print process.




-------------------------
-------------------------
-------------------------
 
# Date/log - Tuesday, 9 March, 2026  0.2Hr
## Finalizing the CAD model
After assembling most of the components I spent some time refining the model. <br/>
I adjusted the spacing between the gantry and the frame to make sure belts will not rub against the extrusion. <br/>

I also verified:
- belt path clearance
- stepper motor alignment
- mounting holes for the idler pulleys

These small adjustments are important because even a few millimeters of misalignment can cause mechanical issues later.<br/>

<img width="465" height="503" alt="Screenshot 2026-03-10 010805" src="https://github.com/user-attachments/assets/5abbfc4a-bad0-4bf6-980c-0600ba16d1da" />



-------------------------
-------------------------
-------------------------
 
# Date/log - Tuesday, 9 March, 2026  0.3Hr
## X-Axis Gantry Design
The X-axis gantry connects both sides of the Z frame and carries the toolhead.
Because the toolhead moves rapidly left and right, this part must be rigid.
If the gantry flexes even slightly, it can cause:
- layer shifting
- ringing
- inaccurate prints
To avoid this I increased the wall thickness of the gantry mount and added extra support ribs.
I also made sure the mounting holes align properly with the aluminum extrusion. <br/> 
<img width="997" height="791" alt="image" src="https://github.com/user-attachments/assets/8e42a581-3453-42a5-a91a-7835fdb3a724" />



-------------------------
-------------------------
-------------------------
 
# Date/log - Tuesday, 9 March, 2026  0.7Hr
## Built Idler Pulleys (Belt Guide Pulleys)
Where did the idler Pulleys To guide the belt Had this part I know that this part is so Sensitive and Broke at high tension So for that I ensured the minimum wall thickness 
And the strengthen the part <br/> 
Here it is <br/>
<img width="788" height="633" alt="image" src="https://github.com/user-attachments/assets/7cba9821-71c2-42fa-98ed-cb085df77b03" />


-------------------------
-------------------------
-------------------------
 
# Date/log - Tuesday, 9 March, 2026  0.6Hr
## Built a mount for the heat bed
Built a mount for the heat bed Ensuring The strength because it Have to carry The weight of aluminium heat bed + the Weight of model  <br/> 
And also we have to maintain the Tolerance Between the threads screw Even a small wobble can affect print quality at high speed 
<img width="842" height="606" alt="Screenshot 2026-03-09 134937" src="https://github.com/user-attachments/assets/d51f10fb-178e-4695-9732-8c0137a6af2a" /> 
<img width="902" height="606" alt="Screenshot 2026-03-09 135104" src="https://github.com/user-attachments/assets/37630a2b-b9b2-4235-ba95-bb4e63863d0b" /> <br/>

-------------------------
-------------------------
-------------------------



# Date/log - Tuesday, 9 March, 2026  1.2 hr 
## build Tools head of the printer
I plan to make Tool header as much light as possible cuz At the high speed And high acceleration, The high inertia make the problem So I reduce the weight so less inertia act and put the extruder at the side insead of Putting it with the Tool head <br/>
here you see <br/>
<img width="796" height="545" alt="image" src="https://github.com/user-attachments/assets/de2fae3f-6885-440a-aae1-b41081e4a74a" />
<img width="1068" height="769" alt="image" src="https://github.com/user-attachments/assets/c66d7070-1bf0-48fc-a153-95855f0d31c0" />





-------------------
-------------------
-------------------

# Date/log - Tuesday, 9 March, 2026  0.7 hr 
## Make the Lead Screw Support Bearing
so To prevent Lead Screw from Vibration i make a Lead Screw Support Bearing That provider strength to rod plus it help to improve the Quality of the printer At high speed <br/> 
<img width="637" height="535" alt="image" src="https://github.com/user-attachments/assets/08098309-f3b0-4591-b535-4088395cec94" />



-------------------
-------------------
-------------------
 
# Date/log - Tuesday, 9 March, 2026  3.9 hr 
## Assembling the component 
Assemble all the component in the In a shape of printer Where I ensure that The weight distribution should be perfect  
also Make the Bracket for the stepper motor to be hold 
<img width="839" height="693" alt="image" src="https://github.com/user-attachments/assets/56299560-b6c9-40ab-9fb4-e7cce76d0c35" />


-------------------
-------------------
-------------------
# Date/log - Monday , 9 March, 2026           2.1 hr 
## Research & plan 
Mt first thing that i check that the BOM are Available in India and While checking that I found out The raw component is Expensive. Delivery date may be high 
Show my new approaches is to buy a Ender 3 at 13k Rs And tear down it fully To grab the raw component And one more Reason is that The printer build may contain some 3d printed parts which Need to be printed but I dont have A 3D printer now it Should help me to print the parts also 
### the component I get after tear down the 3D printer
<img width="1078" height="761" alt="image" src="https://github.com/user-attachments/assets/03aaa20a-286d-4a47-b95b-5bdb15c57b1a" /> <br/>
- NEMA 17 4x
- 24v 15A power supply 
- heat Bed 
- Hotend Assambley + NOzzel
- Colling Fans x 3 
- Aluminium extrusion
- LCD disply
which is the good package at that prize point 
~ Source - Official BOM + https://www.youtube.com/watch?v=5aGzGpcsVZY / https://www.youtube.com/watch?v=dgxH_Si9KCA

----------------
----------------
----------------

# Date/log - Sunday, 8 March, 2026 / 6.5 hr  
## Research & Plan  

Today I worked on planning what features should be included in my 3D printer. <br/>  
Instead of randomly building things, I wanted to first decide the capabilities and design direction of the printer. So I started by making a **feature list** of everything that should be part of the machine. <br/>

Here is the list I made *(please ignore my writing)*  
<img width="280" height="1164" alt="image" src="https://github.com/user-attachments/assets/7636f9e1-0583-4105-b660-580b152ca45a" /> <br/>

At first this list might look simple, but reaching this point actually required **a lot of research and thinking**. <br/> 

I didn’t just write random features. For each item I tried to understand:  
- Is this feature actually useful for the printer ?  
- Will I get the component in India?  
- Will it improve reliability or print quality? <br/>

So this list is basically the result of **many hours of comparison and research**.
## What I researched while making this list <br/>

While creating this feature plan, I explored different topics such as:
- Common features used in modern DIY 3D printers   
- Firmware support for different functions  
- How these features affect print quality and reliability <br/>

This helped me decide **which features are important and which are unnecessary** for my build.
## Resources used

To gather this information I used multiple ~ sources:
- **#infill Slack Community** *(really helpful!!!!!!!!!!!!!!)*  
- Tutorials  
- Documentation  
- AI  <br/>
Using multiple sources helped me verify information and avoid wrong assumptions.



## Outcome of this research
By the end of this session I now have A clear **feature list** for the printer  
here It is <br/>
<img width="568" height="733" alt="image" src="https://github.com/user-attachments/assets/7189edb1-24d2-4484-97a1-18977de32084" />




--------------------------------
--------------------------------
--------------------------------


# Date/log - Saturday, 7 March, 2026 / 5.4 hr
## Research & Plan

I'm good with hardware and electronics, but I never made a plotter-based project before.
And a 3D printer works on the same basic principle as a plotter — controlled movement on X, Y, and Z axes. <br/>
So before starting the build, I decided to properly understand the architecture. <br/>
## First 2.4 hours — Understanding the basics

In the beginning I focused on learning the core concepts of how a 3D printer actually works. <br/>

### Some of the main things I researched were:
~ Source - https://www.youtube.com/watch?v=qub5chyIQ0s&t=4241s
- How Cartesian motion systems work
- How stepper motors control precise movement
- The role of G-code in controlling printer motion
- How the hotend and extruder system push filament
- Basic printer electronics like MCU, stepper drivers, and endstops
- This helped me understand the overall architecture of the machine.

## Next 3 hours — Tutorials and deep research
After understanding the basics, I spent the next 3 hours watching tutorials and technical explanations.
In total I watched 50+ tutorials and guides abou

### I tried to analyze the mistakes people make while building printers, such as:
~ Source https://www.youtube.com/watch?v=c9AS3uP0Lzw&t=17s
- weak frame design
- poor cable management ( It makes difficult to Repair in future)
- incorrect belt tension & Not equal Belt ( Break the pully)
- bad placement of electronics { Causing heat Issue and Not proper weight balance } <br/> 

Understanding these mistakes is important because it helps me avoid them while designing my own printer.
What I learned from this research

This research phase was important because it will help me plan the printer more efficiently before starting the actual build.
