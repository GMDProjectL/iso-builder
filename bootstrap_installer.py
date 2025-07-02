import os

os.chdir("installer")
os.system("distrobox enter --root arch -- pnpm i && pnpm build")