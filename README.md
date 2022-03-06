# Helkur Traffic Stats Collector
> Amazing tool for network traffic capturing and analysis.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)

## General info
Simple tool for collecting network traffic information from a chosen device. 

## Technologies
* Bash Shell
* Python 3.7.2
* mySQL sever version 10.1.37
* Apache

## Setup
* Set up your ftp server on linux via sudo apt install vsftpd - google how to change config and set up users
* Run traffic_scraper.sh on your linux server - set it up as a cron job and adjust tcpdump parameters to suit your needs
* Port Python files to a new project
* Via XAMPP or any other way set up your apache server with MySQL
* Create a new database with the name you want and adjust the db_name in the python files
* Run main.py
* Enjoy!

## Features
* Network data collection:
    *  Time
    *  IP source address
    *  IP destination address
    *  TCP source port
    *  TCP destination port
    *  Protocol
    *  Packet size
* Data parsing and database collection
* Data filtering and basic analytic tools
    *  By time
    *  By protocol
    *  Packet size overview

## To-do list:
* Graphical user interface
* Detailed statistical analysis (over time)
* Report generation

## Status
Project is: _in progress_  
Further development in progress

## Inspiration
Project inspired by Darude and ATA 7.0 Capstone project.
