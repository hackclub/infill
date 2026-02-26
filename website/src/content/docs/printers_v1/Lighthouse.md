---
title: "Lighthouse"
description: "easy to build, easy to hack, quality focused CoreXY 3D Printer."
project_name: "Lighthouse"
repository: "https://raw.githubusercontent.com/roschreiber/Lighthouse/refs/heads/main/JOURNAL.md"
---

Made by Robin Schreiber

Repository link: https://github.com/roschreiber/Lighthouse/tree/main

Total hours so far: 11.5
- [x] I have a 3D printer or will be getting one before March 21st
# Lighthouse 🔦

![Lighthouse Banner](https://raw.githubusercontent.com/roschreiber/Lighthouse/refs/heads/main/assets/banner.png)
<p align="center">[ˈlaɪthaʊs]</p>

Lighthouse is supposed to be a easy to build, open source & hackable CoreXY 3D Printer, with a huge focus on High Quality Prints.
Lighthouse is made for [Hack Club](https://hackclub.com/)'s [Infill](https://infill.hackclub.com/) YSWS, a big thanks goes out to them and Alex Ren for making this possible 🫶

## __Vorgeplänkel__
### The problem:

As of today, most 3D Printers that you buy from a company are restricted to their proprietary firmware. I for example owned two different [Elegoo](https://www.elegoo.com/) brand printers and one [Anycubic](https://www.anycubic.com/) printer, which both have the same issues:

Poor calibration from the factory, inconsistent extrusion, bent lead screws after minimal runtime, and issues with build plate leveling all have a huge impact on the overall print quality. 

Usually, especially for beginner printing enthusiasts, you expect your printer to work perfectly out of the box, with no tuning (except for regular maintenance every now and then) required. While [Bambu Lab](https://bambulab.com/) has managed to fulfill this "dream" in the last two years, their printers are heavily restricted by proprietary firmware, which is not well-received by the printing community. See [this](https://www.reddit.com/r/BambuLab/comments/1i2psvz/firmware_update_introducing_new_authorization/) for example.

I want to fix this with Lighthouse. I want to construct a printer that is easy to setup, easily hackable and actually gives you good print quality for under 200$.

### The goals:

**Lighthouse** ***should***:

- be able to print at a reasonable printing speed without having to sacrifice print quality. I'm looking at 200mm/s - 300mm/s.
- have a build size enough to handle medium sized models, 256mm³ for example.
- should be able to print a variety of materials. PLA, TPU, PETG ...
	- It should also be able to print fiber reinforced filaments. I'm looking at Carbon Fiber PLA / PETG
	- Lighthouse will most likely not have a enclosure to stay under its 200$ cutoff. That also means that ABS & ASA are most likely **out of question** here.
- should be able to be controllable through your Wireless Network. 
  -> Fluidd UI for Klipper maybe?
	- **And / Or** maybe have a touchscreen in the Frame which allows you to control the Printer.
- defeat the following quality issues: (I have encountered all of these on my previous printers..)
	- [**Ringing/Ghosting**](https://www.simplify3d.com/resources/print-quality-troubleshooting/vibrations-and-ringing/) through the use of a **acelerometer**, **vibration dampers** and **linear rails**.
		- Parts of the Frame will be 3D Printed, which could have negative impact on ringing & ghosting, so I need to find a way to reinforce or stiffen these parts to minimize vibrations.
	- [Layer Shifts](https://www.simplify3d.com/resources/print-quality-troubleshooting/layer-shifting/) can be minimized by using high quality stepper motors and a mostly linear rail system instead of a belt system.
		- Belt Systems also suffer a lot from wear & tear, stretching and slippage. They also need a bit more maintenance.
	- [Z-Banding/Z-Wobble](https://all3dp.com/2/3d-printer-z-banding/), which usually happens when your lead screws are bent. Can be fixed by using anti backlash nuts or Oldham couplings.

### The plan:

1. Design the 3D Printer itself, maintain a **BOM** whilst scalping parts from China.
2. Get parts for the frame printed out whilst everything else arrives.
3. Build the printer & make sure that everything works!
4. Get it tuned, use a generic Klipper configuration which is well maintainted. [Klippain](https://github.com/Frix-x/klippain) for example seems great for this one!
5. Post some results and documented instructions on how to build Lighthouse!

# Log ✍️


| Date      | Task                                                                    | Time      | Notes                                                                                                                                                                                                                                                                              |
| --------- | ----------------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 18th. Feb | Set up JOURNAL.md,<br>Designed a 3D Model for 2020 Aluminium Extrusions | 3 hours   | The start of Lighthouse                                                                                                                                                                                                                                                            |
| 19th. Feb | Created Models for Slideable T-Nuts,<br>a 310x310mm Heated Bed.         | 2.5 hours | Also added a Model of MGN12C HIWIN Rails, taken from [traceparts](https://www.traceparts.com/en/product/hiwin-technologies-corp-mgn12c?CatalogPath=HIWIN_2099818092%3AHIWIN.020.060&Product=90-07042020-029715). (I will not be using HIWIN Rails though, they are too expensive!) |
| 20th. Feb | Start working on the Printer Frame itself.                              | 6 hours   | Added Model for a Adjusted Hiwin Rail with 350mm in length to accomodate for the T-Nuts                                                                                                                                                                                            |
