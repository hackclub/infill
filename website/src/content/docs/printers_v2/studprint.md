---
title: "Studprint"
description: "A 3D printer built using classic LEGO bricks."
project_name: "STUDPRINT"
repository: "https://raw.githubusercontent.com/AdamTuraj/Studprint/refs/heads/main/JOURNAL.md"
---
# StudPrint Journal

Back at it this year. This is the journal for Infill V2!

### Day 1 (February 13th)

Hours Worked: 2 hours
Total Hours Worked: 2 hours

---

#### BOM Selection

Began choosing the components for this printer. Since it will be a very barebones printer, the BOM is fairly short. You may be confused on why there is no extruder. I am going to try to use LEGO parts and a rubber band as an idler 😅. The BOM can be found in this repo as [BOM.xlsx](/BOM.xlsx). An image of the current version is also below.

![BOM](https://user-cdn.hackclub-assets.com/019c58b3-5fef-7cc7-87a4-1b7d3abe9489/Screenshot%202026-02-13%20152936.png)

### Day 13 (February 26th)

Hours Worked: 15 hours
Total Hours Worked: 17 hours

---

#### X axis

I haven't been journalling as I should but the X axis has been completed. It is almost all LEGO with the exception of the mounts for the hotend, BLTouch, and the leadscrew adapter. The motion is controlled via LEGO worm screws. Technically they are technique parts but theres no way to get around it. Originally, I wasn't planning on using LEGO for the motion platform but here we are. Below is an image of the X axis:

![X axis](<https://cdn.hackclub.com/019ca178-23c3-7d19-a694-cabbe088ae4c/image%20(1).png>)

#### Y axis

I have also finished the Y axis. It is simply a single linear rod with a LEGO leadscrew. I am a little concerned with the up play but I believe that may not be an issue. Next up is the Z axis, extruder, and electronics, and final touches. Hopefully I can finish it within a week!

![Y Axis](https://cdn.hackclub.com/019ca178-10f9-79f6-ac93-9101c840acd1/image.png)

### Day 14 (February 27th)

Hours Worked: 2.5 hours
Total Hours Worked: 19.5 hours

---

#### Z axis

The Z axis screw on the left side has been added and I created a mounted solution between that, a linear rail, and the X axis. It was tricky to package it all together nicely; however, it worked out really well in the end. The other side will be slightly trickier but I can apply the same strategies and overall design as the left side.

#### Future Plan

I put together an overall plan I can hopefully follow to finish the preliminary design this week:

**Saturday** I need to finish the other side, add the rails, and connect the Z axis to the Y axis.

**Sunday** I connect the sides together at the top and create the extruder.

**Monday** I make the electronics enclosure. Hopefully by Tuesday / Wednesday I have a BOM ready and can go through my LEGO and pick out all the parts so I can figure out what I need to order.

Here is what that section looks like and the overall look of the printer:
![The XZ mount](https://cdn.hackclub.com/019ca287-83b9-7563-9788-3cf95a694f93/Screenshot%202026-02-27%20233122.png)
![The printer](https://cdn.hackclub.com/019ca291-5588-74b0-82ce-145e8a62d24f/Screenshot%202026-02-27%20234557.png)

### Day 16 (March 1st)

Hours Worked: 1.5 hours
Total Hours Worked: 21 hours

---

#### Z axis

Everything took longer than expected so the schedule above is in the trash. I finished the left side Z axis mount and I am working on the right side. For looks purposes, I want the rails on both sides to be mirrored which is causing issues with the X motion system. Currently playing around with placement until something works.

![Z Axis](https://cdn.hackclub.com/019cb185-7ebe-7b3d-8ac5-f01a3997295c/Screenshot%202026-03-02%20212706.png)

### Day 18 (March 3rd)

Hours Worked: 4 hours
Total Hours Worked: 25 hours

---

#### XZ Axis

After much consideration, I decided that mounting the X stepper after the Z rail and using a 3D printed part to connect to the worm gear. Not ideal, I was hoping to minimize the 3D printed part use here but due to time constraints and self-imposed visual requirements, I deemed this good enough.

I followed this by designing a mount for the X motor which took a few tries due to the limited space. I did a quick check to ensure there are no collisions and called this part of the Z axis complete. All that is left to do is:

- Connect the left and right Z axis' at the top
- Design the extruder
- Mount the electronics somewhere

I am hoping to finish it by the end of the week!

![Close up of XZ on right](https://cdn.hackclub.com/019cb5d7-6c97-7116-bb8d-29948ddb7a91/Screenshot%202026-03-03%20173444.png)
![Isometric view](https://cdn.hackclub.com/019cb5d7-c299-7ca1-b9de-ceab2a797b97/Screenshot%202026-03-03%20173537.png)

### Day 20 (March 5th)

Hours Worked: 6 hours
Total Hours Worked: 31 hours

---

#### Z Axis Top

The Z axis has been finished. I'm a little worried that the top won't be stiff enough. I will hope that its enough and if it isn't I'll try to improve until it works. Unfortunately, it is difficult to stiffen it up more due to lack of space and the limitations of LEGO. Below is a screenshot of this assembly.

![XZ Axis](https://cdn.hackclub.com/019cc151-9fd8-7a46-9451-c851d83d22e8/Screenshot%202026-03-05%20230416.png)

#### Extruder

The final major motion part of this project is complete: the extruder. Using a rubber band to provide tension for the idler and a stepper connected directly to the drive wheel, I can only hope this can provide a consistent enough extrusion. It still needs the adapter between the stepper and wheel; however, thats a later issue. Mounting for the extruder is on the top of the Z axis and is connected accross 4 points. This will hopefully be enough to keep it in place.

![Extruder](https://cdn.hackclub.com/019cc151-bc87-756c-8422-77012bc3dae7/Screenshot%202026-03-05%20230404.png)
![Complete printer](https://cdn.hackclub.com/019cc151-d8c5-7be5-9027-b08ea18827ca/Screenshot%202026-03-05%20225251.png)

### Day 21 (March 7th)

Hours Worked: 5 hours
Total Hours Worked: 36 hours

---

#### Electronics

The last part of the project was electronics. Im using the LRS-150 and BTT SKR Pico v1.0. I decided to put the PSU under the printer and mounted the BTT on the back. It looks good and compact. The mounts are not the greatest but they are good enough. My main goal is to get an initial draft done so I can order the parts and get building.

Overall, the initial design is done. I just have to update the BOP and see what parts I need.

![Finished printer](https://cdn.hackclub.com/019ccb5f-7670-7e53-a309-8d6cbaab3454/Screenshot%202026-03-07%20174320.png)

#### BOM

I updated the BOM and added the LEGO parts. I still need to figure out the part numbers for the wheel and axle, along with checking how many of the right angle pieces are inverted. Afterwards, I will go through my stash and see what I need!

![BOM](https://cdn.hackclub.com/019ccbfd-ddc6-71c0-8fcf-3b1d10217087/Screenshot%202026-03-08%20004836.png)

### Day 22 (March 11th)

Hours Worked: 0.25 hours
Total Hours Worked: 36.25 hours

---

#### Extruder

I quickly modelled out the axle adapter for the extruder. Due to lack of space, it will be using a friction fit and I may add a blob of glue to ensure it stays. Im not entirely sure if the axle will fit. Its difficult to measure the part I have due to how small it is.

![Axle adapter](https://cdn.hackclub.com/019cdf23-5bb2-708f-943d-888b14a88b75/Screenshot%202026-03-11%20190050.png)

### Day 23 (March 15th)

Hours Worked: 3 hours
Total Hours Worked: 39.25 hours

---

#### Beginning the build

Day one of the build came with great success. Only two major changes were needed: the Z axis -> top connector, and the Y axis leadscrew mounting on the bed. The custom parts are in the process in being printed and the wormscrews were just shipped. I may completly build it and wait for the wormscrews or 3D print some temporary wormscrews. Below is a picture of the current state of the build.

![Build day 1](https://cdn.hackclub.com/019cf461-0217-7fa8-8e88-ff707ec3ec9f/IMG_8876.jpg)

### Finale (March 16th until April 19th)

Total Worked: 20 hours
Total Hours Worked: 59.25

---

#### Continuing the build

The X axis and stepper mounting went fairly smooth. Some adjustments were made the the X axis mount, along with the buffing up the X axis with the addition of two wheels.
![XZ Wheel change](https://cdn.hackclub.com/019dcae6-d981-7a8e-8eff-5c5183f29a6f/paste-1777225621337.png)

Y axis largely remained the same with the exception of reinforcements to the YZ mounts and the addition of long plates across the bottom to reduce failure.

The Z axis was assembled with minimal issues; only additional reinforcements on the other side of the Z structure along with the removal of top constraints for the Z screws.

The toolhead also had a bit of an upgrade. It had too much rotational play so an additional wheel was added at the bottom of the X rail to mitigate this.
![Toolhead change](https://cdn.hackclub.com/019dcae6-37d0-7795-853c-a9cec8652f35/paste-1777225579869.png)

Finally, the extruder needed a whole redesign. The wheels could not grip the filament well enough so friction from the bowden and hotend caused extrusion to be impossible.

To mitigate this, I decided to ditch the LEGO wheel concept and switched to using BMG dual extruder gears and a springed tensioner. It still utilized LEGO parts; however, it was just unrealistic to use LEGO wheels and expect consistent extrusion.
![New extruder](https://cdn.hackclub.com/019dcaea-21c7-7973-8310-e51f6435b79e/paste-1777225836459.png)

#### Printing!

With all these changes and the printer being fully built, I got printing. After setting up Klipper, I was able to load filament, and successfully print a Benchy boat in about 1.25 hours!
![First successful Benchy](https://cdn.hackclub.com/019dcaec-6203-72af-815c-634c128e2491/paste-1777225983742.png)
![The built printer](https://cdn.hackclub.com/019dcaec-a548-79a8-882b-6ab859ebe0b4/paste-1777226000985.png)

#### Last minute changes

During RMRRF, I was having consistent issues with the extruder regarding kinking of the bowden tube and a bad filament path. After hearing feedback from others, I decided to rotate the extruder 90 degrees which allows more room for the bowden to compress. This would be the final change to the printer!

![Updated motor mount](https://cdn.hackclub.com/019dcaee-c72b-7614-b950-551def17d872/paste-1777226139590.png)
