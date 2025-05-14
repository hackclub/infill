---
title: "Anicept Vex"
description: "A powerful, fast, precise CoreXY 3D printer aimed at intense speed"
project_name: "Anicept Vex"
repository: "https://raw.githubusercontent.com/invictus-anic3tus/anicept-vex/refs/heads/main/journal.md"
---
## firstly,

This 3D printer has been made possible by Hack Club, Alex Ren, and the awesome Polymaker Joel. Let's give them a hand! 👏👏👏

Made by: @anicetus  
Repository link: https://github.com/invictus-anic3tus/anicept-vex  
Total hours so far: 165
 - ✅ I have a 3D printer

### about the anicept vex

I'm Anicetus, and I'm making a CoreXY because my Anycubic Kobra 2 Neo doesn't print over 250mm/s and can't print hotter than PETG. This will change all of that.

🕐 Speed: 350mm/s  
📐 Build size: 230mm x 230mm x 260mm  
👍 Materials I want to print with: anything up to 300°C! Mainly pla, petg, and tpu

You may be wondering where I got the name "Anicept Vex." It seems rather strange.  
First of all, the first word is a play on my name, Anicetus (which means unconquerable in Latin). It's basically just compressed to three syllables. "Cept" comes from concept, invoking thought and power. It's also super cool sounding.
The second word, "vex," is English (and Latin!!) for making somebody annoyed or frustrated, as you probably know.  
It gives off a vibe of hot, fast anger, speedy and deliberate. Another Latin translation for it is to rouse or to excite, again invoking heat and agility. It is also a shortening of "vexare," the Latin word meaning agitation or shaking.  

Again, a short, fiery, awesome name.


OK, good. Down to business.

## researching and printhead CAD
### day 1 - feb 2 '25
Today I'm researching some parts!! Good stuff. I think ima use the Phaetus Rapido ACE hotend and BTT SKR E3 mainboard. Other than that, I have no idea.

The Rapido ACE HF is built for ~45mm<sup>3</sup>/s printing, which is really really fast and happy. I may upgrade to the UHF if I'm underbudget and want to go 75mm<sup>3</sup>/s.

I'm going with Nema 17 stepper motors, the most popular for CoreXY.

So far, we're at 125 USD. 😬

Next, I looked for extruders. I went with the Orbiter v1.5, since it's smaller and has a lot of support. For PSU, I went a generic 24v 600W.

I started CAD-ing, and got only the hotend and extruder in their places :P

Research and parts: 3 hrs  
CAD: 30 minutes

### day 2 - feb 3
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

### day 3 - feb 4
Today was mainly a research day (again.) This is me the following morning because I forgot to update 😁

Anyways, I did a lot of research on the best motors for my setup and found a really good deal for 3 for about $25, and they're strong enough to let me go around 430mm/s straight. If you want the link DM me or check the BOM spreadsheet above  

Then I started CAD-ing, and I've got nearly the entire printhead set up! I think I'm going to use a CFD to simulate the fan airflow just to make sure it works, but other than that I need to add the BLTouch, some PETG framing, and I'll be essentially done there. Also, cable management 😬

