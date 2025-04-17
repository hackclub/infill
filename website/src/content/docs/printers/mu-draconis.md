---
title: "Mu Draconis"
description: "A polar 3d printer with modern hardware, but still not the most practical"
project_name: "Mu Draconis"
repository: "https://raw.githubusercontent.com/WilliamPrime/Mu-Draconis/refs/heads/main/design.md"
---
# mu draconis
Made by : William
respository link: https://github.com/WilliamPrime/Mu-Draconis

i have a 3d printer :D




pitch, make a polar 3d printer, not because its practical, but because its something different :D


i would be taking inspiration from this, but making it more functional
https://www.reddit.com/r/3Dprinting/comments/16dsugh/received_a_ton_of_constructive_criticism_on_my/

i want this to look very clean, probably be control only via klipper, no phyiscal controls

im still deciding if i want to have a heated bed or not, or if i want it to be a "fast" polar printer and use a nema 34 on the bed or something like that

the gantry should also be fairly easy to remove for shipping, so xt-60 connectors and other jst things will be needed to make sure that all the cables are easily detachable

also had the idea of having suction cup style things on the base so it sticks down to a table, its just a funny idea

**so far i have some parts ive found and extracted out of dead 3d printers:**
- ras pi 4 8gb
- big tree tech skr mini E3 (the mosfets for heaters and fans are dead, but stepper drivers still work)
- voron klipper expansion board
- hardmount v6 style hotend
- 70w 24v heater cartridge
- 40w 24v heater cartridge

im hopeing i can use them without them counting towards the cost of the BOM

#
# **first two days of planning, around 4hours into it**:
ive decided quite a bit about my printer
i want to use a 250mm round heated bed
i want to use a slip ring so i can get power to the bed and have a heated bed on this printer
i plan to use linear rods and linear bearing for both the x and z
the x will 100% be belted
im still deciding if the z should be belted or use a lead screw
i also started to model out some of the components i plan to use in fusion 360, such as the bed as a starting point
however it appears the technical drawing from the manufacturer REALLY isnt accurate



current rough BOM as of starting

| Part name                      | price         | notes                                                                                            |
|--------------------------------|---------------|--------------------------------------------------------------------------------------------------|
| 250mm dia hotbed               | £13.89        |                                                                                                  |
| ras pi 4 8GB                   | already owned |                                                                                                  |
| semi broken btt skr mini e3    | already owned | dead mosfets, but stepper drivers still good                                                     |
| klipper expansion board        | already owned | to compensate for the dead mosfets on the mainboard                                              |
| nema 17 motor with leadscrew   | £13.49        | 320mm leadscrew might trim down to 200mm                                                         |
| thermal fuse                   | £1.85         | 100c thermal fuse to prevent run away on the bed                                                 |
| nema 23, 76 mm motor for bed   | £18.69        | overkill, will prob change to help budget                                                        |
| slip ring                      | £13.02        | 3 channel, 30A per channel 22mm dia                                                              |
| bicycle bearing                | £1.46         | cheapest way to get a large bearing for bed (41mm id)                                            |
| C14 S8B3 power panel           | £1.36         |                                                                                                  |
| mellow sherpa mini kit         | £30.39        | good, light extruder                                                                             |
| gates 2GT 6mm belt 1m          | £4.79         |                                                                                                  |
| 20t pulley x2                  | £3.30         |                                                                                                  |
| 20t idler x2                   | £3.10         |                                                                                                  |
| LDO-42STH48-2804AH-R           | £26.09        | the goat of stepper motors, could use a cheaper 42STH48 2804AC-R instead for more torque i think |
| Meanwell LRS350                | £23.59        |                                                                                                  |
| pt1000 thermistor              | £4.53         | overkill but i maybe want high temp, no clue                                                     |
| 250mm bed surface+magnet+sheet | £15.39        |                                                                                                  |
| end stops x3                   | £3.20         |                                                                                                  |
| mosfet for bed/heater x2       | £3.28         |                                                                                                  |
| 200mm 8mm dia linear rod x2    | £5.76         |                                                                                                  |
| 330mm 8mm dia linear rod x2    | £6.32         |                                                                                                  |
| Fushi LM8-UU/2pcs              | £9.79         |                                                                                                  |
| Fushi LM8-LUU/2pcs             | £12.29        |                                                                                                  |



## 08/02/2025  (arround 5 total hours)
put another 2 or 3 hours into sketching out how im going to get this to work
finally managed to start getting stuff modelled in fusion 360

<img src="https://cloud-jr0f3cjmn-hack-club-bot.vercel.app/0image.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

the belting seems daunting but i recon its going to be nice

ive struggled to try and model the bed as almost all of the technical drawing on the aliexpress listings are horrible 

