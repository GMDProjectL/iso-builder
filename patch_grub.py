with open('archlive/grub/grub.cfg', 'r') as fp:
    grub_cfg = fp.read()


grub_cfg = grub_cfg.replace('play 600 988 1 1319 4', '')
grub_cfg = grub_cfg.replace('Arch Linux', 'Project GDL')
# grub_cfg = grub_cfg.replace('gfxmode="auto"', 'gfxmode="1920x1080"')


with open('archlive/grub/grub.cfg', 'w') as fp:
    fp.write(grub_cfg)
