---
title: "MiniPrintV1"
description: "3-axis printer designed for precision and complex parts and maybe even a swappable tool head"
project_name: "MiniPrintV1"
repository: "https://raw.githubusercontent.com/arp2019-Dev/MiniPrintV1/refs/heads/main/JOURNAL.md"
---
Made by: @arp // Akhil Pathapati
Repository link: https://github.com/arp2019-Dev/MiniPrintV1
Total hours so far: 50

- [x] I have a 3D printer or will be getting one before March 21st

Update 1:
Worked on the general outline of the printer and its basic architecture in CAD. Decided to go simple with a bedslinger design with a 180mm cubed build volume.
<img width="604" alt="Screenshot 2025-03-27 at 8 27 03 PM" src="https://github.com/user-attachments/assets/e068dd02-32cf-4a18-bf93-1dec9bb25e6c" />

Update 2:
Started working on the BOM and figured out my constraints for electronics and component selection to help me figure out my design. Need to continue narrowing down options for the Mainboard and extruder. I do know I want to use Klipper so that helps.

Update 3:
I should really update more often so my bad but I worked a lot on the design and I am switching to the MKS Robin Nano series for the main board and a direct drive extruder. I am also using mostly 2020 extrusion and nema17 motors, and igus linear rails for support and rigidity.

Update 4: 
Using an LDO orbiter extruder and High Temp hotend to hopefully print some cool engineering filaments. I also am confirmed making a 150mm x 150mm build volume Z height is TBD but prob more than 150mm. I am cadding the main structure and how/where I want the electronics to be roughly. I'll refine it as I design more.
<img width="605" alt="Screenshot 2025-03-27 at 8 27 43 PM" src="https://github.com/user-attachments/assets/8beb289a-abb7-49d7-9fb2-351aebae4d2c" />


Update 5:
I started finding more parts like belts and pulleys as well as an ABL probe, gonna use the BTT microprobe. I'm also narrowing down my selection of motors, I will use E Series Nema 17 42Ncm motors. I also found a good PSU hopefully it doesn't blow up in my face. I also worked on more CAD to implement all the new components.

Update 6:
I started adding up all the prices for parts and it's not looking good, slightly above 300 so ima switch some things up. I was thinking of doing a 180mm bed again but I want the printer to be small so that it can be focused on precision. I'm starting to work on mounts for the extruder and hot end, and the electronics bay.

Update 7: 
Currently working on an airplane very bumpy but work must be done. Decided to add another extruder for dual extrusion, One direct drive and one Bowden to keep things cheap, secure, and lightweight. Also made the frame more rigid in CAD hopefully it's the same in real life. I am going to start putting all the last touches and fans soon. I also finished some of the mounts and adapters for various components 
<img width="421" alt="Screenshot 2025-03-27 at 8 25 15 PM" src="https://github.com/user-attachments/assets/0229c594-1217-422b-9709-1e688e511653" />

Update 8:
Changed again, I am after all going with a 180mm bed since 150 is comically small, also did not use the LDO orbiter extruder and instead found a better one for a lower price. Hopefully, my cad doesn't die when I try to increase the size. I also need to figure out how I want to implement the Y-axis belt system since I want to make it look nice and not bulky with those long tensioners.

Update 9:
Started working on my PCB for powering the printer, gonna be trying USBC with a 96w Apple adapter. This printer won't have a heatbed but I might just keep the bed there and make it so that if it needs to be heated it needs to have another USB-C adapter connected just for that. Due to this also im final on the 150mm cubed bed size. and not doing dual extruder. For the axis, I moved the stepper into the frame of the printer and will need to figure out how to get the belt attached now. Depending on the price I might add a removable toolhead so I can add other things too.


Update 10:
The printer is almost complete and actually finalized this time lol. I am not doing usbc and instead doing a removable tool head with a laser attachment and regular fdm attachment. I am going to submit for the grant now so I can hopefully get parts ordered before the aliexpress deal ends. My bom is finished and my cad is almost done. its just the cosmetics left.
<img width="595" alt="Screenshot 2025-03-27 at 8 24 37 PM" src="https://github.com/user-attachments/assets/ea671b84-71f4-4212-bac3-53c612fef30b" />

Update 11:
I'm done with my printer, 150mm cubed, ldo extruder, bedslinger with silent drivers and bl touch. Now it's time to order parts if I get approved and start building.
<img width="648" alt="Screenshot 2025-03-27 at 9 05 56 PM" src="https://github.com/user-attachments/assets/d7d35b83-4520-407e-ab75-eb16d3c5fb67" />

Update 12:
Complete redesign, new y axis and fixed all my gantrys and belts also I upgraded to a 180mm cubed build volume. Also the fottprint is a new shape and smaller.
<img width="597" alt="Screenshot 2025-03-30 at 8 59 27 PM" src="https://github.com/user-attachments/assets/ce786950-bbf4-4e20-9b2b-2fa979b8a0ea" />


