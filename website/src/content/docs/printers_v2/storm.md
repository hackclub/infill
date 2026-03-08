---
title: "Storm"
description: "My first 3D printer. Cheap, uses usb c, large, fast (180mm/s), easy to use, accurate, and cool looking (hopefully all of that!"
project_name: "Storm"
repository: "https://raw.githubusercontent.com/the-X-alien/Storm/refs/heads/main/JOURNAL.md"
---
Made by: @Dhiaan Dave // Dhiaan Dave
Repository link: https://github.com/the-X-alien/Storm/
Total hours so far: 13

- [] I have a 3D printer or will be getting one before March 21st (printing legion pls save me)

---
### Goals:

- Beat the A1 at everything
- Cartesian bedslinger (like the Bambu Lab A1)
- 300×300×450mm build volume
- 500–700mm/s, sub-5min Benchy, high quality
- Screen, WiFi, Quiet
- Under $350 including shipping/taxes

---
### Day 1 - Feb 28 2026 - 2 Hours
I thought that Campfire SJ would be a good place to start making my printer because I was an org and not a participant.

But the second I opened the Infill website, I was lost by all the terms like Gantry, Toolhead, and Extrusions. 

But after googling and asking various AI chatbots, I learned that the Gantry is the frame system that allows movement, the toolhead is the part that encompasses the hotend and extruder, and extrusions are metal parts that make up the frame of a printer.

But I was still lost on how to actually make the 3D printer.

After watching a few YouTube videos on how to assemble the frame of a Cartesian 3D printer, I learned that the frame is built of a square base made from metal extrusions, and then there are two extrusions attached vertically on each side with one extrusion connecting them, allowing X Y and Z movement.

One video that really helped me was this one video on how the Bambu Lab A1 works, because it is also a Cartesian printer: https://www.youtube.com/watch?v=f94CnlQ0eq4

I understood the frame completely, but now I was lost on how to make things like the toolhead.

<img width="1240" height="820" alt="image" src="https://github.com/user-attachments/assets/8e75f1ee-b2e3-4fc5-a71a-6963a64ac9bc" />

And right then, Alex (@alexren) pulled up to the event and I asked him for help.

He explained to me how he made his tool head by modeling the inside with the dimensions of the hotend, and how he added magnets to make the hotend hotswapable.
He also recommended that I look at other 3D printers to see what they did for their toolhead and other parts.

So I viewed printers like PandA and Nighthawk and saw their toolhead design.

And now I need to pick a hotend and an extruder so I can model my toolhead.

---
### Day 2 - Mar 3 2026 - 5 Hours

I spent some more time researching what parts I am actually using to build the 3D printer.

(to come up with this list, I had to read alot of reddit, watch many youtube videos, and I had to ask many questions to Claude and Grok)

So, I had to decide what kind of Aluminum extrusions to use.

I needed the frame to be both sturdy and impact resistant.

So, I had a large base made up of 4x 350mm 4040 Extrusions to spread vibration impact,

Then 2x 2040 Extrusions for the Z axis movement,

And the cross bar uptop will be a 2020 extrusion.

To connect them, I will be using cornerplates.

The extruder will be a Orbiter V2.5 which is the evolution of the V2.0 which is the standard lightweight direct-drive extruder for fast bedslingers

And the hotend will be a Trianglelab TZ V6 2.0 Hotend which is considered to be a budget A1 hotend, because it prints 30–45 mm³/s on PLA with a 0.6 mm nozzle compared to the A1's 20–25 mm³/s speed, and it has a bi-metal heatbreak, copper block, fast heating, and it is CHT-compatible nozzle options. It is also super  lightweight, reliable, and it will work with with most V6-style mounts. (V6 style mount to keep in mind when im cadding the toolhead)

For the nozzle, I'll go with any generic no name 0.4 mm hardened steel CHT-style (3-hole/high-flow) nozzle because 0.4mm is the industry standard for a balance of speed and quality for nice printers like the A1, A1 Mini, and Ender 3.

