---
title: "Belty Boi"
description: "A silly little belted printer similar to the CR30 but based on croxy for the gantry "
project_name: "Belty Boi"
repository: "https://raw.githubusercontent.com/WilliamPrime/Infil-V2-printer/refs/heads/main/journal.md"
---



# 14/03/2026 Started a new BOM 1.5h

Originally i had been planning for this to be a corexy belted printer
however i had a change of mind and want to try make a croxy belted 3d printer, which will probably make things harder

if i run out of time, this might get turned into a voron 0.1 size croxy 3d printer, it really depends how things go.

Back to what i actually did


# 18/03/2026 started on a parametric frame 2h

Really just getting back into the swing of parametric CAD.
Last time i did a bunch of things in ways that fusion didnt like, so this time im trying to do things as proper as i can to stop fusion getting annoyed at me.




I then realised mounting rails on the bottom would be wayyy smarter so changed that. 
<img width="998" height="601" alt="image" src="https://github.com/user-attachments/assets/8075db3d-6b44-4262-a55c-fbf9b2f6674b" />

It was much quicker having allready done it once and knowing exactly what i need to use to achive the alignment. That being not the align too, but the constrain component tool.
Last time i tried to make a parametric printer i made the mistake of using the alignt tool a bunch, but i didnt realise that that didnt work well with parametric models.


<img width="1734" height="1040" alt="image" src="https://github.com/user-attachments/assets/76d35a78-d925-45ba-a522-4b33df623c9e" />

im quite pleased with some of the parametric stuff i did to add the right ammount of holes to the rails.

<img width="2164" height="1082" alt="image" src="https://github.com/user-attachments/assets/39898e8b-5d39-439e-97bc-72e819e9c3de"/>
Was there an easier way? Probably.
Did i have fun? yes!

My next task is to try figure out motor, and pulley mounting.

I will probably take inspiration from the Annex K3 for parts of the gantry
<img width="1345" height="1051" alt="image" src="https://github.com/user-attachments/assets/63dc8cae-d287-4995-a8eb-acb58437abfc" />

i loved this method for tensioning the belts, its so elegant and compact 
<img width="749" height="705" alt="image" src="https://github.com/user-attachments/assets/d1bdd392-942c-4d0e-9373-1e92f8af87f8" />


# 21/03/2026 1 hour

You probably cant tell, but when i constrained all of rails, that was done relative to the extrusions, which werent propely constrained. 
So i had to make sure everything was constrained
<img width="1203" height="925" alt="image" src="https://github.com/user-attachments/assets/b2668aa3-34a5-499b-aab7-c264caa66fd4" />


## well, it still wasnt properly constrained oops


i tried moving a carridge, and it was NOT happy
<img width="1728" height="946" alt="image (1)" src="https://github.com/user-attachments/assets/3fca792a-3ab7-45d3-9255-4cbcbb5d88bd" />
so i tried to fix that, which then resulted in 
<img width="1067" height="999" alt="image" src="https://github.com/user-attachments/assets/8ff57477-2e11-4a81-9e27-051501437bc3" />

So i figured, since i should have constrained the frame, THEN the rails, and my rails and frame were both super cooked, I should remove all the constraints on the rails, and re constrain them on the bottom instead of building it all upside down.
Wow the above sentence needed more punctuation.

Anyway YIPEEEEEEEEEEEEEEEEEEEE
<img width="1445" height="781" alt="image" src="https://github.com/user-attachments/assets/65123228-6cfe-4921-8fa7-17cb6ff83e27" />


# 23/03/2026 gantry part 1, 1.5 hour

modelling in anything with gt2 belts is allways interesting, not difficult , it just looks messy 
<img width="837" height="762" alt="image" src="https://github.com/user-attachments/assets/4c983689-3163-4080-ab27-992a2a10c5ac" />


i think ive gotten somewhere with belt mounting, i didnt want to make a 1 for 1 copy of the anex K3 , however this is heavily inspired by it

<img width="759" height="717" alt="image" src="https://github.com/user-attachments/assets/73881704-50af-4041-96c4-986ed2f35a7c" />
<img width="647" height="602" alt="image" src="https://github.com/user-attachments/assets/13c63887-1490-4cd3-a1f1-96b8e0da8e77" />

below is an image of the crossection of the annex k3
<img width="548" height="383" alt="image" src="https://github.com/user-attachments/assets/258a3d78-c412-4bcd-871c-6e1ee51a9326" />

