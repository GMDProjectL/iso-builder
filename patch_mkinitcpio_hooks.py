import os

archiso_mio_path = 'archlive/airootfs/etc/mkinitcpio.conf.d/archiso.conf'

with open(archiso_mio_path, 'r') as f:
    archiso_mio = f.read()


archiso_mio = archiso_mio.replace('keyboard)', 'keyboard plymouth)')

with open(archiso_mio_path, 'w') as f:
    f.write(archiso_mio)