For cooling, I will get Dual 5015 blower fans with high static pressure (24V) because the nozzle and hotend are going to run hot, and so this powerful combination should cool it down.

For leveling, im using the Klicky probe, which is better than the CR Touch and the BL Touch in everysingle way of acuracy, weight, noise.

---
### Day 3 - Mar 4 2026 - 6 Hours (I didn't think research would take this long :heavysob:)

Made some modifications to the above parts list after reading more on Reddit

Aparently since the Klicky probe needs to dock, it's not ideal for bedslingers, and designed for other printers.
So instead, I am switching to the BTT Eddy, because it is super fast and scans the entire bed in one go, making my printing time faster.

Aparently CHT nozzles are a pain to clean if they get a clog and are annoying, and you might just have to throw them away altogether.
So I'll start with a basic standard hardened steel 0.4mm V6 nozzle because I'm a beginner and I want the printer to work before I start trying anything crazy.

Scratch the first thing, I'm going with a CR Touch because the the BTT Eddy is influenced by location and is aparently a pain to calibrate because it is super dependent on the magnetic field of the area.
<img width="352" height="792" alt="image" src="https://github.com/user-attachments/assets/451fb54d-27c4-403d-aa9a-bd238fc0f1fc" />

Wait scratch that again, (I'm sorry) I'm trying to make my printer as fast as possible so a light probe would help, and the Biqu Microprobe is recomeneded because it only weighs 6 grams!
<img width="355" height="587" alt="image" src="https://github.com/user-attachments/assets/55ece148-f39e-4f48-9e35-40dff47505da" />

(I should put a disclaimer that I might change any parts later if I get recommendations or I find a problem with them)

I guess I should start with the motherboard, so for the control board, I am going with the BTT SKR Mini E3 V3, because not only is it super popular, but its also super cheap. It also just makes things simple.
<img width="1409" height="956" alt="image" src="https://github.com/user-attachments/assets/53e2cba0-9552-4b38-b553-0a619aeddd3e" />

Then for the brain, I am using a BTT Pi V1.2.1, because it is designed for the exact motherboard, it can run Klipper, and its optimized for printing. It also has an SPI Port

So I can connect a TFT35 SPI touchscreen for Klipperscreen so I can control the printer without an external screen.
<img width="168" height="168" alt="image" src="https://github.com/user-attachments/assets/bb05352c-ba5b-4bbf-bd1d-b7d27eba63e8" />

For my motors, I am choosing the NEMA 17 Stepper Motors because they have high torque and good precision to have detailed 3D prints.
<img width="522" height="522" alt="image" src="https://github.com/user-attachments/assets/5492777f-fd98-4749-85e0-d0fd00f092e0" />

TO keep the thing running, my power supply will be a 24V 15A one, because all of my components take 24V to have more power.
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/87c9b1b3-fdf8-4ab1-a79e-5540587c41f6" />

For my heated base, I will be using a 310x310mm 24V 220W Aluminum Substrate Heated Bed, so my prints stick to the plate.
<img width="342" height="342" alt="image" src="https://github.com/user-attachments/assets/2a35054d-3fcc-4426-bbc4-bd0e77d0f4af" />

For the actual build plate, I will be using a 256x256mm PEI Textured buildplate because it is a good size so I can make most things, and the texture makes the print stick to the plate and also makes it easy to take off.
<img width="1000" height="1000" alt="image" src="https://github.com/user-attachments/assets/e82596f2-42fd-4914-b653-5e2094203dd5" />

I also added a 24V 4010 Cooling fan to cool the toolhead because its going to get pretty hot.
<img width="220" height="220" alt="image" src="https://github.com/user-attachments/assets/3d9723a1-6bff-4e6c-ab9c-5f2afd717100" />

I also added dual 24V 5015 Turbo Blowers to cool the plate and parts quickly.
<img width="800" height="800" alt="image" src="https://github.com/user-attachments/assets/e8a60b2e-77e4-4b87-a662-3bf5db9a7268" />

I got all the electronics down, but I still need to find the extrusions and rails/rods, and I might have to change some parts because the total is already around $280.

---

