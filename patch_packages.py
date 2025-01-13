with open("archlive/packages.x86_64", 'r') as f:
    packages = f.read()

packages += '\n'
packages += 'hyprland\n'
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

packages = packages.replace('grml-zsh-config', '')

with open("archlive/packages.x86_64", 'w') as f:
    f.write(packages)