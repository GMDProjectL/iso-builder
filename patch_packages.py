with open("archlive/packages.x86_64", 'r') as f:
    packages = f.read()

packages += '\n'
packages += 'hyprland\n'
packages += 'hyprpaper\n'
packages += 'waybar\n'
packages += 'python\n'
packages += 'python-requests\n'
packages += 'python-systemd\n'
packages += 'npm\n'
packages += 'nodejs\n'
packages += 'electron33\n'
packages += 'networkmanager\n'
packages += 'network-manager-applet\n'
packages += 'adw-gtk-theme\n'
packages += 'kitty\n'
packages += 'gnome-disk-utility\n'
packages += 'ttf-roboto\n'
packages += 'polkit\n'
packages += 'polkit-kde-agent\n'
packages += 'linux-headers\n'
packages += 'dkms\n'
packages += 'plymouth\n'

packages = packages.replace('broadcom-wl', 'broadcom-wl-dkms')
packages = packages.replace('grml-zsh-config', '')


with open("archlive/packages.x86_64", 'w') as f:
    f.write(packages)
