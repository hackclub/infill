---
title: "Anicept Vex"
description: "A powerful, fast, precise CoreXY 3D printer aimed at intense speed"
project_name: "Anicept Vex"
repository: "https://raw.githubusercontent.com/invictus-anic3tus/anicept-vex/refs/heads/main/journal.md"
---
## firstly,

This 3D printer has been made possible by Hack Club and the awesome Alex Ren. Let's give them a hand! 👏👏👏

Made by: @anicetus  
Repository link: https://github.com/invictus-anic3tus/anicept-vex  
Total hours so far: 102
 - ✅ I have a 3D printer

### about the anicept vex

I'm Anicetus, and I'm making a CoreXY because my Anycubic Kobra 2 Neo doesn't print over 250mm/s and can't print hotter than PETG. This will change all of that.

🕐 Speed: 400mm/s  
📐 Build size: 230mm x 230mm x 260mm  
👍 Materials I want to print with: anything up to 300°C! Mainly pla, petg, and tpu

You may be wondering where I got the name "Anicept Vex." It seems rather strange.  
First of all, the first word is a play on my name, Anicetus (which means unconquerable in Latin). It's basically just compressed to three syllables. "Cept" comes from concept, invoking thought and power. It's also super cool sounding.
The second word, "vex," is English (and Latin!!) for making somebody annoyed or frustrated, as you probably know.  
It gives off a vibe of hot, fast anger, speedy and deliberate. Another Latin translation for it is to rouse or to excite, again invoking heat and agility. It is also a shortening of "vexare," the Latin word meaning agitation or shaking.  

Again, a short, fiery, awesome name.


OK, good. Down to business.

## day 1 - feb 2 '25
Today I'm researching some parts!! Good stuff. I think ima use the Phaetus Rapido ACE hotend and BTT SKR E3 mainboard. Other than that, I have no idea.

The Rapido ACE HF is built for ~45mm<sup>3</sup>/s printing, which is really really fast and happy. I may upgrade to the UHF if I'm underbudget and want to go 75mm<sup>3</sup>/s.

I'm going with Nema 17 stepper motors, the most popular for CoreXY.

So far, we're at 125 USD. 😬

Next, I looked for extruders. I went with the Orbiter v1.5, since it's smaller and has a lot of support. For PSU, I went a generic 24v 600W.

I started CAD-ing, and got only the hotend and extruder in their places :P

Research and parts: 3 hrs  
CAD: 30 minutes

## day 2 - feb 3
I started today off by doing some research! Some Slack members told me that the Orbiter v1.5 wasn't going to cope with the high-flow Rapido Ace, so I decided to look for a new power pair.

I asked ChatGPT about some stuff, and it pointed me eventually to the Orbiter v2.0 and the Phaetus Dragonfly BMS, getting closer to 450mm/s which is pretty nice! The Dragonfly can also get to around 300°C, which is perfect for PETG and some hotter filaments.

Next, I remembered something kind of big: Klipper host. In my opinion, Klipper is way better than Marlin at a lot of things, and it was a must in my design. I overlooked the hosting, however.
I thought, "Well I can use the Raspberry Pi 3B from my other printer, right?" While that could be a viable option, ChatGPT (coming in clutch yet again) showed me instead the BigTreeTech Manta M4P + CB1, which is a mainboard that has a Klipper host integrated with the mainboard! If I'm under budget by the end of this thing (unlikely,) I'll upgrade the the M8P, which has more capabilities for extra motors and stuff.
I looked for some linear rods and got a good idea of pricing, although I haven't CAD-ed anything since deciding to use the Orbiter v2.0 and Dragonfly. I added a BLTouch to my cart, bringing the total so far to... $240 😭  

Yes, that's nearly the budget right there, without any extrusions or cables or anything. I think I can fit the extrusions and such in the $60, but it may be tight. We'll have to see!

(Later) OK I did some MORE research and decided to go back to the BigTreeTech SKR E3 Mainboard and host both off my one Rpi. If it goes bad, I'll buy a Rpi Zero W.  
I figured out some stuff with part cooling and whatnot, readjusted the CAD, got the printhead semi-set up, and more! Well that's it for today.

Research and parts: 4.5 hrs  
CAD: 1.5 hrs

## day 3 - feb 4
Today was mainly a research day (again.) This is me the following morning because I forgot to update 😁

