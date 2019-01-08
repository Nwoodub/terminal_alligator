import os.path
import time
import math
import sys
import os
import datetime
import shutil

def check(cmd):
    if cmd == 'help':
        print('CLS - clean screen')

    if cmd == 'cls':
        os.system('cls')

    if cmd == 'exit':
        sys.exit()

    if cmd == 'call':
        path = str(input('PATH: '))
        cl = 'start ' + path
        os.system(cl)

    if cmd == 'tasklist':
        ts = os.system('tasklist')
        print(ts)

    if cmd == 'taskkill':
        attr = str(input('TASK: '))
        tk = 'taskkill /im ' + attr
        os.system(tk)
    if cmd == 'cpid':
        id = os.getpid()
        print(id)

    if cmd == 'nwsess':
        os.system('start main.py')

    if cmd == 'qtsess':
        sys.exit()

    if cmd == 'osn':
        osn = os.name
        os2 = sys.platform
        print(osn, os2)

    if cmd == 'oslog':
        logos = os.getlogin()
        print(logos)

    if cmd == 'size':
        path = str(input('PATH: '))
        print(os.path.getsize(path), 'Byte')

    if cmd == 'dir':
        now = os.getcwd()
        dirnw = os.listdir(now)
        print(dirnw)

    if cmd == 'copy':
        path = str(input('PATH 1:'))
        patt = str(input('PATH 2:'))
        shutil.copy(path, patt)

    if cmd == 'cd':
        path = str(input('PATH: '))
        os.chdir(path)

    if cmd == 'ren':
        nn = str(input('PATH 1:'))
        n2 = str(input('PATH 2:'))
        os.rename(nn, n2)

    if cmd == 'rd':
        path = str(input('PATH: '))
        rm = os.removedirs(path)

    if cmd == 'mkdir':
        stng = str(input('PATH:'))
        os.mkdir(stng)

    if cmd == 'chmod':
        path = str(input('PATH:'))
        mode = str(input('ATTR:'))
        os.chmod(path, mode)

    if cmd == 'tree':
        print(os.system('tree'))

    if cmd == 'dirtime':
        path = str(input('PATH: '))
        dir = os.path.getmtime(path)
        print(dir)

    if cmd == 'time':
        time = datetime.datetime.now()
        print(time)
