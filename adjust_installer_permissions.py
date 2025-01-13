import os

profiledef_path = 'archlive/profiledef.sh'

with open(profiledef_path, 'r') as f:
    profiledef = f.read()


payload = '["/opt/installer/"]="1000:1000:7777"\n'
payload += '["/opt/installer/start-here.sh"]="1000:1000:7777"\n'
profiledef = profiledef.replace('file_permissions=(', 'file_permissions=(\n' + payload + '\n')

try:
    os.system("chmod -R 777 archlive/airootfs/opt/installer")
except Exception as e:
    print(f'That\'s not how you do it, {e}')

with open(profiledef_path, 'w') as f:
    f.write(profiledef)