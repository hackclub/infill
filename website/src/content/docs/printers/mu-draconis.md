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

current rough BOM

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