## 15/02/2025 (arround 13 total hours)
made alot more progress
ive been modelling the respective components im going to need for my build
ive also started to model the assemblies so i can start combining them

ive decided to start with the bed because i think the bed will be the biggest challenge to make
the bed is probably my biggest challenge because i need to deal with belts to rotate the bed, and also belt tensioning for that, but i also need to deal with getting power to the bed as i would like to have a powered bed, for that i also need to deal with the slip ring
the solution i think i have come up with is 3d printing a custom hollow pulley/sprocket that will attach to the bed, that way the slipring can be on the inside of it and still deliver power

here are some images of the CAD that ive started to hobble together


<img src="https://cdn.hackclubber.dev/slackcdn/2249a46613cd168fe8c47ccac4479448.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://cdn.hackclubber.dev/slackcdn/4487a36952424e21c55a8125484ab075.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
     <img src="https://cdn.hackclubber.dev/slackcdn/87fea6e6c3f6143f4372952cadccecca.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
     <img src="https://cdn.hackclubber.dev/slackcdn/797f056c130ea83b47509f0e03efe3a4.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
     <img src="https://cdn.hack.pet/slackcdn/1a2a60ba4b11c61f53306f0c2183026c.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
     <img src="https://cdn.hack.pet/slackcdn/7bbc1aec7b0fca603a153226776a2e31.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />


## 18/02/2025 (arround 18 total hours)
started working on belt tensioners
     <img src="https://cdn.hackclubber.dev/slackcdn/db28638079230db44cd8334a3dad00f4.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
they were surprisingly tricky to design 
but im hoping maybe if i go all belts then i can reuse the belt tensioners across the printer

<img src="https://cdn.hack.pet/slackcdn/cbf5c1866e8a1887e0b50253c39c2e33.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

it feels quite voron 0 inspired, but that was what i was inspired by :D 

## im honestly not sure what the time frame was,  probably arround 23 hours total time
anytime i was at my computer doing nothing i would try and get a lil bit done
so i didnt really get much big stuff done
but still
stuff changed

## 07/04/2024 (arround 26 hours total probably more)
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/6809a37ab901d0c59df1570e0966768f70669afb_image.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/bd995bc9d460bce7234d485519b325053d14c932_image.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