i still need to model in screws on mine, the key difference is that mine is in a bit of a smaller footprint , and also the anex team wrapped the belt arround an m3 bolt, i added a 0.8mm wall thickness hollow cylinder arround a bolt because i feared the bolt cutting into or damaging the belt.

# 23/03/2026 gantry part 2, 2h 

Im currently working on finalising which hardware i use and exactly how i mount the rail.

in the previous entry i was mainly focussing on making sure that everything went perfectly with the belts, this time im making sure everything goes perfectly with the rails, i REALYY need to make sure i grip these rails well.

So i plan on having 6 bolts to hold each rail in
<img width="556" height="367" alt="image" src="https://github.com/user-attachments/assets/3242e76a-8ca3-4f67-8357-9d30b4047da0" />

a little detail i like was making sure that the heat set inserts on the bottom that some of those bolts screw into, are recessed so that they dont stick out and cause a misalignment against the carridge of the linear rail.
<img width="1076" height="946" alt="image" src="https://github.com/user-attachments/assets/e3c756de-a7fa-4710-bbff-99402caadd87" />

8 screws of varying length later and we have a hopefully well screwed together little assembly
<img width="745" height="740" alt="image" src="https://github.com/user-attachments/assets/63dc047f-e258-40fe-b654-fa556ecdfc90" />

a mirror and some constraints later
and we get this!

<img width="1673" height="907" alt="image" src="https://github.com/user-attachments/assets/25509371-bd7d-411a-a7d4-8288755284a7" />



# 25/03/2026 gantry part 3, 3h

im so happy its comming together
<img width="1252" height="938" alt="image" src="https://github.com/user-attachments/assets/2de3e820-9f49-4c57-827c-09da444f947a" />

Some of the things im aiming to achive with the cad are
- have the gantry be parametric, so i could scale it from 120x120 to 350x350 or whatever else i want
- have all the constraints modelled in properly so that you can move it arround in CAD and check for interference issues

part of the reason im actually making it parametric is because im not exactly sure what my travel distances will be, since some area will be lost depending on the size of my toolhead, so i want to be able to compensate for that

<img width="1386" height="936" alt="image" src="https://github.com/user-attachments/assets/ba9e4391-7f00-433f-b07f-75dee35d845a" />

the parametric aspect of the CAD works arround 40% of the time
when it doesnt work re defining a handful of the rigid groups seems fix it which is odd to say the least





# 26/03/2026 5 hours

Trying to speed up the build a lot now

i threw together the mounting for the 625 bearings

i had been delaying this for quite a while because i wasnt sure where i was going to place the lower belt which would throw off everything.

<img width="965" height="676" alt="image" src="https://github.com/user-attachments/assets/41c4e42d-e504-414c-adc0-3180f979d8f8" />

the design wouldnt print the best in one peice , also wouldnt be very easy to use a vice to press fit the bearings

so ive split it into two parts
<img width="1294" height="704" alt="image" src="https://github.com/user-attachments/assets/4375ba53-b467-4ca7-accd-9b488f81c9fb" />
<img width="810" height="689" alt="image" src="https://github.com/user-attachments/assets/0ccfcefd-ee16-48d3-ac19-d02b0c02f867" />

but i also believe alignment of these two parts is quite important , so in addition to the m4 bolts that will hold the halves together there will also be locating features 
<img width="1027" height="822" alt="image" src="https://github.com/user-attachments/assets/68d463c0-7687-4025-a8f9-3ab92b7f05ef" />
<img width="1232" height="889" alt="image" src="https://github.com/user-attachments/assets/89014941-9cc5-4cd5-9b6f-9f6ce605cbf1" />

Ive added 0.2mm of clearance between the locating geometries so hopefully they should fit okay

oh yeah
<img width="1076" height="843" alt="image" src="https://github.com/user-attachments/assets/42e75715-940a-49ea-8384-926116f5f2f2" />
shoutout to autodesk for making custom length bolts a payed feature

i get the mild inconvenince of making my own parametric bolts, which really doesnt take long

It should be able to be copied and used for all the other once since i have "A config" and "B config" which flip which is the idler , and which is the pulley
<img width="934" height="891" alt="image" src="https://github.com/user-attachments/assets/30a03ecb-727b-46ea-a456-5506ea1a6022" />
<img width="762" height="644" alt="image" src="https://github.com/user-attachments/assets/6ff68f8d-cc68-4d39-9411-e01a3acb4fc4" />

spotting this wasnt great
<img width="870" height="955" alt="image" src="https://github.com/user-attachments/assets/16bdc0d9-3674-48b4-ba73-eed562f60db6" />

