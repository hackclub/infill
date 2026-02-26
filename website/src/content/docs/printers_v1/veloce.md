---
title: "Veloce"
description: "A powerful, fast, precise CoreXY 3D printer, to get more reliable printing"
project_name: "Veloce"
repository: "https://raw.githubusercontent.com/RR-CREATOR/Veloce/refs/heads/main/DESIGN.md"
---
Made By: @rrop

Repo: https://github.com/RR-CREATOR/Veloce

PS: its still pretty empty, gonna be adding stuf soon

## Printer
Imma be building a core xy supr fast and high quality printr.

## **Day 1**

Research on feasibility, ideas, premade projects, and deciding goals, along with basic planning

Goals: 
- Can print high quality
- Core XY
- Can print pla, petg
- Speed >300 mm/s
- Build volume around 25 cm^3

Read up, watched many videos on how i could start with the design and building

Time: 4 hrs

## **Day 2**

Figured out the basic design pattern i would follow, the various items i would need
Did some feasibility research and figured out if my ideas would work
Decided on a frame and structure, gonna figure out the tech parts of the BOM soon

- Made design sketches, and found build plate and heatbed.
- Also decided to use an aluminium plate bw the bed and pla support.
- Also found rods, screws and decided on nema 17 motors.
- Started with the BOM, although a lot of work is still to be done.

*The plates are 310x310 mm, so thinking of keeping build volume around 300mm^3*

Time: 8 hrs

## **Day 3**

Worked further on my BOM

