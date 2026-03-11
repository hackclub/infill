---
title: "Enderson"
description: "A 240x240x240 Fast Core XY 3D Printer Build from Scratch with feature like Autobed leveling ,Filament run out & etc"
project_name: "Enderson"
repository: "https://raw.githubusercontent.com/smartlearningorbit-arch/Enderson/refs/heads/main/JOURNAL.md"
---
**Made by:** @Paglu // Robotic Paglu <br/>
**Repository link:** https://github.com/smartlearningorbit-arch/Enderson <br/>
**Total hours so far:** 61 Hr <br/>

- [✓] I have a 3D printer or will be getting one before March 21st  

# Date/log - Tuesday, 10  March, 2026      13 hr 
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




 
# Date/log - Tuesday, 9-10 March, 2026      / 18 hr

## Designing the printer

After all the planning is done I finally started designing the **3D printer**.  
This step take a lot of time because many parts I decide to **make from scratch** instead of using ready made models. <br/>

Some of the parts I worked on while designing:

- Frame layout and overall structure  
- Motor mount positions  
- Linear motion system placement  
- Electronics mounting area  
- Belt path and pulley placement  <br/>

Since this is my first time designing a **full printer**, I had to re-check many things again and again to make sure the alignment and spacing is correct. Also tried to keep the design **simple but strong**, because weak frame can cause vibration which affect the print quality alot.  <br/>

Many small small adjustment were made during this process like:
- changing mount holes 
- adjusting motor position  
- fixing spacing issue  
- making sure parts are printable  <br/>

Also there are many thing that i build from Scratch like ts heatbed mount where i have to ensure the Strength <br/>
here U see what i am taking about <br/>
<img width="842" height="606" alt="Screenshot 2026-03-09 134937" src="https://github.com/user-attachments/assets/d51f10fb-178e-4695-9732-8c0137a6af2a" /> 
<img width="902" height="606" alt="Screenshot 2026-03-09 135104" src="https://github.com/user-attachments/assets/37630a2b-b9b2-4235-ba95-bb4e63863d0b" /> <br/>


 
Some parts are still **rough and might be improved later**, but for now the main structure of the printer is ready.  
So here is the **final reveal of the printer design**  

<img width="465" height="503" alt="image" src="https://github.com/user-attachments/assets/cdb8ab3a-6667-40ba-993a-b0603e7a0d3c" />  <br/>

Still some improvement might come later during the build process but the **base design is completed now**.  
Next step will be checking parts compatibility and preparing the **BOM**.




# Date/log - Monday , 9 March, 2026           3 hr 
## Research & plan  3.7 hr
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
## Let's start with the body Designing 





# Date/log - Sunday, 8 March, 2026 / 14.5 hr  
## Research & Plan  

Today I worked on planning what features should be included in my 3D printer. <br/>  
Instead of randomly building things, I wanted to first decide the capabilities and design direction of the printer. So I started by making a **feature list** of everything that should be part of the machine. <br/>

Here is the list I made *(please ignore my writing)*  
<img width="280" height="1164" alt="image" src="https://github.com/user-attachments/assets/7636f9e1-0583-4105-b660-580b152ca45a" /> <br/>

At first this list might look simple, but reaching this point actually required **a lot of research and thinking**. <br/> 

I didn’t just write random features. For each item I tried to understand:  
- Is this feature actually useful for the printer ?  
- Is it possible to implement with the hardware I plan to use?  
- Will it increase complexity t00 much!!! ?  
- Will it improve reliability or print quality? <br/>

So this list is basically the result of **many hours of comparison and research**.
## What I researched while making this list <br/>

While creating this feature plan, I explored different topics such as:
- Common features used in modern DIY 3D printers  
- Hardware requirements for each feature  
- Firmware support for different functions  
- How these features affect print quality and reliability <br/>

This helped me decide **which features are important and which are unnecessary** for my build.
## Resources used

To gather this information I used multiple sources:
- **#infill Slack Community** *(really helpful!!!!!!!!!!!!!!)*  
- Tutorials  
- Documentation  
- AI  <br/>
Using multiple sources helped me verify information and avoid wrong assumptions.



## Outcome of this research

By the end of this session I now have:
- A clear **feature list** for the printer  
- Better understanding of what is **practical to implement**  
- A direction for the **next design steps** <br/>

This planning step is important because it will guide the **mechanical design, electronics selection, and firmware configuration** of the printer.







# Date/log - Saturday, 7 March, 2026 / 12.5 hr
## Research & Plan

I'm not joking here!! — it really took this long. I'm good with hardware and electronics, but I never made a plotter-based project before.
And a 3D printer works on the same basic principle as a plotter — controlled movement on X, Y, and Z axes. <br/>
So before starting the build, I decided to properly understand the architecture. <br/>
## First 3–4 hours — Understanding the basics

In the beginning I focused on learning the core concepts of how a 3D printer actually works. <br/>

Some of the main things I researched were:
- How Cartesian motion systems work
- How stepper motors control precise movement
- The role of G-code in controlling printer motion
- How the hotend and extruder system push filament
- Basic printer electronics like MCU, stepper drivers, and endstops
- This helped me understand the overall architecture of the machine.

## Next ~8 hours — Tutorials and deep research
After understanding the basics, I spent the next 8 hours watching tutorials and technical explanations.
In total I watched 50+ tutorials and guides about:

- 3D printer mechanics
- Motion systems
- Frame design
- Common hardware mistakes
-  Firmware basics
- While watching these, I wasn't just watching randomly. <br/>

### I tried to analyze the mistakes people make while building printers, such as:
- weak frame design
- vibration problems
- poor cable management ( It makes difficult to Repair in future)
- incorrect belt tension & Not equal Belt ( Break the pully)
- bad placement of electronics { Causing heat Issue and Not proper weight balance } <br/>

Understanding these mistakes is important because it helps me avoid them while designing my own printer.
What I learned from this research
### After this research session I now have a better understanding of:
- Basic 3D printer architecture
- Motion system design
- Common design mistakes
- Key components required for the build <br/>

This research phase was important because it will help me plan the printer more efficiently before starting the actual build.