![printhead](https://cloud-eaq9rc33e-hack-club-bot.vercel.app/0image.png)

Research + parts: 4 hrs  
CAD: 2 hrs

### day 4 - feb 5
Today I worked on the BOM a bit and researched where I might find cheaper parts. I think I over-calculated how expensive the frame will be (hopefully) so maybe I'll get out of debt? Worst case I spend 30 bucks out of my pocket.  

I have plenty of doubloons from High Seas, but DigiKey and the rest don't seem to have great parts. Surprisingly, DigiKey has absolutely no 3D printer mainboards, and the stepper motors they have aint worth squat. The rest of the time was basically just CAD, with a side-tangent to try an airflow simulator. I decided not to, though, because I was lazy. I worked on the fans, connected it to the linear rail, and made my logos!

Research and parts: 2 hrs  
CAD: 3 hrs

![vex logo](https://cloud-3vcb9x7yd-hack-club-bot.vercel.app/0vex-logo.png)

### day 5 - feb 6
Today I didn't do a whole lot because of schoolwork and other projects. I CAD-ed a little and that's basically it.

CAD: 1.5 hrs

### day 6 - feb 7
Today I had a stroke of genius *ok maybe just a stroke* and I decided to make the Vex a dedicated **upside-down** CoreXY! It's mainly for print farms and stuff because when the bed cools, the printhead just gives it a little nudge and the print falls right off! Also it just looks cool.

I'll probably make it reversable so you can print like a normal person if you want, with feet that can be put on either side and a removable Klipper host/screen. This does mean using linear rods instead of rails, though, so it may get more expensive? Idk.

Anyways, I'm still deciding on whether to have the motors upside down as well as the printhead, because if they're right side up (from your view), they're sitting on the desk/ground, but the carriage is reversed. This means that the model is effectively flipped X and Y (rotated 180 degrees) which may be an issue? I don't know. Probably not, right? RIGHT??

Either way linear rods are a good thing to do so that's what I'm doing.

(LATER) I did a lot of research and apparently upside down corexys are a really bad idea. Welp. It's OK, I'll do normal CoreXY and use linear rails still because they're also apparently good for speed and such. I did a tiny bit of CAD

Research: 2 hrs  
CAD: 30 min

### day 7 - feb 9
Yesterday I had an all-day D Now (Disciple Now) with my church which was very very fun!! No work though. Today was mostly research and some CAD, as I'm working on #printboard a lot now. Trying to get it done 😭

Research: 30 min  
CAD: 30 min

### day 8 - feb 10
Printboard!!!!!!!!!!!!!!! Some CAD for this though...

My current printhead setup:
![printhead](https://cdn.hack.pet/U07GPJ6V3UZ/printhead.png)

CAD: 1 hr

### day 9 - feb 12
Again, I haven't been doing a whole lot of this due to printboard, but I was able to get the linear rail mounting and a little bit of the hotend screw mounting figured out. Some pics:


![printhead picture](https://cdn.hackclubber.dev/slackcdn/0f6654d1a2b6a3a793b17d9be6afb554.png)
![mounting picture](https://cdn.hackclubber.dev/slackcdn/a26d3902d9a992ea64293aed2e87f950.png)

CAD: 2.5 hrs

### day 10 - feb 13
Today I researched a whole bunch of parts, from Gates belts to idlers, linear rods, and more! You can see my BOM [here!](https://docs.google.com/spreadsheets/d/1GO_HGXTeiZWquWsCZzynmvAluWZnmblAnS994K72vQ0/edit?usp=sharing)

I also did a little CAD today, importing some models for the bed, aluminum extrusions, and such. I fixed some model symmetry issues and increased the tolerance between the parts and the hotend. I've yet to run any CFD (computational flow dynamics) tests, but I may just get all the parts and see how the airflow works in real life instead.

Research: 2.5 hrs  
CAD: 1 hr

### day 11 - feb 14
Happy Valentines Day! Homeschooling doesn't usually provide Valentines though. On the bright side, I got lots of candy!!

Anyways, today was a big CAD day. I did research some mechanics, like the z-screws, bearings, idlers, and whatnot, but mostly just fixed CAD part tolerances and adjusted some of the models to make them more symmetric and nice looking. I've yet to add the BLTouch and Gates belt connecters though... maybe on day 12!!

Research: 2 hrs
CAD: 2 hrs

### day 12 - feb 15
Today I only researched stuff, as my hotend turns out <i>isn't</i> high-flow like ChatGPT said it was, and I needed to find a new one asap. Also researched frame parts and some kinematics!

Research: 3 hrs

### day 13 - feb 17
After finallllly getting my printboard submission in yesterday, today I can work fully on CAD and research. All I have left to do on the printhead is the BLTouch, belts, and accelerometer! I finished adjusting for the new hotend, the TZ E3 2.0, which doesn't get the 45mm<sup>3</sup>/s that I hoped for in the beginning, but gets 33mm<sup>3</sup>/s (according to the seller.)

I'm expecting probably 30mm<sup>3</sup>/s out of it, which is plenty for what I want.

CAD: 2.5 hrs

### day 14 - feb 18
Ouch. Turns out the hotend _doesn't_ fit all the way yet... well I guess I know what I have to do 😭

Other than that, I started the BLTouch mount and did some research on how to mount the belts and accelerometer :/

Research: 1 hr
CAD: 2 hrs

### day 14 - feb 19
I finally got the hotend to fit! I also mounted the BLTouch and the accelerometer. I started a bit on the belts, but wasn't able to get them done quite yet. [Here's](https://cdn.hackclubber.dev/slackcdn/afa3ab80102c1eb30fef80da450fb23d.mp4) a video of what my printhead looks like so far!

I also did more to improve tolerances and printablility. I decided to wire the accelerometer through a little printhead tunnel, which is 1) cute and 2) saves space :3

CAD: 2.5 hrs

### days 15 + 16 - feb 20 + 21
WOOOOOOOOOOOOOOOOOOOO  
I got the printhead done :D

I do still have to do the belts, but I'm saving that for when I get my gantry figured out. I also did a bunch of the frame! Pic (20th):

![frame with printhead](https://cdn.hackclubber.dev/slackcdn/404ca1ab919aa36960e3d61a59125e0a.png)

This thing is really coming together!!!

All I have left to do with the z-axis is add the linear rods and attach them to the bed. The gantry is looking quite daunting, but I guess I'll cross that bridge when I get to it. So far, the build size is 230x230x280mm, which is way bigger than my current printer (220x220x250mm)! Good deal.

CAD: 7 hrs

## z-axis - revision one && electronics housing - revision one

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

### days 24 - 34 - feb 28 - mar 16
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

## problems: days 34 thru 57 - mar 17 - apr 15
I thought I was bad at updating before..................... I've had a butt ton of school work and other stuff and lowk been forgetting to journal.

anyways here's what I got done in this month. I finished everything of the list above, and ordered parts. I paid about 70 bucks out of pocket, not including high seas credits. Now here's where the trouble begins.
I posted my design on the 3d printing discord server, open to critique. Turns out there was a ton of stuff that wasn't going to work, forcing me to all but redesign the entire kinematics for x, y, and especially z. I've gone from a single lead screw to dual screws operated on a belt system, like the vzbot. At the time of writing, I've just finished the design. It was tough, I'll admit. But it's way worth knowing that all the things I'd worried about were OK and that the printer will be AWESOME. All of the parts I'd ordered arrived minus two that got lost 😭

I'm planning to refund the lost orders tmrw, and I also had to refund some 8awg wire that I got in favor of 10awg. The new wire was stopped and delayed by customs, so I don't have very high expectations for that, either. Oof. I also reached out to polymaker about a filament donation, since the only PLA I have is black, white, and blue. I requested a spool of black PETG and a spool of their panchroma gold-silver pla. I think it'd look fantastic with the gold pei sheet and silver aluminum extrusions! It's been a few days, though, and they haven't responded. I don't have high hopes for that either, and worst case the printer is kinda splotchy looking.

It's been a real journey, and I've learned a lot thus far. Like, don't buy parts before you get people to look at your design. Bad idea. Speaking of parts, I have to return a few things:
1) Z flexible coupler: not necessary with a z belt system
2) Lead screw: 20mm too short with the new design
3) M5 screws: should have been M6 (for connecting stuff to the corner brackets)
4) Part cooling fans: they may not be powerful enough. Getting 5015s would be what I'd get instead, but would mean redesigning the entire printhead. I'll do some tests with my current 3d printer to figure it out.
5) LM8LUU bearings: by using 4 linear rods for z-axis instead of two, I'll need two more bearings, likely LMF8UU's, which only come in packs of four. I'd return these and buy the four-pack, but it's probable that I could 3D print bearings.

