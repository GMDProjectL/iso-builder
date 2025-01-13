import os

os.chdir("installer")
os.system("npm install")
os.system("npm run build")