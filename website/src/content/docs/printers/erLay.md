---
title: "erLay"
description: "A ultra portable 3D printer designed for competitions"
project_name: "erLay"
repository: "https://raw.githubusercontent.com/Badbird5907/erLay/refs/heads/master/README.md"
---
erLay is a ultra-portable CoreXY 3D printer made by [Evan Yu](https://evanyu.dev) and [Aaron Huang](https://runthebot.me)

This printer is built to print small parts needed fast at robotics competitions where our main limitations are space and time. This printer will mainly print spacers, shaft collars, pullies, etc.

# Goals
- Ultra-portable (for robotics competitions!!)
- CoreXY
- Pico MMU (Optional)
- Zero Click ABL
- Built-in carrying case (The printer will collapse into something like a pelican case)
- Can be powered by a (multiple) power banks

# Total Time

Aaron: 64.5h
Evan: 36h

# Feb 12 2025

- Came up with name, specs, and design.
- Research on different 3d printer designs & parts (VORONDesign, etc...)
- Started options for BOM

Evan: 2h
Aaron: 4h

## Both
### What was done:
- Discussed name, specs and design
- Rabbit holing and yapping about option
- Both already have 3D printers
### Some of our other ideas:
- 2/3 stage elevator on a bed slinger 💀
- smaller Voron v0


## Aaron

- I'm the one that dragged other bozo onto this
- I am in the process of building a [Hex Zero](https://github.com/Alexander-T-Moss/Hex-Zero)
- Went down a printer rabbit hole

### ABL:
- [ZeroClick](https://github.com/zruncho3d/ZeroClick)
- Seams nice and cheap
- Used on Hex Zero
- ABL needs more research

### Hotend/Toolhead:

Requirements:
- COTS
  - We do not want to be designing a Toolhead
  - We can use a custom one if it relly came to it
- Direct drive
  - Keep it compact
  - Print filaments that are harder to print (Remember robotics!)

Options:
- [Apogee Extruder](https://www.filastruder.com/products/ldo-apogee-toolhead-for-ender-3)
  - Light 170g
  - Cheap
- [Creality Sprite](https://www.creality.com/products/sprite-extruder-pro-kit)
  - Kinda heavy 266g
  - Dual-Gear Drive for flexibles
  - Cheap
- [BIQU H2](https://biqu.equipment/products/biqu-h2-v2s-extruder-for-b1-bx-ender-3-3-v2-5-6-cr6-10?variant=40218342555746)
  - Dual-Gear Drive for flexibles
  - Weight ok 195g
  - Cheap ish
  - Big
- [**Orbiter**](https://www.3dlabtech.ca/product/ldo-smart-orbiter-extruder-kit-v3/)
  - Probably this?
  - Cheapish
  - Canadian website???
  - We are Canadian so no tarifs!!?!??!?
  - Light 175g
  - Dual-Gear Drive for flexibles
  - With a CHT nozzle??!!!?!?
  - WHAT??? for 87 USD?????? (The Canadian dollar is not doing so well)


Ok that's it for today I have school tmr

# Feb 13 2025

Aaron: 5h
Evan: 2h

## Aaron:


Yay snow day!!! 
Ok so I was losing my mind at midnight yesterday and did not realize that the Apogee uses an orbiter
I probably need to find a better source

### Frame


I was brainstorming frames today and I wanted the hingeing lid of the case to be the Z-axis
I started with some CAD (Bad idea) and I got almost nowhere

Anyway I do here are the current frame options after spending 30 mins failing at CAD:
- Hingeing lid with the bed in the middle
- Linear Rods as the Z-axis support (Similar to Neutrino)

I also started a basic Onshape Part Lib and did a lot more research

I've learnt my lesson and now will spend the next hour **drawing concepts** before CADing

### Drawings


I spend half an hour making a Iso Grid YAY!
Anyway Heres the idea
![3D Printer Concept Iscometric](https://cdn.hack.pet/slackcdn/e7751f85e307172b6f68b6b7c01aed9b.png)

## Evan:

Spent most of the day working on [makropad](https://github.com/Badbird5907/makropad), it's almost done!

### Research:
- Researched how CoreXY works
  - https://corexy.com/theory.html
  - https://all3dp.com/2/corexy-3d-printer-is-it-worth-buying/
  - https://3ddistributed.com/belt-frequency-and-tensioning/
  - 3 Stepper Motors:
    - 2 for the XY
    - 1 for the Z
  - Print head is fixed to XY axis, while z axis is moved for printing
  - Belt frequency can differ between machines
  - Tensioning is important for performance. Frequency can affect speed and print quality
  - Over-tensioning can cause the belt to slip/wear out faster
  - Tighten belt until there is some resistance when pushed. There should be no slack.
  - Looser belt = layer shifting when printing (misaligned prints)
  - Failure can be caused by:
    - Belt friction
    - Damaged belt teeth
    - Slip/rubbing of the belt
    - Debris
  - Loose/missing pulley teeth can cause jerky movements
  - Pitch = distance between teeth (most are 2mm)
Pros of CoreXY:
- Speed
- Accurate
- Compact
- Rigid frame
This makes it perfect for our use case, as we want a small and fast printer we can take to competitions (hackathons and FRC).

Limitations:
- Complex assembly
  - This could be an issue for portability, if we need to disassemble the printer.
- Higher cost
- Z axis constraints

![Reference Mechanism](https://corexy.com/reference.png)

[CoreXY vs Bedslinger](https://store.creality.com/blog/corexy-vs-bed-slinger)

Bedslinger:
- Advantages:
  - Simple assembly
  - Affordable
  - Easy to use
- Disadvantages:
  - **Inertia** caused by the bed moving
  - Speed is slower due to bed inertia 
  - Higher vibration due to bed movement
  - As size of bed increases, the slower the printer has to be due to higher weight

## Aaron Part 2:
I've been laying out the printer

So the idea was to have both the gantry and the bed fold up but after an hour of layout it looks pretty impossible with the stock Voron 0 layout
![Voron Layout](https://cdn.hackclubber.dev/slackcdn/604e7b44379364c485696c60c2bfce4b.png)

There's also a concept sketch that I will put on here sometime

### Feb 14 & 15 2025

Evan: 0h
Aaron: 0h

random thought from Evan: What if the Z axis was telescoping or something
![image](https://github.com/user-attachments/assets/70f3963c-5d15-45f7-8c60-03f8c70ef597)


14th: We spent the day preparing for a robotics competition

15th: Competition Day

# Feb 17 2025

Evan: 2h
Aaron: 0h

## Evan
Researched other people's custom CoreXY builds:
1. https://www.instructables.com/CoreBot-CoreXY-3D-Printer/ **this is a really good blog/guide**
 - X/Y Movements: 12mm y / 9mm x linear rails
 - Z: 2x 10mm lead screws + 4x 12mm smooth rods.
 - At the length of spindels, constraint the spindle at top + bottom to keep distortion/ghosting low
 - Long travel distances will cause bowden tube to flex, causing friction + jams
 - Frame assembly should be straight forward
2. https://www.instructables.com/How-to-Design-and-Build-a-3D-Printer/
 - 3030 extrusions have higher rigidity
 - Aluminum is cheap, light, and can be anodized
 - Aluminum extrusions can be connected in many ways
 - Blind joints = lower part count, less tollerences to worry abt, simple
 - CoreXY reduces weight by putting motors on frame rather than head
 - Can accel head much harder with less inertia
 - Instead of X/Y motors, there are A/B motors, connected directly to the XY belts
 - Belt loop allows for a gear ration between motor and CoreXY belt. (see the writeup for full info)
 - GT2 belts are cheap and easy to source
 - Belts can be run along the inside of frame
 - Bed is 8mm thick aluminum tooling plate
 - Significant thermal mass = stable temps
 - Thick = less bed warping
 - 200w DC silicone heater under bed
 - Can be replaced with PCB heated bed
 - Extruder w/ 3:1 gear ratio = finer control of filament
 - Hot end is where plastic is heated and extruded

# Feb 22 2025

Evan: 2h
Aaron: 10h

## Aaron
### Folding Printer (Frame V1, V2, V3)
![V1 and V2](https://cloud-kcrikwrqr-hack-club-bot.vercel.app/0notewise-untitled_2025-02-13-1__1_.jpg)
This is how 2 different versions of the frame would fold. I layed out V1 a while back and it did not fit. 
V2 also has problems with the center of gravity.
![V3](https://cloud-6ti4f5y08-hack-club-bot.vercel.app/0image.png)
This is the latest frame that we have made. It will have a bed on one side and a gantry on the other. This frame costs way too much and it still needs a gantry and a bed

### New idea
Instead of making it fold and making it fast, go all out on the portable aspect and make the printer powered off a USB c power bank (100W)

## Evan
### Researched different power supplies
- Our power budget should be around <=180W
- USB-C PD
 - Can supply up to 240W
 - Maybe we can pull either 180-240w from a single USB-C PD supply
 - High wattage is _expensive_ (easily $50-100+)
 - Or we can pull 60w from 4 power banks, allowing hot swapping power supplies on the fly. Also much cheaper since lower wattage per power bank
 - Concern: how long the power banks will last
 - I'm probably going to design a custom PCB to do this
  - Suitable(?) controllers:
   - [TPS25750](https://www.ti.com/product/TPS25750)
   - [STUSB4500](https://www.st.com/en/interfaces-and-transceivers/stusb4500.html)
 - I want to keep the cost of the PCB as low as possible, the STUSB4500 is probably the best as it has way more stock on LCSC (8.3k vs 14) than the TPS25750, and is 20c cheaper.
- Use a LTC4370 to load share between the different supplies
- Use Diode OR-ing or Ideal Diode controllers to isolate power supplies and prevent **backfeeding**
- Also made our hours auto update via github actions + a python script
- 
## Aaron 
Spent a lot of time researching Linear rails/rods and how to hold a heated bed.
A lot of Cadding

# Feb 24 2025

Evan: 2h
Aaron: 1h

Discussed details over dinner.
### USB PD Power Supply
- 240W power budget (400 max but we wont be testing this)
- Load balancing (diodes) / backfeeding
- Boost -> 24v
- Screw terminal output
- Automatic negotiation
- 4 USB-C inputs
- Screw terminal input (bypasses load balancer and connects directly to output screw terminals)
 -> (For testing)
- Boost every input before load balancing to prevent issues w/ voltage diff
- Pico negotiates even wattage from all to reduce load on balancer
- Digitally set target voltage via pico (?)

# Feb 25 2025

Evan: 1h
Aaron: 0h

Did some research on USB-C PD controllers.
There are a couple options, but i've only looked at two so far:

| Name                                                                     | Max V | Max A | Max W | I2C Address Configurable | Notes                                    | Suitable |
|--------------------------------------------------------------------------|-------|-------|-------|--------------------------|------------------------------------------|----------|
| [TPS65987D](https://www.ti.com/lit/ds/symlink/tps65987d.pdf)             | 20V   | 5A    | 100W  | Yes (ADCIN1/ADCIN2)      | Address configured with Analog signal(?) | Yes      |
| [STUSB4500](https://www.st.com/resource/en/datasheet/stusb4500.pdf)      | 20V   | 5A    | 100W  | Yes (ADDR0/ADDR1)        | MAX 4 on 1 i2c line. (See 4.1)           | Yes      |
| [FUSB302](https://www.onsemi.com/download/data-sheet/pdf/fusb302b-d.pdf) | 20V   | 5A    | 100W  | No                       |                                          | No       |

# Feb 24-26
Aaron: 3h
Evan: 3h

## Aaron
Decided to build a custom tool head similar to ESO3D. CADing that and gantry.

Inspiration:
ESO3D
Creality K1
Voron V0

## Evan
Did some research on the RP2350. Read through the [integration guide](https://datasheets.raspberrypi.com/rp2350/hardware-design-with-rp2350.pdf) and [datasheet](https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf).
We'll probably use the A variant over the B variant as we only need the I2C.

# March 9-11
Aaron: 36h
Cadding

![](https://hc-cdn.hel1.your-objectstorage.com/s/v3/77764ee2d9902558b36006d0567d32e953ed0d55_screenshot_2025-03-09_174912.png)
![](https://hc-cdn.hel1.your-objectstorage.com/s/v3/b58ed7af6b8390dd2260b838b87cf3647395d5b5_screenshot_2025-03-09_170620.png)
![](https://hc-cdn.hel1.your-objectstorage.com/s/v3/0413d1285abeacb02bde7a57890c2a7a92ba62bc_screenshot_2025-03-10_021449.png)
![](https://hc-cdn.hel1.your-objectstorage.com/s/v3/e3bd04a5aadf4aa9010ca2115e4d4cfd83b76efd_screenshot_2025-03-10_021441.png)
![](https://hc-cdn.hel1.your-objectstorage.com/s/v3/861d3e04107265b51eb068c50b367189b72301d2_screenshot_2025-03-10_015741.png)
![](https://hc-cdn.hel1.your-objectstorage.com/s/v3/6cd0273d3beca79aefc81e11777e9dfeedac7693_screenshot_2025-03-09_175539.png)
![](https://hc-cdn.hel1.your-objectstorage.com/s/v3/2ecf0c055b351388e8a5fd1cf67841e1918324b0_image.png)

# March 23
Evan: 2h

## Evan
Did some research into the USB PD 3.0 spec (specifically PPS). Currently, there doesn't seem to be a (cheap) sink ic that supports PPS and a **configurable** i2c address.
I basically want the [AP33772S](https://www.diodes.com/datasheet/download/AP33772S.pdf) but with a address configuration function (it has a static address of 0x52)

Also watched [Phil's Lab #104](https://www.youtube.com/watch?v=W13HNsoHj7A) and [#114](https://www.youtube.com/watch?v=kUruN6WBgSw)

# March 24
Aaron: 2.5h
![image](https://hc-cdn.hel1.your-objectstorage.com/s/v3/5a871d017b01af523516121f1572278c6bb2117e_image.png)
![image](https://hc-cdn.hel1.your-objectstorage.com/s/v3/bfbba6814d80e5459c0b27108d4db9ab9f8c9274_image.png)

Made a master sketch for the bed and the actual bed mount.
Made of 0.75in square extrustion

# March 26
Evan: 6.5h

## Evan
I spent most of my time trying to figure out how to design the schematic. A major blocker I'm stuck at right now is *how* to power the rp2040. Because I want the power banks to be hot-swappable, I need to power the rp2040 off any one of the USB-C ports, and I don't want to add a buck converter for each port... Things can get expensive *quickly*.

*This is likely a fire hazard :trollface:*

Current progress:
![image](https://github.com/user-attachments/assets/796e684e-09f3-46bf-81a6-0f619603a5c8)
![image](https://github.com/user-attachments/assets/73953d6d-58ae-4eef-b516-209afc0b4c3b)

The PSU is being developed in [Badbird5907/PDSU](http://github.com/badbird5907/PDSU)

I'm probably going to just buck the voltage for each USB port with 4x TPS54331 and use diode OR-ing if I don't have any better ideas tmr morning.

# March 29
Aaron: 3h

Added Z-Axis Motor. Way too painful
![image](https://hc-cdn.hel1.your-objectstorage.com/s/v3/ce4d11413c8954bd62e26e882ce9796a30e27996_image.png)

# March 30
Evan: 6h

Did a bunch of research/video watching, and some chatgpt-ing.
The MCU will likely pull its voltage from a step-down converter after the diode ORing to keep costs down. I still have my doubts weather this will work or not...

# March 31
Evan: 3.5h

The PD controllers are complete, now I need to figure out how to load balance and combine the inputs. Right now i'm trying to find the perfect buck/boost VRM that's cheap enough to get 4 of.

# April 1 & 2
Evan: 4h

STILL trying to find a suitable buck/boost VRM. I found the XL6019, which is PERFECT... *except* it's max switching current is 5A, which is does not work well for our design, which pushes 20A/3A -> 12V/5A (60W) through. That means our **switching current** (the current that flows through as it makes/breaks contact) is about 8.53A, which is way too high for this chip and will likely burn it.
I found the LT8645S, which seems to support our use case and switching current, however it costs $8.77 each, making it prohibitively expensive as we need 4 per board.

[4pm] I'm going to spend the next few hours looking through MORE datasheets... I'm going to see if it costs less to use a MOSFET **controller**, which should be cheaper and allow for more current as these controllers do not include a FET. 
