# Setup

1. Initial software
```
yay -S debugedit fish libinput-gestures
yay -S brave
```
2. Restart the system
```
sudo pacman-key --init
sudo pacman-key --populate archlinux
sudo pacman -Sy archlinux-keyring
sudo pacman -Scc
yay -Syyu
```
3. config files while update is taking place. 

4. Change Shell
```
sudo chsh -s /usr/bin/fish
echo $SHELL
```
output for echo should be */bin/fish*.

5.  Gestures
```
cp /etc/libinput-gestures.conf ~/.config/libinput-gestures.conf
sudo gpasswd -a $USER input
chmod 644 ~/.config/libinput-gestures.conf
libinput-gestures-setup stop
libinput-gestures-setup start
libinput-gestures-setup autostart

xinput --set-prop "ELAN07D2:00 04F3:321A Touchpad" "libinput Accel Speed" 0.3
```

6. Download - wallpaper, pass/bookmark, polybar files. 

7. Brave Stuff
brave settings
brave shortcuts
brave extentions - vpn yt-enhancer
![image](https://github.com/user-attachments/assets/b7c514af-d543-46cf-8c8e-3987904dbd6d)


8. Misc Stuff
```
yay -S telegram-desktop zathura lxappearance unimatrix cava neovim ranger locate
betterlockscreen -u Pictures/wallpapers/mountain.png
git clone https://github.com/NvChad/starter ~/.config/nvim && nvim
yay -R firefox
setxkbmap de us
```

8. Spicetify
```
yay -S spotify

LOG INTO THE ACCOUNT

sudo chmod a+wr /opt/spotify
sudo chmod a+wr /opt/spotify/Apps -R

yay -S spicetify-cli
curl -fsSL https://raw.githubusercontent.com/spicetify/cli/main/install.sh | sh

nvim .config/spicetify/config-xpui.ini
it should be 
spotify_path = /home/nyxn/.config/spotify

spicetify backup apply      
spicetify apply
```
![image](https://github.com/user-attachments/assets/cf0592dc-67cd-4f17-9c1d-6261f982a42d)

10. change font, and theme of geany
11. betterdiscord

12. minecraft
    ```
    yay -S nvidia
    yay -S optimus-manager
    yay -S nvidia-prime

    sudo systemctl enable optimus-manager
    sudo systemctl start optimus-manager

   RESTART 
    
