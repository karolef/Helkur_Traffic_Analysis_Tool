import csv
import pymysql
import os
import zipfile
import pymysql
from ftp import ftp
from ftplib import FTP
from datetime import datetime
from unzip_the_goddamn_file import unzip
from push_to_db import init_db, push_files_to_db
from helkur_search import show_all_for_protocol, show_sum_for_protocol, show_chosen_column_for_protocol

"""
ftp()

unzip()

init_db()

push_files_to_db()

show_all_for_protocol("TCP")
"""

show_sum_for_protocol("DNS")

show_chosen_column_for_protocol("ip_dest", "OCSP")
