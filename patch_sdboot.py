import os

with open('archlive/efiboot/loader/entries/01-archiso-x86_64-linux.conf', 'r') as fp:
    sd_archiso = fp.read()

sd_archiso = sd_archiso.replace('Arch Linux', 'Project GDL')
sd_archiso = sd_archiso.replace('%ARCHISO_UUID%', '%ARCHISO_UUID% quiet splash')

with open('archlive/efiboot/loader/entries/01-archiso-x86_64-linux.conf', 'w') as fp:
    fp.write(sd_archiso)


with open('archlive/efiboot/loader/entries/02-archiso-x86_64-speech-linux.conf', 'r') as fp:
    sd2_archiso = fp.read()

sd2_archiso = sd2_archiso.replace('Arch Linux', 'Project GDL')

with open('archlive/efiboot/loader/entries/02-archiso-x86_64-speech-linux.conf', 'w') as fp:
    fp.write(sd2_archiso)



with open('archlive/efiboot/loader/loader.conf', 'r') as fp:
    sd_loader = fp.read()

sd_loader = sd_loader.replace('timeout 15', 'timeout 0')
sd_loader = sd_loader.replace('beep on', 'beep off')

with open('archlive/efiboot/loader/loader.conf', 'w') as fp:
    fp.write(sd_loader)
