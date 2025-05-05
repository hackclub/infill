---
title: "Ender X4"
description: "A low cost, quad extruder 3D printer based on the Ender 3."
project_name: "Ender X4"
repository: "https://github.com/ading2210/ender-x4/raw/refs/heads/main/journal.md"
---
Made by: ading2210 // vk6

Repository link: https://github.com/ading2210/ender-x4

Total hours so far: 82

- [x] I have a 3D printer or will be getting one before March 21st

This printer is has been designed as part of Hack Club's [Infill](https://infill.hackclub.com/) event. 

## 3/13/25 - Research design goals and feasibility (2.5 hrs)

<details>

<summary>I did these notes on a Google Doc originally, so here it is copy-pasted.</summary>

**Goals:**

* Reuse as many parts as possible from 2 stock Ender 3 printers   
* Quad extruder with independent hotends (IDEX or single toolhead?)  
* Under $250, used parts allowed  
* Entirely off the shelf components and printed parts  
* Maximize build volume 

**IDEX Design**

* Need 4 x axis motors and 4 belts  
* Total motor count – 4 x axis, 1 y axis, 4 extruder, 2 z axis (total: 11).   
  * 1 extra motor (Nema 17\) needed for x axis ($10)  
* Control boards (option 1):  
  * Main: BTT Octopus ($80)  
    * Used for x, y, z axis and bed heater  
  * Extra: 2x stock Creality v1.1.4 (or v4.2.7)  
    * Used for all 4 extruders, 4 hotend heaters  
* Control boards (option 2):  
  * Main: BTT SKR v1.4 ($30) \+ 5x TMC2209 ($20)  
    * Used for x, y axis and bed heater  
  * Extra: 2x stock Creality v1.1.4 (or v4.2.7)  
    * Used for all 4 extruders, z axis, 4 hotend heaters  
* Control boards (option 3):  
  * Main: BTT SKR Mini E3 v2 ($35)  
    * Used for x axis and bed heater  
  * Extra: 2x stock Creality v4.2.7   
    * Used for all 4 extruders, z axis, y axis, 4 hotend heaters  
* Extra cost: $35-$90

**Single Carriage Design**

* Only 1 x axis motor and belt  
* Total motor count – 1 x axis, 1 y axis, 4 extruder, 2 z axis (total: 7\)  
* Control boards:  
  * Main: BTT SKR Mini E3 v2 ($35)  
    * Used for x, y, z axis and bed heater  
  * Extra: 2x stock Creality v1.1.4  
    * Used for all 4 extruders, 4 hotend heaters  
* Extra cost: $35

**Attributes Common to Both Designs:**

* Ender 3 v2 Neo might be used instead because those are cheap on ebay  
  * Otherwise use the Ender v3 v1 because that one is open source  