Anyways, I did a lot of research on the best motors for my setup and found a really good deal for 3 for about $25, and they're strong enough to let me go around 430mm/s straight. If you want the link DM me or check the BOM spreadsheet above  

Then I started CAD-ing, and I've got nearly the entire printhead set up! I think I'm going to use a CFD to simulate the fan airflow just to make sure it works, but other than that I need to add the BLTouch, some PETG framing, and I'll be essentially done there. Also, cable management 😬

![printhead](https://cloud-eaq9rc33e-hack-club-bot.vercel.app/0image.png)

Research + parts: 4 hrs  
CAD: 2 hrs

## day 4 - feb 5
Today I worked on the BOM a bit and researched where I might find cheaper parts. I think I over-calculated how expensive the frame will be (hopefully) so maybe I'll get out of debt? Worst case I spend 30 bucks out of my pocket.  

I have plenty of doubloons from High Seas, but DigiKey and the rest don't seem to have great parts. Surprisingly, DigiKey has absolutely no 3D printer mainboards, and the stepper motors they have aint worth squat. The rest of the time was basically just CAD, with a side-tangent to try an airflow simulator. I decided not to, though, because I was lazy. I worked on the fans, connected it to the linear rail, and made my logos!

Research and parts: 2 hrs  
CAD: 3 hrs

![vex logo](https://cloud-3vcb9x7yd-hack-club-bot.vercel.app/0vex-logo.png)

## day 5 - feb 6
Today I didn't do a whole lot because of schoolwork and other projects. I CAD-ed a little and that's basically it.

CAD: 1.5 hrs

## day 6 - feb 7
Today I had a stroke of genius *ok maybe just a stroke* and I decided to make the Vex a dedicated **upside-down** CoreXY! It's mainly for print farms and stuff because when the bed cools, the printhead just gives it a little nudge and the print falls right off! Also it just looks cool.

I'll probably make it reversable so you can print like a normal person if you want, with feet that can be put on either side and a removable Klipper host/screen. This does mean using linear rods instead of rails, though, so it may get more expensive? Idk.

Anyways, I'm still deciding on whether to have the motors upside down as well as the printhead, because if they're right side up (from your view), they're sitting on the desk/ground, but the carriage is reversed. This means that the model is effectively flipped X and Y (rotated 180 degrees) which may be an issue? I don't know. Probably not, right? RIGHT??

Either way linear rods are a good thing to do so that's what I'm doing.

(LATER) I did a lot of research and apparently upside down corexys are a really bad idea. Welp. It's OK, I'll do normal CoreXY and use linear rails still because they're also apparently good for speed and such. I did a tiny bit of CAD

Research: 2 hrs  
CAD: 30 min

## day 7 - feb 9
Yesterday I had an all-day D Now (Disciple Now) with my church which was very very fun!! No work though. Today was mostly research and some CAD, as I'm working on #printboard a lot now. Trying to get it done 😭

Research: 30 min  
CAD: 30 min

## day 8 - feb 10
Printboard!!!!!!!!!!!!!!! Some CAD for this though...

My current printhead setup:
![printhead](https://cdn.hack.pet/U07GPJ6V3UZ/printhead.png)

CAD: 1 hr

## day 9 - feb 12
Again, I haven't been doing a whole lot of this due to printboard, but I was able to get the linear rail mounting and a little bit of the hotend screw mounting figured out. Some pics:


![printhead picture](https://cdn.hackclubber.dev/slackcdn/0f6654d1a2b6a3a793b17d9be6afb554.png)
![mounting picture](https://cdn.hackclubber.dev/slackcdn/a26d3902d9a992ea64293aed2e87f950.png)

CAD: 2.5 hrs

## day 10 - feb 13
Today I researched a whole bunch of parts, from Gates belts to idlers, linear rods, and more! You can see my BOM [here!](https://docs.google.com/spreadsheets/d/1GO_HGXTeiZWquWsCZzynmvAluWZnmblAnS994K72vQ0/edit?usp=sharing)

I also did a little CAD today, importing some models for the bed, aluminum extrusions, and such. I fixed some model symmetry issues and increased the tolerance between the parts and the hotend. I've yet to run any CFD (computational flow dynamics) tests, but I may just get all the parts and see how the airflow works in real life instead.

Research: 2.5 hrs  
CAD: 1 hr

## day 11 - feb 14
Happy Valentines Day! Homeschooling doesn't usually provide Valentines though. On the bright side, I got lots of candy!!

Anyways, today was a big CAD day. I did research some mechanics, like the z-screws, bearings, idlers, and whatnot, but mostly just fixed CAD part tolerances and adjusted some of the models to make them more symmetric and nice looking. I've yet to add the BLTouch and Gates belt connecters though... maybe on day 12!!

Research: 2 hrs
CAD: 2 hrs

## day 12 - feb 15
Today I only researched stuff, as my hotend turns out <i>isn't</i> high-flow like ChatGPT said it was, and I needed to find a new one asap. Also researched frame parts and some kinematics!

Research: 3 hrs

## day 13 - feb 17
After finallllly getting my printboard submission in yesterday, today I can work fully on CAD and research. All I have left to do on the printhead is the BLTouch, belts, and accelerometer! I finished adjusting for the new hotend, the TZ E3 2.0, which doesn't get the 45mm<sup>3</sup>/s that I hoped for in the beginning, but gets 33mm<sup>3</sup>/s (according to the seller.)

I'm expecting probably 30mm<sup>3</sup>/s out of it, which is plenty for what I want.

CAD: 2.5 hrs

## day 14 - feb 18
Ouch. Turns out the hotend _doesn't_ fit all the way yet... well I guess I know what I have to do 😭

Other than that, I started the BLTouch mount and did some research on how to mount the belts and accelerometer :/

Research: 1 hr
CAD: 2 hrs

## day 14 - feb 19
I finally got the hotend to fit! I also mounted the BLTouch and the accelerometer. I started a bit on the belts, but wasn't able to get them done quite yet. [Here's](https://cdn.hackclubber.dev/slackcdn/afa3ab80102c1eb30fef80da450fb23d.mp4) a video of what my printhead looks like so far!

I also did more to improve tolerances and printablility. I decided to wire the accelerometer through a little printhead tunnel, which is 1) cute and 2) saves space :3

CAD: 2.5 hrs

## days 15 + 16 - feb 20 + 21
WOOOOOOOOOOOOOOOOOOOO  
I got the printhead done :D

I do still have to do the belts, but I'm saving that for when I get my gantry figured out. I also did a bunch of the frame! Pic (20th):

![frame with printhead](https://cdn.hackclubber.dev/slackcdn/404ca1ab919aa36960e3d61a59125e0a.png)

This thing is really coming together!!!

All I have left to do with the z-axis is add the linear rods and attach them to the bed. The gantry is looking quite daunting, but I guess I'll cross that bridge when I get to it. So far, the build size is 230x230x280mm, which is way bigger than my current printer (220x220x250mm)! Good deal.

CAD: 7 hrs

## z-axis and electronics days

### days 17 - 20 - feb 22 - 24
These days I got finally got the Z-axis done! Connected the linear rods to the bed, the lead screw to the bed, all sorts of good stuffs.

CAD: 10 hrs

### day 21 - 23 - feb 25 - 27
Got most of the electronics done!!
Mounted PSU and mainboard, added a fuse and a power cable thingy!

CAD: 7.5 hrs

### days 24 - 29 - feb 28 - march 6
I know my updates are getting less frequent, but there's really not a lot to update _on_. I did get all the electronics finished, as well as adding an integrated two-port power strip for the rpi and the filament dryer. I also got an idea of how the gantry will work and fixed some Z-axis stuffs.

CAD: 15 hrs

## days 24 - 34 - feb 28 - mar 16
wow... I'm being very bad about updating. I'm so sorry! Tomorrow I'll post a butt ton of pictures that will mark my progress. _my screenshots folder is getting kinda big..._

but over these days, I've all but finished the printer. I finalized the z-axis and attached the x-aluminum extrusion to the y-gantry. I've mounted the gantry on top of the aluminum extrusions to save space and mounted most of the idlers.

So far, here's what I have left:
1) Finish mounting the idlers that attach to the y-linear rods
2) Mount the motors
3) Create belt models
4) Mount the belts to the printhead
5) Redo some text on the underside of the plate holder
6) Research M5 screws and assorted inserts
7) See what lengths of screws to get
8) Buy parts!
And then design will be done!
Not so hard.... right?