however couplers like these exist
<img width="1927" height="876" alt="image" src="https://github.com/user-attachments/assets/9e430d2c-4dc5-41c8-b2fc-02e8104fdaa2" />
which mean i dont need to redesign anything which is amazing



<img width="1323" height="1059" alt="image" src="https://github.com/user-attachments/assets/77d8dd44-2303-4e4c-8a0b-15cd79ee27fc" />

Realised i need to rework this as theses are far to close
<img width="1162" height="959" alt="image" src="https://github.com/user-attachments/assets/a4d511f1-b8fe-4185-8465-5d78dd1d053b" />
In the process of fixing the above issue i also discovered the holes for the motor attachment were slightly ofset, meaning i had to remove and readd the motor mounting holes. I am however glad that it was simply the motor mounting holes and not the motor which is aligned with a bunch of other stuff

ah this is a lot of errors
<img width="945" height="924" alt="image" src="https://github.com/user-attachments/assets/aeadb14d-1aac-4404-80f9-8cfb40820360" />

Given the ammount of errors i was getting I decided the best course of action would be to export the completed assemblies, like the ones for the motor / pulley mounting. Then go back to an earlier version of the file without the errors and import the assemblies to get a much cleaner doc,
<img width="1687" height="1026" alt="image" src="https://github.com/user-attachments/assets/c0a194c7-a82c-44cd-b9e6-dcfc1465ee1b" />

i still need to import the rail holders again, but this looks a lot better, and takes way less time to compute when changing perameters


# AHHHH 27/03/2026 6h

lovely how in fusion its shown as <img width="551" height="130" alt="image" src="https://github.com/user-attachments/assets/a353b3d0-2d27-4183-ade3-40085bd145aa" />
but once you dare to look at it
it turns into this AHH
fussssiiioonnnnn 

<img width="2357" height="1079" alt="image" src="https://github.com/user-attachments/assets/6cfbcf9f-e0f8-4926-a7df-792e1ada78f8" />


it appears exporting as a step
and then importing fixes the issues?
im not exactly sure how that works but ok fusion


if we ignore bits of floating here and there its starting to look quite good
<img width="1421" height="1029" alt="image" src="https://github.com/user-attachments/assets/22f98b70-ae70-4ebe-9a47-15d7a6d87c8e" />

time to fix the floaties

Screws first
<img width="1202" height="969" alt="image" src="https://github.com/user-attachments/assets/ca2d1893-1099-427c-8825-874b5f007ba0" />


i could have just made a block, and i did
but i felt like doing something a little fun just because ive been doing CAD for 6 hours straight at this point
<img width="1185" height="728" alt="image" src="https://github.com/user-attachments/assets/a3436d73-d60d-45da-8a14-0e7c2e78b5a2" />
i know infil could have reduced the weight, but i just like hexagons

wow this is definetly comming together quickly now
<img width="1693" height="938" alt="image" src="https://github.com/user-attachments/assets/4e86d047-c066-48f5-b682-b0f6ecf486ec" />

sumarry of what ive done so far today
- made progress on a bunch of stuff
- broken a bunch of stuff


To elaborate what i meant when i said breaking a bunch of stuff, i managed to create circular dependancies, amongst other unpleasant things, which resulted in the file breaking or crashing any time i attempted to change the perameters of the frame.

So my solution to that was to once again export the completed assemblies as step files
and then make a new file to recombine them all into again
which fixed the issue


in the image below you can see me trying to make sketches to work out roughly where i was allowed to with my hotend without it coliding with the frame
<img width="721" height="572" alt="image" src="https://github.com/user-attachments/assets/9db950be-c84f-4d92-bc5f-7da6cbfbd60a" />
i could then export that sketch into the file where i was building my hotend


<img width="1844" height="1360" alt="image" src="https://github.com/user-attachments/assets/2bcd4a1a-86cb-4bb5-a045-d48830b5b0c8" />


modelling in no go zones so i can rearrange things with more awareness for how it interacts with the frame
<img width="1092" height="764" alt="image" src="https://github.com/user-attachments/assets/d030c659-6486-4a13-aa8d-e26fb2512f74" />




<img width="714" height="484" alt="image" src="https://github.com/user-attachments/assets/c42c97f0-7662-4f44-90a8-6d6996bffae3" />
<img width="758" height="460" alt="image" src="https://github.com/user-attachments/assets/53636fc6-0c71-4d22-89ee-92d444264940" />
<img width="846" height="620" alt="image" src="https://github.com/user-attachments/assets/1746c072-44a3-4684-a6c3-b8439fa5416a" />

