import alligat as sys #Impoting main module, wich is processing all the command's
import os
import ftpp
import time

os.system('title TERMINAL ALLIGATOR - VER 1.5')
#ASCII art :)
print(' ▄▄▄       ██▓     ██▓     ██▓ ▄████  ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  ')
print('\n▒████▄    ▓██▒    ▓██▒    ▓██▒██▒ ▀█▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒')
print('\n▒██  ▀█▄  ▒██░    ▒██░    ▒██▒██░▄▄▄░▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒')
print('\n░██▄▄▄▄██ ▒██░    ▒██░    ░██░▓█  ██▓░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  ')
print('\n ▓█   ▓██▒░██████▒░██████▒░██░▒▓███▀▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒')
print('\n\n Terminal "Alligator" - Console is better than GUI ! v1.0')


while 0 == 0: #Infinite loop
    cmd = str(input('>>>')) #Waiting for user cmd
    sys.check(cmd) #Sending it into main module
    ftpp.check(cmd)
