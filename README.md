# krita-vertical-brush-docker

Docker that features vertical brush sliders for size and opacity for touchscreen devices - tablets, transformers/2-in-1, drawing monitors, and mobile devices.

<br />
<center><img width="76" height="391" alt="short" src="https://github.com/user-attachments/assets/6c55c73a-1a31-4fc2-8c21-d7aaedab864d" />
<img width="61" height="959" alt="looooooong" src="https://github.com/user-attachments/assets/71f61cdc-8478-40e0-bcc1-bfdfc2aa2ba5" />
</center>

# What are Dockers in Krita?

Dockers are panels/subwindows that provide the way to select, adjust and actually use various tools in Krita. Without those, only canvas and toolbars are available.<br />

Details - https://docs.krita.org/sl/reference_manual/dockers.html

# Why?

This docker is made with the sole purpose of making Krita far easier to use on the (touch)screens.<br />
Before that, user had to stick with built-in toolbars with horizontal brush sliders, or use gestures, keep using keyboard hotkeys, resort to macropads, or use 3rd party software like TabletFriend or Tablet Pro for adjusting brush parameters in a more convenient manner.<br />
Adding two sliders makes UX far better, expecially considering Krita already has decent gesture support. Effectively, adding that thing alone to Krita's toolset makes it fell almost like any other drawing software tailored for the de-facto Procreate-alike experience.<br />
It also duplicates main "Brushes and stuff" toolbar settings, which basically unchains interface customization and lets moving the toolbar to more convenient positions or removing it altogether, thus freeing up real space estate.<br />
<br />
Examples:<br />
<center><img width="514" height="1032" alt="image" src="https://github.com/user-attachments/assets/edec7ae1-3846-4ee4-aa6f-d1cac623e567" />
<img width="514" height="1032" alt="image" src="https://github.com/user-attachments/assets/37d80f1a-1617-4e24-b2a9-e7cfda599b52" /></center>
<br />

# Compatibility

Krita in both Qt5 and Qt6 is supported thanks to the conditional check.

# Installation

Clone/Download and then unpack to the relevant location (Iceberg sort):
- Universal:<br /> `Settings > Manage Resources > Open Resource Folder`<br /> and then pykrita subfolder
- Windows:<br />`%APPDATA%\krita\pykrita`
- Windows Store:<br />`%LOCALAPPDATA%\Packages\49800Krita_RANDOM STRING\LocalCacheRoamingkrita/pykrita`
- macOS:<br />`~/Library/Application Support/Krita/pykrita`
- Linux/AppImage:<br />`$HOME/.local/share/krita/pykrita`
- Flatpak:<br />`$HOME/.var/app/org.kde.krita/data/krita/pykrita`
- Snap:<br />`$HOME/snap/krita/current/.local/share/krita/pykrita`
- Android:<br /> By default it's `/storage/emulated/0/Android/data/org.krita/files/pykrita`
Though user would've to resort to the ADB shell or file managers from the outside of the Play Store with special permissions to access the folder. Resource folder can be changed to other, far more user-accessible location, using `Settings > Configure Krita > General > Resources`
- Haiku (ohmygodreally?):<br />`/boot/home/config/non-packaged/data/krita/`
- iOS/iPadOS: The stuggle continues folks. https://docs.krita.org/en/KritaFAQ.html#can-i-get-krita-for-ipad-or-for-android

Details about directories (very incomplete) - https://docs.krita.org/sl/reference_manual/resource_management.html

- After copying, (re)start Krita, and go to `Settings > Configure Krita > Python Plugin Manager` and check the `ProBrushSliders`.<br />
- Restart Krita.<br />
- Open any image/project file, or create new to switch into the workspace.
- Choose the workspace you want to modify, or better create a new one, by accessing `Workspaces` at the top left of the `Brushes and stuff` toolbar.
- Go to `Settings`, check `Show Dockers` if not yet checked or if no dockers are displayed for some reason.
- Go to `Settings > Dockers > ProBrushSliders`.
- Move the docker around the workspace until it works for you.
- Click the lock if you want it to stay where you put it.
- If you want it to occupy the entire workspace height and if there are existing dockers in a way, then  existing dockers must be unattached from the side you want to put it in first. Then, attach the docker there, then put previous dockers back one by one.
- Enjoy sliding brush setting vertically like a modern, Pro artist, yo.

# Configuration

None. Making it any fancier that it is now is unfortunately out of my scope for the time being.

# Known bugs/TODO

- Once enabled - cannot be disabled, only removed from the folder. Root cause of the behavior is unknown. Will fix later.
- Updates each tick instead on the slider release. Adjusting slider makes every other brush slider for the same setting also move in live. This differs with how every slider in Krita behaves, and may (or may not) affect the end user experience. Will fix later.
- Can't be infinitely adjusted in width, otherwise it wouldn't be possible to make it as slim as it is. It is a Qt quirk I failed to work around. Therefore, the only intended use of it is either as a floating window or on the side of the canvas/other docker.

# Expected behavior

If you hide all dockers - It will go away together with all other dockers. This is different from how toolbar on the top of the workspace behaves (it's called Brushes and stuff), which usually has these sliders and keeps them when dockers are being hidden. It is expected, and there's no workaround other than resorting to the methods listed at the second paragraph of "Why".

# TODO

I may (or may not) improve this docker as I continue to make art.<br />
Owning, using various devices/peripherals and successfully producing content with them makes it far more likely.

# See also (things I use with Krita/Photoshop)
- TabletFriend - FOSS Windows Explorer sidebar, specifically designed for artists, that provides on-screen keyboard shoctruts in appealing manner. Utilizes ancient APIs, which unfortunately makes it broken on Windows 11 once switched to the tablet mode (there's a gap between the bottom of the sidebar and the taskbar). Quite handy otherwise https://github.com/Martenfur/TabletFriend
- Tablet Pro - Mainstream sidebar for artists. Functionally is the same as above, but different. Free, but not opensource. Very well featured and supported however. https://tabletpro.com/
- PureRef - Application that lets you collect, organize and keep references in a separate file without being dependent on the specific art software, working file/directory management, or Windows Explorer/Graphical Environment limitations. Can be used as a floating always-on-top window, or side-by-side with the main program. https://www.pureref.com/
- Pigment'O - Color picker that enhances the color selection within Krita, features different color harmonies, color spaces, and also allows to colorpick from outside of Krita instances. If you're looking for Coolorus but for Krita - this is it. https://github.com/EyeOdin/Pigment.O
- procrepad - project that contains resources for left-/right-handed macropad, based around Jorne and dumbpad projects. Heavily WIP, frozen for the time being. https://github.com/cyanoger/procrepad