realised how much easier it would be if i just went the route of desiging some parts seperately then importing them into the main file
i can definetly say
it took me way to long to get that basic belt tensioner working :( 
but oh well

## 07/04/2024 arround 31 hours in
some more jumps got stuck as one of my parts was 0.2 degrees misaligned and that really threw me off
BUT I FOUND THE ALIGN TOOL

i had been using components to make everything work
but i realised how much it helps me to focus when i make things in smaller files where i can and combine them into a bigger file later :D
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/e27147d0ae0ed23eb96c917d1e0006914f1f460e_image.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />


## im doing this while sleep deprived

so im still working on the printer


made some overall progress on tidying up the hierarchy of mess in the component tree
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/2fc1a9c94b623b9eac78f002a31bd8c028b12ec3_image.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/372e3ef31efd20ed396d5c5ea15405b7422d3038_image.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
made alot of work on getting the motor for the x axis actually mounted
i think it maybe gets easier and harder from here
from hearing from other people the tool head might be hard
but i also dread the weird bearing thing i made for the rotation axis



<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/7314904a7d169b0a2d5c07f96fdbfca2011fbb9c_image.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
     

realised that i needed more material there to propperly support everything
2.5mm of  pla didnt really feel enough
also wanted extra thickness there so that i can use heat sets to mount my hot end stuff :D 



## another update
started and "finished" on the hotend
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/37b29bc5192f4756bbafea258dcb289f7c5ff2e3_image.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/a495a2c704a08c9458223e8a892c03d2bdce808b_image.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/f7ba5e60490d17250a35571ab1bb2649b27e8abe_image.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/31273505aa11195a763bba6274ca1df6d5acd30e_image.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
i was anticipating alot more difficulty designing the ducts for the hot end fans than i actually encounter

however i did encounter some difficulty
since my hot end is going on the same side of my carridge as my belts, im encountering issue of how to mount the hot end without sacrificing rigidity, i believe it shouldnt be too hard to just have the hot end on the other side, and then just flip the bed onto the other side of the bottom 2020 extrusion, and that should then fix the issue without needing any extra hardware, right now im trying to get the printer functional so i can refine the cad more and fix some the issues that can be fixed without needing more hardware.

you can also see the fan ducts are aligned with the centre of the nozzle, also not intentional :(
sorry

this ended up being really spaghettic like, im not sure how to use mark down files properly, you can probably tell
updated BOM is here
https://docs.google.com/spreadsheets/d/1IZOwHB4fpJywedBBVYQKaOOAUHnNrE4fSURzN-7t6E4/edit?gid=0#gid=0


## managed to count some bolts 
now at least i know the hardware i need to add to my bom

bed assembly
m3x8    8pcs
m3x12 5pcs
m3 x35   4pcs
m3 x30 6pcs
m3 x30 6pcs , 45 degree angle
m3 nylock nut,   6pcs
m5 t sloct nut , 2pcs
m5x18 , 2pcs
m5x10 , 2pcs
m3 heat sets , 11pcs


frame
m6x20 , 2pcs
m3x12 , 21pcs
m5x8 , 8pcs
m5 t slot nut, 8pcs
m3 x8, 6pcs
m3x20, 8pcs
m4x28, 2pcs
m4 nut, 1pcs
m3 heat set, 3 pcs



# 17/04/2025 big changes and a bit of a write up and summary that is long due

<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/37b29bc5192f4756bbafea258dcb289f7c5ff2e3_image.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

     
spent the last 10 hours working on the 3d printer polishing out all of the missing bolts in the cad
and making a copy of the cad, the removing each body until there was nothing left to get a good BOM that is actually complete and accurate :D

so, going through some of the issues that ive faced and problems as i think that is what i should probably put here, the end result is nice and all but its the challenges we faced along the way and all of the little decisions we make that really define a project

the first issue i really faced in the project was the slip ring for powering the bed
i realised i needed both power for the bed and some sort of bearing that was big enough for the slip ring to go through the bearing
i reallyyy didnt like the look of how expensive beaings costed
so my solution was to 3d print a bearing
i found a couple of videos that served as a good starting ground as to how to make a bearing
i also decided on using a thrust bearing as those have good axial and radial stability which i thought would be usefull
<img src="https://cdn.fluff.pw/slackcdn/8a3f4df7fb7a52623e637efdca4d7c22.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://cdn.hackclubber.dev/slackcdn/553f5c9ee2c64cd7d511de5192805539.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://cdn.fluff.pw/slackcdn/5d0447e687a3665127562cfc6f3593ed.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />





i then stacked two of those on top of each other to try and get a bit more stability
as i  REALLY dont want my bed to be wobbly
that would kill my print quality
so that gets us to about here


<img src="https://cdn.hack.ngo/slackcdn/4d7636f2917300e47599d96ff16be786.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://cdn.hackclubber.dev/slackcdn/65983c089fffe8714f3ef4a00ad519e0.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

my next task was to try and transmit the actual mechanical power that was going to turn the bed
so i want to try and have some sort of "gear ratio" since i dont think i need the max speed of the nema 17 motors that i wanted to use
however to spin the bed it think i need more torque so my solution was for the bed to have a sprocket that has a more teeth, then the motors has a pulley with less teeth

now the issue is trying to get a pulley that has something like 80 teeth 
out of metal that would be big and expensive and i dont know how i would mount it 
so why not 3D print it i thought?
WHY NOT 3D PRINT IT
so i set out on a journey to try and model a pulley with a custom ammount of teeth
then some youtube following later and some thinking 
you get this :D 
(i really dont know why this bit started to feel like a monologue from something, its fine im just tired)


<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/d4e66f1cfb928d36813db7cc3069780253fcada6_gt2_pulley_v20230127_v19_bb.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

now i just need to design a motor mount that has a tensioner aswell because i will need to use a closed belt loop
i have a v0.1 (im proud of this i will say it now and i will probably yap and say it again)
and i was inspired by the way they did it 
so i set along desinging the mounts the way i wanted to 



<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/b602801982ba89e59a38b8189c6f013b6d53573c_image.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

here you can also see my stupidity in full force
i didnt use contraints properly
and as a result 
there is a tiny angle between the two sides of my tensionser
i didnt realise this until ALOT
later in the design

i did think something was off when i designed it
however my normal checks for how square the coners for something are, are
check the opposing sides are equal
then check the diagonals are equal

since the angle was so tiny
the diagonals were so closer that fusion said they were the same :sob :
     
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/795d3f197e265576b7fdaa632c4ab405d09838d8_gt2_pulley_v20230127_v19_bbb.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />



so looking at what i have so far in that assembly it looks something like this
i also added in a pair of bearing to  help the belt contact more of the pulleys teeth at any one time
since the pulley will be 3d printed after all

i also 3d printed a test of the pulley to see if the teeth mesh properly with some spare gt2 belt from my V0.1 (i told you i would mention it again)
sadly ive managed to loose that :sad:


<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/8d8144b9ed315e830718423095f8427d36e04b5f_gt2_pulley_v20230127_v20a.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
     
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/3bccfe6fabf2646c911e2e7b7a6824c4aaf9f47e_aaa.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
i also added on some little sticky out bits to the bearing that i hoped to later use for mounting to the frame of the printer




