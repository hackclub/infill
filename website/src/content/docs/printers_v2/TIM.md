---
title: "TIM"
description: "60mm^3 CoreXZYZ 3d printer made to fit in a carry-on"
project_name: "TIM"
repository: "https://raw.githubusercontent.com/2Mon/tim/refs/heads/main/JOURNAL.md"
---
Made by: @1Mon

Repository link: https://github.com/2Mon/tim

Total hours: 22

# Feb 15 2026 | Research

ive been wanting to make a silly printer for a while. I came across some cool motion systems from OYO, the person who made POYON. I was inspired by his design for a CoreXZYZ, which he called MOT. I was talking with some friends and they showed me MIR, which is another printer made by Apsu. It uses the same motion system. Neither design had much progress outside of the motion system, so I want to flesh it out a bit and make a working machine. Also, OYO's design has some weird mounts for the idlers. Its kinda impossible to use as is, so I will be expanding the frame a bit to make it easier to fit everything in. 

This is OyO's design with the impossible idlers. He seems to design motion systems without caring if they are usable lol.
<img height="450" alt="Screenshot 2026-02-27 at 5 25 16 PM" src="https://github.com/user-attachments/assets/18169bb7-1bf3-405f-8f28-beb0c8c0dce6" /> <img height="450" alt="Screenshot 2026-02-27 at 5 26 08 PM" src="https://github.com/user-attachments/assets/a0e23e30-e03b-4da0-94a1-900485af7521" />

This one is MIR, and while it is more fleshed out it still needs a toolhead. 
<img width="600" alt="image" src="https://github.com/user-attachments/assets/ee94fbd4-fc64-4340-86b1-e14044969b20" />

I want to keep the compact size of OyO's design while using the better XYZ (if we want to call it that) joints from MIR. I call it TIM. in theory because its MIR and MOT combined and reversed, but also tim is a cool name.

Time Spent: 2h


# Feb 20 2026 | Motor Mount

I really like the way that OyO laid out the motors in his design. Since I am trying to bring this to RMRRF, I need to keep this small enough to fit in a suitcase. I set up the motors so that the bodies are on the inside, right below where the build plate will go. I think that I will end up doing an external electronics bay on this, so this will help keep everything super compact. I am using two bearings to make the belt go to the edge of the motor, maximizing the xy travel while keeping the footprint very small. I can probably fit this as a carry on. 

<img width="644" height="484" alt="Screenshot 2026-03-01 at 12 24 00 PM" src="https://github.com/user-attachments/assets/6f057836-9704-4737-aafb-274700c4edde" />

This part also includes mounting for the four Z rods, which currently just slot into the holes. I should probably add a way to constrain them better. I dont plan to have an actual extrusion frame around this machine, so those rods need to be super rigid in the printer part.

And here you can see it with the motors, z rods, and bearings. 

<img width="642" height="439" alt="Screenshot 2026-03-01 at 12 27 45 PM" src="https://github.com/user-attachments/assets/c3349bf4-d860-414a-a0ad-f390e702669d" />

Time Spent: 4h

# Feb 25 2026 | Gantry Stuff

Making the gantry for this is going to be VERY difficult. I am trying to keep it compact, and the belt path is not exactly easy to make compact. My first iteration turned out to be impossible to make IRL. there were sections that were WAYY too thin to be able to print well and stay stable during prints and under belt tension. Heres that first design: 

<img width="229" height="260" alt="Screenshot 2026-03-01 at 6 39 12 PM" src="https://github.com/user-attachments/assets/859b9020-4565-43bc-8e4a-8d54dc865435" />

I ended up changing up the belt path a tiny bit from this version, as the innitial setup didnt really allow a lot of space for the belt to be able to pass over the bearings. I changed it to have the single side of the bearing (wow i need a better name for this) be further out on the rod, which restricts my travel a bit but ends up making the belt path MUCH easier. 

Here is my current design. It uses 125mm long 8mm linear rods and F693ZZ bearings for the belts to ride on. 

<img width="522" height="394" alt="Screenshot 2026-03-01 at 6 45 04 PM" src="https://github.com/user-attachments/assets/3388542c-d7cb-471f-bd92-a020d7e2485f" />

And here it is with the bearings and rods. Its a little difficult to see how it will go together.

<img width="634" height="296" alt="Screenshot 2026-03-01 at 6 45 33 PM" src="https://github.com/user-attachments/assets/144ac54c-452f-4766-976d-7d5e57152660" />

And here it is in the context of the rest of the machine. You can kinda see how the belts will go up from the motors to the gantry and back down. 

