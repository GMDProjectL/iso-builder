with open("archlive/profiledef.sh", 'r') as f:
    profiledef = f.read()

profiledef = profiledef.replace('iso_name="archlinux"', 'iso_name="projectgdl"')
profiledef = profiledef.replace('iso_publisher="Arch Linux <https://archlinux.org>"', 'iso_publisher="Project GDL <https://t.me/ProjectGDL>"')

with open("archlive/profiledef.sh", 'w') as f:
    f.write(profiledef)