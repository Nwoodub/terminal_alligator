import ftplib

def check(cmd):
    if cmd == 'ftp.connect':
        global ftp
        global host
        global ftp_user
        global ftp_password
        host = str(input('HOST: '))
        ftp_user = str(input('USER: '))
        ftp_password = str(input('PASSWORD: '))
        ftp = ftplib.FTP(host, ftp_user, ftp_password)
        print(ftp.getwelcome())
        while 1 == 1:
            cm = str(input('.>'))

            if cm == 'ftp.cd':
                path = str(input('DIR: '))
                ftp = ftplib.FTP(host, ftp_user, ftp_password)
                ftp.cwd(path)

            if cm == 'ftp.rename':
                f1 = str(input('FILE TO REN: '))
                f2 = str(input('NEW FILE NAM: '))
                ftp.rename(f1, f2)

            if cm == 'ftp.delfile':
                fd = str(input('FILE: '))
                ftp.delete(fd)

            if cm == 'ftp.deldir':
                fd = str(input('DIR: '))
                ftp.rmd(fd)

            if cm == 'ftp.mkdir':
                md = str(input('PATH: '))
                ftp.mkd(md)

            if cm == 'ftp.sendcmd':
                dmc = str(input('CMD: '))
                ftp.sendcmd(dmc)

            if cm == 'ftp.retrbin':
                retr = str(input('FILE: '))
                ftp.retrbinary('RETR %s' % retr, file.write)

            if cm == 'ftp.list':
                ftp.retrlines('LIST')

            if cm == 'ftp.storlines':
                st = str(input('FILE: '))
                ftp.storlines('STOR ' + st, open(st,'rb'))

            if cm == 'ftp.storbinart':
                ft = str(input('FILE: '))
                ftp.storbinary(ft)
