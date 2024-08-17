djd# Setup

1. Initial software
```
yay -S debugedit fish libinput-gestures
yay -Syu
yay -S brave
```
install fish first, otherwise alacritty wont work. 

2. Config Files

3. Change Shell
```
sudo chsh -s /usr/bin/fish
echo $SHELL
```
output for echo should be */bin/fish*.

> Gestures
```
cp /etc/libinput-gestures.conf ~/.config/libinput-gestures.conf
sudo gpasswd -a $USER input
chmod 644 ~/.config/libinput-gestures.conf
libinput-gestures-setup stop
libinput-gestures-setup start
libinput-gestures-setup autostart

xinput --set-prop "ELAN07D2:00 04F3:321A Touchpad" "libinput Accel Speed" 0.3
```

5. Download - wallpaper, pass/bookmark, polybar files. 

6. Brave Stuff
brave settings
brave shortcuts
brave extentions - vpn yt-enhancer

7. Misc Stuff
```
yay -S telegram-desktop zathura lxappearance unimatrix cava neovim ranger locate
betterlockscreen -u Pictures/wallpapers/mountain.png
git clone https://github.com/NvChad/starter ~/.config/nvim && nvim
yay -R firefox
```

8. Polybar
```
git clone --depth=1 https://github.com/adi1090x/polybar-themes.git

cd polybar-themes
chmod +x setup.sh
./setup.sh
bash ~/.config/polybar/launch.sh --forest
```

9. Spicetify
```
yay -S spotify

sudo chmod a+wr /opt/spotify
sudo chmod a+wr /opt/spotify/Apps -R

yay -S spicetify-cli

nvim .config/spicetify/config-xpui.ini
it should be 
spotify_path = /home/nyxn/.config/spotify

spicetify backup apply      
spicetify apply
```

10. change font, and theme of geany
11. betterdiscord
