profiledef_path = 'archlive/profiledef.sh'

with open(profiledef_path, 'r') as f:
    profiledef = f.read()


payload = '["/opt/installer/"]="1000:1000:7777"'
profiledef = profiledef.replace('file_permissions=(', 'file_permissions=(\n' + payload + '\n')


with open(profiledef_path, 'w') as f:
    f.write(profiledef)