* 2 power supplies (stock ones used)  
* 2 of the hotends and extruders need to be purchased  
  * [Creality Direct Drive Kit](https://www.amazon.com/Creality-Original-Extruder-Flexible-Filament/dp/B09NVWJYMT) x2 ($60)  
* Purchase 2 Ender 3 v1s used ($100 \- $120)  
* Main computer is Raspberry Pi 3 with Klipper  
* Dual X axis gantry, dual z axis motors  
* Keep a belt slinger design   
* Use stock rollers for x axis (linear rails if within budget)  
* Keep stock hotend   
* Keep stock motors  
* Direct drive

</details>

## 4/1/25 - Frame, Y Axis (1.5 hrs)

I'm going to re-use the Ender 3 Y axis carriage and use the same design for the bottom portion of the printer's frame. I don't see a way I can improve the Y gantry without excessively modifying the parts, because the aluminum extrusions are already machined with slots for the Y axis gantry. Also, the various Ender 3 variants use slightly different Y axis gantries (this is pretty much the only mechanical change between the different Ender 3s) so making a single design to accommodate all of them is unrealistic. 

## 4/2/25 - Frame, Start X Axis (1 hr)

This was just some basic CAD work. A lot of the time was spent importing the parts from the original Ender 3 into Fusion.

- Assemble the Y Axis and attach it to the frame
- Start assembling the X gantry

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/printer_assembly_1.png" height="300px"> 

## 4/4/25 - Continue X Axis (2 hrs)

This part of the mount is inserted into the V slot extrusion for more stability.

- Create mount for second X motor
- Add motors to X axis assembly

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/x_gantry_part_1.png" height="300px"> 

## 4/6/25 - Create A/B Toolheads (10 hrs)

In my design, there are two different toolhead designs. The "A" toolhead is on the left side of the X gantry, and the "B" toolhead is on the right. The hotend assembly is mirrored on the B toolhead, but the extruder mount has to be different. The goal for the hotend assembly is to get the hotend as close to the center of the printer as possible. This allows the hotend on each toolhead to come close to each other while printing, thus maximizing the printable area.

Creating the hotend assembly was a bit annoying because of the unconventional layout. I need the hotend fan to be *behind* the hotend rather than in front of it, so the hotend can't be directly mounted to the X carriage base. The fan duct for the part cooling fan was also a pain, but I'm going to blame that on my inexperience in modeling this kind of part in Fusion. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/hotend_assembly.png" height="400px"> 

Following the hotend assembly, I moved on to building both toolheads. This was relatively simple, since I just had to attach the hotend assembly to the extruder and X carriage base. I also added a mount for a CR Touch probe on the A toolhead.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/toolhead_a.png" height="400px"> 
<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/toolhead_b.png" height="400px"> 

## 4/7/25 - Finish X and Z Axis (10 hrs)

First, I needed to modify my B toolhead design to add in a belt holder. This is because the belt for this toolhead will be placed well above the aluminum extrusion rather than around it like the stock toolhead does. This was a simple addition, and I used a model of a GT2 belt as a reference so I could make a cut of the belt profile.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/toolhead_b_back.png" height="400px"> 

I then finished one half of the X axis gantry, which contains both A and B toolheads on the same axis. The new additions here are the endstop mounts, belt tensioner, and the brackets on either side for the joining pieces to the other half of the X gantry.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/x_gantry_part_2.png" height="400px"> 

To create the full X axis gantry, I copied the part shown above and rotated it 180 degrees. I added connecting pieces between the two halves, and attached the Z nuts to them. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/x_assembly_1.png" height="400px"> 

In the full printer assembly, I added the extrusions for the Z axis as well as the X gantry. I made a mount for the Z motors, lead screws, and Z endstop.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/printer_assembly_2.png" height="400px"> 

## 4/8/25 - Finish Initial Printer Design (10 hrs)

Although the Z axis was complete, I still needed to put braces between both sides of the Z gantry. On top of these braces, I put the 4 spool holders as well.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/top_assembly.png" height="400px"> 

Next, I modeled the mounts for the two PSUs and the power switch. I found that arranging the PSUs on their sides wastes the least amount of space, and simplifies the mounting hardware.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/psu_mount_1.png" height="400px"> 

To mount the 3 control boards, I have them arranged in a rack, with each stacked on top of each other. It's in a rack like this because it's the easiest to design and 3d print a mount for, even if the wiring will probably be messier. This rack attaches to the 4040 extrusion on the base of the printer. I'm a bit concerned that there won't be enough airflow across the control boards, but I'll have to wait until this is actually built to see if that will be a problem. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/control_board_rack_1.png" height="400px"> 
<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/control_board_rack_2.png" height="400px"> 

I also quickly made a bracket for the Raspberry Pi 3. I used an RPi 3 instead of a newer model mainly because I already have one lying around. The other reason is that it's significantly cheaper ($20 used) and I don't need more processing power anyways. This bracket, just like the control board rack, attaches to an extrusion on the base.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/rpi_mount_1.png" height="400px"> 

The final item missing in the printer is the LCD mount and legs for the frame. The legs attach to the side of the 4040 extrusions on the base, and the LCD attaches to the front right leg. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/leg_and_lcd.png" height="400px"> 

And with that, the initial version of the printer is complete. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/printer_assembly_3.png" height="400px"> 
<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/printer_assembly_4.png" height="400px"> 
<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/printer_assembly_5.png" height="400px"> 
<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/x_assembly_2.png" height="400px"> 

Here it is next to an original Ender 3 v1 for comparison.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/printer_next_to_ender_1.png" height="400px"> 

## 4/9/25 - Design Revisions (2 hrs)

I added end caps to the 4040 extrusions on the base and chamfers to the legs to improve the aesthetics.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/4040_end_cap.png" height="400px"> 

I also made the spool holder arms thicker in order to improve their strength. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/spool_holder_1.png" height="400px"> 

Finally, I added chamfers to a bunch of other parts and fixed various errors with intersecting geometry. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/printer_assembly_6.png" height="400px"> 

## 4/10/25 - More Revisions, Work on BOM (3 hrs)
I went back and reviewed all the screw holes and made sure they were the right diameter. Most of them will be self-tapping, so I had to reduce the hole diameter to accommodate. I also changed some of the screw type which were used in order to reduce the cost. For instance, I replaced the usage of M2 square nuts in the belt tensioner to use M3 square nuts instead. This was so that fewer unique fasteners would need to be purchased, thus saving me about $10.

I then put together a BOM for the printer.

![A screenshot of the BOM](https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/bom.png)

## 4/11/25 - More Revisions, Source Parts (4 hrs)

I changed the base of the spool holder to use two M3x16 screws on either side instead of two M3x35 screws that go all the way through.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/spool_holder_2.png" height="400px"> 

The usage of 2.0mm thick M3 square nuts was changed to 2.5mm thick ones because they are cheaper and more commonly available. I can save about $3 this way.

I also researched every part I needed to buy and found that it barely fits in my $300 budget. The Hack Club grant is only $300 and these prices don't include tax so I'd probably have to pay for part of it out of pocket. There's many things that I already own that I am reusing, so if this was built from scratch the cost would be about $60 higher.

![A screenshot of a spreadsheet with the costs of each part.](https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/bom_cost.png)

## 4/12/25 - Set up Repository and Publish (4 hrs)

I wrote the README for this repository, added more images, added the license and published the repo publicly.

I also made a PR in the [Infill website repo](https://github.com/hackclub/infill/pull/63) to improve their build scripts. This journal markdown file contains a lot of relative image URLs pointing to files within this repo. Before, this wasn't supported and I would be forced to replace all of them with absolute URLs. 

## 4/14/25 - Order All Parts (1 hr)

I have ordered all of the parts from Ebay and Amazon. The total cost was about $340, $300 of which was covered by the Hack Club grant. The stuff on Ebay should arrive by 4/17 and everything from Amazon will arrive by 4/15.

## 4/15/25 - Research Klipper Configuration (1 hr)

While I wait for the rest of the parts to arrive, I spent some time researching how I might configure the printer with Klipper. Having multiple control boards is pretty trivial, but the tricky part is the X axis movements. Even though Klipper already supports IDEX printers via the [`dual_carriage`](https://www.klipper3d.org/Config_Reference.html?h=safe_#dual_carriage) config, it only supports 2 toolheads on a single gantry. 

Thus, I need to manually set up the X motors and set the kinematics manually using GCode macros, similarly to this post in the Klipper forum: https://klipper.discourse.group/t/emulating-6-carriage-idex-by-syncing-steppers/18391/7

Another issue is that regular Klipper does not support multiple bed probes by default. Currently, I'm using two CR Touch probes for each X gantry, so this is a required feature for me. It seems that the [Klipper for CNC fork](https://github.com/naikymen/klipper-for-cnc?tab=readme-ov-file#multi-probing) does support this, but that fork comes with a bunch of other caveats.

## 4/16/25 - Start Printing Parts, Revise Design (5 hrs)

Last night I started a printing the legs. This print finished in the morning. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/printed_parts_1.jpg" height="400px"> 

Some people that reviewed the design were concerned that the 3 control boards wouldn't get enough cooling. Thus, I added a mount for an 80mm PC case fan to the side of the control board rack. The fan is 12V while the Ender 3's PSU is 24V, so I bought a [buck converter for 24V to 5V](https://www.ebay.com/itm/126774882802), which I'll use to power both the Raspberry Pi and 80mm fan. This fan will be running at about 20% power because it it's running at a lower voltage, which is fine with me because any higher and it becomes very noisy. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/control_board_rack_3.png" height="400px"> 

I also added this corner brace to the base of each of the extrusions for the Z axis. Before, I assumed I would drill holes into the base 4040 extrusions but I now have realized that will be a massive pain so I will use this 3D printed bracket to attach it instead. I don't know if this will be stable enough because it only uses M5 T nuts, but I will have to wait until it is built to see.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/4040_corner_brace.png" height="400px"> 

The top brace pieces were just barely too wide to fit on my Prusa Mini+ so I made them 4mm thinner so they are printable.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/top_brace.png" height="400px"> 

I added this small protrusion in the base of the spool holder so that the spool holder arms cannot rotate inadvertently.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/spool_holder_3.png" height="400px"> 

In the evening, I printed some more parts. I now have all of the legs and the two braces that go at the top of the frame. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/printed_parts_2.jpg" height="400px"> 

At this point, I realized that I had made a mistake with the sizing of the holes for the M5 screws. Because I had ordered button head screws instead socket cap screws, the diameter of the screw head was 9.5mm instead of 8.5mm. The counterbore in my parts was only 9mm, so I had to expand the hole using an 3/8 inch (9.52mm) drill bit. 

To test the fit of the screws, I used the M5 screws and T nuts to attach one of the top braces to the 2020 extrusion on my old Ender 3 v1. This worked perfectly and gave me confidence that the design would be strong enough mechanically.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/2020_t_nut_test.jpg" height="400px"> 

I then started another print to run overnight. This print contains the corner braces for the Z axis extrusions and the mount for the Z axis motors.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/printed_parts_3.jpg" height="400px"> 

Finally, I removed the X endstop from my old Ender 3, so that I wouldn't need to buy any new ones. I need to switch my Ender 3 to use sensorless homing, but I have not yet configured this.

## 4/16/25 - Repair Ender 3 Printers (6 hrs)

The two Ender 3 V2 Neo printers that I ordered from Ebay arrived today. My plan is to reassemble both printers, verify that all the components work, and then disassemble them for the parts.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_packages.jpg" height="400px"> 

Unfortunately, the Ebay seller didn't send me all of the items that I paid for. I'm missing a screen, spool holder, power cord, and CR touch sensor. However, I contacted the seller and they agreed to send me the missing parts. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_package_contents.jpg" height="400px"> 

Even though I was missing parts, I still had to get to work on repairing the two printers. I didn't have a functioning screen (the one that I did receive from Ebay had a broken click wheel), so I used a spare 128x64 LCD that I had and flashed the Ender 3 Neo (not V2) firmware to the printer. The only real difference between the Ender 3 V2 Neo and the V1 neo is the display, with the regular Neo using the 128x64 LCD and the V2 Neo using the larger full color LCD. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_1_power_on.jpg" height="400px"> 

The first thing I had to fix was the fact that the base of the toolhead carriage was bent, preventing the wheels from being aligned. So I took the toolhead off, bent the metal back into place, and reassembled it. After that, this printer worked perfectly with no problems. I was able to complete a test print without issues, so I moved on to the next one.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_1_test_print.jpg" height="400px"> 

I noticed there was a loose capacitor in the box for the second printer. It turns out that this capacitor had somehow been ripped off of the control board, taking with it the solder pads.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_2_bad_board.jpg" height="400px"> 

I checked the schematic for the Creality 4.2.2 board and it appeared that the missing capacitor, C3, isn't too important. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_board_schematic.png" height="400px"> 

So I powered on the printer and sure enough, the board appeared to work fine. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_2_power_on.jpg" height="400px"> 

Since the scroll wheel on this screen didn't work, I connected to the printer via Pronterface. This confirmed that all of the motors worked. However, the temperatures reported were completely wrong. It was reporting about 100c for the hotend and 90c for the bed even though the printer was cold and no heaters were running. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_2_wrong_temp.jpg" height="400px"> 

To check if this problem was the thermistors or with the board, I plugged the thermistor and my spare screen into an old Creality 1.1.4 board which did read the correct temperature. So this confirms that the board is indeed broken and I would need to buy a new one. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_3_correct_temp.jpg" height="400px"> 

For now though, I need to use the 1.1.4 board to test the rest of the printer's components. I replaced the broken 4.2.2 board with the working 1.1.4 board, added in a Z endstop, and powered on the printer. This time, everything seemed to work, but I have not yet tested to see if it can still print.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_2_board_replaced.jpg" height="400px"> 

## 4/19/25 - Continue Repairing Ender 3s (4 hrs)

I bought a working 4.2.2 board from a friend for $20, so I no longer have a need for that old 1.1.4 board.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_2_board_replaced.jpg" height="400px"> 

The metal plate for the X carriage on this printer was also bent just like on the first one. This was a simple fix though.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_2_bent_carriage.jpg" height="400px"> 

The plastic fan shroud was cracked so badly that the threaded inserts fell out and the fan could not be attached. Thus I just removed it and zip-tied the fan to the X carriage. After that, I could start printing. At first, it seemed to be working great.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_2_printing.jpg" height="400px"> 

Halfway through this print when it started underextruding really badly. Replacing the nozzle helped but did not eliminate the problem. I spent a while tweaking the hotend and at some point I accidentally stuck a wrench through the running hotend fan and broke it. So after ordering new fans, I'm calling it a day.

## 4/20/25 - Redesign Electronics Mount, Y Axis Mounting (7 hrs)

After printing the original stacked control board mount, I quickly realized that it was not going to work. There was simply not enough vertical clearance between the control boards, so routing the wires and screwing in the board would be near impossible. For this new design, I decided to lay out the boards side by side. The fans attach to a separate bracket that screws into the top of the mount. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/electronics_mount_1.png" height="400px"> 

Here it is in the printer assembly.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/electronics_mount_2.png" height="400px"> 

I also redesigned the Raspberry Pi mount. Because the RPI uses M2.5 screws (which I don't have), I can't use its mounting holes. Instead, the screws clamp onto the edge of the board. This RPI mount screws into the bottom the of electronics assembly.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/rpi_mount_2.png" height="400px"> 

I printed a small test part for this, and confirmed that it does indeed work well. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/rpi_mount_3.jpg" height="400px"> 

Additionally, I made some tweaks to the LCD holder to better accommodate the physical item. This required cutouts at the edge of the screen, below the screen, and around the potentiometer. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/lcd_mount_1.png" height="400px"> 

I also needed a custom bracket for the Y axis assembly. This is because the Y axis in this printer is shifted to the back by a bit, and thus the original screw holes don't work.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/y_axis_bracket_1.png" height="400px"> 

Afterwards, I returned to working on repairing the printer. Eventually, I figured out that the hotend was fine, and that it was just the extruder which couldn't push the filament through. The issue appears to be that the PTFE tube is scratched on the inside and thus has too much resistance. The final printer design is direct drive and thus this wouldn't be an issue, so I shouldn't need to worry about this anymore.

## 4/21/25 - Print Parts, Start Assembly (6 hrs)

That $3 buck converter I ordered has arrived today. I measured the dimensions, and tested the mounting with a small print. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/buck_converter.jpg" height="400px"> 

This worked, so I modeled the buck converter PCB in Fusion, and added a mount for it next to the Raspberry Pi.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/rpi_mount_4.png" height="400px"> 

The missing parts from the Ender 3s that I purchased also arrived today. Everything was in good condition, and the screen was even brand new.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_missing_parts.jpg" height="400px"> 

The screen and CR Touch worked perfectly. I'm probably going to use this screen in the final printer, but this would have to be done later, since the screen is not supported by Klipper.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_working_screen.jpg" height="400px"> 

I finished printing all of the parts for the electronics mount today, so I was able to assemble it. Everything went smoothly here.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/electronics_mount_3.jpg" height="400px"> 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/electronics_mount_4.jpg" height="400px"> 

I then began to disassemble the second Ender 3 printer so I could reuse the Y axis and frame. I first assembled the Y axis bracket.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/y_axis_bracket_2.jpg" height="400px"> 

And then attached the feet to the frame, which completes the base of the frame. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/frame_base.jpg" height="400px"> 

Finally, I attached the LCD to its mount.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/lcd_mount_2.jpg" height="400px"> 

## 4/26/25 - Reverse Engineering, Start Redesigning (6 hrs)

I noticed that the toolhead bracket on the Ender 3 V2 Neo is different from the bracket on the original Ender 3. It has different screw holes and the mounting for the hotend is offset. Fortunately, I can just print the original Ender 3 V1 toolhead bracket. However, I needed to modify it so that it's more rigid and to add cuts for M3 square nuts to sit in. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/toolhead_bracket_modified.png" height="400px"> 

I also modified the belt tensioner assembly so that the slots in the tensioner case are not at right angles. This should help with the printability of the model. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/belt_tensioner.png" height="400px"> 

I then spent some time reverse engineering the Z stent component on the Ender 3 V2 Neo. This part on the Ender 3 V2 Neo is different from the one on the Ender 3 V1 or V2, so I need to create a 3D model so I can reference it in the CAD design.

I placed the Z stent on my document scanner, then imported and traced it in Fusion.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_z_stent_1.jpg" height="400px"> 
<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_z_stent_2.png" height="400px"> 

Then, I had a model that almost exactly matched the original part. I also 3d printed it to confirm.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_z_stent_3.png" height="400px"> 
<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/ender_3_z_stent_4.jpg" height="400px"> 

Afterwards, I [put the model up on Printables](https://www.printables.com/model/1277986-ender-3-v2-neo-original-z-stent-3d-model), just in case it might be useful to anyone else. 

After inserting the model into my design, I realized that my existing design for the X motor mount doesn't work since it'll intersect with the Z stent. 

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/x_gantry_part_3.png" height="400px"> 

## 4/27/25 - Continue Redesigning X Axis (2 hrs)

I worked on redesigning the right side of the X gantry. This time, I made it so that it sits in front of the Z stent, and made it so the belt tensioner is integrated into the part.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/x_gantry_part_4.png" height="400px"> 

## 5/10/25 - Finish X Gantry Redesign, Revise PSU Mount (7 hrs)

I finished the X gantry redesign. I added the mount for the limit switch and the mounting for the X connector piece.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/x_gantry_part_5.png" height="400px"> 

I then simplified the PSU mount and made it thinner to save on material.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/psu_mount_2.png" height="400px"> 

I also needed to redesign the power switch mount because the power switch on the Ender 3 V2 is different than what it is on the Ender 3 V1. Also, my previous design was pretty bad.

<img src="https://github.com/ading2210/ender-x4/raw/refs/heads/main/images/power_switch_mount.png" height="400px"> 

I then started printing a bunch of parts for the spool holder and X gantry.
