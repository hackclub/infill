---
title: "VoltCore"
description: "Battery-powered 3d printer to print without access to any nearby outlets!"
project_name: "Volt-core"
repository: "https://raw.githubusercontent.com/TheRealMopcornPuncher/VoltCore/refs/heads/main/CAPTAINSLOG.md"
---
Made by: @Amaya and @Jonathan G 
Repository link: https://github.com/TheRealMopcornPuncher/VoltCore
BOM: https://docs.google.com/spreadsheets/d/1q4xtd6th8_cM6Qn8iwp2R4_8qS0gYeFDji75B9E_PQI/edit?usp=sharing
Images: https://docs.google.com/document/d/1O2JPVw-2Jhm0MzPRCLd0zcRRRKDtKQYV07AwvWWCOpY/edit?usp=sharing

Fusion 360 PCB link: https://a360.co/4jejSvC (DEPRECATED - DOES NOT WORK)
Fusion 360 Printer assembly link: https://a360.co/3RkSeRq

Total hours so far: 82 hrs 5 mins
- [x] I have a 3d printer or will be getting one before March 21st

---
NOTICE! Print files and quantity specifications listed in STLs folder on github repo. I'm printing all of the files in PLA with standard infill (lol) and 2mm layer height. Basic settings. Tolerances are baked into the models. NOTICE END!

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

We'll be using the Sherpa Mini.

All of this in mind... I'm fairly confident I can just- START with the final CAD model tomorrow :DD 
EXCITINGGGG

*I love you spring break <3*

Total time elapsed: 3 hrs

___

# Day 7

### April 1st

My computer exploded and I lost all of my project files.




Just kidding. :3

Today I've decided to model the full printhead. To do this, I'll need to create a holding mechanism or structure for the E3D V6 hotend that links up to the Sherpa Mini extruder. Shouldn't be too hard, but then, what do I know lol.

NOTES: Self supplying 2x motors with pre-fastened timing pulleys for the X and Y axis, self supplying 2x additional motors and flex couplings for Z axis (Will need to purchase lead screws). This leaves only one motor to be actually purchased for the extruder.

It's going to be tricky with clearance, but I just need to design an adapter between the E3D's obnoxious 16mm notch connector thingy and the even more obnoxious space consuming Voron M4 extruder (Which by the way we're using now instead of the Sherpa because it's so insanely inexpensive.)



Total time elapsed: 1 hour

---

# Day 8

### April 3rd

It's been an abysmal pain trying to use all of the models I've collected for this project for reasons beyond me. Despite that, I've continued to make progress, although extremely slowly. I've got no idea what I'm doing with this project and it's driving me insane.

Today, I hope to actually model the stupid gantry, but luck seems to despise me as of recent.

To make things different from my multiple prior attempts to design this, I'll be designing it in reverse, starting from the mount attached to the 2020 extrusion acting as a frame for the x-axis, and working my way up to the hotend.

Holy molay I forgot just how much music helps me to get out of depressive moods lol. I LOVE YOU RWBY SOUNDTRACK.

Also sidenote why do I write like... idk something fancy whenever I'm upset lol???

MODELING IS GOING GREAT I'VE DONE SO MUCH ON THE MOUNTING PLATE FOR THE PRINTHEAD YIPPIEEEEEE!!!

Update: Spent 3 hours modeling something I didn't need :D I LOVE LIFE GUYS I LOVE MY LIFEEEEEE!!!11111

(Also personal note: Pester my elder engineers more)

I know what I'm doing now. Just added a full kit of the ender 3's POM wheels and spacers to the BOM, so I'll just need to model or scrape those from somewhere to get them in Fusion 360 :P

GODSPEED TO YOU FUTURE ME

Total time elapsed: 4 hrs

---

# Day 9

### April 4th

New day, new stuff. I'm fetching the models for the "Isolation Column" and 5mm eccentric spacers I need to the POM mounted motion systems

Updating most of the spacers/washers, lock nuts, and other components in my final printhead/gantry assembly to fit with an M5 screw since I previously modelled them to interface with M4 screws.

After about 2 hours I finished redesigning the mounting plate for the printhead. Later today after a break, I'll model the notches for the ends of the belt and the mounting system for the extruder.