Since I already returned the 8awg wire, I only have 4 more monthy free returns from AliExpress. I probably won't return the LM8LUU's, and possibly not the M5 screws since they were only a buck fifty anyways. Lead screw is a must, and Z-coupler was five bucks so it'd be best if I can. Again, part cooling fans I'll have to wait and see.

List of stuff I had to change:
1) Shear the motors: I had to add bearings to the ends of the motors shafts so that the tension of the belts doesn't ruin the motors - $2
2) Add dowel pins to the idlers: Pins are necessary because 3D printed shafts to hold the idlers will snap under tension - $4
3) Redesign kinematics: The belts have to be routed straight. They weren't, and I had to redesign _everything__.
4) Redesign Z-axis: since the entire bed was held up by only one lead screw in the back, it would have sagged immensely. I was mistaken in assuming that the bearings in the front would give it some leverage and keep it up. They would only catch onto the screw and bend the bed more. A kind discord user pointed out the VZBot, which uses two lead screws on either side and four linear rods at the corners of the build plate. I basically copied this layout. No need to reinvent the wheel, right? Anyways I just now finished the lead screw holders and belt system, and it's ⬇️🔑🔥 (low key fire for you silly people)

Here are some pictures

![full printer pic](https://hc-cdn.hel1.your-objectstorage.com/s/v3/c5beb8d4fe4e04ff0a58194a03bc22a99109f588_image.png)

</br>
</br>
</br>
belt drive pic  

![belt drive](https://hc-cdn.hel1.your-objectstorage.com/s/v3/5e91e337324f3ce90279a0e2045dcece1b8d728c_image.png)

</br>
</br>
</br>
belt drive again  

![belt drive again](https://hc-cdn.hel1.your-objectstorage.com/s/v3/f701f4e7789ec5bf884b1ab685407637a06d4a06_image.png)

</br>
</br>
</br>
linear rail holder  

![linear rail holder](https://hc-cdn.hel1.your-objectstorage.com/s/v3/305967b105307954a096fe71786344b1c8ac1adb_image.png)

</br>
</br>
</br>
lead screw holder  

![lead screw holder](https://hc-cdn.hel1.your-objectstorage.com/s/v3/b152f07c15e7ed25768a8299dcc95e13ffad4681_image.png)

</br>
</br>
</br>
castle idler hast becometh mansion idler  

![super sturdy idler holder](https://hc-cdn.hel1.your-objectstorage.com/s/v3/766493a561bee6ab1e09e516b168070fb76ac700_image.png)

</br>
</br>
</br>
x/y idler holders!  

![x/y idler holders](https://hc-cdn.hel1.your-objectstorage.com/s/v3/27b1ff8fcb953c6bf06f155bcf06d7171ee241e7_image.png) 

For a month of work, I'd give this a solid 40 hours. Not a ton, but like I said there's been a bunch of school and stuff that tbh takes priority.

## parts
### day 58 - apr 16

Today I got my current 3D printer back up and running after a week or two of inactivity due to wifi issues. It's all set and ready, and I started by doing a test. I printed a benchy at 50% fan speed to see what would happen, in order to test if the 4010 blower fans would be enough for the Vex. It turned out well. Not great, but not awful. I did some research and asked perplexity.ai and got the general consensus that 7+ CFM would be best for 30mm<sup>3</sup>/s or more. The fans I got are about 3.62 CFM each, and I have two, so that could be enough? I'm not sure but I want to try them. I also connected the lead screw nuts to the bed holder, meaning all I have left is attaching the back linear rods. I'm planning to order parts tmrw after some research today.

Here goes nothing.

Research: 1 hr 30 min, CAD: 1 hr

### days 59 thru 61 - apr 17 - 19

These days I ordered all of the remaining parts after getting refunds from AliExpress. They should arrive in about a week, and in the meantime, I'm printing parts. I plan to make a livestream of me building the printer on the HC slack as soon as I get parts printed, but I'm not sure how my parents will react. 🤞

But here's a really big thing.

On day 61,

## Polymaker sponsored my 3D printer

That's right!! I sent them an email, and none other than Polymaker Joel responded by giving me free filament to make the Anicept Vex! Gigantic shoutout to them. Polymaker ROCKS. Like this has singlehandedly rekindled my love of humanity. it's just a little reminder that good people exist, and i'm so blessed to be able to interact with them. as im writing this im literally grinning widely because of how great it all is. thank you so, so much.

Polymaker🔛🔝

(plz note, if you're a hackclubber reading this I'd appreciate if u didn't tell everybody on slack,,, not because they don't deserve the sponsorship but because if 50 ppl ask polymaker for free filament for the same reason, they may start to become suspicious and less lenient. this can put a bad name on hack club. thx.)

## parts arrive - and more problems
### days 62 thru 70 - apr 20 - 28

In these days pretty much all the parts arrived, plus my polymaker order! I got a spool of white and a spool of black pla, which I already owned but needed more of, a spool of red pla, a spool of black PETG, and a spool of metallic gold pla!!! My printer is gonna be sick with the white/black/gold theme.

I started 3d printing a bunch of parts for it, and began to piece it together bit by bit to make sure it works. I'm planning to do a livestream of me building it, and I might record it somewhere and link it, but idk if my parents will let me :b  
As I'm writing this I'm setting up my new gold pla with a temp tower (looks like it just finished 215°C!) and then I'll get my black petg set up. I won't be using the polymaker petg for this project, since, while it's better, I have some rapid petg for the bigger parts so that it doesn't take ages to print them.

One kinda weird thing that happened tho, a linear rod from aliexpress arrived empty 😭
Like, you can't do that!!!! Looks like the seller shipped it empty!!!!!! I applied for a refund but they haven't given it yet since I can't really prove it. So I'm waiting on that (actually it's kinda not necessary maybe. I'll see.) and a digikey order just for some sttuff like wires, wire nuts, etc.

Anyways that's basically it. Z axis belt system works good. Oh yeah, I also need to get a build plate from amazon. Will do.

OH YEAH and I also................... waiiit........... i forgot... oh yeah. I changed the printhead logo to be super sick and much better since it was super ugly. Now it matches my logo at [https://anicetus.dev](https://anicetus.dev) (shameless plug) as a cool hexagon thing:

![new logo](https://hc-cdn.hel1.your-objectstorage.com/s/v3/bf08cb30a5bd7cdd6134c7e9cb830e697c99ef9c_anicept-vex-new-logo.jpg)

and here's a belt drive rendered pic for good measure

![belt drive](https://hc-cdn.hel1.your-objectstorage.com/s/v3/16d1f4e7901421dfefa5fa2ac5ddbe8fe9146de4_belt-drive.jpeg)

### days 71 thru 76 - apr 29 - may 6

Well, my digikey order and amazon order arrived. AliExpress still wont let me refund the package, but this time around I chatted with the seller and they acknowledged that the packaeg was empty. I took a screen recording of the chat as well as the chat ID so they can check it. I really hope I get it refunded! However I'm like 79% sure I won't need the rod, so no rush on the refund really. 3 rods should be enough according to some geeks in the 3d printing discord.

[This](https://www.amazon.com/gp/product/B0CQ1S6Z32/) is the build plate I got from amazon (gold pei + gold peo). it looks ssooooooo goooood!!! the peo side is super shiny and makes amazing rainbow reflections

turns out I didnt need to get wire nuts from digikey tho, since my dad has some... well it's too late. completely unrelated but with my new digikey order I now have 14 esp32s and an arduino uno :D

however  
I need to do more redesign. Again. Yes. Ow. so turns out my mainboard wouldn't fit in the enclosure i made for it with all the wires and stuff blocking everything (the spade connectors for the psu are suuuuper long) so i had to totally redesign it. i think im just about done, and I made a new design with the mainboard above the aluminum extrusions and rotated 180° to make it fit better.

unfortunately, moving the mainboard around and such will mean editing the z-axis. this is probably for the better, cuz some geeks on the 3d printing discord were saying that having 4 linear rods will overconstrain the bed or something like that. my current design has 3 rods (which is what I currently have) but if need be I can easily add a 4th (granted stupid aliexpress refunds me)

this means all but redesigning the entire heated bed holder. ouch.

ig that's enough yap for today. my hour count is super inaccurate already so for the 6 days since last update I'll give it a 15 hrs of cad.

P.S. I've blown through about 500g of filament in the past two weeks
P.P.S. I finished my school year so i'll probably have more time to write these updates!

## 3d print parts + more issues
### days 77 thru 82 - may 7 - 12
so yeah i 3d printed a buncha parts! nearly all of the pla ones. i still have to print the petg bed holder, motor mounts, idler holders, etc.  
i also fixed the z-axis and electronics casing thankfully. aliexpress still isn't refunding me and I decided the 4 bucks wasn't worth my time so i gave up. no biggie ig. i'll attach some pics soon, can't rn

### day 83 - may 13
Continued printing parts! I did a lil bit of PETG printing, but ran into an issue. Again.  
My fan ducts don't work at all. Like, 0 air comes out. It's all bouncing back out of the duct and through the fans' air inlets. It is 100% not going to work and im afraid ill have to redesign the entire printhead. I'll experiment tmrw and see what happens.

### day 84 - may 14
I THINK I DID IT. I widened the duct holes a LOT to let more air in, and sure enough the airflow septupled. It's not very focused, but that's OK I guess. The air still bounces back some, so i may need to do a bit more so that the fans aren't like blowing directly at a solid wall of plastic. However making the holes any wider would point air in directions I don't want it to go, so to fix this I'd need to smooth out the 75-ish degree turn in the duct and possibly angle the fans different. But honestly, this new printer will probably be mainly for rapid PETG or other filaments that don't need a ton of fan power, so I may just leave it be.

For now, I'm gonna keep the ducts as they "air" (hehe) and see how it does with regular ol' PLA. Wish me luck 🫡

## what i've learned from making the Anicept Vex

1) NEVER EVER EVER EVER EVER EVER EVER trust AI alone. Always google it first and if you're lucky, some rando on reddit has already answered it. if not, get some help from ppl who actually know what they're doing. If you have to use AI, use [perplexity](https://www.perplexity.ai/) it uses much more sources than other ais, like chatgpt. the way most ai works is it scours the web for data, and whether or not it's true or not doesn't make a difference. it might take the statement "idk but im pretty sure that it gets up to 45mm<sup>3</sup>/s" and use it as proof that the hotend gets up to 45mm<sup>3</sup>/s, even though it's likely just somebody's arrogant opinion. I was researching what hotend to get and chatgpt told me that the Phaetus Dragonfly gets up to 45mm<sup>3</sup>/s, when, in reality, it only gets 15mm<sup>3</sup>/s. I'd already designed the entire printhead when I learned this, and thus had to redo a lot to account for a new one. Not only does trusting AI waste time making you redesign and do more research, it wastes time and effort making you redesign and do more research.
2) dont make compromises. it never works. dont buy the cheap thing because its cheap. there's a reason it's cheap. and when designing stuff, dont maximize space. leave tolerances and tons of room for wires and whatnot. cutting corners, as fun and easy as it may look, never works. this is probably cliche to you, but it's very true. when i was designing the z-axis (the first time) for the vex, it seemed ok to be able to use one screw in the back and two rods in the front. this was a huge mistake on my part. in the back of my head, i thought the bed might sag and it might not work, but i ignored it. welp now I'm redesigning it, for the _second_ time. don't make compromises.
3) do your research. always, always, always read aliexpress (or amazon) reviews. check the product specifications before buying. I thought my motors had a 2.7mH inductance, but they have a 3mH inductance. This isn't ideal, and will hamper how fast I can print. I thought it had the lower inductance because, surprise surprise, the aliexpress page said it did. but when I got the motors, the card that came with them clearly said 3mH inductance. I checked out the official store, omc-stepperonline.com, and the page there clearly said 3mH inductance. the aliexpress page was dead wrong, and it's costing me. I won't return them, because I couldn't find any better motors for a decent price anyways, but always remember to do your research, and never trust aliexpress specifications. you'll be sorry if you don't.
4) dont get discouraged. believe it or not, you _can_ do it. It'll take time and effort, and you'll be sick of it, but power through and just DO it. the only way to get a hard thing done is to do it or hire somebody else to do it, and nobody can afford that. when you get bored or angry, don't doomscroll youtube shorts. literally just do it. honestly this is tough for me, especially designing tough parts like the printhead and gantry of the vex. but when it's done, it's DONE! Now reward yourself and watch 11 hours of zach freedman.
5) remember that _you_ decided to do this project, the highs and the lows, so have fun with it. it's easy to get frustrated at the amount of work you have to do, but soon enough you're gonna be a responsible adult who has an actual job doing something likely even more frustrating. have fun with a project that you're doing of your own free will, and know that soon enough it'll be over, and you'll feel both sad and happy. You'll be sad because it was a big journey that you no longer are on, and happy for the exact same reason.
6) you're not alone. probably. at least for infill, it's me and a dozen other active members. they're doing the same thing you are, and probably feeling just as frustrated as you. go chat with them about whatever it is you're doing. it helps. and help people who are new or just starting. use your minimal experience to guide people who were in the same place as you. when I was starting, i had a bunch of help from assorted people, but i had to research a ton of stuff myself. i.e. what motors, belts, and other parts to use. if other people are working on the same thing and are a bit ahead of you, they've likely already researched those parts. ask them what parts they use. to be fair, it may not apply sometimes, particularly with a scope as broad as a 3d printer to design. dont be afraid to ask for help, and especially not to give help when you can
7) here's a bit of 3d printer specific advice: design the printhead, gantry, and z-axis before you design anything else. I went straight from printhead to electronics casing because I was scared of the gantry. dont be. it'll be super tough, but it'll save you a bunch of heartache having to redesign stuff because it doesn't fit in what you already have.

Well that's it!! Hope that helps somebody.

## pictures!! my timeline of the printer :D

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

That's quite a gap to bridge,,,

![uhoh](https://hc-cdn.hel1.your-objectstorage.com/s/v3/426656da9cbad3609a97db1f1353591fadfdea3a_screenshot_2025-03-19_154424.png)
