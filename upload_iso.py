import os
import subprocess


for filename in os.listdir('out/'):
    print(f'Uploading {filename} to temp.sh ...')

    process = subprocess.run([
        'curl', '-F', f'file=@out/{filename}', 'https://temp.sh/upload'
    ])

    url = process.stdout.decode()

    print(f'Uploaded: {filename} to {url}')
