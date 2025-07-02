import os

os.chdir("installer")
os.system("distrobox enter --root arch -- pnpm i")
os.system("distrobox enter --root arch -- pnpm build")