might just be the worst looking duct ive ever made, or ever seen
but if it cools, it cools


i can prob use aux cooling if i really need

It needs to be at an angle because its a belted printer

i was also really limited on the fan placement because of the gantry
soo there is probably a far better way to do it

# 28/03/2026 5 hours

Modelling the no go zones REALLYY helped me work out how to arange things.

ive tried to design the printed parts so that they are easy to print since the last printer i designed had some rather akward and support needing parts.
<img width="985" height="680" alt="image" src="https://github.com/user-attachments/assets/31d7da99-ff49-4499-9aba-6fb35cbf704f" />
<img width="1569" height="905" alt="image" src="https://github.com/user-attachments/assets/859c4a77-5dc3-4aaf-b4ef-53357eb77fa7" />
<img width="1228" height="961" alt="image" src="https://github.com/user-attachments/assets/3bfbd575-7cda-43d8-8da3-40e0a3d872bb" />

hopefully its not awful to print


Anddd i think thats the hotend
<img width="2561" height="1156" alt="hotend r1" src="https://github.com/user-attachments/assets/da2f4dc8-c3d9-4228-819b-fc59252b215f" />
<img width="2561" height="1156" alt="hotend r2" src="https://github.com/user-attachments/assets/dc099763-485d-4706-bfc4-770f6a82320f" />
<img width="2561" height="1156" alt="hotend r3" src="https://github.com/user-attachments/assets/8905f7c7-a49a-4e95-ba4f-ed3ba8bacfc6" />
<img width="2561" height="1156" alt="hotend r4" src="https://github.com/user-attachments/assets/c966f1bb-bbd3-4015-8314-65be0e8a839c" />
<img width="2561" height="1156" alt="hotend r5" src="https://github.com/user-attachments/assets/a0003a75-fa42-4dab-997f-6a7c29682667" />

the hotend took me a bit longer that i expected, but hopefully it should all join together well when i bring it back into the other file

 # 29/03/2025 1h

stuff is all comming together now, well, we can ingore the parts that spontaneously broke
 <img width="1491" height="943" alt="image" src="https://github.com/user-attachments/assets/beedd2c5-cfde-417f-8372-952d0f944878" />


 now its fixed i can check if my clearances are working out ok, if i did everything right the carridges should hit the end before anything on the hotend colides with the frame
 this one looks good
 <img width="913" height="796" alt="image" src="https://github.com/user-attachments/assets/467e925c-e59b-4a0b-b348-67794b6e8ea2" />

this one doesnt look like a pass
<img width="579" height="664" alt="image" src="https://github.com/user-attachments/assets/ececb5f1-788f-4ee0-9f13-34a90a74744d" />
however
<img width="1255" height="863" alt="image" src="https://github.com/user-attachments/assets/614a8cf9-520e-4e48-a5d4-2686df30cd8e" />
<img width="1447" height="937" alt="image" src="https://github.com/user-attachments/assets/7e9bb310-5d33-4b04-b5c8-d6279f57da27" />
its a pass

this corner is not the best at all
<img width="668" height="618" alt="image" src="https://github.com/user-attachments/assets/f71234d0-20ac-4fcf-8356-bfb6d2dec274" />

then this corner is ok
<img width="642" height="525" alt="image" src="https://github.com/user-attachments/assets/c51f74f3-7c1a-46e4-941a-11c2a31c2192" />


overall i dont think i did a bad job

the moment of truth now is working out if i can change parameters without it breaking or crashing

it did it without crashing however it broke in some places again
<img width="458" height="425" alt="image" src="https://github.com/user-attachments/assets/ab128d76-26fe-4888-a79e-967b2661b0b1" />

an export an import later and i think its fixed



Some things i did on my hotend that i forgot to mention earlier

the first is im going to need to remove or use a hacksaw to make this tube shorter
<img width="697" height="694" alt="image" src="https://github.com/user-attachments/assets/a29f1bf3-5059-4db4-9046-203fa1897d72" />

the second is i plan on using superglue to help secure the 4020 fan
i didnt believe the two screws one above the other would sufficiently secure the fan, so i added little spur to the side which i could use superglue, or double sided tape, or PVA etc
<img width="1773" height="1658" alt="image" src="https://github.com/user-attachments/assets/8bfd7b83-e133-45ce-8a98-eb1af519b2a1" />
<img width="973" height="870" alt="image" src="https://github.com/user-attachments/assets/931c936e-0db5-4d80-8023-089613b3e196" />