oh yeah, and funny thing this printer was originally called the anixus vex! I like the current name better, and decided the new one on March 16th. If you go thru this repo's commits you can see the previous name ;)

CAD: 15 hrs, research 5 hrs

## pictures!! my timeline of printer 🥲

Ahh... simple beginnings. Here's when I was using the Rapido Phaetus ace hf 2 hotend with the orbiter v1.5 extruder:
![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/1606de4940ed5a146b976a6f102ae7194444790e_screenshot_2025-02-02_182817.png)
</br>
</br>
</br>

The earliest full revision of my printhead!
![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/ef1a7a00ad13aab12d308e6f1773b24e09f19e29_screenshot_2025-02-04_170418.png)
</br>
</br>
</br>

Created two logos (one for the earlier name of Anixus and one for the Vex,) reoriented the linear rail, finalized the front panel, and made the top panel!

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/0f1b0b42727a257a6e56509bf5444474f4f7a0b3_screenshot_2025-02-11_174838.png)
</br>
</br>
</br>

COLOR!!!!!!!!!!!!!

![COLOR!!!!!!!!!!!!](https://hc-cdn.hel1.your-objectstorage.com/s/v3/de7697b2c68818bd0c6183cb052fc8570c410a30_screenshot_2025-02-12_170300.png)
</br>
</br>
</br>

Aha the backing

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/6346dc79eab17be685cdb2af4f4d06587416aa69_screenshot_2025-02-12_171053.png)
</br>
</br>
</br>

