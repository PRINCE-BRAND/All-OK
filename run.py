import os, sys
os.system('clear')
os.system('git pull')
try:
    __import__("𝕻𝖗𝖎𝖓𝖈𝖊-𝕭𝖗𝖆𝖓𝕯-𝓿𝓲𝓹").make()
except Exception as e:
    exit(str(e))
