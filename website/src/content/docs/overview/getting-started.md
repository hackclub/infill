---
title: General outline
description: how to get started
---

Welcome to infill! In-_fill_ the gaps you see in 3D printing with your own printer design. I'm more or less modelling this based on my experience building [Neutrino](https://theopenary.com/neutrino), which is a compact, portable 3D printer I designed _from scratch_ for under $250 USD.

**Here's how to get started:**

---

### 1. Setup

Before you start designing, you need to do a couple of steps:

**1. Join the #infill channel on the slack**
If you're not already in it, go back to the front page and enter your email. You'll get an invite

**2. Set up your repository for your printer**

Create a repository for your printer! You can use any git provider, but most people use GitHub.

In this repository, create a file called JOURNAL.md - this will be where you keep track of your progress! Every single time you work on your printer, you should quickly jot down what you did and total hours spent. The top of the file MUST include the following info:

```markdown
Made by: @dari // alexren
Repository link: https://github.com/qcoral/infinite-benchy-theorem
Total hours so far: 7

- [x] I have a 3D printer or will be getting one before March 21st
```

**3. Add your journal to the website**

Head on over to the [config.yaml file](https://github.com/hackclub/infill/blob/main/doc_update_script/config_v2.yaml) in the repo and add your printer! It should follow this format:

```yaml
Your Printer Name:
    title: "Your Printer Name"
    description: "Your Printer Description"
    repository: "https://raw.githubusercontent.com/user/repository_name/refs/heads/main/JOURNAL.md"
    file_name: your_printer_name.md
```

After that, you're done! Now you can move on to actually designing

### 2. Start designing your printer!

Come up with a 3D printer design! If you already have an idea in mind, great! If you don't, here's a couple prompts:

- Solve one thing you've always hated in 90% of 3D printers you've seen
- 3D print a new material
- Add a feature that you've always wanted (i.e 4-axis 3D printing, a conveyor belt, etc)
- Just make something that works a little bit better than what you already have! Nothing wrong with only making a small improvement.

For Neutrino, I wanted to do a couple things:

1. Make a 3D printer that fits inside a filament box. I thought it was cool as hell.
2. Design it so that it can be built with ENTIRELY off-the-shelf components. no CNC or laser machines required
3. Have it be affordable. As many people as possible should be able to have that experience/

It'll be different for every printer, but hopefully that gives an idea!

Once you have that sorted - get away to planning, 3D modelling, PCB designing, etc. Draw sketches. Post in #infill often! We're all in this together

(Btw: You DON'T have to design all the electronics, but I ask you design at least ONE pcb for a function of your choosing. Whether that be a display, a toolhead PCB or sometihng else!)

### 3. You submit your design!

Submit a BOM in CSV format, complete with links of what you need to get.

On top of the BOM, you'll need the following to get funded:

- a CAD model of your entire printer!
- an overall planning document of what it's going to do and how it's going to fit together

If approved, you'll get an HCB Card grant of **$350 USD** for you to spend on your printer. Now's the time to buy your parts!

### 4. Build the printer and tune it

Once the parts arrive after 2-3 weeks, now it's time to build it!

It's not going to work the first try. It's going to suck. That's where the tuning comes in. Keep tuning and iterating on your design until you have a printer that works well. Eventually, a somewhat high quality benchy should pop out! That's when you know you're ready.

### 5. Submit your print. Get flown to RMRRF.

Submit your printer. I'll hop on a call and verify you have a good machine. After that, pack up! We're heading over to Colorado.

---

Hopefully that covers everything - let me know if there's something you want added!