mounted the ADXL and 3DTouch!

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/790ab72b294016c9dc86bdb197f13a021c3a5e13_screenshot_2025-02-19_164007.png)
</br>
</br>
</br>

wow! started on the frame! looks kinda ugly and fat :b

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/461de71477c5a21b166ecbc61b7e7d2fb9457e42_screenshot_2025-02-20_172430.png)
</br>
</br>
</br>

looking better! got the z-axis motor and gantry in place

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/f98c083ec2269ffe7c159d353498b47956183ed7_screenshot_2025-02-22_143522.png)
</br>
</br>
</br>

placed and mounted the PSU, z-motor, linear rods, and the mainboard!!!

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/3873b448ed1191135501498cff11c9419b0063c8_screenshot_2025-02-26_161859.png)
</br>
</br>
</br>

Ah... the power panel PCB. Didn't turn out to work, but I learnred some about buck converters!

![sad](https://hc-cdn.hel1.your-objectstorage.com/s/v3/0197595bc2aaa76708569f23b57206c1f7462d31_screenshot_2025-03-03_174815.png)
</br>
</br>
</br>

Wh-what's this?? A power strip built into a 3d printer?? Amazing!

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/a5bc39fa00f8e61820d3f5a61bb8d1b831fb7147_screenshot_2025-03-06_154357.png)
</br>
</br>
</br>

3DTouch didn't work 😭  
Turns out those Chinese clones aren't worth it... I went Klicky!!!!!!!!!!!!!!!

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/a38616c23ed12e614ae79b3dfcfa3dcd49cccad5_screenshot_2025-03-09_170147.png)
</br>
</br>
</br>

Mounted the linear rails and connected the x-axis to the y! Also started them idlers :3

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/d82f3d5e6bc73728c7ef85bf4986da288f6e3a91_screenshot_2025-03-11_155645.png)
</br>
</br>
</br>
"What questionable design considerations?" -Anicetus, 20xx - 2025

![💀](https://hc-cdn.hel1.your-objectstorage.com/s/v3/38b1981f7d686146327da0ac0ee80e31f80e0576_screenshot_2025-03-12_155632.png)
</br>
</br>
</br>

✨Mystical Castle Idler!✨

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/bb8dd330cba161304122183a95105661d2ef0f3e_screenshot_2025-03-12_165403.png)
</br>
</br>
</br>

So many different logos! (I went the all-bold one :D)

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/02842b59596d9e134741baa2837ebf098a9f941b_screenshot_2025-03-17_145359.png)
</br>
</br>
</br>

Wow! Beautiful render

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/6965fd7ac766bb53ed822808b5c1b88a1dec5f4e_screenshot_2025-03-18_155136.png)
</br>
</br>
</br>

That's quite a bridge to gap,,,

![uhoh](https://hc-cdn.hel1.your-objectstorage.com/s/v3/426656da9cbad3609a97db1f1353591fadfdea3a_screenshot_2025-03-19_154424.png)
