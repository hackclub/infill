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
total hours so far: arround 60



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


# 17/04/2025 BIG changes and a bit of a write up and summary that is long due arround 



     
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

https://hc-cdn.hel1.your-objectstorage.com/s/v3/0fb4699f730b00b6d34ee98721cad8a2cb5b5bb7_aaaa.png
<img src=""
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

i will come back to the custom 3d printed bearings again later and how they should be assembled because i think thats probably a good idea


my next step was to start desinging a frame 

<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/a4281b408b863e5e372d6c7b032734ca29c093a2_frame_1.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/7156bb5a7499150568c56d813a0a457d4c8d5f1e_its_a_simple_frame.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

and then after that some feet so it doesnt fall over
the timeline is a bit messy here
but i think it would be better to have them here with the frame, it just makes sense that way

the design of the legs are pretty simple
just doing it by eye so the printer is stable enough
im going to have the powersupply at the bottom later , and the priter should be pretty stable as any wobling would be parralel to the bottom extrusion 

the feet are also two part to make them easier to print
then using a heat set and a screw  to join them together 


<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/3f51bcdc3bb8617c94d9e346289e3074da05f885_legs_close_up.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/676064ef896a37624a84b696d0332c8d6b32bbfb_just_legs.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/190d31337b33a842dba1131238115d85ee2a0b56_feet.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

chronologically, i had started to work on getting the bed mounted 
however i wasnt sure exactly where the hotend was supposed to end up
so it ended up being a bit overwealming and that lead to me getting lost quite a few times while trying to go that route
so instead i started work on the Z axis
with hopes of then working on the X axis, 
and then the hottend so i could actually see where my nozzle was going to end up

my first step towards a Z acis was getting something to hold to linear rods
and for that i designed this little thing that could be used for the top and the bottom of each rod
nicely securing them to the extrusion :D


<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/632528b3460264b9e73d4814cb13a0eb14fa55e7_single_rod_holder.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

and then adding in the rods,

<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/54cbfa8752e390414a62922718f1d3906033979e_printer_prototype_1_v53.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

then got a nice little carridge going :D

<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/ed000ce97eaec9d004aa89687c4825e24e2b2603_frame___z.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

and realised i needed a way to get the belts to actually be gripped onto
my soltion, just weird grippy thing :D with teeth or the blet profile, whatever you want to call it


<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/e4a08658c974a6a0c9ae8223eab1de8035b36890_belt_gripper.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

then with another chunk of messing arround i got the belt modeled in with all the teeth,
i dont exactly know wher i deceided to modeling in the teeth, i didnt do it for any of the other belts, so now it just looks a bit odd

BUT YEAH
i got the belts modelled in
and then i also got a nice little motor bracket modelled in with a motor and pulley i got from grabcad
very nice so far


<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/41ab42b438bd0783c88b2e29603b431f1ca96f5c_motor_mount_png.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

thats the Z axis done

good time to also mention
breaking the chronological timeline here
but i designing a belt tensionser while making the x axis
with the idea being to use it wherever i need to tension belts so that was also used here
to avoid the overwhelming mess of what the fusion file was at this point, i designed the idler in a different files and then imported it into the main file


<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/f72c2692a40c57fca44bc38c3196042ccb8f295c_tensioner.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

you do have to love the way i designed the bracket that holds the tensioner 
it's HORRIBLE
BUT IT WORKS
you just need to tension the z before you mount the belt idler

<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/d74014b47b385b4378cc463bb2d0db2258731c1a_horrible_z_axis_mount.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
so actually the Z axis looks like this


<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/4482abbf5940694846faa8c2ebf4c437de6e3e59_another_z_axis_photo.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

first thing i did was quickly throw together a plate to finish attaching the X axis rods to the Z axis







<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/550000d71b361c0edc9900587851f0d097d1cc73_step_1_x.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/157699d0951cc8afec68cd665f17ce208045a7e3_x_axis_2.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/729722f46ca12e9bdc219234baadc3bd395e54eb_x_axis_3_another_use_of_that_idlet_thing.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/a977c225d8bf1812b08dfec78daaf00c7d7fd3b3_another_one_of_those_grippy_plates_for_x_axis_4.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/8133603e89dd5bdcb5fc5bc1f0212e8fb43daee6_nice_chunky_x_motor_bracket_5.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/6cc750f8558057b66d48fdee3e098ecc48d77a9c_x_6_what_we_have_so_far.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />


then that gets us onto the next bit
the hotend, the fun fancy probably most expensive part of this whole thing
i decided to save a good chunk of the budget, i was going to use the dragon HF hotend, with the mellow NF crazy volcano heatblock for this printer
and i would take it off of my voron 0.1 (WOOO THE VORON V0.1 MENTIONED AGAIN), and use the stock hotend that came with the voron on the voron
meaning this printer gets quite a nice hotend :D
i also wanted to use a sherpa mini extruder as i have found them to just be a nice extruder that is relaiable, and can handle pretty much whatever material you can throw at it
ive printed TPU with it so its pretty nice :D
 here is a little render of the hotend




<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/2921c9a01d15f689d849ce04473063b6ab6bb767_hotend_pretttyyy.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/1aaa8ab847f2dd543859224de700ef470266aa14_midplate_hotend.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/4c2d9f76f1b20ebcc7c516300e15e9bc12377007_hotend_midplate_and_sherpa.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />



fan mount for this was super simple
i do love the simplicity of it :D

<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/43d0647659dfa3759a56e4342b59883b2aed7eb7_cheeky_lil_fan_mount.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

add in some ducts


<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/71a95cbfc4675e34f97d032da97a18cd14388a46_and_thats_a_hotend.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/f8018bf92a7501edb24200e65ad7e923c1c5298a_frame___x___y.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />


this is probably the least gracefull, and most confusing part of the entire printer
the bed
my first step was to create something to mount the two bearings to the frame
its not gracefull
but here is the little mount i designed
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/dd60cff176a750daa79ba3b6e0b2c5565fe2dd1d_render_of_the_attachment_for_those_bearings.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
the next step was actually joining the two bearing and the pulley together to get it all working as one nice big peice
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/0c2640f1cf173a07840c3e34afbafabdd15197ea_start_of_bed.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

i also realised that i need something to stop the stationary part of the slipring from just spinning
since there wount be much force on it AT ALL , i could make it really quickly and not worry about strength, which gives us this little cute thing
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/81b3960a68aa22956eac1bd4a5e2d13fddd03047_anti_twisty_thing.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

then for the electonics
i threw together a little mount for the skr mini
and the ras pi i have allready has a heatsync and i dont really want to take it out of that
so im just doulble sided taping it to the frame :D
then the mount for the skr mini will also be getting the double sided tape treatment 
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/4e4ee00423cb85bf02bf9c283e6c288953738706_skr_mini.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/17e6f1f24cc8f0bf7bed7d8d3304cec9ca37b2e6_doulbe_sided_tape_ras_pi_mount.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

i also had a nice little solution for how to mount the c14 inlet
i first designed a thing to hold the c14 inlet
and then just joined it to the same leg that has the pi and skr mini
just on the other side

<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/ad1740a3e4afd5808a67f2b0a24d178b71fa66f2_other_side_of_c14.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/5395992a6c0613aa9078ed1ef33dde49fb2004c6_c14_mount_thing.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />



but i wasnt quite sure where to put the psu 
since the vertical extrusion has stuff all over it
i cant mount it to that
the horizontal extrusion has stuff
and then it just seemed really hard to find anywhere that it could actually mount to
but i found a nice little place to nestle it
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/9938794e1a9b2ebbfad29169aea849332a75ee2b_where_psu_2.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/98382c8bee9e9d3b8d621843d633d4c9d14209e4_where_psu.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

the soluation i managed to come up with     
was to raise the "feet" of the printer a little bit i think arround 4mm
and then it fits VERY snugly under the z motor with that extra clearance
and its right next to the foot under the vertical extrusion which gives me something nice for it to mount to

here you can see ive raised the feet to fit it, and then the holes that will let me mount the PSU
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/c2ad02e4ba71402850c94e94b8a03999de563317_raising_the_feet_so_it_fits.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
and then with the psu it looks like thise
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/00554409dadbf4d4a6942ec921cdd0b22423cbb3_mounted_psu.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

however the screw terminals looked a bit exposed

<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/0c0d71f225338157ca6ec41493fe225d3277082b_unsafe_psu_smoller_file.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
     
and i REALLYY dont want to accidentally touch live 240v ac 
thats not how i want to go out
so i designed a nice little cover for the screw terminals to prevent me accidentally zapping myself 

<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/688367c394d2c4927cdece1cd4788c7c28199e39_safer_psu_even_smaller_file.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />




now that we are on electronics i should probably make an electronics diagram for this
but im not sure if it needs one

so i will just write it out

240v comes in through the C14 inlet
That then goes to the PSU so i have 24v for the rest of the printer

that 24v will need to power the:
2 heater relays,
SKR MINI E3 V3, and
kliiper expansion board

the motors all attach to the SKR mini
the endstops all attach to the SKR mini
thermistors attach to SKR mini

however because of the me having an SKR mini that has a dead multiplexer, meaning that none of the mosfets work
i need to use a klipper expansion board to get mosfets to controll my fans and heaters
my fans will connect directly to the klipper expansion board
the bed and hotend however draw alot more power
the bed could draw 150w
and the hotend 80w
im not confident the klipper expansion board can handle that much current , arround 3-6A
so im using a little external mosfet board to power the bed and hotend
the boards get power from the PSU
but they get the signal from the klipper expansion board mosftets





random bits for the end
almost forgot to make endstops
so i came up with this cute little thing that fits on the the 8mm linear rods, as shown here :D




<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/91c783fab330cab99d186919589173521b7cd190_endstop_on_its_own.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/97e0418ba3bd944ecc93f7dc82496af1b2232157_end_stop.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/5f18c54eebadf9dd56dc3ebeae7205ff896d0ef6_use_of_enstop_again.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />

so that gets us to this nice render of the printer in what is currently its finished form :D
















<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/6241c7993d7a243c48dfeaf707213b25041c25ed_wow_thats_close.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />




<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/0edb0c29515d91259e80ba64416a0e4c7e0aaf2e_printterrr.png"
     alt="image of printer"
     style="float: left; margin-right: 10px;" />


i have got some things i do want to improve, but those involve change the 3d printed parts not any of the hardware
the list of stuff i want to make less bad are:

make the hotend mount more secure

better fan duct design

fix the 0.0027 degree angle on the sides of the bed belt tensioner thing