I forgot to log most of what I was doing so I'll speed run explaining all of it really really quickly. OKAY SO. I imported the aluminum extrusion (2020 x 200mm) and modeled everything around it, since HEY y'know, kinda a STUPID amount easier when you're modeling stuff in decending order of importance.

So anyways, I started with the extrusion, slopped in the POM Wheels and jointed them to the rail in Fusion 360, gave it a sliding joint because why the flip not (I spent way too much time doing that in school to not use it here), then I made a plate using the projected positions of the wheels hugging the extrusion. This was helpful because it allowed me to get a really good estimation of where the holes in the plate would need to be.

Then I had to research how to fasten the wheels to the plate and tighten them on the aluminum extrusion. To do this I simply stared at an image of the ender 3 and drank an abnormal amount of coffee before getting extremely jittery and crying over stupid stuff for like 2 hours. After this mindbogglingly stupid way of research, I learned what I was doing wrong. Eccentric nuts need a slot in the mounting plate to rotate in, otherwise they're useless.

Oh also yes I literally just stole I mean stole I mean stole I mean- borrowed the x-axis/gantry design of an ender 3. I LEARNED SOMETHING REGARDLESS, SO I DON'T WANNA HEAR IT, SHUSH.

BUT ANYWAYS, after figuring out what spacers to use, how the eccentric nut worked, where I could buy everything, etc. I got to work again. I put those holes into the mounting plate and then jointed everything together, spacers and all. That made me really happy and I thought I was done, but then I was like "wait no there's literally nothing on that plate", and so you'll never guess what I decided to do next. Actually I slept for like 10 hours, but AFTER THAT, I modeled.. heh.. you guessed it, a TRIANGLE SHAPED HOLE! ....It helped remove unnecessary material okay?

After wasting wayyyy too much time on that, I moved on to modeling the slots/notches for the belt, that was simple enough (HAHA NO JK IT TOOK HOURS AND AT LEAST 5 SEPERATE REDESIGNS. ALSO I CRIED AGAIN). After the notches were modelled I decided to move onto making a mount for the extruder, which took the most time by a LONG SHOT. I kept projecting sketches, revolving circular depressions, and otherwise just fumbling around with it until it looked semi-functionable. Then I fumbled with it some more and got this kind of like, pressure mount? You have to screw a plate that compresses the E3D V6 hotend into a groove that keeps it tightly secured. HOPEFULLY, THAT'S ENOUGH.

I already KNOW this is gonna be a major p.i.t.a. when I print it, but that's a future me problem.

Something ended up happening so I decided to work the rest of the night until early morning to take my mind off things, as I typically do to take my mind off of things.

Ended up modeling a shroud and mount for the 5010 blower fan I've decided to use for print cooling, so that's nice. It only took an additional 2 hours... TT

Christ I'm still going and it's 12:31 A.M.... waiiit I need to switch logs.

Total time elapsed: 12 hrs

---

# Day 10

### April 5th

Got my partner to start working on the project again, surprisingly we're both nocturnal. 