Figured out a way to prevent pla warping, but still pretty sure gonna print PETG for parts
Also, found hotend and extruder. A BGM clone and a creality clone. Figured out hotend design as well, just the tech parts and psu is left.
Should be able to get around 300mm/s speed. Soon gonna add the BOM.
Honestly, finding parts has been supr painful. Lik srsly why are chinese stores banned in india :(.
Gonna be using a boden setup, as dont really need to print flexible mats.

Time: 5 hrs (lik srsly, it took sooo long to find any good items)

## **Day 4**

Finished my BOM, decided on all the parts I would need, and made some changes to previously selected parts so I can get about 500m/s print speed.
Also made some basic design plans. Goona start cadding soon. This took way too much time.

Time: 7 hrs

## **Day 5**

Decided to use an aluminium frame to get faster speeds, also 300x300 bed could cause wayyy to many issues on first time build, and cant find any close to 250, so gonna do 235x235 bed now,
so changed BOM and re finalized it. Still gonna keep double z as i want to achieve high quality at faster speeds, so going to try to implement closed loop fixing for realtime z correction and print condition adjustment. Hopefully am able to mk smtg that can print high quality at 500+ speeds. Using cartographer with adxl345 so dont need piezo.

Time: 4 hrs

***Total Time: 28 hrs***

## **Day 6**

Alright, now im modelling.

Started by importing the rails, and building a mount around them. This somehow took much more time than it should have.
Imported the hotend and extruder. Played around with their positioning and then realised that the extruder was wayyyyyyyyyyyy too huge, so either buy to direct drive or gonna be using a different one.
Soooo i decided to use a sherpa micro.

https://www.youtube.com/watch?v=Q-7pia9jpuo&t=510s&ab_channel=Kapman%27sBasementWorkshop

found this neat video, and am just gonna get a pancake stepper from ebay and a set of bmg internals, and make one.
So i changed the extruder and figured out its positioning. I designed basic structures to hold them and placed the heeatbreak cooling fan. 
Also created a scuffed angular structure to hold the cooling fans.

PS: Using GrabCAD a lot and printables etc to get models of these parts.

Time: 8 hrs

***Total Time: 36 hrs***

## **Day 7**

Alright, so i made a proper housing and screw structure for the cooling fans.
Also added the fasteners to the project.
SOOOOOOOOOOO, it turns out im stupid.
I spent a huge amt of time making an angular structure mount for the radial fans, so that they blow air somewhat sideways, but that doesnt really matter.
It seems that it doesnt have any advantages and its creating tooo many issues.

So i redesigned part of it, and replaced everything.

Now i had to build vents to direct airflow.

I did some searching and found this video.
https://www.youtube.com/watch?v=1Vs4bE6sE1g&t=1255s&ab_channel=LearnEverythingAboutDesign

it pretty much tells you whatever you should know and partly guids you.
So i spent lik an hour building this.
Now, i wanted to do CFD tests.

I tried searching, but couldn't find anything. Lik 30mins of searching later,
found this vid
https://www.youtube.com/watch?v=1pMJQetyA4A&t=263s&ab_channel=NeedItMakeIt

This once again teaches you how to do sims. I did the test, and apparently my ducts were wayy too squared
The air was not flowing smoothly and had wayy too high pressure.

So i made the vents curved and redid the tests. Now, there wasn't enough air at the back.
So i remade them, and did another simulation, and finally got good results. 

![Screenshot 2025-03-30 162221](https://github.com/user-attachments/assets/b1fbe5a1-ec1f-4fdc-81d1-79dbfc940825)

![Screenshot 2025-03-30 162643](https://github.com/user-attachments/assets/d444339b-d78e-46e8-85bf-ba6cfc1190b5)

![Screenshot 2025-03-30 162719](https://github.com/user-attachments/assets/70e6367a-38b5-4e9a-9cd1-b957ba451a9c)

Time: 10hrs

***Total Time: 46hrs***

## **Day 8**

Klicky time, so somehow found a model online. was glithcing so i made the magnts myself.
Mounted it at the front. 
For that i a thing. I cant cover the top cause fan, and cant do sides cause fan, and cant do back cause adxl345 😢

Somehow figured it out.

Added a 2020 extrusion. Extended it and made it full size and put it behind the rail: yup, x axis majorly done

I added a 3030 extrusion, copied it, moved it and made a frame. Yup, main stuf done.

Time: 4hrs

***Total Time: 50hrs***

## **Day 9**

Alright, XY joint time....

So i have no idea how this gonna work
Imma just look at a lot of cads (ps alex inspiration moments)

Somehow understood how this works. Spent a lot of time figuring out sizes for my desired build volume.
Like a lot of time: was supr confusion.

Started by extending the rail head and adding screws.
Then extended out an attachment and extruded it upwards.

New issue unlocked. Where tf do i attach belts :| the fans took up all the space
SOOOOOOO, i spent a lot of time and decided to extend top part and keep the bottom as is.
And somehow managed to make the xy joint after that, without many issues.

Except the position which took ages. :p


Time: 6hrs

***Total Time: 56hrs***

## **Day 10**

Time to work on the idlers.
Soooo I started by looking at other printr designs, and decided I want to incorporate a tensioner.

I planned out an overall belt path, and placed the gt2 pulleys at the proper places. I then designed around them.
I made a joint which connected to the y extrusions, and left an empty space in middle, for idlers.
Then I made a body which had clearance to move left and right, and passed a screw through it and the idler, to allow it to move with the body.
I also passed a screw through the movable body, to provide a straight line for it to move to prevent the idler from getting misaligned.

So one idler done.
I mirrorred it on the other side, and basically redisgned part of it so it could align with the belt path. THIS WAS PAAAAAAAAIIIN... ;(

Idlers done doh

![image](https://github.com/user-attachments/assets/efb8dc7b-b51d-489a-81d5-83ba132b0abd)



Time: 7hrs

***Total Time: 63hrs***

## **Day 11**

Motor mount time...

So i posititoned the motors and other pulleys to align with the belt path, and once again designed around them

I made a bottom holder for the motor, and screwed it into extrusion. I also screwed motor to attachment to help in vibration distribution.
I made a top layer to allow me to make attach pulley for top belt. This was honestly pretty simple.

I then mirrored this, and changed part of the design to allow everything to align. I moved the motors in the mirrorred one more backward, so there was space for pulley and belt.
I also moved it upwards, as it didn't need the lower height.
This was also done pretty quick (Comparatively)..

PS: Im designing everything on the insie and below so itll be easier to enclose later on.

![image](https://github.com/user-attachments/assets/c64dbf41-49ce-49e6-aa82-525e5f47a0c4)

Time: 5hrs

***Total Time: 68hrs***

## **Day 11**

Z time, So i played around with heights and added rods and screw. I made a bed mount thingy on top of the screws.
I added my planned stuuf to it.
So lik a block representing cork sheet for insluation, springs, then alu sheet for rigidity and temp and heatbed on top of that, and then the buildplate.

Honestly? the main stuf of z took pretty less time. But like fine tuning the heights and positioning took a shit ton. I moved it up and down constantly and moved the x axis to see if it could reach the entire bed, and fine tuned stuff till it could.

I also mounted a webcam to the bed, which is my main idea.........

Im pretty sure the z height is 256 - 265??? not 100% but in this range.

![image](https://github.com/user-attachments/assets/5d6a4d56-6e83-486a-a71c-4567ebf43c4a)


Time: 5hrs

***Total Time: 73hrs***

## **Day 12**

More fine tuning and skirt and electronics

So i added right joints to the frame with screws to estimate fixings and stufff.
Also made little mounting feet and added electronics to try to simulate their actual positioning. Played a bit with y disctance.

SOOOOOO i messed up. I didnt look at z clearances properly, and it turn out the hotend couldnt reach the back of the buildplate. I had to increase the space, and it was soooo painful :(
But everything is fixed now.

I added colors. YIPPEEEE. perfection. hopefully ; p

![image](https://github.com/user-attachments/assets/a008c3a0-c15c-4684-a610-d76752d1696a)

SOOOO this printr satisfied by build volume req, and its main purpose was rapid prototyping with good quality print,
which it should be able to do. I tried to optimize it as much as I could, and im using pretty good motors and balanced stuf so it should be pretty fast.
Im also using webcam for continuosly altering print settings to try to get better quality, using AI/ML.
Hopefully it works ;)

Time: 5hrs

***Total Time: 78hrs***
