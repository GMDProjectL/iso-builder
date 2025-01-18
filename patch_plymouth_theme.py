import os

pmt_directory = 'archlive/airootfs/etc/plymouth'

if not os.path.exists(pmt_directory):
    os.makedirs(pmt_directory)

pmt_path = pmt_directory + '/plymouthd.conf'


with open(pmt_path, 'w') as f:
    f.write('[Daemon]\nTheme=michigun')

print('Created plymouth config from scratch!')