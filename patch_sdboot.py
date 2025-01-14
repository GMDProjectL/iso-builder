import os

with open('archlive/efiboot/loader/entries/01-archiso-x86_64-linux.conf', 'r') as fp:
    sd_archiso = fp.read()

sd_archiso = sd_archiso.replace('Arch Linux', 'Project GDL')



with open('archlive/efiboot/loader/loader.conf', 'r') as fp:
    sd_loader = fp.read()

sd_loader = sd_loader.replace('beep on', '')


#os.remove('archlive/efiboot/loader/entries/02-archiso-x86_64-speech-linux.conf')
#os.remove('archlive/efiboot/loader/entries/03-archiso-x86_64-memtest86+.conf')


with open('archlive/efiboot/loader/entries/01-archiso-x86_64-linux.conf', 'w') as fp:
    fp.write(sd_archiso)

with open('archlive/efiboot/loader/loader.conf', 'w') as fp:
    fp.write(sd_loader)

