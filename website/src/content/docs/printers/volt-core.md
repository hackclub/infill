---
title: "VoltCore"
description: "Battery-powered 3d printer to print without access to any nearby outlets!"
project_name: "Volt-core"
repository: "https://raw.githubusercontent.com/TheRealMopcornPuncher/VoltCore/refs/heads/main/CAPTAINSLOG.md"
---
Made by: @Amaya
Repository link: https://github.com/TheRealMopcornPuncher/VoltCore
Total hours so far: 18 hrs 5 mins
- [x] I have a 3d printer or will be getting one before March 21st
---
< Briefing >
A silly concept accidentally turned reality
Pitch: An extra portable and partially remote solution to printing without an active power source

---

# Day 0 - Preparations and planning

### Feb 4, 2025

I began by generating a timeline for me to operate within, as to avoid me procrastinating and not finishing the project at all.

**Deadline: Feb 11**

- Finalize battery system and power management.
    
- Generate a rough BOM (electronics, motors, extruder, frame materials, etc.).
    
- Confirm which parts I can salvage from my spare Sovol SV01 Pro.
    
- Research and select a control board + firmware (e.g., Klipper or Marlin).
    

**Deadline: March 31** _(Finalized Design & Parts Ordered)_

- Design a compact frame in CAD, ensuring it satisfies a small size profile (X and Y dimensions are 6-7 inches).
    
- Simulate motion system (belt routing, pulley positioning, etc.).
    
- Plan the mounting locations for electronics and battery.
    
- **Finalize the design and order all necessary parts.**
    

**Deadline: April 14** _(All Parts Arrived & Assembly Begins)_

- Assemble frame and install motors, belts, and pulleys.
    
- Wire up control board and power system.
    
- Perform first motion tests (homing, jogging, etc.).
    
- Mount and test the extruder and hotend (ensure >220°C capability).
    
- **All parts should be in by this date to stay on track.**
    

**Deadline: April 28**

- Flash firmware and configure motion system.
    
- Tune motion system and stepper settings.
    
- Ensure power consumption is within acceptable limits.
    
- Run first test prints and refine print quality.
    

**Deadline: May 4** _(Final Benchy Print Verified & Ready to Ship)_

- Complete final tuning and ensure prints are high quality.
    
- Verify folding mechanism and portability.
    
- Confirm battery efficiency for intended use.
    
- **Must have a successful Benchy print by this date!**
    

**Deadline: May 6** _(Ship Everything or Carry it with You)_

- Pack the printer securely for shipping.
    
- Ensure documentation and necessary tools are included.
    
- Consider taking it as a carry-on for guaranteed arrival.
    

Besides this, I've also done some research on suitable parts. Mostly minimal. Total time elapsed: 2 hours

# Day 1

### Feb 5, 2025

I felt pretty energized with the project today so I decided to start working on pushing my project into the tank with the others. (Started writing and journaling today, previous entry was made up for yesterday.) I intend to jot some stuff down into the BOM and continue fleshing out my solution for power. Mostly stuff from my first deadline/checkpoint.

I started my BOM by snatching and customizing a template for it off the web in google sheets. After creating the BOM, I started looking for the components I'd need to assemble the frame, and I got a recommendation for some of the nicest prices and highest class extrusions I could find from a company called 80/20 LLC.

After getting the link to the extrusion, I was going to start modeling it in Fusion 360, when I proceeded to fall down a rabbit hole of logo design. In the end, I installed Inkscape and began learning how to craft a nice looking logo to slap over the rest of this project.

I decided to take a break from learning how to use Inkscape. After hopping into a call with my brother and ranting about the project, he suggested I use a single motor for the Z-axis linked via a belt to support all sides of the bed (Maybe via linear rods/rails?)

Total time elapsed: 1 hr 40 mins

---

# Day 2

### Feb 6, 2025

Today was a little hectic so I'm mostly just pushing myself to keep going for the sake of progress. Maybe I'll get some coffee... besides the point though.

Attempts to fill out my bill of materials went pretty good today. I got a lot done in terms of meeting my Feb 11th deadline. The help of my brother, who's an experienced engineer, came in handy quite often since he knew more about this than I did, and told me whenever I added something that wouldn't work to the BOM, as well as giving me recommendations on where to look and what I could use.

I also am deciding to keep track of what 3d printed parts I'll need to model and make for this printer to function:

- Bed mounting bracket
    
- Extruder fan shroud and mounting bracket
    

Total time elapsed: 2 hrs 25 mins

---

# HIATUS PERIOD: Feb 6th - Feb 12th

### Project resumed.

