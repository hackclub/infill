---
title: "Grasshopper"
description: "A cheap, fast, CoreXY 3D printer with multicolor capabilities."
project_name: "Grasshopper"
repository: "https://raw.githubusercontent.com/IM-THE-GRASS/Grasshopper/refs/heads/main/journal.md"
---
Made by: @The Grass

Repository link: https://github.com/IM-THE-GRASS/Grasshopper/



Idea: My open-source, DIY 3D printer that aims to be <$300, fast and have multi-color capabilities
(basically a knockoff Bambu Labs printer :P )


Needs:
- Klipper compatibility 
- Multicolor capability
- Speed
- <$300 
- tool changing w 3+ toolheads
- doesn't burn my house down



## BOM: https://github.com/IM-THE-GRASS/Grasshopper/blob/main/V2/BOM.md

> [!NOTE]
> Price & Source is the case for my part individually. Source parts yourself if you plan on building a Grasshopper




<div align="center"><h1>Day 1</h1></div>

<hr>
Today I talked to @darii/alexren and I realized that the the original Grasshopper project had strayed quite far from my original intentions for this project. Instead of a multicolor and user friendly printer, what I made was a rushed & generic corexy machine running Klipper. Because of that, I'll be spending a while to try and completely redesign the project into a toolchanger printer similar to a Prusa XL that's a bit more reasonable in terms of cost.

In the new BOM we're using 3 toolheads that each have HGX LITE extruders and Bambu lab x1c hotends. The hotends may seem like an odd choice, but they surprisingly have a large market of clones on AliExpress with decent performance and dirt-cheap prices compared to some other hotends. heres a detailed list of why i chose each part on these new toolheads:

HGX lite
- super powerful with the big gears
- dirt cheap (fr tho how do they make these so cheap??? theyre all metal!!!)
- all metal (somehow)

Bambu lab hotend
- small so I don have to make my printhead tooo big (unlike my old one ☠)
- oddly good performance
	- according to people on reddit, also an x1c can run at 500mm/s
- dirt cheap
	- it has a huge market for clones on aliexpress, and even the legit ones are kinda crazy cheap
 
5020 blower fan
- apparently the bare minimum according to @evan le (lol)
- not tooo big but probably enough cooling that i can have only 1 fan instead of 1 on both sides like before
  
klicky auto leveling
- this thing is suuuper cheap somehow 
	- ~$5 instead of $60 for a BLtouch?!?
- has good enough performance for me

Now it's time to start making the toolchanger. 


### update 1:

After searching around, I found ankurv2k6's DAKSH V2 project on [Github](https://github.com/ankurv2k6/daksh-toolchanger-v2/tree/main) and it's perfect for the Grasshopper. I'm certainly going to heavily modify his design but the basic connection mechanism will stay the same. For more info [this video](https://www.youtube.com/watch?v=OmmizInw3kI) (from ankurv2k6 himself!) explains the mechanism pretty well.



### update 2:
I managed to position most of the parts including the fans, hotend and extruder. I'm now realizing though that there are some major clearence issues with the extruder and the dock. I'll try and modify the dock a little bit tommorow to rememdy that. I also got a fan duct that I'm not sure will work very well but it's the best I could do. 

<img src=https://hc-cdn.hel1.your-objectstorage.com/s/v3/0907216a2ebc2f3ca47dfa407b0ede9cf5a8cf24_pasted_image_20250402005109.png>

## update 3:
I realized this positioning won't work, because the extruder motor and fan both interfere with where the dock would connect to the printer. Because of that, I flipped the extruder around and cut a hole in back. This design is a lot better because it 
1. clears up some space so we can have a bit more build volume
2. makes it actually feasible to make lol
3. makes the center of gravity a bit closer to the actual center.

<img src=https://hc-cdn.hel1.your-objectstorage.com/s/v3/5077f0535e6fb918c8460ab92b5b20f581463c9e_pasted_image_20250412115956.png>
Along with that, to fix the fan's positioning I moved it to be part of the base of the toolchanger. I also made a basic fan duct using the revolve and loft tools (may or may not work idrk lol)
This is better because
- now we only have to buy one fan, instead of 4 which saves a ton of money 
- the center of gravity is closer to the back 
- also frees up a bit of space for more build volume