I did a lot today, not as much as yesterday, pretty sure that was like a one time thing (I ended up sleeping until after 12pm today, so safe to say we won't be trying that again lol).

Today I've decided to work on the Z-Axis and adding in the stepper motor for the x-axis, which should in all honesty be connected to the same mounting plate as the z-axis carriage. If you don't know what that means, I didn't either when my brother was explaining it, but after brute forcing the design a few hours, I think I understand it now.

Spent most of the day modeling the Z-axis when I learned I had to redesign almost everything because it couldn't be 3d printed and still function well.

yay.

Total time elapsed: 6 hrs

---

# Day 11

### April 6

I have today and maybe 1 or 2 hours (thanks American education system for taking away any liberty over my own personal life) to finish this entire design.

I do not believe it's enough time, considering I have to redesign literally everything to be under budget again, but I'm not going to sleep, so I intend to use every hour available.

Just a note, I have m3, m4, and m5 t-nuts

Current total cost of BOM excluding taxes and shipping sits at $239.86

Spent a little time organizing everything into folders in fusion 360 so I can stop scrolling all the damn time.

NOTE: Use M4 screws to mount printhead carriage. 

Added 0.5 tolerance to the hotend mounting brackets.

Printhead assembly now contains both interference fittings for the linear bearings (2 rods per axis, excluding Y with it's linear rail), and a mounting bracket for the hotend. I'll add the print cooling fan and BL-Touch later today.

Finished the printhead at the end of the day
Fasteners are obnoxiously large.

Total time elapsed: 8 hrs

---

# Day 12

### April 8th

Hoping to finish designing the gantry today. I created a tensioning bracket to hold the linear rods yesterday, a simple clamping shape that fits around the rods and is held together via one M4 and two M3 screws. Didn't document it though because I only just finished designing that.

My current design challenge of the day is modifying that same bracket to include space for a linear bearing (For the Z axis) and a stepper motor to drive the X axis.

I am currently approaching this design by adding the linear bearing on the back of the tensioning bracket. Adding the lead screw will be harder, though. After asking my brother (Thank you big brooooo lmfaooo) I learned that the hardware I need is called a "lead screw nut", and I'll need to model a part on the tensioning bracket to hold it very, very securely. I found a pack on amazon, 250mm lead screws and lead screw nuts, perfect for the project. I added them to the BOM, and got to work adding the lead screws into my CAD model for the gantry. It'll be a little bit difficult since I'm trying to keep the size of the tensioning bracket down as much as possible, however it should be possible to fit them both onto the bracket if I move the linear bearing towards the center, and the lead screw somewhere near the edge.

Ended up opting for the kit with only one screw and one nut, so total cost is down to $244.95, which is dangerously close to my limit, but we're still floating.

I realized far too late that the tensioning bracket's current design makes it impossible for the x-axis to move, and that the way I had intended to move it originally wasn't possible to begin with. I'm now redesigning a small part on the tensioning bracket to make space for the new motion system, then I'll redesign a small part of the printhead to interface with the belt properly.

It took many hours, but after making things bigger and smaller over and over again, everything finally fits, and the parts are beautiful. I just have to design the right side version of the tensioning bracket for the linear rods and we're pretty much done for today! Gantry done and over.

Worked until really late, but the entire gantry is finally finished. Tomorrow, I'll work on the Z-axis.

Total time elapsed: 8 hrs

---

# Day 13

### April 9th

After about two hours, I fixed a few glaring issues with the gantry. I forgot to add an idler pulley to the right brackets (timing pulley was on the left side already), so I did that, and then I modified the print head so that the notches for the belt were in the correct locations and not on an entirely different axis... TT

Moving on- I'll be working on the z axis today. I don't actually know what that part is called- sorry.

I'm going to start by putting two linear rods in. That'll be the last two I have available from the BOM, so for the last axis (Y), I'll use my linear rail. To start, I need to collect the distance of the linear bearings (specifically their center), and replicate that with the position of the linear rods in the z axis part of the gantry... wait omfg this means I'm not done with the gantry doesn't it. Oh well.

When does this count as the frame in my books? Idk. I guess when you make A FRAME. ??? lol
From now on, I'm just going to call this next part "UPPIES" because I can't think of a technical term, and I'm chill like that

After a quick edit, I just changed the spacing of the linear bearing's centers to EXACTLY 220mm. I would have preferred 240, since the spacing would be like 20mm + 20mm (since 2020 extrusions) + 200mm (The extrusion between two extrusions), but I can get creative and make it work anyways.

Wait no technically this would count as part of the frame, because I'll need to design some of it for this anyways-

WELL, FRAME TIME.

Wait also I just realized- 220mm spacing works perfectly because I forgot to divide the 20mm length since we're imagining the center of the aluminum extrusion... Yay :3

After moving stuff around in CAD for a bit, I settled on a layout/setup for the frame. It was so perfect, that I didn't even need 300mm long 2020 extrusions, only 200mm long ones, so I deleted the 300s from my BOM and saved a few bucks by just doubling the 200s. Very nice :D

I created a specialized corner bracket to hold the linear rods in place using the same kind of tensioning plate as the x-axis portion of the gantry.

It looks really really ugly though lmfao.

To drive the Z axis I've decided to take a page out of the Prusa Mini's book and mount the stepper at the top of the printer, facing down.

Is current total $244.6 with the additional hardware. Cut costs ever so slightly by ditching the limit switch and finding a cheaper 4020 axial fan.

Did a lot of research today and learned about thrust bearings, which is the additional hardware I mentioned earlier. It's extremely helpful for mounting the stepper upside down, but it's also nice that I learned something pretty cool today :D

Didn't get a whole lot done because of the research breaks, but I still did a lot today and I can be proud of that. I estimate I should finish this project either before or during Saturday. Before I end today's work, though, I'm going to add the new models for the new additions to the BOM. Just two things, won't take very long if I'm lucky enough to find premade step files for the parts.

Total time elapsed: 7 hrs

---

# Day 14
### April 10th

We're practically in overtime now and I need to finish everything immediately. I still have to fix a few things on the Z-axis, mount the electronics, finish the Y-axis, and find out our power situation. Let's begin then:

I DO not want to solve the battery issue, so I'll start with it. I need a battery that's close to 24 volts.

I have little to no experience, so I'm going to spend a few hours reading up on voltage regulators and creating PCBs in Fusion 360.


[ PROJECT TERMINATED AND RESUMED ON APRIL 14th ]

Total time elapsed: N/A

---

# Day 15
### April 14th

We're on a tight deadline as usual so I have to make this quick. This is the outlook of our current schedule by order of importance:

1. Revise BOM to operate within budget and time constraints (Today/Immediately)
2. Finish designing Z axis (Today/Immediately)
3. Finish designing Y axis (Tomorrow)
4. Extruder mounting and filament holder at top of frame (Tomorrow)
5. Electronics mounting and battery situation (Tomorrow)
6. Printer review (Tomorrow)
7. Purchase parts (After review, est. 4/15-4/17)
8. Assemble printer (When parts arrive, est. 4/22-4/23)
9. Test for any major issues and fix immediately (est. 4/22-4/23)
10. Ship battery to location (est. 4/23-4/24)
11. REP RAP!!! (May 16)

So, as the schedule suggests, I'll start by revising the BOM. We'll remove most things and rearrange them, starting with the battery. It's important that I get an estimate of the total cost of everything ASAP so my partner can find a suitable battery while we work in tandem.

The battery will be hot swappable now to ensure ease of installation when we ship it to the festival.

Keeping track of everything that I delete from the BOM:
1. Original GT2 6mm belts from Creality (Scrapped them myself)
2. Ferrule connectors (Don't need them anymore for new battery design)

I saved additional funds by disassembling the Sovol Sv01 I've been hollowing out completely.

Now that the BOM is revised, I'm going to continue modeling the rest of the motion systems while my friend works on our power situation.

Total time elapsed: 3 hrs

---

# Day 16
### April 15th

Modeling day. I need to have the entire thing ready for review for tomorrow.

I modified the brackets so that the screws wouldn't collide with the aluminum extrusions, then rejointed everything in the frame. Next up is assembling the thrust bearing housing bracket.

I'm looking at the weight distribution of the flipped Z axis motion system, and we'll most likely need to put something underneath the thrust bearing housing bracket. I suggest something rubber-like with an adhesive backing, but we'll most likely just shove a folded shirt under it at the actual festival.

Minor adjustments to the thrust bearing housing bracket were made to allow the top washer to make exclusive contact with the shaft collar, since the previous design had little to no clearance between the 3d printed part and the shaft collar, which would have rendered the thrust bearings useless.

I noticed that the gantry would need to be updated to accommodate our belts so I completely revamped the right clamps. For all of these clamps, I've modeled two brackets that hug the linear rod, one bracket always slightly thinner so that if the two halves were to touch, they would not form a complete circle. This intentional bit of removed material gives an offset that a screw can utilize to tighten around the linear rods.

With the same concepts I learned designing the bracket the first time, I strived to recreate it with a belt tensioner. After the revamp, I reassembled the gantry (had a few issues with Fusion randomly not letting me save things :/ thanks guys) and went to bed for my pre-act test the following morning (YIPPIIEEEE (not)).

Total time elapsed: 4 hrs

---

# Day 17
### April 16th, 2025

As crazy as it is to think about, I'm actually almost entirely done with my work. That's just completely insane to think about considering how for most of this project, I felt like I'd always have half a dozen more things to do until the end of time, but no. We're really in the home stretch (fingers crossed I didn't just jinx it.)

Today I plan to finish the Y-axis, and it'll be the easiest of the three to be entirely honest. It's comprised of 3 components (not always just in my design): the underplate (what I'm calling the thingy underneath the buildplate), the mounting bracket (shaped like an X, screws to the part underneath which is the next item), and the spacing bracket. 

It took barely more than 2 hours and I finished modeling all of the components. I then jointed everything and double checked if I missed anything. I forgot the belt. Obviously you... you kinda need that. TT.

In the upcoming parts of this journal I'll attempt to add images, not really sure how to yet but I'll figure it out. I just want to explain how everything works.

Few more issues to work out before we're done here. I didn't think when I was modeling the notches in the mounting bracket of the build plate, so they're on the wrong axis TT.

I've moved the notches slightly to the side, the stepper motor will need to be mounted on it's slide in order for the belt to slot in properly. I've also added a lot of structural support for the new notches, since they're hanging now, but I'm still worried the tension could cause problems later on. We'll keep moving on for now.

I finished designing the tensioner and the Y axis is done, we are approaching the finish line.

Mounting the extruder and creating a filament holder were by far, the easiest part of this entire project lol.

It took awhile, but I decided to create separate mounting plates underneath the bed in the remaining space of the frame. These plates would be problematic normally, but I created plastic risers to account for their low-clearance with the ground.

After all of that, we're done.

Well, with the bulk of it at least. I still need to clean everything up, prepare a portfolio of all the screenshots I've been taking, and submit my work for review for the "Infill" challenge.

In order of what I need to do and what:

1. Add screws into brackets
2. Retrieve all printable files and put into a folder on my computer or github (not sure where exactly, just make publicly accessible.)
3. Put all major screenshots into a google doc and add notes for context
4. Submit printer design for review to purchase parts


Total time elapsed: 9 hrs

---

# Day 18
### April 20th 2025

Purchased the parts a few days ago, and now we're just waiting for all of them to come in. I started assembling what we had today, which was all of the parts for the frame, bed, and the electronic mountings (excluding the voltage regulator).

At some point, Josef Prusa must have blessed me or something, because I literally FOUND Haribo gummy bears near my backpack that fell from my closet.

Thank you Josef... I think???

Assembling was and will be much harder than I initially theorized. It took a total of 4 hours to square the 4 2020 extrusions at the base of the frame and insert the extrusion with the fully assembled bed. I think the bed was the easiest part to design and assemble out of the entire machine. A few redesigns were necessary to keep screw management in check (There was far to many M4s being used and we don't have that many), as well as some redesigns for design errors. I think that we'd be much more re-assured with a backup voltage regulator, so I'm going to do some research to find one that we can get for cheap in case our custom regulator dies/shorts. 

And for the millionth time, we have battery problems. The voltage regulator we ordered is most definitely not up to code, so we're gonna have to order a new one...

I've had to make a few redesigns as I'm assembling, mostly to the brackets, as well as adding some stuff in where there should've initially been supporting brackets.

Personal note:
Following parts need a redesign before continuing:
- ~~Y Axis Idler and Tensioning Bracket (Make thicker to use an M3)~~
- ~~Extruder mounting bracket (Change to M3)~~
- ~~Filament mounting bracket (Change to M4 x 20mm)~~

Total time elapsed: 7 hrs

---

# Day 19
### April 21

More parts arrived. I'll be assembling the Voron M4 extruder later today when the parts finish printing, until then, I have what I need to continue assembling the frame.

There's a lot of issues now, these linear bearings don't fit in any of the parts, and I used screws that we don't have in the cad model. SERIOUS redesign binge or this doesn't work, and that cannot happen.

Stuff that works so far:
- Angle brackets
- All bed parts
- Filament holder (with slight modifications)

Screws used so far (tracking M4 and M5):
- M4 x 10 (16)
- M5 x 10 (8)

Stuff to redesign/design:
- ~~Anything with linear bearings to diameter of 15.35 instead of 15.1~~
- Completely redesign right bracket for gantry (Using M3 x 20 not M3 x 30)
- Redesign both idlers (M3 x 30 does not exist)
- New voltage regulator bracket
- ~~Thrust bearing housing (Bearings are too low and not enough screw clearance)~~
- CR Touch mounting bracket (No cable clearance)
- ~~Y axis stepper mounting bracket (Overhang makes it JUST too fat to use)~~
- ~~Extruder mount (Backside is JUST too close to the frame)~~
- Printhead clamps (M3 x 40mm screw doesn't exist)

Stuff redesigned:
- ModF_YAxis_Idler_&_Tensioning_Bracket.stl
- Y axis stepper mounting bracket
- Thrust bearing housing
- Extruder mount

To make my life easier, I concluded that I'll redesign all the listed files, as well as the entire gantry.

Total time elapsed: 6 hrs

---
# Day 20
### April 22

The following modules are complete and do not require further adjustment until a test involving the entire printer is conducted:
- Frame (Generic structure, angle brackets only)
- Extruder

What I finished today: Complete mounting and assembly of the Mobius extruder. (Voron M4 extruder kit).

Total time elapsed: 5 hrs

---

# Day 21
### April 23

I've managed to disassemble the bed and am now going to take the time to redesign a clamping system for the belts so that they may be attached properly this time.

After redesigning the bed, I decided to use my time to work on the gantry, which I've been putting off for a few days. I wanted to make the design much more organized and much cleaner than the last time, since it was previously so messy that the file decided to straight up off itself mid-modeling session and destroyed a bunch of stuff. To do this, I'm employing the same design solutions I came up with for the gantry previously, only this time I'm designing them all together, instead of smaller and uncontrolled edits of a larger part. Sorta like resolving a puzzle that didn't change.

The gantry is in reality, a stepper motor with a lead screw nut and a supporting/alignment structure of your choice (in this case, linear rods). The left side of our gantry is a tensioning bracket for the linear rods, where the lead screw nut resides, and a mount for the X-axis stepper motor. The right side is the same thing, but with a (typically adjustable) idler instead of a stepper.

I finished redesigning the gantry after awhile, and honestly the revised version is much cleaner and a little bit more compact. I have no idea if it works, that's obviously the idea, but we won't know until the parts finish printing and I won't be awake when that happens.

Did a lot today, got the Y axis working (FINALLY.) and finished remodeling the gantry. Tomorrow, assuming the gantry assembles good, I'm going to move on to finishing up the Z axis modifications. It's still not working.

Total time elapsed: 6 hrs

---

# Day 22
### April 24

Not a lot done today, mostly just minor redesigns and whatnot. Added screw-tightened clamps to the bed since the previous method to hold them in place was just not working, fixed up the gantry some more (some stuff didn't fit), and that's about it. The bed works now, in theory, and the gantry is almost done being perfected.

Total time elapsed: 4 hrs

---

# Day 23
### April 25

Spent some time to redesign the printhead today, I'll be printing the revised parts momentarily, but I wanted to fix up the X axis idler body, since it didn't quite work out the first time. Tolerances are way too out of whack with the M4 nut we're using to tension the idler; it literally bumps into the idler pulley and prevents it from being screwed in place. Not ideal.

After redesigning the printhead and sending it off to the printer, there were a few more things I needed to do with the new files. First, and most importantly, I need to add it to the complete assembly in CAD, so we have a finished model of the revised printer. At this point, there is only one thing dysfunctional in our design, the Z axis thrust bearing housing bracket, and it may not even be necessary considering how well the printer seems to old it in place with absolutely no help.

The next thing to do is revise the entire github, there's been so many changes in the design that I may as well take the time to dump all the old files and replace them with one zip of all the printable parts.

Lastly, I'll have to make a few adjustments with some more images and files per the recommendation of Dari, the event organizer. 

Checklist of updated README.md in STLS folder of the github repo:

- [x] Printhead
- [x] Gantry
- [x] Extruder
- [x] Bed
- [x] Frame

After finishing the reorganization, I decided to continue with adding Dari's recommendations, before I collapse from sleep deprivation. Remember to not stay up until 2 AM regularly, kids!

Files have been added, we are good for now. I'll let you all know how it goes horribly wrong when I wake up from my nap and all the printed parts I left running explode or something else equally as absurd.

Total time elapsed: 3 hrs

---
