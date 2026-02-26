---
title: "Radeon"
description: "A budget-friendly printer designed around CoreXY kinematics and linear rails."
project_name: "Radeon"
repository: "https://raw.githubusercontent.com/pmnlla/radeon/refs/heads/master/docs-head.md"
---

## Toolhead Planning

First up, pick a random model of linear bearings off of the adsk parts library. Does it matter which ones you pick? yes. Are you designing parametrically, and adapting to different bearings will be hella easy? also yes.

You'll already encounter an issue here - with 35mm spacing between the rods, you lack the room to fit a full sized heatbreak fan like a Bambu printer uses. 

![](https://cloud-1jevp0mxl-hack-club-bot.vercel.app/0fusion360_vwbkaals58.png)

There are a few solutions to this:
- Increace the rod spacing, i.e. what a sane person would do
- Switch to a blower fan for heatbreak cooling with a really fancy mounting mechanism, i.e. what I did.


### Hotend

The best I can do for a hotend design is to use an off the shelf part. There are several options:

- Rapido: takes up the entire budget.
- Anycubic Kobra/Vyper hotends: I've got plenty of experience with these, they're insanely cheap, and easy to mount. However, they have such horrible flow rates that there's no point in using one with CoreXY kinematics.
- Elegoo Neptune 4 hotend: Disappointing at best, but super easy to work with.
- Bambu P1/X1 series hotend: also very easy to work with, has a very compact footprint, and very high flow. A little more difficult to mount, and the heatbreak fan is one hell of an obstacle. Also has a stupid proprietary connector that I CBA to reverse engineer. However, I can find them plentifully on AliExpress for around CA$15 per unit.

At the end of the day, I picked the Bambu series hotend. The reason for this decision is that they're yet to disappoint me - I've got one in my Elegoo printer right now and it performs excellently, heats up quick, and is very budget friendly, so I may as well give it a shot.