I'll admit, I gave up. I didn't think I knew enough, I ran out of motivation, and there it just felt like this whole thing was a waste of time for someone inexperienced like me.

Then, I rejected that philosophy. Of course there was going to be hurdles, there always is. I just needed to get back up and keep working. Nothing I've ever done happened unless I told myself I could be capable, and I'm doing that right now.

---

# Day 3

### Feb 12th, 2025

Running partially behind schedule, I knew I needed to catch up, so I decided to use my time on this day to finish my B.O.M. and move on.

My biggest issue was the cost of the parts. In their current state, I was up to over 300 dollars, and not even completely done with the list. To cut down on cost, I began looking for cheaper alternatives to my existing parts.

I devised a plan regarding the frame: The bed would be 3d printed at a size contained inside of a 100mm by 100mm space and would be covered with masking tape. Frame will be joined with aluminum extrusions and metal brackets, then reinforced with 3d printed corner braces.

I ended up revising literally everything in my BOM and got the price down quite a bit. The next steps would be to figure out what I'm doing for my extruder and hotend, cooling fans, and my z axis.

Total time elapsed: 2 hrs

---

# Day 4

### Feb 17th, 2025

I ended up getting sick for a few days which kinda... super sucked, but I'm back and feeling moderately okay. I'm running low on time to meet my deadlines so it's time for me to reorganize and plan out what I'm doing next. Only really one of these needs a change.

**Deadline: Feb 20**

- Finalize battery system and power management.
    
- Generate a rough BOM (electronics, motors, extruder, frame materials, etc.).
    
- Confirm which parts I can salvage from my spare Sovol SV01 Pro.
    
- Research and select a control board + firmware (e.g., Klipper or Marlin).
    

I ended up finishing an entire disassembly in about an hour and a half.

Total time elapsed: 2 hrs

---

# Day 5

## March 30th, 2025

Panic time!!! The deadline is very very close and I don't entirely know if we'll be getting an extension. To combat this, I've invited one of my closest friends to help me with the project. It also helps that he knows significantly more than I do, and is an extremely fast worker. 

We've gotten the BOM pretty much completed, all that's left to do know is model and joint everything in Fusion 360 so we can see what we're missing and revise the BOM based on that data. Jonathan, my friend, ended up modeling a few things last night, which is why I'll be taking up modeling as much as possible for my current task of the day. 

I almost forgot to mention one of the more important changes we made to the project. We ended up having to change the motion system from corexy to cartesian. Ultimately, the decision was just made due to time constraints and the complexity of the corexy motion system, which we are simply not prepared for.

I intend to work all day.

Organization is key to this project, so I'm going to be modularizing and listing the parts of the printer I will need to model here:

Frame
	3x 100mm extrusions for the bottom
	2x 200mm extrusions for sides extending up
	1x 100mm extrusion for connecting 200mm extrusions at the top of the structure
	2x 200mm extrusions for the x-axis and the y-axis
Gantry (X-axis)
	Printhead: Extrusion and hotend assembly
	Stepper controlling movement
	200mm 2020 Extrusion
Buildplate/Bed
	Mounting solution to base of device
	200mm 2020 Extrusion
	(Mount higher in the structure to accommodate large battery)
Base
	Housing for electronics and IO/other interfaces
	3x 100mm 2020 Extrusions
Z-Axis or as I like to call it, "Elevator"
	Dual support from Z-axis lead screws, must allow gantry to travel up and down
	Stepper controlling movement
	2x 200mm 2020 Extrusions

Total time elapsed: 7 hrs

---

# Day 6

## March 31st, 2025

I made an immense amount of progress yesterday and I honestly feel like completing this project is very much possible. Although I had tasked my partner with creating a voltage regulator, I very stupidly forgot to specify what for... so I now need to create a voltage regulator. again. This time with the LM2576-5.0 voltage regulator, since *it* will work between the battery and the mainboard. Which, might I add, isn't much of an impressive battery TT

Since I'm very... uh... for lack of a better term uneducated, I'll be using Fusion 360 to design my PCB. Additionally, Fusion 360 and I seem to share that trait, so I'll need to give it some of the libraries myself, instead of being able to just find what I need in the software. Very fun stuff.

UPDATE: I let my partner know about the correct specifications and he agreed to revise it himself, yippie :D

I've also worked out our extruder situation considering the E3D V6 Hotend I picked earlier. This was important, because my stupid #$% didn't realize you... didn't have to design an extruder from scratch.... oh well.

We'll be using the E3D Titan Extruder.

All of this in mind... I'm fairly confident I can just- START with the final CAD model tomorrow :DD 
EXCITINGGGG

*I love you spring break <3*

Total time elapsed: 3 hrs

___

# Day 7

### April 1st

