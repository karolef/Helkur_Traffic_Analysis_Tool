from ftplib import FTP
from datetime import datetime


def ftp():
    start = datetime.now()
    ftp = FTP('172.30.158.153')
    ftp.login('anonymous', 'fatyga.karol@gmail.com')

    # Get All Files
    files = ftp.nlst()

    # Print out the files
    for file in files:
        print("Downloading..." + file)
        ftp.retrbinary("RETR " + file, open("C:/Users/kfatyga/PycharmProjects/database_bullshit/" + file, 'wb').write)

    ftp.close()

    end = datetime.now()
    diff = end - start
    print('All files downloaded for ' + str(diff.seconds) + 's')

# ftp()
