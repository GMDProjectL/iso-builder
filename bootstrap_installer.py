import os

os.chdir("installer")
os.system("pnpm i")
os.system("pnpm build")