<img src=https://hc-cdn.hel1.your-objectstorage.com/s/v3/8e68ab58c3b5e327442473bf643656b181d24be0_pasted_image_20250412120149.png>
also i fixed the position of the klicky :P

## update 4

<img src=https://hc-cdn.hel1.your-objectstorage.com/s/v3/92d17536dd27f5011e55d92f4404c59e6696d21b_pasted_image_20250412120508.png>
I positioned the hotend and the cooling fan. The position is actually completely diffrent from what I chose before because I needed to make it line up with the extruder (lol) 

I also made some minor changes to the dock by moving some parts around like some of the magnets and stuff, but they weren't really noticeable enough for me to take a photo.




<div align="center"><h1>Day 2</h1></div>
Today I planned to start working a bit on the frame. I would mostly be stealing parts from the Grasshopper v1 but making it a lot longer so I would have space for the toolchanger in the back. 
I also decided to try and use some metal connectors from aliexpress instead of the 3d printed ones i made mostly because they were 1. a lot stronger and 2. took less time ( i didnt have to design them :P )


## update 1
I used mainly the same peices for this, but i also added a couple 2020 extrusions that I didnt have before because in my past design 2/4 of the extrusions on the top were 3d printed which was certainly not very good for the structural rigidity

The PSU was also positioned kinda odd but that's because the gap will be filled by a box to hold some electronics.

<img src=https://hc-cdn.hel1.your-objectstorage.com/s/v3/2628bb02bc8877ee750cb1785c8a674897bf9a7a_pasted_image_20250412134507.png>


## update 2
Next I added the X axis and the toolhead. The part that connects the linear rails on the y axis and the 2020 extrusion for the X axis is a pretty basic 3d printed part. I'm not quite sure it'll hold up in the end but if it doesn't I'll just redesign it in the future.

<img src=https://hc-cdn.hel1.your-objectstorage.com/s/v3/6f1611befbcf7ce6ba1bd64612548bd46347f0b8_pasted_image_20250412141939.png>


Heres how it looks w/ the toolchanger: (there isn't going to be 4 in the end prolly its just gonna be 3)

<img src=https://hc-cdn.hel1.your-objectstorage.com/s/v3/38f4a59c4bb0bb549c7b071269d7efc79f67e7b6_pasted_image_20250412142056.png>


## update 3
After doing the x and y axis, I made this triple lead screw z axis.
in the OG grasshopper I used only 1 and 2 linear rods, but after talking a bit online I realized that would cause a lot of issues with the z axis locking up. Also, I had some extra motors and ports either way so it wouldnt take much out of my budget

<img src=https://hc-cdn.hel1.your-objectstorage.com/s/v3/e67ad0fea0ab7b7aa8353be60891e90b577b6ccc_pasted_image_20250412143243.png>



## update 4
At this point I was basically done the printer's CAD so i just tried to add some finishing touches.
I added a screen holder for a random car display i had in my garage and a couple boxes to hold the elexctronics. 

<img src=https://hc-cdn.hel1.your-objectstorage.com/s/v3/a9e4b5b588f8c5bea3a94fee58b5d4a5f50b41a6_pasted_image_20250412144345.png>

Other than that, I also added a small camera in the corner. The camera is a composite one that runs on 12v that i stole from my garage jus like the screen :P

<img src=https://hc-cdn.hel1.your-objectstorage.com/s/v3/c271211791758cb3f25ba66a821f273bb89a53db_pasted_image_20250412144535.png>





<div align="center"><h1>Day 3</h1></div>
Today I basically just did the belts on the top and the overall motion system. In the past it really wasn't that good because I was really confused about how a corexy belt path worked, but now I think I got it a bit more nailed down.


### update 1
I made this kinda belt path but idrk if it will work too well
the idlers are just kinda screwed into the extruison and I'm afraid the screws holding them in might bend. If they do then I'll prolly change them up a lot but rn I have a math test and I want to ship this printer 😭

<img src=https://hc-cdn.hel1.your-objectstorage.com/s/v3/49285c0e45f7e32027b6f85ed6823e348486b1c2_pasted_image_20250413143211.png>


