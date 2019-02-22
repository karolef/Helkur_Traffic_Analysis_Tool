import csv
import pymysql
import os


def init_db():
    db_name = "Helkur"
    db_user = "root"
    db_password = ""
    db_host = "localhost"

    conn = pymysql.connect(host=db_host,
                           user=db_user,
                           password=db_password,
                           database=db_name)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS traffic 
                    (time text, ip_source text,
                     ip_dest text, port_tcp_source text,
                      port_tcp_dest text, 
                      protocol text, frame_length text)''')
    cursor.close()
    conn.close()


# init_db()

def push_files_to_db():
    db_name = "Helkur"
    db_user = "root"
    db_password = ""
    db_host = "localhost"

    extracted_files = os.listdir('C:/Users/kfatyga/PycharmProjects/database_bullshit/extracted')
    # print(extracted_files)
    conn = pymysql.connect(host=db_host,
                           user=db_user,
                           passwd=db_password,
                           database=db_name)
    cursor = conn.cursor()
    for file in extracted_files:
        csv_data = csv.reader(open('C:/Users/kfatyga/PycharmProjects/database_bullshit/extracted/' + str(file)),
                              delimiter=',')
        for row in csv_data:
            # print(row)
            # print(row[0][7: 17])
            cursor.execute('INSERT INTO traffic VALUES (%s, %s, %s, %s, %s, %s, %s)',
                           (row[0][7: 17], row[1], row[2], row[3], row[4], row[5], row[6]))
    conn.commit()
    cursor.close()
    conn.close()

# push_files_to_db()
