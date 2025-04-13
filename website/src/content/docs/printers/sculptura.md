---
title: "Sculptura"
description: "Open-source and customized budget 3d printer built from scratch for printing multicolor decorative items :D"
project_name: "Sculptura"
repository: "https://raw.githubusercontent.com/arsoninstigator/sculptura/refs/heads/main/README.md"
---
# sculptura ☆.ᐟ

> username: @arsoninstigator aka @anne on the slack (she/her) <br>
> here's the printer's [github repository](https://arsoninstigator/sculptura) and the main [infill page](https://infill.hackclub.com/printers/sculptura/) <br>
> total time spent on this till date: 52 hours (as of 28/03)
- [X] i currently / will have access to a 3d printer before 21st march (bambu a1 mini)

## about
sculptura is a wip fully **open-source** and customized budget 3d printer made from scratch for printing smooth, detailed and precise models that are meant to to be used as high quality decorative pieces (like you would see at an art gallery) :D


## daily log
### ⋆ day one - day ten — initial research (time taken: ~ 15h)
found out even more about how 3d printers work by reading documents, watching youtube videos, looking at existing open-source builds (including neutrino), sketching out what i was trying to achieve. i loosely consulted reddit threads that answered my super specific questions and asked a lot of questions on dedicated discord servers (i'm surprised they didn't ban me for being annoying). i did my initial light research on:
- frame and motion system
  - frame design & materials
  - printer kinematics & motion types
  - linear motion
  - belt & pulley system
- extruder and hotend
  [i spent a lot of time going back and forth to decide whether i wanted to make a clay or paste-y printer (since the name of my printer is sculptura) but ultimately decided against it and took the traditional route]
  - hotend types
  - nozzles & material compatibility
  - direct drive
- bed and print surface
- firmware (will run klipper)
- electronics
  - mainboard selection
  - stepper motor drivers
  - power supply & wiring

at this point i obviously knew only the basics so nothing was set in stone but i started to form a **very rough image** in my head of what my printer would look like and started to make interations on the components i had chosen and added to my current bom before i started cad-ding and got in too deep!

### ⋆ day eleven - day nineteen — research + begin cad (time taken: ~ 17h)
continued my quest to research on more stuff and get into the details. watched actual people talk about their experience working w 3d printer builds to get a holistic view that's beyond the pages of a book. some topics i covered included:
- bed & print surface
  - heated bed types
  - bed surfaces
  - auto bed leveling?
- cooling & enclosure design
  - part cooling fans and ducts
  - hotend cooling fans
  - enclosures and filtration

sketched out a wip printer and its measurements with a paper/pencil and then started working on the cad. focused on the frame. decided: aluminum extrusions, no question. modeled a simple 2020 extrusion profile, then tried to boolean it into a frame mockup. fusion crashed twice. used a combination of fusion 360 and freecad (love the open source-ness but it's not quite there yet in terms of features) and even though this wasn't the hardest part of the build, but i had to restart from scratch multiple times and do it all over again and again till i was somewhat satisfied with the results.

### day twenty - day twenty-five — cadding
realized i didn’t dimension the extrusion lengths. spent a whole day fixing it. fusion's sketch constraints started ghosting me. drove myself mad figuring out why my midpoint constraint wasn’t snapping. next day, found a nice trick on grabcad for corner brackets. "borrowed" the design and parameterized it to fit my frame. made fusion crash only once which is a victory in itself in my book. next two days, scrolled discord printer groups. stumbled across some fun idler designs. screenshot folder became 134 images deep. did no cad stuff since i felt kinda burnt out. after that, finally locked in and started laying out core xy belt paths. sketched some pulleys and tried routing the belt. decided it looked like spaghetti and got hungry. googled “corexy belt routing diagram” 17 times and was still confused.

### day twenty six - day thirty two
made some core xy progress - refined the belt paths. added idler pulley placeholders. felt like a god for 30 minutes until i realized i forgot to check belt tensioning. next day, modeled my first tensioner block. completely forgot clearance for the screw head. redid the whole thing. scrapped it entirely in anger. redid it *again*. next, i borrowed some gantry ideas from voron. decided on linear rails. modeled a rail and slapped it onto the frame. *wingardium laviosa* noticed it's floating in mid-air but oh well. next, added actual mounting points to the frame for rails. realized i sized them 3mm too short. adjusted everything. fusion performance starting to tank from component count. next, modeled a rough carriage and constrained it to slide on the x rail. watching it move felt great. next, added pulley mounts to the carriage. spent 40 minutes debating between single or dual pulleys. settled on dual for tensioning flexibility. upped my dosage for ritalin (prescribed ofc) to lock in but fell asleep with fusion open and my head on the keyboard so that went as well as you can imagine.

### day thirty-three - day forty
designed a motor mount plate. fusion crashed during patterning. auto-recovered my file but lost constraints. raged. cried. ate chips. returned. next day, ranted in my journal about fusion not autosaving often enough. redesigned motor mount properly this time. frame finally started feeling real !!! next, got stuck deciding between optical or mechanical endstops. prototyped a slot for microswitches, decided to stay simple. will probably regret this later. next, modeling the y carriages today. realized they look suspiciously like voron’s. decided that was good ??? looked up juvenile sentences for shoplifting (/s). next, redesigned how extrusions join for better rigidity. added hidden fasteners. model was getting heavy but fusion was surprisingly cooperative. next, discovered i need spacers everywhere. modeled one spacer, then made 12 variants. started going insane and had to go for a walk. started raining while i was walking. yay. 

### day forty-one — printhead-ing
explored printhead designs. half-considered a compact, single-fan setup but ended up copying a stealthburner clone layout. next, modeled the printhead mount. forgot to add wire management. amazing. next, finally added wire guides. fusion assemblies slowed to 5 fps but the model looked neat.
