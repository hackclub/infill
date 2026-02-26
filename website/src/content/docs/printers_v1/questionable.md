---
title: "QuestionalPrinter"
description: "A large-build volume 5-axis printer"
project_name: "QuestionableAtBest"
repository: "https://raw.githubusercontent.com/DinosaurPotato534/questionableAtBest/refs/heads/main/JOURNAL.md"
---
Made by: @dinosaurpotato (shaan) & @justaglitchfl (aidan) & @castoway (dimitri)
Repository link: https://github.com/DinosaurPotato534/printer
Total hours so far:
Shaan: 30
Dimitri: 22

- [x] I have a 3D printer or will be getting one before March 21st

2/26/25
-
Shaan & Aidan - ~3 hours
* began researching printer designs and looking into how exactly to get started
* began brainstorming an interesting concept for a printer
* began looking at guides and what parts we would need, with a maximum budget of $300 in mind

2/27/25
-
Shaan & Aidan - ~2 hours
* continued brainstorming concepts
* watched *several* videos and resources on custom printer builds
* looked at other submissions to infill

2/28/25
-
Shaan & Aidan - ~2 hours
* started setting up github repo
* kept brainstorming concepts
* potential concepts:
	* live recycling printer
	* conveyor printer
	* dual feed printer
	* printer on a vex drivetrain
	* infinite z-axis printer (prints itself higher)
	* 4 axis
	* modular build volume
	* portable printer
* will hopefully settle on an idea tomorrow to get started :)

3/1/2025-3/2/2025
-
Shaan & Aidan - ~6 hours
* decided on 5-axis coreXY based printer
* developed implementation:
  	* rectangular exoframe (ie. voron 2)
  	* coreXY printhead movement
  	* dual lead screw z-axis (for supporting axes 4 and 5)
  	* 4th axis is rotating build plate mount left/right using a central pivot at the back and belt reduction (or gears) to a stepper to tilt the entire plate 45deg either direction while leaving the most build plate area
  	* 5th axis is tilting the plate back and forward from a stepper on a belt below so the plate is on the plane created by the two pivots (less slicer math) and the motor is below
  	* each axis can be locked out with a pin to allow for max accuracy in prints where the 4th or 5th axis isn't required
* other features:
  	* bltouch-style auto leveling (would be near impossible to get the bed calibrated without). Instead of like in a normal printer, where the sensor is brought to points on a stationary plate, this would go to the center and get the ideal height for each axis (because it's all in plane so center never changes), then go to each corner and rotate the plate in each direction until it hit that height, ensuring a proper centering for the 4th and 5th axis
  	* idk some other qol stuff like filament runout
 
3/15/2025
-
Shaan & Aidan & Dimitri- ~3 hours
* Dimitri joined the squad
* redesigned the 4th and 5th axis for the printer
 	* there will now be three lead screws for the z-axis, which with the combination of movements can control the 4th and 5th axis
   	* the print bed will be similar to a delta printer with 3 linear slide being able to pull each corner down to tilt the bed
   	* auto bed leveling will work by having 2 of the lead screws moving, thus only tilting one axis
* decided on this new design because of the complexity of having a bed and it's 4th axis being mounted to the 5th axis and all of that needing to be moved up and down
* decided on the name for this project to be "Questionable at Best"

3/22/2025
-
Dimitri ~3 hours
* gained a fusion 360 student account
* began to practice using fusion(had prior experience with OnShape)

3/23/2025
- 
Dimitri & Shaan ~4 hours
* researched necesssary electronics for 5 axis printer
* figured out we would need 6 stepper motors(2 corexy, 3 zed, 1 filament)
	* forces us to use a motherboard capable of having this many motors
   	* we need a raspberry pi with klipper for the kinematics of a moving bed
* began researching on how autobed leveling would work

3/24/2025
-
Dimitri ~5 hours
Shaan ~3 hours
* began to fully find exact electronics that we would be using
  	* found a motherboard cabable of having 6 stepper motor drivers
  	* decided on using a raspberry pi 4 for klipper installation
* figured out that autobed leveling would work by adjusting each of the z motor until it is flat
* found some previous examples of how the linear slides for 5 axis function

3/25/2025
-
Dimitri and Shaan ~4 hours
* Dimitri created the CAD file and started to import all necesasary parts for the design
* Shaan researched necessary electronics and created a bill of materials

3/27/2025
-
Dimitri and Shaan ~3 hours
* Dimitri set up basic framing for CAD
* Shaan researched custom slicers for a 5 axis tilting bed printer
* Aidan left the project due to being too busy

