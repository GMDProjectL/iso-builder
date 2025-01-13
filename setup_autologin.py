autologin_file = 'archlive/airootfs/etc/systemd/system/getty@tty1.service.d/autologin.conf'

with open(autologin_file, 'w') as f:
    f.write('[Service]\n')
    f.write('ExecStart=\n')
    f.write('ExecStart=-/sbin/agetty --autologin liveuser --noclear %I 38400 linux')