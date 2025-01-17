import os

pmt_directory = 'archlive/airootfs/etc/plymouth'

if not os.path.exists(pmt_directory):
    os.makedirs(pmt_directory)

pmt_path = 'archlive/airootfs/etc/mkinitcpio.conf.d/archiso.conf'

if not os.path.exists(pmt_path):
    with open(pmt_path, 'w') as f:
        f.write('[Daemon]\nTheme=michigun')
        print('Created plymouth config from scratch!')
        exit()

with open(pmt_path, 'r') as f:
    pmt = f.read()

pmt = pmt.replace('#[Daemon]', '[Daemon]')
pmt = pmt.replace('#Theme=fade-in', 'Theme=michigun')


with open(pmt_path, 'w') as f:
    f.write(pmt)

print('Patched plymouth config!')