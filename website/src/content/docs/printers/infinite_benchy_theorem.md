---
title: "Infinite Benchy Theorem"
description: "A belted, enclosed 3D printer designed for 24/7 3D printing"
project_name: "Infinite Benchy Theorem"
repository: "https://raw.githubusercontent.com/qcoral/infinite-benchy-theorem/refs/heads/main/journal.md"
---
Made by: @dari // alexren \
Repository link: https://github.com/qcoral/infinite-benchy-theorem \
Total hours so far: 8h
- [x] I have a 3D printer or will be getting one before March 21st

---

dari // alexren's attempt at making *yet another* 3D printer!

Pitch: budget enclosed belted 3D printer. Can print farm for all my YSWS needs. Also just a fun device
## Day 0: February 1st, 2025

Basically did some planning and preliminary research

Here's my unfiltered notes for the day: will probably keep this in a separate document?? idk

Links I've gathered so far:
- https://www.reddit.com/r/3Dprinting/comments/sjnw7z/conveyor_belt_3d_printers_are_they_a_viable/
- https://www.youtube.com/watch?v=cfD20oOWD28
	- I want to do something like this? and then a fusion of The 100:

I want this thing to be very easy to mod & hack. Should be able to live on my desk if I want

MUST be enclosed. I'll print the parts out of ABS cause I have an X1C? Thinking of a cheaper, easier to mod V0 (albeit prints slower but that's okay)

**Time elapsed: 1h**

## February 4th, 2025
Didn't get too much time to work on stuff today - recovering from a concussion + got caugh up in other stuff

I did move my planning and stuff from bare sublime text to an actual obsidian thing though!! So there's that

also, remembered the nevermore exists so I'm going to try to integrate that since this thing will be printing 24/7

**Time elapsed:** **1h**

## March 27th, 2025
Didn't touch this for two months whoops - let's lock in

**Time elapsed: ~6h**

Did a BUNCH of research and re orienting - I realized that a belt 3D printer was pretty pointless and a toolchanger with a print pushing tool would be a lot more fun.

![[assets/day1.png]]

I also spent a ton of time looking into the bed setup. PCB heaters are boring, expensive, and dubious to source as they usually come from a black box. The usual alternative to this is just a slab of drilled mic-6 with a silicone heater on top and having the spring setup, but I wanted to avoid this b/c it seems overkill and also requires you to drill metal.

Instead, I'm going to try slapping on a slab of g10 and adding a silicone heater underneath. It's going to be clamped onto the bed via a compliant spring mechanism. I was considering using aluminum for this but I'm worried the thermal conductivity + thermal expansion might deform the bed over time if I'm printing at 100C on the bed

Fiberglass has a generally pretty poor thermal conductivity so I think I can get away with the g10 - overall though, I'm probably just gonna buy multiple solutions and test

Anyhow - decided this was gonna be a fun printer to just implement & test features I've always wanted to.

Also, it's super trippy to go back and play catch up for the past 2 years of the 3D printing market? weird to see how much stuff has changed but still cool to see how much is the same.

I used to record a vlog after every day and just dump my mind of what I did and stuff I came across. Maybe I should start doing that again soon. Little awkward with other people around though.

Status of printer: give or take using a lot of the same design considerations as I did with Neutrino, but I think the screenshots & commit history should speak for itself?? idk

## March 28th, 2025

**Time elapsed: ~2h**

How the fuck is it 3:51pm when I started this lmao

lock in.

okay today was a bunch of meetings for stuff that I can't really talk about or else it'd be leeks lmao. Also first day I ran the mini hardware[[ ]]thing (?) too so that was awesome

Anyways today was mostly solidifying the rest of the printer & figuring out some triple Z stuff - definitely appreciate the engineering that went into the 2.4 and Trident after this.
(more specifically, it never occurred to me that having a slanted bed would cause stretching - I need to account for that when designing my own)

Also [ov3660's](https://www.aliexpress.us/item/3256807837835215.html) webcams are so cheap. what. had no fucking clue lol. definitely gonna use them in my next build

Mainly just still researching all the different parts. This is taking a ton of time b/c I really want to make something high quality

## March 30th -> April 1st, 2025

**Time elapsed: ~12h?**

Didn't touch this at all yesterday b/c I needed to adult & get my life together. Came back today

Mainly spent my time doing research and solidifying what exactly the printer is about, which is basically going to answer "*how can we pack the most features into a printer while spending under $300?*"

Also going to try to reuse as many parts from Hack Club's old blot stash. There's a bunch of leftover parts from its development that I inherited that will pretty much never get used, so. I'm going to try to eat up most of it with this printer. It includes stuff like belts, motors, extrusions, pulleys, fasteners, etc.

Here's what the BOM looks like currently - $230 missing a bunch of stuff but I think $70 should be enough leeway for the rest of what I need

![[Pasted image 20250402115512.png]]

Some of the part choices will be a little funky as a result, but it'll still be a solid printer!!

Also looked into some toolchanger stuff. WP-DAKSH, Stealthburner, etc

(insert images from ipad here later.)

I'm going to try recording videos for this in the future and just ranting my mind and trying to have AI summarize it? idk. That was a lot more natural for me back in the day and it made it feel better.

officially started 3D modelling!!

## April 2nd, 2025

W 

![[Pasted image 20250402151400.png]]


