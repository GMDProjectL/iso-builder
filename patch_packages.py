with open("archlive/packages.x86_64", 'r') as f:
    packages = f.read()

packages += '\n'
packages += 'vulkan-intel\n'
packages += 'vulkan-nouveau\n'
packages += 'vulkan-mesa-layers\n'
packages += 'hyprland\n'
packages += 'hyprpaper\n'
packages += 'waybar\n'
packages += 'python\n'
packages += 'python-requests\n'
packages += 'python-systemd\n'
packages += 'python-dbus\n'
packages += 'python-pyudev\n'
packages += 'python-gobject\n'
packages += 'adwaita-fonts\n'
packages += 'npm\n'
packages += 'pnpm\n'
packages += 'reflector\n'
packages += 'nodejs\n'
packages += 'electron34\n'
packages += 'networkmanager\n'
packages += 'network-manager-applet\n'
packages += 'adw-gtk-theme\n'
packages += 'alacritty\n'
packages += 'gnome-disk-utility\n'
packages += 'ttf-roboto\n'
packages += 'polkit\n'
packages += 'polkit-kde-agent\n'
packages += 'linux-headers\n'
packages += 'dkms\n'
packages += 'plymouth\n'
packages += 'mesa-utils\n'

packages = packages.replace('broadcom-wl', 'broadcom-wl-dkms')
packages = packages.replace('grml-zsh-config', '')


with open("archlive/packages.x86_64", 'w') as f:
    f.write(packages)
