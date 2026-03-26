---
title: "moron"
description: "120x120x120 Polar-CoreXY hybrid printer, inspired by the Voron V0."
project_name: "moron"
repository: "https://raw.githubusercontent.com/RedBigz/moron/refs/heads/main/JOURNAL.md"
---
**Made by**: @redbigz // may<br/>
**Repository link**: https://github.com/RedBigz/moron<br/>
**Total hours so far**: 20

- [x] I have a 3D printer or will be getting one before March 21st

# 7/3

## Mind Map

**Approximate hours**: 2

So there used to be an old mind-map here that uses cross-gantry kinematics because I abandoned my plan for a hybrid polar-CoreXY V0-style printer. I just found out it's stupid easy to make a polar bed!

Lazy susans spin infinitely and are relatively cheap (https://www.aliexpress.com/item/1005007540027466.html), so i can just screw some mounts in and have a polar bed! Would still have to devise printed idlers and such though.

Here's my new mind map!

![New Mind Map](https://raw.githubusercontent.com/RedBigz/moron/refs/heads/main/media/logs/26-3-07/mind_map.excalidraw.svg)

# 22/3-23/3

## Z Axis

**Approximate hours: 9**

I created the Z axis, including the lazy susan system for the bed.

![Z Axis](https://raw.githubusercontent.com/RedBigz/moron/refs/heads/main/media/logs/26-3-23/zaxis.png)

### Bed

For the bed, I'm planning to CNC a custom 120mm diameter polar bed design (inspired by the V0 120mm plate). I mocked up a basic 6mm three-screw (M3) bedplate in OnShape and created all the necessary adapters to place it on the Z axis. A slip ring mount point was also implemented into the bed adapter to stop wire tangling. I'm using a 4" lazy susan for this as any larger would introduce more issues when mounting (I noticed >4" lazy susans have glued feet as well, which sucks).

![Cross-section of the Z axis](https://raw.githubusercontent.com/RedBigz/moron/refs/heads/main/media/logs/26-3-23/xsection.png)

### Motion

I'm using two motors for the Z axis to maintain stability, as I couldn't find a way to implement a cantilever polar bed since the weight requirements would be high.

I have yet to set up the polar rotation system, will do that soon.

That's pretty much it <3

### Rotation

This took forever to set up. I realised that a belt path couldn't be made above the lazy susan, so I elongated the slip ring and added 2GT teeth to allow for rotation *under* the bed.

![Rotation](https://raw.githubusercontent.com/RedBigz/moron/refs/heads/main/media/logs/26-3-23/sliprotation.png)

# 24/3-26/3

## Gantry

**Approximate hours: 9**

I made the gantry! Yay! I ended up using MGN9 rails since linear rods would be annoying to tap, and they're relatively cheap when you get them off sketchy AliExpress stores.

![Gantry and bed](https://raw.githubusercontent.com/RedBigz/moron/refs/heads/main/media/logs/26-3-26/gantryandbed.png)

I ripped off the placement style of the idlers and motors from the Voron 0.2 since I barely had space, but all the modelling and calculations were done by me.

**BEHOLD: THE CRAPPY EXCALIDRAW BELT PATH**

![Belt path](https://raw.githubusercontent.com/RedBigz/moron/refs/heads/main/media/logs/26-3-26/beltpath.png)