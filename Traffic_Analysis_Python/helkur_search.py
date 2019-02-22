# import the needful

import pymysql


def show_all_for_protocol(pro):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database="helkur"
    )

    cur = conn.cursor()
    cur.execute(
        'SELECT FROM_UNIXTIME(time, "%s") AS second, ip_source, ip_dest, port_tcp_source, port_tcp_dest, protocol, frame_length FROM traffic WHERE protocol="TCP" ORDER BY FROM_UNIXTIME(time, "%s")'.format(
            pro))
    rows = cur.fetchall()
    print('second, ip_source, ip_dest, port_tcp_source, port_tcp_dest, protocol, frame_length')
    for i in rows:
        print(i)


# pull frame length sum for protocol

def show_sum_for_protocol(pro):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database="helkur"
    )

    cur = conn.cursor()
    cur.execute(
        'SELECT FROM_UNIXTIME(time, "%s") AS second, protocol, SUM(frame_length) AS frame_lenght_sum FROM traffic WHERE protocol="{}" GROUP BY FROM_UNIXTIME(time, "%s")'.format(
            pro))
    rows = cur.fetchall()
    print('second, protocol, frame_lenght_sum')
    for i in rows:
        print(i)


#  pull whichever column for given protocol

def show_chosen_column_for_protocol(col, pro):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database="helkur"
    )

    cur = conn.cursor()
    cur.execute(
        'SELECT FROM_UNIXTIME(time, "%s") AS second, protocol, {col} FROM traffic WHERE protocol = "{pro}" ORDER BY FROM_UNIXTIME(time, "%s")'.format(
            col=col, pro=pro))
    rows = cur.fetchall()
    print('second, protocol, ' + col)
    for i in rows:
        print(i)
