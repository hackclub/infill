---
title: "ED3D"
description: "A printer that has hologram showing whats being printed"
project_name: "ED3D"
repository: "https://raw.githubusercontent.com/Fastestkyo/ED3D/refs/heads/main/journal.md"
---
# ED3D Project Journal

**Author:** [@karnx](https://github.com/Fastestkyo)  
**Repository:** [https://github.com/Fastestkyo/ED3D](https://github.com/Fastestkyo/ED3D)  
**Total Time Spent:** 20.5 hours (as of last update)

---



## Progress Log

### Day 0: February 13, 2025 (0.5 hours)
- **Initial Ideation:**
  - Conceptualized the ED3D project: a 3D printer with a transparent display to visualize the print in real time.

### Day 1: February 15, 2025 (5 hours)
- **Research & Planning:**
  - Researched transparent screen and stuff. This video was very sigma https://www.youtube.com/watch?v=IhldXT7yxXo
  - Started with the BOM. EVERYTHING IS EXPENSIVE IN INDIA 😭. Added basic stuff like galvanized square steel, or skr mini e3v3.


### Days 2–4: February 16–18, 2025 (11 hours)
- **Component Research & Design Skills:**
  - Sourced mechanical and electronic parts for the BOM. EXPENSIVEE!!
  - Learned basic 3D modeling techniques for part design and visualization. Using fusion cuz sigma

### Day 5: February 20, 2025 (4 hours)
- **Hardware Assembly:**
  - Updated the BOM. Added other electronic components. like 24V 16.7A 400W power supply and nema17 motors. 
  - Cadded the printer frame using welded galvanized square steel tubing. 
 
    ![PRINTER-FRAME](https://github.com/user-attachments/assets/fef93311-ddb1-49f1-8a58-a70679d587c3)


### Days 6–16: February 21–March 2, 2025 (24 hours)
- **Z-Axis Development:**
  - Began construction of the Z-axis assembly, thinking of using lead screw instead of ball screw actuator. 
  - Revised BOM based on component fit and new constraints, Removed ball screw and added the lead screw stuff (linear shafts, rails.)

    ![Z AXISS](https://github.com/user-attachments/assets/536d5975-e3ec-4e65-87a3-0dc43c495e3e)

### Days 17–22: March 2–6, 2025 (5 hours)
- **Heatbed Mounting & Continued Research:**
  - Added support structure for the heatbed, revised z axis to use lead screw, linear rail and linear shaft. Im going to make a cantilever bracket from steel flatbar.
  - Continued background research. Thinking of adding bl sensor. bl sensor very expensive in india (75 dolla).

    ![Z AXIS](https://github.com/user-attachments/assets/a56423a7-f586-4adb-a9e5-d7c679b7e917)
 
      
    ![Z AXIS](https://github.com/user-attachments/assets/52c3d090-2eeb-432f-a230-d23d1db38c38)

### Days 23–30: March 7–13, 2025 (30 hours)
- **Z-Axis Finalization & XY Initiation:**
  - Completed Z-axis mechanics and calibration, decided on 1 linear rail, 1 lead screw, 2 linear shafts.
  - Began building the XY axis using belt-driven motion systems. Corexy belt routing from reprap website.
 
    ![COREXY BELT ROUTING](https://github.com/user-attachments/assets/65d4a6e9-30a5-4cf5-abff-ac4c4e845f0b)

    ![Z-Axis Finished](https://github.com/user-attachments/assets/32ac731c-7475-4b3c-b002-14f731b863bc)

### Days 31–37: March 13–20, 2025 (23 hours)
- **XY Axis & Toolhead Development:**
  - Completed XY axis assembly. Using 6 16t pulley, 2 20t stepper pulley, 2 16t smooth idler pulley
  - Initiated design and construction of the toolhead. Using 2 4010 axial fans and 1 4010 blower for cooling and v6 e3d hotend clone. Im also going to be using a bl sensor.

    ![xy-assembly](https://github.com/user-attachments/assets/fa92bf7b-fd68-4b7d-9ae4-94b5f682391a)
  
### Days 38–40: March 20–23, 2025 (26.5 hours)
- **Toolhead Completion:**
  - Finalized toolhead mechanics and mounted extruder assembly. Extruder is gonna be dual gear drive clone (again cuz of expensive)
  - Revised BOM cuz of expensive parts 🤫🧏‍♂️
 
    ![image](https://github.com/user-attachments/assets/66bb0a5b-2c68-43ee-8bd2-acfb032acdd1)


### Days 41–47: March 23–29, 2025 (26.5 hours)
- **Final Touches & Submission:**
  - Submitted the finished ED3D printer for review.
 
    ![PRINTER](https://github.com/user-attachments/assets/f3fd9fda-ad09-4d44-9c03-00bf5b19854b)
    ![PRINTER-TOP](https://github.com/user-attachments/assets/26eac7e6-4b60-45c7-854c-48d358da1f2e)


---
## Here is the BOM:

| Item                               | Quantity |
|------------------------------------|----------|
| Linear Rails (MGN12C)              | 4        |
| Lead Screw for Z Axis              | 1        |
| BTT SKR Mini E3 V3                 | 1        |
| FYSTEC Mini12864 RGB LCD (CHEAP)   | 1        |
| Stepper Motors (NEMA 17, 48mm)     | 4        |
| 24V 16.7A 400W Power Supply        | 1        |
| Dual Gear Drive Extruder (Clone)   | 1        |
| Capricorn PTFE Tube (Set)          | 1        |
| Heatbed (Ender 3)                  | 1        |
| Heatbed Knob Set                   | 1        |
| V6 Hotend Set (E3D Clone)          | 1        |
| V6 Hotend Aluminum Bracket         | 1        |
| CHT 0.4mm Nozzle (Clone)           | 1        |
| Endstop Limit Switches             | 3        |
| 4010 24V Cooling Fan & Blower      | 1, 2     |
| GT2 Timing Belt (Set)              | 2        |
| 20T Stepper Pulley (GT2)           | 2        |
| 16T Idler Pulley (GT2)             | 6        |
| 16T Smooth Idler Pulley (GT2)      | 2        |
| 5mm Coupler                        | 1        |
| M3 Threaded Heat Insert Set        | 1        |
| M3 Washer Set                      | 1        |
| 1x1" Steel Tubular (7m)            | 1        |
| 1" Steel Flatbar (1m)              | 1        |
| 2020 Aluminum Profile(0.5m)        | 1        |
| 2020 M3 T-Slot Nuts (Set)          | 1        |
| Generic ABS Filament               | 1        |
| BL-Touch Bed Leveling Sensor       | 1        |
| Screws (M3)                        | 1        |
| Filament Detector                  | 1        |
| Filament Detector Cable            | 1        |
| Linear Shafts                      | 2        |
| Linear Bearing Block               | 2        |
| Raspberry Pi4                      | 1        |
| Hand Tap Set (M3)                  | 1        |
| Monitor (LCD)                      | 1        |
| Wire Spool                         | 1        |

*Note: This journal will be updated regularly to document ongoing progress and developments in the ED3D project.*
