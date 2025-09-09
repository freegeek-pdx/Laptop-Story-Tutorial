# Script of Laptop Story - A Tutorial on How to Refurbish and QA Test Laptops the Free Geek Way

#
# Tutorial game created by Raul Betancourt
#
# MIT License
#
# Copyright (c) 2025 Free Geek
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

define g = Character("Spirit of Free Geek", color="#975ebd")
define r = Character("Sticky the RAM Stick", color="#009900")

image bg matrix = "matrix.png"
image bg laptopcloset = "laptopcloset.jpg"
image bg refurbdesk = "refurbdesk.jpg"
image bg typingdesk = "typingdesk.png"
image bg printershelf = "printershelf.jpg"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg matrix

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show geek at top

    # These display lines of dialogue.

    g "Welcome to Free Geek's refurb department!"

    g "I am the Spirit of Free Geek...the ghost in this geeky machine!"
    g "And this is my assistant, Sticky the RAM stick!"

    show sticky-small at left

    r "I AM STICKY."
    r "VERY STICKY."

    g "Yes, the laptop components that come in here are frequently sticky."
    g "Anyway, thank you for sitting down to watch this tutorial! Both you and Sticky will be the students today, and you will be learning how to refurbish a laptop the Free Geek way!"
    g "Hopefully this will be slightly more interesting than reading documentation."

    r "And hopefully it will stay in our MEMORY easier! Tee-hee!"

    g "Are you ready? Come with me...on a journey..."

    r "A journeeeeyyyyyy..."

    scene bg laptopcloset
    show geek at top

    g "Welcome to the Laptops closet. This is where we will start our tour."

    g "It is generally here in the closet where you will grab a laptop to refurbish!"
    g "They will either be in a bin or on the shelf. A regular supply of 'cleared' laptops (laptops that have had their drives removed) will magically spawn here."
    
    show sticky-small at left
    r "I'm also in the closet!"

    hide geek at top

    show closet-hardware-shelf at top

    g "That's right. You'll find RAM and other hardware components on this shelf."

    hide closet-hardware-shelf at top
    show closet-memory-area at top

    g "These bins right here hold spare RAM that you can use, categorized by their various types, speeds, and capacity."

    g "You may not need to grab memory from this area every time, though. Many of the laptops already have RAM in them when you get them, but not all."
    
    hide closet-memory-area at top
    show geek at top
    
    g "So pro tip: If a laptop is not turning on and you know it has power, make sure it's not missing RAM!"

    r "I'm an essential worker!"

    g "Sure, sure."
    g "More importantly, you will also get your freshly wiped SSD drives here, which will be the storage for your newly refurbished laptops!"

    show ssd at right
    hide geek at top
    show geek-surprised at top

    g "Ah! Who's that?"

    show sticky-small at left

    r "It's my friend Matilda the m.2 drive, you silly!"

    hide geek-surprised at top
    hide sticky-small at left

    show closet-hardware-shelf at top

    g "Oh right! Well, while we're on this topic, you should know: SSD drives in the closet will come in two form factors."

    show mdot2-bin at top

    g "Matilda is in m.2 format, which can be found on this shelf. M.2 interfaces are keyed and come in two types: 1) B+M format, which has two notches and 2) M format, which has one notch."
    g "As you can see, Matilda uses the M style of m.2 key."

    hide mdot2-bin at top
    show 2point5bin at top
    
    g "We also have 2.5-inch SATA drives, which can be found here and are quite a bit larger."

    hide ssd at right
    show ssd2 at right
    "2.5-inch SATA" "Hello."

    g "Ah!"

    hide 2point5bin at top
    show ssd-in-bin at top

    g "Um, ok. Well, the important thing to remember is just that different laptops may take different drives, which we will see in more detail when we open one up."
    
    hide ssd-in-bin at top
    show geek at top
    show sticky-small at left
    hide ssd2 at right
    show ssd at right
    
    g "For now, let's grab the m.2 drive, since it is more common these days and most of the laptops we get will take them."   
    g "Either way, we will be installing the end user's OS (operating system) on it so that they can use their new computer!"

    r "What OS do we install? Linux or...the other one that no one uses? I forget what it's called. Starts with a W."

    g "Glad you asked, Sticky! We'll get to that part over on our desk in the refurb area! Let's go!"

    scene bg refurbdesk

    show geek at top
    show sticky-small at left

    g "Once you have grabbed your laptop and drive, now you can make the magic happen!"

    r "Magic!"

    g "And like any magic, we need the 💫✨energy of the cosmos✨💫 to make it happen!"

    r "Oh, where do we get this mystical energy?"

    g "From the power outlet of course!"

    hide geek at top
    hide sticky-small at left
    show power-adapter at top

    g "I'm talking about ⚡electricity⚡! Every computer needs a power supply, and in the case of our laptops that is a power adapter that looks like this!"

    hide power-adapter at top
    show power-adapter2 at top

    g "It can also look like this!"

    hide power-adapter2 at top
    show power-adapter3 at top
    
    g "...Or like this!"

    hide power-adapter3 at top
    show power-adapter-collection at top
    
    g "There are countless types of power adapters, and each model of laptop has its specific power needs."


    r "Oh my, how will we know which adapter to use from that rat's nest?"
    g "Don't worry, Sticky, everything is properly labeled on the adapter shelves and luckily many models of the same brand will use the same adapter."
    g "But when searching for an adapter, here is what you should do: "
    g "1) Look in the bin that corresponds to your laptop brand for an adapter with a connector style that fits your laptop. If it does not slide in easily, then it is the wrong type!"
    g "2) Check that the adapter has the correct voltage AND current (amps) that matches the requirements of the laptop."

    hide power-adapter-collection at top
    show power-adapter-closeup at top

    g "This is what this info looks like on many Dell chargers."

    hide power-adapter-closeup at top
    show laptop-back-info-arrow at top

    g "You can usually find the laptop's power requirements right on the bottom. It varies, but will usually be included in a printed blurb with its serial number and manufacturing information."

    hide laptop-back-info-arrow at top
    show geek at right
    show sticky-small at left

    g "Keep this in mind as an IMPORTANT NOTE: The voltage of the adapter must ALWAYS match the voltage required by the laptop."
    g "For example, if the laptop indicates that it needs 19.5 volts, you must supply exactly this! However, when it comes to the amps, there is a little more wiggle room..."
    g "As long as the adapter is supplying MORE amps than the laptop needs, it will be fine!"
    g "For example, if the laptop says it wants 19.5 volts with 3.34 amps, and you only have an adapter that will supply 19.5 volts with 4.62 amps, you can go ahead and use that."
    g "Laptops nowadays are good at drawing the exact current they need, as long as they have enough. This is especially true with USB-C chargers, which fit a wide range of laptops and are becoming more popular!"
    g "3) Last but not least, check for damage on the adapter before using it. If it has any visible damage, it will need to be recycled, since we can't give it to the user."

    r "Ok, great! Are we ready to plug the power adapter into the laptop and see the magic happen?"
    g "Not quite, Sticky! First, we're going to check out the inside of the laptop, and it should ALWAYS be unplugged and powered down when we do this!"

    show laptop-back at top

    g "When you first set your laptop down, you will notice it usually has a bottom panel. This is what we're going to unscrew and remove to access the laptop's inner components."
    g "Many times the screws will already be loosened for you, so it should be easy to open."

    r "I have a screw loose!"

    g "RAM sticks like you don't use screws, Sticky. -_-"
    g "But you know what does need a screw to stay in place? Our m.2 drive!"

    hide laptop-back at top
    show laptop-open at top

    r "Yay!"

    show laptop-open-arrow2 at top
    g "Before we start working, let's unplug the battery cable from the motherboard. This will protect the components from any discharges and keep the laptop from accidentally turning on."
    hide laptop-open-arrow2 at top
    show laptop-open at top
    g "We can also have a quick look and make sure the inside of the laptop isn't super gross."
    g "If it is, then we can blow out the dust bunnies with canned air or take the laptop to the dusting hood--which is kind of like a desk with a vacuum built in."
    hide laptop-open at top
    show dust-hood-desk at top
    g "It looks like this!"
    hide dust-hood-desk at top
    show laptop-open at top
    g "Now that the laptop is open and we're done checking everything out, we can look for the m.2 socket..."
    hide laptop-open at top

    show laptop-open-arrow at top

    g "Which is right here on this model!"
    g "Keep in mind that the location varies from model to model."
    g "Ask a technician to show you a few different examples if you are unsure, but it will be a keyed slot where you can insert the drive on one end, with a post to screw the drive in on the other end."

    hide laptop-open-arrow at top
    show m2-closeup at top

    g "Now we can insert our drive into the socket like so."

    hide m2-closeup at top
    show m2-closeup-2 at top

    g "Then we simply screw it in place and are good to go!"

    hide m2-closeup-2 at top
    hide geek at right
    show geek at top
    show sticky-small at left

    r "Wow, so easy!"

    g "In most cases, yes! But there are some things to consider..."
    g "On older laptops, there may be no m.2 interface, and you will find the older SATA ports that take 2.5-inch drives."
    g "Others will give you the option for both. Since we do keep both types of drives in the closet, take your pick based on available supply!"

    g "Once the drive is inside and everything looks good, go ahead and close the laptop up."

    r "No more loose screws!"

    g "Actually, that reminds me of a tip: Keep your screws loose until you have finished testing the laptop! This will save you time in case you need to open it back up to adjust anything!"

    r "Like what?"

    g "Oh, lots of different issues can arise during testing. That's why we test, Sticky! These are used machines, after all."
    g "But we will get into the troubleshooting process later."

    r "I love trouble!"

    g "I'm sure you do."
    g "Anyway, after you have placed the drive in the slot, re-connected the battery cable to the motherboard, and closed the laptop up, it is time to turn the laptop over and power it on!"
    g "From here, we will need to take a look at the UEFI Setup."

    r "What's that?"

    g "Also frequently called a BIOS Setup (though that term is outdated), it is a very basic utility that you can access to fiddle with the laptop's most low-level settings before you even install an OS."
    g "You can change things like which drive the laptop should boot from, what security features are enabled, and even the date and time that the laptop is set to. We'll need to adjust a few of these settings before we install anything."

    r "Oh, ok!"

    hide geek at top
    show drive-missing-screen at top

    r "How do you get to the BIOS setup menu? I tried to turn this computer on and it just beeped and complained that there was no bootable drive!"

    show geek at top
    hide drive-missing-screen at top

    g "To get to the BIOS setup screen, you will usually need to tap a function key. Which key that is depends on the make and model of the laptop, but here is a quick reference as a rule of thumb:"
    g "On Dell computers, it is usually F2. On Lenovo computers, it is usually F1, and on HP computers, it is usually F10. Occasionally, other keys like ESC will also work."
    g "For other brands--and sometimes even within these brands--it can be a little random. Sometimes the logo screen when you first turn on the laptop will tell you what key to press."
    g "If you are unsure and can't find documentation, it is no big deal. You can keep trying keys until it works. Nothing will break."
    r "Trial and error!"
    g "That's right! Just keep in mind that often you have to get the timing just right. Since you only have a few seconds to mash the key, start pressing it as soon as you turn it on."

    r "Great, it's working now! What do I do with it?"

    g "Well, let's take a look at our BIOS setup a bit more deeply."

    hide geek at top
    hide sticky-small at top

    show bios-screen-1 at top

    g "This right here is a fairly typical BIOS/UEFI setup screen for a Dell laptop."

    hide bios-screen-1 at top
    show bios-screen-2 at top

    g "This one here is an older style interface, but it is also fairly common, especially on Dell laptops with gen 8 and older intel CPUs."
    g "Notice also that on this particular machine, the BIOS setup is actually locked with an admin password. You can see the little lock towards the bottom left that shows this."
    g "When a laptop is BIOS-locked, this means that some or all of the settings are not accessible to be changed, unless you happen to know the password."
    g "Sometimes the organization that gave us the machine will provide us with this password to clear it ourselves, but usually that is not the case."

    hide bios-screen-2 at top

    show geek at top
    show sticky-small at left

    r "Oh no! Does that mean we can't refurbish the laptop?"
    g "It depends. On some machines, the lock will not affect settings that are essential for booting, and so we will still be able to boot and test the machine."
    g "In that case, we can proceed normally and simply mention in the testing notes that the machine is BIOS-locked."
    g "In other words, we can still sell the machine or give it away, as long as it is communicated to the end user that these settings cannot be changed!"
    
    r "Ok great! What if the lock makes it so we can't change the boot settings?"
    
    g "Well, unless the default settings allow us to boot the machine from our external drive (more on that later)--or we find some sort of workaround--then we won't be able to refurbish the machine."

    r ":("
    g ":("

    g "Luckily, this doesn't happen that often! Most laptops come to us with the BIOS password already cleared."

    hide geek at top
    hide sticky-small at left

    show bios-screen-1 at top

    g "Since that is the case for this newer machine, we will proceed with this one!"
    g "But first, a little quiz!"

    g "Which of these is a sign that there is no RAM in a laptop?"
    menu:
        "A. The laptop will show the BIOS setup screen, but will not boot to an OS.":
            g "Nope! The answer was B. The laptop will not show anything on the screen, typically."
        "B. The laptop will not show anything on the screen at all, even if you turn it on.":
            g "Yay! That is correct!"
        "C. The laptop will boot with a common virus called Microsoft Windows":
            "You" "Why use Windows, when Linux opens doors?"
            g "Sorry, the answer was B! The laptop will not show anything on the screen."
            g "But you are right that Linux opens doors. That's why we use Linux Mint here!"
    
    g "All right, let's move on! Before anything else, we will need to change the settings in the BIOS setup utility!"
    g "Here at Free Geek, we set a few flags in the setup beforehand to make it easier to install our OS."
    g "Click on each item in the following menu to learn about it or click 'I think I get it' when you are done!"

    hide bios-screen-1 at top

    label biosMenu:
        menu:
            "1. Check Date and Time":
                show bios-date at top
                show geek at right
                show sticky-small at left
                g "The first thing we will take a look at is the date and time settings of the machine."
                g "Ideally both of these are correct! Sometimes, they are a little off, like for example if the machine came from a different time zone. If this is the case, then just change it to the correct local time and move on."
                g "If the time is waaaay off, though--for example, it is showing a date from five years ago--then it is likely that the laptop's date has reset to the time it was made."
                r "What does that mean?"
                g "It means that the CMOS battery probably needs to be replaced! This is the battery that helps keep the correct time, even if the computer is powered off and out of charge."
                g "Not all laptops have these, and increasingly, consumer-grade machines will simply use their rechargeable battery to keep the time. Most of the laptops that come into Free Geek still have a CMOS battery, though."
                g "If the CMOS battery is not working correctly, you can either replace it or you can note that it needs replacement in the system notes."
                r "Ah, so it can become the user's problem instead!"
                g "Right! Eh, I mean--no! It's actually not a huge problem and the time will remain correct in most cases as long as the laptop doesn't run completely out of charge."
                g "But, it is still important to note anything unusual that we haven't fixed to the end user, so we put it in the system notes!"
                hide bios-date at top
                hide geek at right
                hide sticky-small at left
                jump biosMenu
            "2. Reset BIOS/UEFI Defaults and Reboot":
                show bios-screen-1 at top
                show geek at right
                show sticky-small at left
                g "Since we don't know what state the settings are in from the last user, we're going to want to set the BIOS/UEFI back to its defaults before messing with them."
                g "Like most settings, changing the defaults with vary by brand, and you may need to hunt around for it, but once you do you will need to reboot (if the computer doesn't do so automatically)."
                hide bios-screen-1 at top
                show bios-defaults at top
                g "In this example, the button to change the BIOS defaults is at the bottom left of the screen with no need to search the menus for it. This is common on Dell computers."
                hide bios-defaults at top
                hide geek at right
                hide sticky-small at left
                jump biosMenu
            "3. Disable Secure Boot Mode":
                show secure-boot at top
                show geek at right
                show sticky-small at left
                g "Ok, let's look under the Boot Configuration heading and make sure that secure boot is turned OFF."
                r "What's that?"
                g "It's a setting that restricts which sources the laptop can boot from. We disable this beforehand because it can get in the way when we want to install our new OS!"
                r "Oh, like it might not let us boot the OS from an external drive?"
                g "Exactly! Different makes and models of laptops will have different default restrictions that come with Secure Boot."
                g "Sometimes you can boot from a USB drive just fine even with Secure Boot enabled, but it's best to avoid any shenanigans by just turning it off."
                g "You might have to hunt around in the BIOS utility to find this setting, too. On our example machine, it is under Boot Configuration, but it varies depending on make and model."
                hide secure-boot at top
                hide geek at right
                hide sticky-small at left
                jump biosMenu
            "4. Enable AHCI/NVMe Mode":
                show ahci-mode at top
                show geek at right
                show sticky-small at left
                g "Let's take a look at the SATA/NVMe Operation Settings now. In our example, you can find it in the Storage section, but it will vary by the brand of BIOS setup utility, so you might have to hunt for it."
                g "This is a setting that will tell the laptop what type of drive it will be using for its long-term storage and what 'mode' it should be in."
                g "Usually you will have two options: AHCI/NVMe mode and RAID mode. Make sure AHCI/NVMe mode is selected. This tells the laptop that it will be an SSD that is treated normally, as a single drive. Often, this mode will already be selected by default."
                hide ahci-mode at top
                hide geek at right
                hide sticky-small at left
                jump biosMenu
            "5. Disable Security Tracking":
                show absolute-screen at top
                show geek-tinfoil at right
                show sticky-small at left
                g "Finally, a lot of the laptops we get are from corporate or government entities, so sometimes Big Brother likes to watch where the laptop went with tracking software like Absolute or Computrace as an anti-theft measure!"
                r "Oh no!"
                g "Don't worry, this is usually easy to disable--unless the laptop is BIOS-locked with an admin password. Assuming you have the clear to fix the settings, you can usually just toggle a switch."
                g "In our example here, you can disable Absolute in the Security section."
                hide absolute-screen at top
                hide geek-tinfoil at right
                hide sticky-small at left
                jump biosMenu
            "Ok. I think I get it.":
                show bios-exit at top
                show geek at right
                show sticky-small at left
                g "Great, now that all our BIOS utilities settings are where we want them, we can hit the EXIT button."
                hide bios-exit at top
                show bios-exit-2 at top
                g "At this point, you will usually be asked if you want to save your new settings. Say yes and the laptop should now reboot on its own!"
                hide bios-exit-2 at top
                hide geek at right
                show geek at top
    
    
    g "Let's move on and get the testing process started!"
    g "We'll first need to get a special external drive to boot from our testing environment!"
    r "Oh yeah! I booted from a USB thumb drive once to install the OS on my gaming PC."
    g "Great! If you are already familiar with booting from a USB drive, this process won't seem too different. It is the same idea, except we will be using an SSD housed in an external enclosure."

    hide geek at top
    hide sticky-small at left
    show usb-dongles at top

    g "First, grab yourself a drive with a dongle. You can find it dongling from the same shelf as the printer in the refurb room."
    r "Oh golly gee whiz, there are so many drives in there! How will I know which one to take?"

    hide usb-dongles at top
    show geek at top
    show sticky-small at left

    g "Don't worry! The drives are each marked with a unique letter for identification, but it doesn't matter which you grab. Each one is equally capable of installing both Linux or Windows--which reminds me..."
   
    hide geek at top
    show geek-shadowed at top
   
    g "You're going to have to make an imporant choice soon, Sticky."
    r "!"
    r "Uhhh...what's that?"
    g "You're going to have to choose which OS to install on our laptop: Linux, or...the other one. You know the one."
    r "Wait, what? Why do I have to be the one to decide?"
    g "Make the right choice, Sticky: Do you want to become a hapless cog in the vast corporate machine that has become our commercialized society? Or, for the rest of this tutorial..."
    
    hide geek-shadowed at top
    show geek at top

    g "...do you want to work with Linux?"
    r "Uhhh, well, I...."
    show geek at top:
        ease .5 zoom 1.5
    g "What'll it be, Sticky?"
    show geek at top:
        ease .5 zoom 2.0
    r "......."
    show geek at top:
        ease .5 zoom 2.5
    r "............................"
    r "Oh...uh, I think I'll go with Linux for now! Heh. Eheh."
    hide geek
    show geek-pleased at top
    g "Good choice!"
    show tux at right
    g "Most of the laptops we will be refurbishing will be imaged with Linux Mint. This is because Linux Mint is a free and open source operating system, so we don't have to worry about things like licensing!"
    r "So it saves money?"
    hide geek-pleased at top
    show geek at top
    g "Yes, that is indeed a factor! But there is more to it. With free and open source software, we have a lot of flexibility to modify the software and tools to suit our needs. This is not so with most commercial operating systems."
    g "Occasionally, Free Geek will need to image devices with closed-source, proprietary operating systems. This happens if we have a contract with an organization that requires it, for example."
    g "Sometimes employees or community members that go to our classes may also need a laptop with a more popular commercial OS on it."
    g "All in all, the process of putting the OS image on our laptop is similar regardless of the OS we use. For this tutorial, we will go the Linux Mint route, since this is what you will be doing the most."
    r "Ok, got it! What do we do next after we get our external boot drive?"
    hide tux at right
    hide geek at top
    hide sticky-small at left
    show usbc-port at top
    g "Now we can connect the drive to any of the free USB-C ports on our laptop!"
    r "What if there is no USB-C port, though? Or what if the only USB-C port is being used to charge the laptop? Oh my goodness, what do we do???"
    hide usbc-port at top
    show usb-dongle-cap at top
    g "That's no problem, Sticky. If the laptop doesn't have any USB-C ports or it can't boot from them, then you can place the cap on the end of the cable in order to create..."

    hide usb-dongle-cap at top
    show usb-dongle-cap2 at top

    g "A USB-A interface! Plug this into any of the USB-A ports on the laptop."

    hide usb-dongle-cap2 at top

    show geek at top
    show sticky-small at left

    g "Once we have connected the drive and turned the machine on, the next thing we might have to do is point the laptop in the right direction!"
    g "Usually, the laptop will know to boot from the USB drive without prompting, but it doesn't always go according to plan."
    g "It will scan for a bootable drive from a list of possible boot sources and boot from the first one it finds. This is called the 'boot order,' which can be changed in the BIOS setup."
    g "For example, maybe it checks the USB ports first, then looks for a SATA drive, then tries PXE (network boot)."
    g "If the USB drive is not at the top of the boot priority, the laptop may try to boot from somewhere else if it finds a connection, or it can get distracted trying to run diagnostic tools."
    r "Oh, I see. Well, what do we do about that?"
    g "One way is to change the boot order settings in the BIOS, but that is not usually necessary. Instead, we can go directly to a boot menu and manually tell the laptop to boot from the USB drive."
    r "How do we get to the boot menu?"
    g "Similar to getting into the BIOS/UEFI settings, you can access the boot menu by powering the laptop on and then tapping a function key."
    g "The exact key depends on the brand. Look for text on the logo screen that might tell you, but here are some rules of thumb:"
    g "Dell and Lenovo usually use F12, and HP usually uses F9 to access the boot menu. Some others brands will use F1, F2, or ESC. When in doubt, use trial and error, or look it up!"

    hide geek at top
    hide sticky-small at left
    show boot-menu at top
    r "Ok, F12 seems to have worked for this Dell. I'm at the boot menu now. Seems like it is a list of boot sources, like you said. Oh, and look, it even mentions at the top that secure boot is off!"
    g "That's right, you can get all this info from the boot menu if you are ever unsure."
    r "But what do we do now that we're here?"
    g "Since we're trying to boot from the USB drive for now, look through the options and find the one that lists your USB drive. The exact name will vary depending on brand..."
    g "...but it will usually have the term 'USB' in the option and may mention the drive's capacity, brand, and other stats."
    g "In this case you can see the USB drive listed simply as USB: UEFI. It is selected already in this example. All you have to do is choose it with the cursor arrows and hit ENTER."
    
    hide boot-menu at top
    show geek at top
    show sticky-small at left
    g "From there, we should now be able to boot from the USB drive."
    
    hide geek at top
    hide sticky-small at left
    show blue_screen_of_life at top
    g "You will see a selection screen like this once it boots. Choose the first option to launch our testing environment."

    hide blue_screen_of_life at top
    show live-os-loading-screen at top
    g "Next, you will see the special Linux environment loading like this."
    show sticky-small at left
    r "Cool, so then we can install Linux now, right?"
    show geek at top
    g "Not so fast!"
    g "At Free Geek, we need to test the devices first to make sure they are in good condition for the users, so the USB drives will actually first boot into a testing environment!"
    
    hide live-os-loading-screen at top
    hide geek at top
    show live-os-ready at top
    
    g "It is a live version of Linux that runs directly from the USB drive and launches testing software called QA Helper. It will also help us install the actual OS."
    r "Ok, ok! Sheesh!"
    hide live-os-ready at top
    show qa at top
    g "The testing environment looks similar to this. It is basically just a little window with buttons that you can use to test different aspects of the laptop."

    hide qa at top
    show geek at top
    show sticky-small at left

    g "We will explore these in more detail later, but first quiz time!"
    r "Yay!"
    g "Question 1: What is a BIOS/UEFI utility and what does it do?"

    hide geek at top
    hide sticky-small at left

    $ answerCount = 0

    menu:
        "A. It's a utility that lets you change what operating system you put on the computer.":
            show geek at top
            g "Sorry, no. The correct answer is C. It allows you to change low-level settings, especially those related to hardware. We change the operating system on the laptop by installing an OS on the drive, which is unrelated to the BIOS settings."
            hide geek at top
        "B. It is where elite hackers can enter your laptop's CPU and send it low-level binary instructions to plant a back door through which they can take over your computer at the hardware level and use it to mine crypto.":
            show geek-serious at top
            g "Eh, you sure about that?"
            "You" "Absolutely."
            g "Yeah, sorry, that makes no sense. The answer is C."
            hide geek-serious at top
        "C. It allows you to change low-level settings, such as the date and time on the laptop's internal clock, the boot order, and hardware-level security settings.":
            show geek at top
            g "That's right!"
            $ answerCount += 1
            hide geek at top

    show geek at top
    g "Question 2: What is Secure Boot?"
    hide geek at top
    menu:
        "A. It is a setting that restricts where we can boot from, so we should turn it off when we are changing the BIOS/UEFI settings.":
            show geek at top
            g "Right! Sometimes we can boot just fine even with Secure Boot on, but it makes things easier to just turn it off."
            $ answerCount += 1
            hide geek at top
        "B. It is part of a spy program developed by the CIA to monitor what you're doing on your computer to allegedly keep you safe, hence the newspeak word 'secure' in the name, which is meant to leave you with a false sense of security.":
            show geek-tinfoil at top
            g "Uhhh...sorry, no. The answer is A."
            hide geek-tinfoil at top
        "C. It will protect your computer from social engineering attacks.":
            show geek at top
            g "Probably not."
            g "Sorry, the answer is A."
            hide geek at top

    show geek at top
    g "Question 3: Before we install the OS, what will we need to boot into our live testing environment?"
    hide geek at top
    menu:
        "A. A floppy disk.":
            show geek at top
            g "Nope, the answer is C! We will boot to the live environment with an external SSD USB drive."
            hide geek at top
        "B. Blood, sweat, and tears.":
            show geek at top
            g "Nope, sorry, the answer is C! We boot from an external drive."
            g "The tears come later."
            hide geek at top
        "C. An external SSD drive attached to a USB port.":
            show geek at top
            g "Correct!"
            $ answerCount += 1
            hide geek at top

    show geek at top
    show sticky-small at left

    if answerCount == 3:
        g "Congrats, you got them all right!"
    if answerCount == 2:
        g "Nice, you got 2 out of 3 right!"
    if answerCount == 1:
        g "Well...at least you got one right!"
    if answerCount == 0:
        g "Uhhhh...you might want to go over this last section again, since you didn't get any of the answers right."
        r "Unless you were trying to get them wrong on purpose."
        g "Yeah, unless you were doing that for some reason."
    
    g "Moving on.................."
    g "To recap: We have the BIOS/UEFI settings correct, we've connected our boot medium, and we've chosen the correct boot option to get into the live testing environment."
    r "Does that mean we can start testing now?"
    g "Yes!"
    r "Finally!"

    hide geek at top
    hide sticky-small at left
    show live-os-ready-2 at top

    g "Take a look at the window that comes up in the testing environment. This is a tool called QA Helper. Actually, it's a *tool of tools* you could say."
    g "Each of the buttons you see here launches a sub-menu where you can test a core functionality of the laptop--such as the speaker audio or the camera--using specialized software tools."
    r "Sounds fancy!"
    g "Don't worry, it's pretty easy. QA Helper lives up to its name: It helps make the process of testing easier. All of the tools that it launches are open source and self-explanatory. It will also launch instructions with each tool."
    g "You can think of it as a checklist. As soon as you finish testing each item, you will be prompted to 'verify' that item, and this way you can keep track of what you've tested."
    r "Oh great! Do I have to test each function in the same order they are displayed here? Like, do I have to test the internet connection before I test the screen, for example?"
    g "You can test these functionalities in any order, but when you are learning, we recommend you go through them one by one as they are ordered in the window."
    
    hide live-os-ready-2 at top
    show geek at top
    show sticky-small at left
    
    r "Ok, will do. But how do I know what each one does? Some of them sound straight forward, like the audio test, but how do I know what 'Drive Health' means?"
    g "QA Helper comes with on-screen instructions, but we'll go over each test together right now before we dive in. Review the following menu to get familiar with the first few testing tools."
    

    label qaHelperMenu1:
        hide geek at top
        show geek at right
        menu:
            "1. Stress CPU":
                show stress-test at top
                g "The first test will be to stress the CPU. You will see a set of instructions come up like in the image here. Just click OK to begin the test."
                hide stress-test at top
                show stress-test-2 at top
                g "QA Helper will now throw all kinds of difficult tasks at the processor and see if it survives the stress."
                r "What? I don't want to make the laptop stressed out!"
                g "Understandable, but the test only lasts 5 minutes and most of the laptops can take it. If you find one that doesn't--for example, it shuts down during the test or the test results indicate that there is a problem--then that means it has failed this test."
                r "Oh, what happens then?"
                g "Well, in that case, the laptop will need to...move on from Free Geek."
                r "What do you mean? What happens to the devices that we don't refurbish?"
                g "..."
                r "...hello?"
                g "We'll talk about their fate later, maybe. Don't worry about it for now."
                g "The vast majority of the time, the laptop will pass through the fires of this test just fine and you will be prompted to verify. Just click 'Yes' and move on to the next test."
                r "Excuse me, but you didn't really answer my--"
                g "Let's move on to the next test!"
                hide stress-test-2 at top
                jump qaHelperMenu1
            "2. Drive Health":
                show drive-health at top
                g "This test is for the 'health' of the SSD drive that we installed before we attempted to boot the laptop. Actually, QA Helper already did some tests automatically when we booted to the live environment."
                g "This means there is nothing much to see here except to verify that the drive is fine, which it usually is. Take a look at the parameters on this screen and follow the instructions listed up top."
                g "If the result says 'no actions needed' that means that the drive is ok and you can go ahead and verify it."
                g "If there is some kind of error listed there or if the font that shows the drive is in orange, then there is a problem!"
                r "Oh no, what do we do?"
                g "In that case, just get another drive and set the broken one aside."
                g "The vast majority of SSD drives that you encounter will pass this test, since they are actually already tested as part of their wiping process in the SDA."
                g "If you encounter a failed drive that has made it this far, this means that it either failed somewhere between the SDA and installation in your laptop, or it somehow fell through the cracks."
                hide drive-health at top
                show it-character at top
                r "Ah! Who's that?"
                g "Our IT department!"
                "IT" "Hi."
                g "When you find a drive that has failed, make a note of it and give the drive to the IT department. They will examine the drive more closely, since this should not have happened...in theory!"
                g "In fact, generally speaking, if anything weird happens that is not mentioned in this tutorial, you can have IT come take a look at it. This helps the refurb department discover any problems in the process that may have been unknown!"
                hide it-character at top
                show drive-health at top
                g "In the example here, the drive is fine, so we can just move on."
                hide drive-health at top
                jump qaHelperMenu1
            "3. Disk Drive":
                show disk-drive at top
                g "This test will be available if the laptop has an optical disk drive, such as a DVD or Bluray drive."
                g "All it will do is eject the drive. If it is successfully ejected, you can consider the test a success and say 'Yes' when prompted to verify."
                r "Wow, those laptops with DVD players must be ancient!"
                g "Indeed, most of the laptops we refurbish now don't have any moving disk drives at all. Since that is usually the case, you will mostly see this option unavailable with the phrase 'Disk Drive: N/A' in red or orange font."
                r "What do I do when there is no disk drive, then?"
                g "Nothing. Click 'verify' if you want, just to keep things uniform as you go down the checklist, but it makes no difference. You can safely ignore this test if there is no disk drive."
                g "On the other hand, if there IS a drive, but it fails to open, then make a note of it. This fact will be listed in the system notes at the end of our testing phase."
                hide disk-drive at top
                jump qaHelperMenu1
            "4. Test Internet":
                show ethernet-port at top
                g "Next we will test the network connection and internet."
                g "If your laptop has an ethernet port, make sure there is a working ethernet cable plugged in that is attached to the network. Even if you booted from a USB drive, it is necessary to have an ethernet cable plugged in for this test."
                hide ethernet-port at top
                show internet-test at top
                g "When you click the Test Internet button, this is what will pop up."
                g "QA Helper will run a test to check if the network adapters on the laptop are working and that they are able to connect to the internet. This includes both the ethernet adapter and the WIFI adapter."
                hide internet-test at top
                show internet-test-2 at top
                g "If the test is successful, you will get something like this."
                hide internet-test-2 at top
                show internet-test-3 at top
                g "If you forgot to plug in your ethernet port or the ethernet port is plugged in improperly, QA Helper will prompt you to fix it with this message."
                r "Oh ok. But what if the internet is down and there is just no internet service coming through the cable? Can QA Helper tell the difference between that situation and the cable being unplugged, or will it just keep asking me to plug it in?"
                hide internet-test-3 at top
                show internet-test-4 at top
                g "QA Helper can tell! If internet service isn't coming through, you'll get an error like this one at the end."
                g "There is a similar error if the WIFI card is detected correctly, but it's unable to connect to the internet either due to driver issues or a simple service interruption."
                r "Got it! But we talked earlier about how on some laptops there is no ethernet port. What happens if that's the case?"
                hide internet-test-4 at top
                show internet-test-5 at top
                g "You will see something like this instead. Technically, this means that QA Helper did not detect any ethernet ports, so it just skipped this part of the test automatically."
                g "There is something important to remember about this, though: Now and again, you will get this message even though your laptop DOES have an ethernet port."
                g "This means that the operating system does not detect the existence of the ethernet port for some reason, which may happen with some models of laptop. It is usually a driver issue, but can also be a physical issue with the ethernet adapter."
                g "If you ever encounter this, just write it down and move on, since we will be putting it in the system notes in the end."
                hide internet-test-5 at top
                g "The same goes for any other hardware failures that prevent the laptop from connecting to the internet. Make a note of them!"
                g "And of course, if you suspect that internet service in general has been interrupted at Free Geek, contact the IT department as soon as possible!"
                show it-character at top
                "IT" "Hiya."
                r "Ah!"
                r "Uh...ok, sounds good!"
                hide it-character at top
                jump qaHelperMenu1
            "5. Test Screen":
                show lcd-test at top
                r "Are we going to test the screen now?"
                g "Yep, this is the part where we will examine the screen for scratches, hot spots, and other imperfections."
                g "As long as the screen isn't cracked or unusuable, the laptop can still be refurbished for an end user, but these imperfections should be noted."
                r "Ah ok, well, how do I see if anything is wrong with the screen? Do I just eyeball it?"
                g "Well, after you click the button to start the test, the test will consist of either one or two stages:"
                g "If the laptop does not have a touch screen--which is most of them--it will just be a single test that will display different colors on the screen to make any screen damage easier to see."
                g "Examine the screen closely, note any flaws, then tap enter to move on to the next color until you are done."
                r "What if it is a touch screen?"
                g "If it is a touch screen, you will be presented with two tests: The color test, which I already explained, and a test that requires you to tap different areas of the screen to determine that the touch screen works."
                g "QA helper has instructions for each of these tests right on the screen. You can do either test first; the order doesn't matter."
                g "What if the screen is so messed up, I can't read the instructions?"
                g "Haha, if it's that bad, then we won't refurbish the laptop, since the screen would not be usable to the end user, and that is a fundamental element of using a laptop."
                r "Can't we replace the screen, though?"
                g "In practice, no. We recieve a wide variety of laptops and don't have much direct control over what comes through the door."
                g "Since laptop parts can be very specific to the brand and model, we don't tend to carry spare screens and it would be impractical to order them for each specific laptop with a broken screen."
                g "Generally speaking, if the screen is messed up beyond a few dead pixels or hot spots, the laptop will be...relieved of its duty to Free Geek and will not be refurbished."
                r "Ok, that makes sense...but wait, what do you mean by 'relieved of its duty?'"
                g "..."
                g "Anyway, so if you find something unusual about the screen or touchscreen function, but that laptop is still usable, write it down because we will input these types of issues into our notes later."
                hide lcd-test at top
                jump qaHelperMenu1
            "6. Test Audio":
                show audio-test at top
                r "Time for some music!"
                g "Indeed, we will be testing the laptop's audio functions next!"
                g "There are two important functions that QA Helper will check: The quality of the external speakers of the laptop and the ability for the laptop to play audio through a pair of headphones."
                g "When you launch this test, QA Helper will automatically detect whether you have plugged in a set of headphones or not. If you have, then it will route audio through them. If not, it will play the audio on the external speakers."
                g "You will need need to test both, so you will be running this test twice."
                g "In both cases, follow the instructions and listen carefully for anything unusual in the audio. It should play at a normal volume and sound crisp."
                hide audio-test at top
                show audio-test-2 at top
                g "As you can see here, there will be some buttons that let you adjust the volume of the play back if you find it too low or too high."
                g "Same as with the other tests, if you find anything unexpected, write it down because we will need to reference it later. Once you are done with both tests, you can verify."
                g "If there is something amiss that you suspect could be a driver issue--like for example, if you don't hear any sound at all or the volume is super low--you may want to test again when the OS is fully installed."
                g "You can hold off on verifying until then."
                r "Got it!"
                hide audio-test-2 at top
                jump qaHelperMenu1
            "Ok, I think I've got it so far.":
                g "Great! Now that you have an idea of these first few tools, let's pause for a knowledge review."
                
    g "Answer me this: What happens if there is no optical disk drive in a laptop? What do you do?"

    menu:
        "A. Just ignore that test and don't worry about it. It will usually not be available unless there is an actual optical disk drive.":
            g "Correct!"
        "B. Write that there is no optical drive on a note and tape it to the laptop so that the end user will know.":
            g "Incorrect. There is no need to note anything about this feature."
        "C. Cry.":
            g "You can cry if you want to as a side-quest--but the correct answer is A. Just ignore this if there is no optical disk drive."
    
    g "All right, moving right along, let's check out the last few testing items that you will find in the live testing environment."

    label qaHelperMenu2:
        menu:
            "7. Test Microphone":
                show microphone-test at top
                g "Now that we have tested the audio output, it's time to test the audio input!"
                r "You mean the microphone?"
                g "That's right. Most laptops come with a built-in microphone, which is usually placed right next to the webcam. QA Helper will detect the microphone if the laptop has one and then you will be prompted to talk into it."
                hide microphone-test at top
                show microphone-test-2 at top
                g "After you click OK to start the test, this window will come up and it will record a short clip of audio."
                hide microphone-test-2 at top
                show microphone-test-3 at top
                g "When it's done with all that, you will hear the playback of what you recorded. As with the audio test, there is a simple volume control you can use to raise or lower the playback volume."
                hide microphone-test-3 at top
                show microphone-test at top
                g "Remember to consider the standards that were listed in the instructions when you evaluate the quality of the micrphone. Verify the microphone if everything sounds good, but if anything seems off--for example, if the microphone is not picking up audio--make a note of it!"
                g "Similar to the audio test, if you suspect the microphone is malfunctioning solely due to a driver issue, hold off for now and we will test again when the operating system is fully installed."
                hide microphone-test at top
                jump qaHelperMenu2
            "8. Test Camera":
                show camera-test at top
                g "Now we can test the built-in webcam that comes with the laptop--if it has one. Some laptops don't, in which case QA Helper will simply tell you it does not detect one and you can ignore this test."
                g "If you physically SEE a camera and QA Helper says it can't find one, then write this down, since this is an issue that will need to be noted for the end user."
                g "Another limit you may run into when launching the camera test is RAM: If there is not enough RAM to run the test, QA Helper will tell you and you will have to wait until after OS install to test it."
                g "This is because during the live test, the entire OS and tools are loaded into RAM, so there may not be space for this specific test."
                hide camera-test at top
                show camera-test-2 at top
                g "But if QA Helper detects the camera normally and we have enough RAM to proceed, it will launch a window like this."
                g "Look closely at the screen and check for anything weird in the image."
                r "Uh...yeeeeaaaah, I already see something super weird in this one. Who's that guy?"
                g "That's the technician testing the laptop! When you try this for yourself, you will see your own beady eyes staring back at you, don't worry!"
                g "You should then check for any signs that the camera is malfunctioning. For example, if you see any weird artifacts in the image or if you can't see the whole image."
                g "You should also wave your hand around in front of the camera to make sure it can pick up motion reasonably well and that the image isn't ghosting or freezing up."
                r "What if you just see nothing at all, though? A void. A BOTTOMLESS NOTHINGNESS."
                g "Well, sometimes the laptop camera will have its lens cover on! That can usually be toggled on and off with a slider. If you see a black window or part of the image is obscured, it may simply be that you need to open this cover!"
                g "If that doesn't help, then the camera may actually be broken or its connection to the motherboard may not work. Sometimes it's just drivers, though."
                g "As with the speakers and microphone, camera function can be especially affected by drivers, so consider testing the camera again after the OS is installed if something is not right and it's not clear why."
                r "Do I write it down, too?"
                g "Yes, indeed! If you find anything unusual about the camera, jot it down, since you will be putting this info in the system notes in the end."
                hide camera-test-2 at top
                jump qaHelperMenu2
            "9. Test Keyboard":
                show keyboard-test at top
                g "Let's have a look at the keyboard now. This test requires a bit more participation than the others, since you will have the check the functionality of each key."
                r "Eh...how do I do that?"
                g "QA Helper will launch a virtual keyboard that detects each keyboard stroke you make. It will turn the keys green on the screen if they were detected correctly."
                hide keyboard-test at top
                show keyboard-test-2 at top
                g "In the image above, the first few number keys have already been tested and have turned green. You will also see your keyboard output in a textbox."
                g "You can test the keys in any order you like, but it is KEY (heh) that you test them one by one and don't simply mash a bunch of them at once!"
                r "How come? Won't the test be over faster if I just sit on the keyboard and test them all at once?"
                g "Sure, it will be faster, but it may not be accurate!"
                g "When keyboards fail, they don't always fail predictably. Sometimes they will fail in such a way that striking one key will cause the laptop to detect a different key or may even activate multiple keys, especially if there was water damage."
                g "To be able to tell whether this is happening or not, the best approach is to type coherent phrases that contain the entire English alphabet and check to make sure that it is both coming up correctly in the text box and activating the green virtual keys."
                g "For example, you can type 'The quick brown fox jumps over the lazy dogs.' That contains all of the letters! Then you can move on to the non-letter keys."
                r "Got it! What do we do if we see a problem?"
                g "If it is something minor--like a single key being hard to press--just make a note of it."
                g "But if the issue is something that greatly affects the usability of the laptop--for example, if an entire row of the keyboard or the entire keyboard itself does not work--then we may need to...retire the laptop."
                r "Retire???"
                r "Ok, look, you've been using all these euphemisms, and I just need to know. What happens to--"
                hide keyboard-test-2 at top
                g "Now that we're done with the keyboard, we can move on to its close cousin, the trackpad! That is up next."
                jump qaHelperMenu2
            "10. Test Mouse/Trackpad":
                show mouse-test at top
                g "To test the trackpad, you will be performing a few different tasks, which you can see in the window here."
                g "Just follow the instructions to test the left click, middle click, right click, and scroll function. Finally, you can do some dragging and dropping at the bottom to make sure the individual buttons can perform long clicks."
                hide mouse-test at top
                show mouse-alternative at top
                r "Ok, but what if the laptop has one of these nub things and not a trackpad?"
                g "These are common on business class laptops--such as Thinkpads and some Dell Latitudes--but usually they will also have a trackpad. BOTH the trackpad and the nub will need to be tested seperately."
                hide mouse-alternative at top
                show mouse-alternative-2 at top
                g "Same goes for these. Often the nub will have its own set of left, middle, and right click buttons. You will have to test these in addition to the buttons that come with the trackpad."
                r "So you mean I'll have to do the test twice if I see one of these nubs?"
                g "Yes, exactly!"
                hide mouse-alternative-2 at top
                show mouse-test-2 at top
                g "There is a button to reset the test so you can start again and test the alternative mouse setup."
                g "And, as with everything else, note any problems that you find!"
                hide mouse-test-2 at top
                jump qaHelperMenu2
            "11. UEFI/BIOS Setup":
                show uefi-test at top
                g "This next part is not so much a test as a verification that you have changed the BIOS/UEFI settings to the ones we discussed before."
                g "You should have already done this in an earlier step, but if you were unable to for some reason--for example, if there was an admin password lock in the BIOS/UEFI settings--then make a note of it."
                hide uefi-test at top
                jump qaHelperMenu2
            "12. Check Ports":
                show port-test at top
                g "Finally, let's check the ports! This is mostly just a physical test."
                g "Grab a USB mouse or other simple USB device and check that it works on all the USB ports. Use an adapter if necessary--for example, if there are USB-C ports and you have a USB-A mouse."
                g "Do the same for the other ports you find on the laptop: Plug in a device that would work with that port and verify functionality."
                g "If there are any ports on there that you don't recognize, look them up! If a port is so obscure that you can't find a device on hand that would work with it, then just put in your notes that you could not test it."
                r "Ah ok, great! Let me give it a try..."
                r "Hey, wait, the HDMI port doesn't seem to be working. What do I do?"
                g "Oh right! I almost forgot to mention: Some ports may not work well in the live environment and you may have to wait until the OS is actually installed to test them."
                g "This is especially the case with video ports, such as HDMI, DisplayPort, and VGA. They may need drivers that the live environment does not have access to."
                r "Does that mean that QA Helper is available even after we are done installing the OS?"
                g "Yes! QA Helper will follow through the process with you until you have marked the laptop as completed. In fact, there are two more tests that can only be done after the OS is installed that will appear in QA Helper then."
                g "We will get to those very soon, but for now it is up to you: You can check some of the ports now and wait until after installation to re-check any that don't work in the live testing environment..."
                g "...or you can simply test them all at once after OS installation."
                r "All right! I think I will just wait until our OS is installed!"
                hide port-test at top
                jump qaHelperMenu2
            "Ok, I think I've got it.":
                g "Awesome!"

         
    g "Again, keep in mind that these are the tests that are available in the live environment. There are a couple of others that will pop up in QA Helper once the OS is actually installed on the drive, but we will discuss those more when we get there."
    show live-os-ready-3 at top
    g "For now, double-check that you have verified the available tests and made all the notes you needed to make, then go ahead and hit the 'Install OS' button at the bottom of QA Helper."
    hide live-os-ready-3 at top
    show install at top
    g "You will be prompted to choose a drive to put the OS on. Typically, there will only be one choice: The SSD that we installed in the laptop earlier. Select that and hit OK."
    hide install at top
    show install-2 at top
    g "You will then be given one final warning that the drive will be entirely erased and formatted. Hit YES and QA Helper will take care of the rest."
    r "Great! What do we do now?"
    hide install-2 at top
    show install-3 at top
    g "It will take awhile to install the OS--around ten or fifteen minutes--so grab a bag of fritos and sit a spell."
    g "Or work on another laptop in the meantime. Whatever. I ain't the boss of you."
    r "..."
    hide install-3 at top

    show installed-desktop at top
    g "Once everything is installed, we should see a desktop come up that looks like this. This is our Linux Mint desktop, which is now fully functional with all the software and tools that the user will have!"
    g "QA Helper will automatically launch and let you continue testing for now."
    r "Oh good! But QA Helper looks a little different from before. What happened?"
    hide installed-desktop at top
    show qa at top
    g "Now that we are out of the live environment and have an installed OS, you may notice we have two new tasks to check off the list that weren't there before: Drivers and System Updates."
    g "Let's discuss those in detail!"
    hide qa at top

    label qaHelperMenu3:
        menu:
            "13. Check Drivers (Appears After Installation)":
                show driver-test at top
                g "This is a quick check to see if there are any extra or alternative drivers that need to be installed for this machine."
                g "Normally, the test will result in nothing, since most generic drivers are already built into the Linux kernel and will be applied during installation. That's the case in this image you see here."
                g "However, if there are any proprietary drivers that QA Helper suggests as an alternative, they will be listed here. You can select them and then install them following the on-screen instructions, then reboot once the driver has been installed."
                r "Wait, but if I reboot, won't I lose my progress?"
                g "Nope! QA Helper and your checklist of verified functions will still be here when you reboot, until you mark the laptop completed. (We'll get into how to complete the process shortly.)"
                hide driver-test at top
                jump qaHelperMenu3
            "14. System Updates (Appears After Installation)":
                show update-requires-reboot at top
                g "This button will just run a system update to make sure this installation of Linux Mint is up to date. It will automatically open up a terminal and look for system and firmware updates."
                g "If it finds any, it may ask you for permission to install them, which will usually be in the form of a prompt that will ask you to type Y and ENTER. After that, it may ask to reboot to finish the update, which is safe to do!"
                g "Anyway, once the update is done, it will tell you. You can hit ENTER to close the terminal window, wait for it to reboot if it needs to, and then you can verify when you're back on the QA Helper window. This will be our last task in the QA Helper to-do list!"
                g "We can now move onto the next phase: QA-completing the laptop. Are you ready?"
                hide update-requires-reboot at top
                jump qaHelperMenu3
            "All right, I am ready to QA Complete the machine!":
                g "Perfect! Let's go ahead and finish our first laptop!"
    

    show qa at top
    g "Take a look at this. Do you notice something that we have been ignoring this whole time, Sticky?"
    r "Um, well, you've ignored a few things so far. Mainly, you've been ignoring me every time I ask about the fate of the laptops that don't pass the--"
    g "You might have noticed that there are three text boxes at the top of QA Helper that seem to ask for login credentials!"
    r "Oh...yeah, now that you mention it, I do see those. Why haven't we logged in yet?"
    g "You can log in at any time, but logging in is only needed at the end to complete the test and put the laptop's info in the system, so we'll do that now."
    g "We'll use the same credentials that we use to get into our inventory management system (PCsCRM)! If you don't have those credentials or aren't sure which credentials to use, ask your manager about it."
    hide qa at top
    show qa-helper-login at top
    g "For now, I have just provided a generic example. Put your username in the left box and your password in the middle. On the right, we will input the product ID of the laptop."
    r "What's that?"
    g "It's basically the Free Geek equivalent of an asset tag. It is an ID that we use to keep track of each device internally. It is seperate from the device's serial number and can be found on a sticker on the bottom of the laptop."
    g "It starts with FG and follows the pattern you see in the example, except that instead of X's, they will be numbers."
    r "Got it!"
    g "The tag also comes with a barcode, so you can either input the number manually or scan it in with a barcode scanner to avoid typos."
    g "If you type it in manually, you will have to hit enter to submit everything, and will be prompted to enter the ID again in order to verfiy. With the barcode scanner, you won't need to do this."
    g "Let's have a technician actually log in with a specific machine so you can see how it works."
    hide qa-helper-login at top
    show refurbish-in-progress at top
    g "Now we can see our status up top--which is 'refurbish in progress'--and the name of the technician who is working on the laptop."
    g "At this point, you might notice that yet another element has magically appeared in the window!"
    r "The notes?"
    hide refurbish-in-progress at top
    show add-notes at top
    g "That's right! We're finally here! Gather all the notes you made this entire time about anything that went wrong with the laptop and click this button."
    hide add-notes at top
    show write-notes at top
    g "Now you can input these facts as notes in the system. They will also show up on our labels when we print them out before giving the laptop to sales--but we'll get to that a bit later. First we have to finish the QA completion process!"
    hide write-notes at top
    show done-testing at top
    g "Double-check that everything has been tested. Now you can tap the 'Done Testing' button in the corner of QA Helper."
    hide done-testing at top
    show set-product-type-arrow at top
    g "Next, you will see this dialogue box pop up. Click on 'Set Product Type.'"
    r "What is that for?"
    g "Right now, the laptop is still listed as an 'Unbuilt' laptop in our inventory system. So we are going to need to access the system and change it to a 'Standard' laptop."
    hide set-product-type-arrow at top
    show select-product-type at top
    g "After you click the button, this dialogue should pop up. Use the drop-down menu to select the status you want to set the laptop to. By default, it will be set to 'Standard Laptop.' This is what we want for our purposes, so you can leave it like that."
    hide select-product-type at top
    show select-product-type-arrow at top
    g "Next, just hit 'Set Selected Product Type' to confirm!"
    hide select-product-type-arrow at top
    show set-product-type-2 at top
    g "You will see this confirmation dialogue if everything went right. Click OK!"
    hide set-product-type-2 at top
    show set-status-qa-complete-arrow at top
    g "...and you should be back at this dialogue box again. This time, click 'Set Status to QA Complete' and another box should come up."
    hide set-status-qa-complete-arrow at top
    show confirm-qa-complete at top
    g "This window will allow you to confirm that the laptop should set itself up for a new user on the next reboot. The checkbox should already be ticked for you. All you have to is hit 'Yes'!"
    hide confirm-qa-complete at top
    show qa-complete-result-arrow at top
    g "Once you are done with that, you will see this new dialogue box."
    g "Hit the 'Reboot' button and the laptop will finish the QA process, remove QA Helper from the installation, and get itself ready for the user!"
    r "Yay!"
    hide qa-complete-result-arrow at top
    show language-screen at top
    g "When the laptop boots back up we will see this. It is the language screen so that the end user can start setting up their account and preferences. This means that our work is done!"
    g "...Or nearly so! Our last testing task is to pull the plug on the charger and see how the laptop reacts. If it doesn't turn off immediately, that's good! It means the battery can hold some sort of charge."
    g "Once you have verified this, you can go ahead and hold down the power button to shut down the laptop. The testing phase is officially complete!"
    r "🥳"
    g "Clean the laptop up thoroughly, remove any stickers, and re-tighten any screws. We're moving on to the last phase: Printing out labels and sending our machine to sales!"
    hide language-screen at top
    
    scene bg typingdesk
    show geek at right
    show sticky-small at left
    g "All right, let's sit at our computer desk and open up the label creation page in our favorite browser!"
    r "My favorite browser is Edge!"
    g "..."
    g "...All right, so opening up Chrome, we can simply type the URL for the Free Geek label creation app (which will be given to you by a supervisor)--unless IT changed it recently."
    show it-character at top
    "IT" "We'll let you know."
    "IT" "If available on your desktop, you can also click on an icon that says 'Create Specs Labels' and it will take you to the same page."
    hide it-character at top
    show label-creation-page at top
    g "Great, perfect! Type your laptop's ID into the textbox and click 'Create Specs Label' or scan it in with a barcode scanner."
    hide label-creation-page at top
    show label-creation-page-2 at top
    g "Either way, you should see this page load right after."
    g "It will show all of the laptop's specs in a table-like layout and will even display the notes that you wrote about your laptop."
    hide label-creation-page-2 at top
    show label-creation-page-2-arrow at top
    g "Click this button here to send the spec label to our wonderful thermal label printer."
    hide label-creation-page-2-arrow at top
    show label-creation-page-3 at top
    g "Hit this button to print and then go get your label!"
    hide label-creation-page-3 at top
    r "Oh, where do I get it?"
    g "I'll show you!"

    scene bg printershelf
    show geek at right
    show sticky-small at left
    g "Here we are at the printing station. You can find both our printers on a shelf here, but the one we are looking for is this one:"
    show thermal-printer at top
    g "It's a Star TSP100III series thermal printer. No ink, all efficiency! It prints like a dream."
    r "Uh...great."
    hide thermal-printer at top
    show label-printer-1 at top
    g "If everything went according to plan, it should look like this, with your label freshly printed."
    hide label-printer-1 at top
    show label-printer-2 at top
    g "Check to make sure it's yours and rip it out!"
    hide label-printer-2 at top
    show label-on-laptop at top
    g "Put some tape on and slap it on your laptop!"
    hide label-on-laptop at top
    show laptop-sales-bin at top
    g "Then put your laptop gently in one of the sales bins!"
    hide laptop-sales-bin at top
    show power-adapter at top
    g "Don't forget to grab the power adapter for your laptop and drop it in the bin, too. You can use a matching pair of stickers to mark which adapter goes with which laptop."
    hide power-adapter at top
    show power-adapter-sticker at top
    g "Like so!"
    r "Nice! Do we give the laptop to the sales team now?"
    g "Wait until you've done 6 or 7 per bin, then you can place the bin on the shelf in the hallway for the sales team to take care of."
    g "Just don't overfill the bin--limit it to 7 at the most--since they can get too heavy after that."
    r "Got it!"
    hide power-adapter-sticker at top

    scene bg matrix
    show geek at right
    show sticky-small at left
    r "Oh wow! We're back in...wherever this place is!"
    g "Indeed we are, Sticky! Our journey has come full circle. You have learned to refurbish a laptop the Free Geek way! Congratulations!"
    g "Roll the credits!"

    scene bg laptopcloset
    show geek at right
    show sticky-small at left
    r "Hey, hey! No, wait!"
    g "What is it, Sticky? We're done here."
    r "You never told me what happens to the laptops that...don't make it."
    g "Ohhhhh."
    g "..."
    show laptop-recycle-bin at top
    g "They just go in here."
    r "What?"
    g "Yeah, we write them off and then send them to get recycled by a downstream recycling service."
    r "But why were you making it sound all sinister, then???"
    g "I was?"
    r "Yeah! And what happens to them when they get recycled?!"
    hide laptop-recycle-bin at top
    show crucible at top
    g "Oh, nothing."
    hide crucible at top
    show laptop-recycle-bin at top
    g "Just remember that the ones with the green sticker go in the bin marked 'covered' and the ones that have both a white and green sticker go in the bin called 'uncovered' due to reasons."
    hide laptop-recycle-bin at top

    scene bg matrix
    show geek at right
    show sticky-small at left
    g "*Ahem* Anyway!"
    g "Congratulations--for real this time! And welcome to the Free Geek refurb team!"
    r "Thanks for hanging out with us!"
    g "If you have any questions, ask any of the members of the refurb team! We are happy to assist!"




    # This ends the game.

    return