my plan for the duct at the moment is also just tape, i believe once i have the parts i will need to iterate on that in significant ways
<img width="1556" height="1130" alt="image" src="https://github.com/user-attachments/assets/184f3ea8-e674-4449-8b4d-a8d5d203f988" />



Here are some renders of what its like now
<img width="3840" height="1782" alt="main r4" src="https://github.com/user-attachments/assets/a34f5c3f-0d6e-479a-be48-f45726c10781" />
<img width="2561" height="1156" alt="first render of it" src="https://github.com/user-attachments/assets/0456429e-a582-4b1f-a7bb-ed116dba24dd" />


# 29/03/2026 working on the bed/belt assembly, 3 hours

started working on belt assembly again

<img width="1637" height="778" alt="image" src="https://github.com/user-attachments/assets/2a0a5217-c221-4572-b982-5563e5388da6" />
<img width="1631" height="725" alt="image" src="https://github.com/user-attachments/assets/fb24d717-68c3-41de-858d-e40d37987cfe" />
<img width="1467" height="768" alt="image" src="https://github.com/user-attachments/assets/5f99c5b5-de4b-4f87-800e-6925aa4af4e7" />
<img width="1731" height="883" alt="image" src="https://github.com/user-attachments/assets/691a91bc-2c4c-4875-b910-b48dbe857b74" />
<img width="1751" height="953" alt="image" src="https://github.com/user-attachments/assets/9a4f4e72-f51a-411f-ba0e-cc82ad8afd3f" />
<img width="736" height="957" alt="image" src="https://github.com/user-attachments/assets/579115b7-b317-4be4-86a0-2dc7115f2cfd" />
<img width="1635" height="788" alt="image" src="https://github.com/user-attachments/assets/ed5aad72-2ee8-429a-ba7c-b8ffaab3453a" />
<img width="1568" height="819" alt="image" src="https://github.com/user-attachments/assets/1388ae53-f059-4418-bc4d-26bdd4560001" />

<img width="941" height="906" alt="image" src="https://github.com/user-attachments/assets/cad6b023-e86c-42f4-a5c7-bb2463705350" />
using those mesurements i can find the perimeter to be

93+93+ (( (360-153)/360) x 57 x pi) + ((153/360) x 12.8 x pi)

which evaluates to be 306mm
so my minimum belt length is 306mm , and therefore my max should be arround 318mm




back to the rollers
i could have left them as plain cylinders, however that feels rather boring

<img width="1218" height="721" alt="image" src="https://github.com/user-attachments/assets/b9400508-5d62-4ac7-8e0f-421cebdcc334" />

for the sillies i also decided that the spoke count, width and radii for the chamfers should be parametric

<img width="849" height="153" alt="image" src="https://github.com/user-attachments/assets/b68b6458-730a-4bd3-944a-ae4734edaaf9" />

so putting all of that together we get this
<img width="2561" height="1156" alt="bed assebmyl current state" src="https://github.com/user-attachments/assets/6211fca1-9fe9-4a8a-8a7a-a94e2780dc62" />

# 2/03/2026 belt time

Im aiming to design some sort of mechanism between the two flats that push against each other to acomplish bed tensioning
<img width="1596" height="852" alt="image" src="https://github.com/user-attachments/assets/0294c213-d4ed-44b9-b5be-bc865beec27e" />

more refinement
<img width="1738" height="991" alt="image" src="https://github.com/user-attachments/assets/bea6fb44-3143-48be-a3b4-1b1e80c31947" />

ive treally tried to keep these parts printable so far
<img width="1564" height="842" alt="image" src="https://github.com/user-attachments/assets/c5a067d1-08c0-415f-8ee6-5588f767541c" />
<img width="1832" height="653" alt="image" src="https://github.com/user-attachments/assets/63b2f756-7449-47d7-a3c7-167c2a100f34" />

im a bit scared of the shafts wiggling out of the bearings
<img width="884" height="878" alt="image" src="https://github.com/user-attachments/assets/0d661260-3478-43e4-98b5-1f92985caa41" />

this with a screw could be a solution, especially since it would add a splash of colour
<img width="1306" height="920" alt="image" src="https://github.com/user-attachments/assets/a2402d7b-eeab-4c87-b6ad-18304403e19d" />
<img width="2561" height="1156" alt="lil render whatever" src="https://github.com/user-attachments/assets/c63aa176-72a4-4def-a097-34b87937886e" />