<img width="595" height="386" alt="Screenshot 2026-03-01 at 6 46 22 PM" src="https://github.com/user-attachments/assets/f1e5e52f-7b3b-418b-9ba0-3eeb92c75535" />

Time Spent: 6h 

# March 1-5 2026 | XY Stuff

Outside of the weird Z axis, this printer is basically just a messed up cross gantry machine. So I need all the hard parts of a cross gantry, while getting literally 0 benefits. yay. Cross gantry is a bit weird to design around, as toolheads need to have a lot of room for the carriages/bearings. 

I started off my design with the XY rods. I innitially used 8mm rods, which you can see here. 
<img width="400" alt="image" src="https://github.com/user-attachments/assets/f615af22-7353-4d37-8132-daae677135ab" />

It is fairly simple, basically just two more 8mm rods with bearings on them, with printed parts to connect them to the other bearings. I plan to have the bearings press fit into the parts for simplicity. After attempting to design a toolhead for this, I realized that the 8mm rods would be wayyy too big for the tiny nature of this machine.

I switched to 6mm rods with carbon bushings instead of bearings. This means that instead of a 16mm hole for the bearing, its only an 8mm hole which makes packaging a lot easier. 

<img height="228" alt="Screenshot 2026-03-05 at 11 33 41 PM" src="https://github.com/user-attachments/assets/de98f933-f51c-44b9-8c64-0004378b47dd" />

These are the bushings I am going to use, specifically 6x8x20mm. This should give me a good balance between rigidity and compactness, which I REALLY need to optimize in this machine. I want to keep the outer dimensions within 200mm so I can bring it on a plane. 

I started to design a toolhead around these bushings, using a TZ6 at the start, and then moving to a TZE3, and then to a bambu hotend. I needed something that was small so that I could get as much travel as possible. 

<img width="300" alt="Screenshot 2026-03-05 at 11 35 49 PM" src="https://github.com/user-attachments/assets/b30cd138-8779-4291-bf81-19b78cf7b177" />

This was my first idea for the layout of the toolhead. very compact but not really easy to design around. 

<img height="300" alt="Screenshot 2026-03-05 at 11 36 34 PM" src="https://github.com/user-attachments/assets/352b4d96-b2b8-4f43-b14d-cd79eb45a320" />

I made a big block to try laying it out, but I ended up realizing that I wouldnt be able to get full travel, which you can see here. The bed in this image is 72mm, which is pretty close to the 60mm that I am trying to get. 

<img width="500" alt="Screenshot 2026-03-05 at 11 37 59 PM" src="https://github.com/user-attachments/assets/21b86997-77c9-48ed-a8e9-b8d7fbcc903b" />

I could have offset the bed a bit but I decided that that would be really ugly and I didnt want to do that. I was also experimenting with colors that I wanted to do for the printer. I think I'm gonna do this cool shiny pink stuff. Because why not. Pink is cool. 

Next, one of my friends gave me the genius idea to use a 2 in 1 out hotend. Most of my issues were coming from the fact that hotends are always going to be centered around the bowden input, meaning that I would need to offset it so that the linear rods dont interfere with it. I had the idea to make the bowden tube kink around the rod, but i decided that that would be too annoying and weird. I discovered the E3D Cyclops hotend, which is a 2 in 1 out hotend. By some miracle, the rod can go right between the two bowden tubes. Its perfect. Its also incredibly silly, and will let me do multi color on this stupid thing. Heres a pic of how it looks. 

<img width="237" height="436" alt="Screenshot 2026-03-05 at 11 45 41 PM" src="https://github.com/user-attachments/assets/e464b9a9-fb46-4da9-af6a-8b34acccc5fa" />

The rod can go right through the middle and the bowden tubes can come out around them. Its awesome. Its also really cheap on aliexpress. Overall 10/10. I needed to do some little changes to some of the parts, including the xyz joints to allow for some extra travel so the nozzle can reach the whole bed. This is what the new part looks like. 

<img width="402" height="358" alt="Screenshot 2026-03-05 at 11 47 26 PM" src="https://github.com/user-attachments/assets/636cba22-952f-4bc5-9c41-75f8a8185616" />

I think that overall its an improvement. Part uses less material, i get to mess with a cool hotend, and i get to have fun. win win win. 

Lastly, I added a top plate for the printer. Currently its very simple and just holds the bearings for the z idlers. In the future I want to add a place for people to be able to sign it during RMRRF, as well as hold the extruders. 

should I develop my own silly dual extruder? maybe. would be funny. 

Time Spent: 10h
