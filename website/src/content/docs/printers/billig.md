---
title: "Billig"
description: "Sub 300$ 400²x250mm CoreXY enclosed 3D printer"
project_name: "Billig"
repository: "https://raw.githubusercontent.com/playlogo/billig/refs/heads/main/JOURNAL.md"
---
**Done:** **Yes**  
**Result:** *<300$ 440x230x230mm 3D printer*

**Author:** [@playlogo](https://github.com/playlogo)  
**Repository:** [https://github.com/playlogo/billig](https://github.com/playlogo/billig)  
**Total hours so far:** - *lost count*
**3D Printer available:** Yes  

**Bom**: [Google sheets](https://docs.google.com/spreadsheets/d/1451xPwitG2cd0BywjLuyT1Flae_F1tCVU7JKSqZtRoc/edit?usp=sharing)  
**CAD**: [Onshape](https://cad.onshape.com/documents/d0a1f0aa5ccbfda89a60ed00/w/724bd13dc87be16ac72aafeb/e/ab5d18244eafa3c49944618e?renderMode=0&uiState=67cdf3b468bb893dcada95f7)

[Text written on April 7] About the journal: So this journal didn't really work out that well. I started planning the printer and a timeline ~4 weeks ago on March 9., but then got sidetracked by other things (hackboard, pre-final school exams, irl stuff). During this time I constantly though about it though and decided to try to convert 2 broken [Anycubic Kobra 2 Neos](https://de.anycubic.com/products/kobra-2-neo) into *this* one big printer.

### April 4th - Friday

4 Days ago I finally started to speed-run the entire CAD design starting with the frame (which I then redid one day later...). I started by converted these drawing I made the past days during school into this frame:

![Intial sketches](images/sketch_initial.PNG)
![Initial frame](images/friday.png)

As you can see in the sketches, I was initially targeting a CoreXY build with linear rails, but this idea later got ditched in favor of a simple V-Wheel based Belted XY-Gantry.

I also started dissembling one of the broken printers to take measurements of the heatbed, etc.

Time spend in CAD: 2h during the morning (since I'm almost done with schools, I don't have to go to every lesson anymore), 6h in the afternoon, evening and early night.

### April 5th - Saturday

*A caddy day*

On saturday i basically redid everything I did the day before. Instead of bolting the profiles strait to each other using blind joints, I took some inspiration of the Ender3NG, and created these "in-between structures" (see picture). I also converted this sketch (which i created the night before) into CAD (once again, inspired from the Ender3NG, but created from scratch and the final part also ended up complexly different)!

![Sketch of Z-Axis bottom mount](images/sketch_z.PNG)

Time spend in CAD: ~60% of my awake time (pain) -> 9-10h

---

<br>
<br>
<br>

> Below is the unused initial version of the journal (from 4 weeks ago) for conservation

<br>
<br>
<br>

---

**Status Update**: Due to final school exams, hackboard and terminal-craft the timeline has been delayed by one and a half weeks. This means i will be aiming for OpenSauce and not RMRRF.

**Journal Overview:**

| Date | Total time | Description | Happy with progress ? |
|------|------------|-------------|-----------------------|
| [08.3](#march-8---3h)|     3h     | Brainstorming & Gathering & Online research | Yes, finally locked in on one idea. Was really torn between the print farm, module based printer and Billig|
| [09.3](#march-9---25h) | 2.5h | Documentation & Organization | Yes, really happy: Did all the annoying markdown formatting and stuff |

---

**Timeline:**

| Date | Estimated hours | Description | Possible motivational problems |  
|------|-----------------|-------------|--------------------------------|
| 09.03 - 16.03 | 10h - 20h | Research & Parts selection - Found vendors, lock-in parts for everything, created BOM with estimate expenses, find / create CAD models for individual parts, create dimensionally accurate design specification | Unlikely - I love organizing, planning, and shopping for stuff |
| 17.03 - 23.03 | 15h - 20h | CAD design - covert design specification into CAD (and find a dark theme for onshape)| Maybe - Staring at a CAD design for multiple hours, multiple days strait can be ... exhausting |
| 24.03 - 27.03 | - 10h | Implement "Should-have" features | Unlikely - Improving a finished Design should be really motivating, cause you see what you've achieved |
| 28.03 - 31.03 |  | Buffer | |

Total expected hours: ~45h
Real-life multiplier: x1.5 -> 68h -> ~3h per day -> Realistic

---

**Features:**

| Must-have | Should-have | Probably not enough time|
|-----------|-------------|-------------------------|
| (400mm)² for X&Y, Z should have 200mm+ | Filament runout sensor | 2 Build-in filament holders (Prusa Core style: inset into case, on the left&right) |
| CoreXY with Belts | LED-Bar under Bed for status, etc| Build-in filament weight sensor (using [one of these](https://de.aliexpress.com/item/33046037411.html))|
| Enclosed (for ABS) | Exhaust air filtration using [activated carbon](https://meltbro.de/nevermore-activated-carbon-aktivkohle-fuer-voron-2-4-0-1-0-2-trident-3d-drucker.html) | External [Multi-filament switcher (Pico-MMU, 2 filaments)](https://www.printables.com/model/1083174-mmu-multi-material-upgrade)|
| Direct drive | | |
| ABL using cheap [BLTouch clone](https://de.aliexpress.com/item/1005007554425544.html)| | |
| Temperature Sensor inside & Temp-control fans | | |

---

### March 8 - 3h

Brainstorming about goal. Final 3 candidates:

- Print farm: Similar to [this](https://blog.prusa3d.com/wp-content/uploads/2021/10/DSC6780-scaled.jpeg) - Why not: Basically would only copy their design and scale it down, due to budget only 2 integrated printers -> kinda useless
- Module based: 250x250x100mm modules with only the heated, joinable in one direction, rack & pinion system on the sides, hotend on a ["crane" (picture explains it best)](https://image.made-in-china.com/203f0j00dwPqjhLbGOkI/Zpmc-Spreader-for-Rtg-Type-Container-Gantry-Crane.webp) - Why not: Budget would only allow ~2 modules -> Print volume way to small
- Billig (this): There seems to be no big (~(400mm)³) enclosed printer for under 1k -> Should be doable with only 300$ when cutting corners

Billig will be a mix of:

- [Prusa XL](https://blog.prusa3d.com/wp-content/uploads/2021/12/main_1.jpg) (frame design)
- [Voron 2.4](https://cdn03.plentymarkets.com/ioseuwg7moqp/item/images/29251/full/Copymaster3D-Voron2-V2-4-R2-SB-Kit-350-x-350-x-350mm-With-StealthBurner-29251.png) (artistic style)
- [Ender 3 NG](https://media.printables.com/media/prints/922401/images/7302744_6c89a110-ee20-4af6-ad0b-d029573e6b25_aa334db1-1287-41b3-9dea-289b26e3adf5/thumbs/inside/1280x960/jpg/dsc03455_fhd.webp) (enclosure design)

Accepted tradeoffs:

- Longevity: Will be using the cheapest parts for everything
- Print speed: Won't be fast due to size
- Power draw: Will need A LOT of energy to heatup the entire chamber

Initial design ideas:

- Printbed consist of 4 [smaller (and cheaper) print beds](https://de.aliexpress.com/item/1005007288279620.html): ~ 40€ total

### March 9 - 2.5h

Well, this document...
