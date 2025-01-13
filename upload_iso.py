import os
import subprocess


for filename in os.listdir('out/'):
    print(f'Uploading {filename} to temp.sh ...')

    process = subprocess.run([
        'curl', '-F', f'file=@out/{filename}', 'https://temp.sh/upload'
    ])

    print(f'\n\nUploaded: {filename}')
