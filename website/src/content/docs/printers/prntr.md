---
title: "prntr"
description: "A small, fast printer used for rapid prototyping"
project_name: "prntr"
repository: "https://raw.githubusercontent.com/M0HID/prntr/refs/heads/main/design.md"
---
# prntr
Made by: @dari // alexren
Repository link: https://github.com/M0HID/prntr
Total hours so far: 38

- [x] I have a 3D printer or will be getting one before March 21st

I've always wanted a 3D printer that can quickly print parts for prototyping. The Bambu Labs A1m I have right now takes ~7 minutes of calibrating before the print has even begun. Let's try to change that...

## Specs
- Needs to print decently fast (not slow)
- Should be able to print anything an A1 can print
- Should be able to start printing as quickly as possible (for rapid proto)

## Research - Time: 1 hour
- Looked into different motion systems, decided on a cartesian system similar to an ender 3 or an a1.
- [Kappy, a simple 3D printer](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DfQB077PBMZ0&psig=AOvVaw0-DsXJjWiAjD6cZEaGG2r8&ust=1738670582802000&source=images&cd=vfe&opi=89978449&ved=0CBcQjhxqFwoTCKDiuee6p4sDFQAAAAAdAAAAABAE)

## Parts - Time: 4 hours
- Researched different parts on AliExpress for cheapest price, found some decent parts for cheap
- Decided to go for a simple cartesian printer similar to a prusa i3??
- Initial sketch:
- ![image](https://github.com/user-attachments/assets/b0811393-5efd-439d-87b6-c3a57fc865ec)

- Shopping Cart below:


| Item                 | Total  Price    |
|----------------------|-----------------|
| M4 Bolts             |  £        1.01  |
| M4 Bolts             |  £        1.06  |
| Power Socket         |  £        1.16  |
| Steel Rod            |  £        1.34  |
| Limit Switch         |  £        1.43  |
| T-Nuts               |  £        1.46  |
| Steel Dowel          |  £        1.92  |
| Cooling Fan          |  £        2.15  |
| Timing Belt          |  £        2.63  |
| Aluminium Extrusions |  £        3.00  |
| Belt Pulleys         |  £        3.00  |
| Extruder Gear        |  £        3.11  |
| PTFE Tube            |  £        3.35  |
| M8 Bolts             |  £        4.20  |
| Accelerometer Board  |  £        4.44  |
| IR Filament Sensor   |  £        5.05  |
| Stepper Motor Cable  |  £        6.23  |
| Aluminium Extrusions |  £        6.94  |
| Idler Pulley         |  £        9.23  |
| Steel Rod            |  £     10.18    |
| Twin Turbo           |  £     12.35    |
| Linear Bearings      |  £     12.47    |
| Hotbed               |  £     23.27    |
| Stepper Motors       |  £     24.23    |
| Motherboard          |  £     27.23    |
| Power Supply         |  £     29.75    |
| Hotend               |  £     79.91    |
|                      |                 |
| Total                |  £  282.07      |


We are a littleee over budget atm but that should hopefully come down once we research cheaper alternatives/finalise parts.



# Starting CAD

## Initial hotend mount: 2 hours
Ok this is the most difficult step so far... Mainly because i have no idea what to do (and my amazing fusion skills)

Just went straight into it and imported the hotend into fusion and started making a mount. Took some inspiration from e3dv6 hotend mounts online.

Progress:
![image](https://github.com/user-attachments/assets/4fd18eb9-88f5-4aba-be0d-0b909c0debef)

## Hotend fan mount: 1 hour

Today I started work on a mount for the cooling fan for the hotend. Had no idea what to make and spent too long overthinking it :sob:
Learnt that its better to go straight into it and use your imagination rather than keeping all of your ideas in your head.

Progress:
![image](https://github.com/user-attachments/assets/7705d917-33b2-4436-bf3c-cbcdbf8c2eb4)

## Extruder: 3 hours

I spent wayy too long on this. Mainly learning how to do different things in fusion 360 e.g. importing and scaling components. Using a premade extruder and made the mount for it today. Im hoping the screwholes line up because I kinda winged it for this one...

Progress:
![image](https://github.com/user-attachments/assets/638ae73a-a623-49fe-aa5e-f5f60c905dd8)

## Part cooling fan + duct: 12 hours

This is by far the most difficult thing i have had to model so far, mainly due to the rounded shape of the duct. Spent around 2 hours just trying different shapes and here is v1 of the cooling duct: Time += 1 hour

![image](https://github.com/user-attachments/assets/29e03186-944a-46f8-bbf2-0930d4c9e20d)
I will be remaking this shape however because the output of the duct isnt exactly in the correct position and the shape seems a little too big.

Update: I remade the duct shape and now it looks a lot better, i have decreased the output width of the duct and also changed its shape to be more rounded. The output is also tilted so it is aiming more downwards. Time += 2 hours

![image](https://github.com/user-attachments/assets/a2de6761-0b82-495b-b77d-b459020dae20)

Update 2: After many many iterations and failed attempts i have finally come up with this vent design. I also redid the mounting style for the hotend to use a hard mount so that should make things more secure as well. This part cooling ducc has 3 profiles rather than 2 and took me forever just because of me trying different variations and designs. Time += 5 hours

![image](https://github.com/user-attachments/assets/cbc9b7e0-61d1-428a-b9fc-9713ca34061e)

Update 3: Learning how to use offset + combine in fusion 360 to turn the duct body into an actual duct
I tried at first to use the 'shell' feature however that wasnt working well for my use case as it created a wall 'inside' the body, instead of outside... if that makes sense?
Heres my updated ducts now, going to try doing some cfd on this to see if they are any good. Time += 1 hour

![image](https://github.com/user-attachments/assets/af9441ef-02d4-4dc8-91c3-59ec370dd3e9)

Update 4: Redid the ducts yet again, I realised the angle of airflow was meant to be angled downwards instead of perpendicular to the hotend, so it wasnt as effective at cooling down the parts. Created the ducts this time using an angled profile which should hopefully improve part cooling.
Time += 3 hours
![image](https://github.com/user-attachments/assets/a391eb97-ce7c-4554-9f2b-13c2fb518207)

## Continue work on Hotend assembly

### Belt clip
Learnt how to use the rectangle array tool to create a kind of clip for the belt to slide into. Hopefully it wont slip at all otherwise that wouldnt be good...
This should be able to secure the belt securely and tightly otherwise id need to redesign this bit :(
Time += 1 hour
![image](https://github.com/user-attachments/assets/fc4371ed-4eee-4e80-a86d-0cfc94936413)

### Linear bearing mounts
Decided to do something crazy. My idea is that the linear bearing can be embedded into the print by adding a pause and placing it inside the print, and then printing over it. Hopefully i never need to replace the bearings...
Time += 3 hours
![image](https://github.com/user-attachments/assets/d6853de1-b346-454b-8827-a0e29ee071d4)
![image](https://github.com/user-attachments/assets/07d0ae4f-965f-4a02-9251-6104e272d07d)

## Start work on the z axis

Sorry for the delayed update, I forgot to post a log here :sob:
Heres the design so far, im hoping just friction will be enough to hold the linear bearing in place but we will have to see
Time += 5 hours
![image](https://github.com/user-attachments/assets/1e8c6c93-41d5-4e68-ba77-9221426b1749)

### Continue work on the z axis

Spent some time aligning everything and remaking the z axis mount on both sides cos i didnt leave enough room for the belt :(
Time += 2 hours
![image](https://github.com/user-attachments/assets/2a2c1865-7821-4c87-a550-7160cbae7a49)

## Y-axis (hotbed)

Did some research on how different hotbeds mount, how they're levelled etc etc. Going to be buying these parts to mount it on

| Levelling kit                                                                             | Carriage plate                                                                            | Hotbed                                                                                    |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| ![image](https://github.com/user-attachments/assets/03fd8f16-c96f-4637-9792-9f6f133dd0e9) | ![image](https://github.com/user-attachments/assets/db5c9f52-fed7-4cb0-89a2-f29a6852444f) | ![image](https://github.com/user-attachments/assets/b4416ba1-ea9c-4718-aa76-4fef9c7f6355) |


Didn't model this in my cad but there will be linear bearings ziptied to the carriage plate, which will secure it to the rest of the printer. (which is why it looks like its floating rn)

not much else to say here its just long
![image](https://github.com/user-attachments/assets/5fef573b-8354-4bec-ae48-5c809fe43726)

Time += 7 hours

## X-axis (hotend)

Added a motor/idler mount to either side and made cutouts for the belt.
Time += 2 hours
![image](https://github.com/user-attachments/assets/3ed2f983-8d30-4d64-ae53-fedb996509fd)
![image](https://github.com/user-attachments/assets/76d732e8-785f-4f6f-b521-8d951a502f05)

Ok annd with that i think thats all! Ill be doing wire management and all that stuff once i acc get the hardware so uh yeah hopefully it works :pray:
