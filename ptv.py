# -*- coding: utf-8 -*-

#ptv.py by Piotr Kozieł

"""
This program will get TV schedule from txt files and let user choose to see what's currently,
or at specified hour, on chosen TV station.
"""

from os import system
from os import name
from os import path
from datetime import datetime
from time import sleep, strftime


# creates dictionary of stations based on txt file.
# creates keys only if there is file with a schedule for station in list
def count_lines(f_stations):
    list_of_stations = {}
    f = open(f_stations, "r")
    i=0
    for station in f:
        s = station.replace("\n", "")
        if path.isfile("schedules/%s.txt" %s) == True:
            list_of_stations[i+1] = s
            i+=1
    f.close()
    return list_of_stations


#displays welcome screen
def welcome_screen():
    system("cls" if name == "nt" else "clear")

    print("========================")
    print("   TV schedule v. 0.95   ")
    print("release date: 23.07.2018")
    print("========================\n")


#allows user to choose which TV station's schedule she/he wants to check
def choose_station(STATIONS_DICT, f_station):
    print("TV stations:")
    count = STATIONS_DICT
    for i in count:
        print("%s. %s" % (i, count[i]))
#////////////INPUT PROTECTION\\\\\\\\\\\\\\\
    cor = True
    while cor:
        stat_choice = input("Choose TV station (number): ")
        try:
                int(stat_choice)
                cor = True
        except:
            cor = False
        if cor is False or int(stat_choice) < 1 or int(stat_choice) > len(count):
            print("wrong choice, no such station on the list")
            cor = True
            break
        else:
            cor = False
    stat_choice = int(stat_choice)
    return stat_choice


# prints current program on chosen station
def now_schedule(cur_stat):
    with open("schedules/%s.txt" % cur_stat, "r") as f:
        f = f.readlines()
    f1 = f[::3]
    f2 = f[1::3]
    i = 0
    for hour in f1:
        hour = hour.replace("\n", "")
        # hour = datetime.strptime(hour, "%H:%M")
        f1[i] = hour
        i += 1
    i = 0
    for show in f2:
        show = show.replace("\n", "")
        f2[i] = show
        i += 1
    d = {}
    tuple = list(zip(f1, f2))
    i = 1
    for tu in tuple:
        d[i] = tu
        i += 1

    t = strftime("%H:%M")

    di = 0
    for key in d.keys():
        if (datetime.strptime(t, "%H:%M") >= (datetime.strptime(f1[di], "%H:%M"))) and (
                datetime.strptime(t, "%H:%M") < (datetime.strptime(f1[di + 1], "%H:%M"))):

            cur_program = str("%s,  %s" % d[key])
            print("\nAt this very moment on %s you can watch:" % cur_stat)
            print(">" * 5 + " " + cur_program + " " + "<" * 5),
        di += 1


# prints tv show on chosen station at chosen hour
def specific_hour(cur_stat):
    with open("schedules/%s.txt" % cur_stat, "r") as f:
        f = f.readlines()
    f1 = f[::3]
    f2 = f[1::3]
    i = 0
    for hour in f1:
        hour = hour.replace("\n", "")
        # hour = datetime.strptime(hour, "%H:%M")
        f1[i] = hour
        i += 1
    i = 0
    for show in f2:
        show = show.replace("\n", "")
        f2[i] = show
        i += 1
    d = {}
    tuple = list(zip(f1, f2))
    i = 1
    for tu in tuple:
        d[i] = tu
        i += 1
    check = True
    while check:
        try:
            t = input("What time should I check? [HH:MM]: ")

            di = 0
            for key in d.keys():
                if (datetime.strptime(t, "%H:%M") >= (datetime.strptime(f1[di], "%H:%M"))) and (
                        datetime.strptime(t, "%H:%M") < (datetime.strptime(f1[di + 1], "%H:%M"))):
                    cur_program = str("%s,  %s" % d[key])
                    print("\nAt %s on %s you can watch:" % (t, cur_stat))
                    print(">" * 5 + " " + cur_program + " " + "<" * 5),
                di += 1
                check = False
        except:
            print("Wrong format, please try again.")
            check = True


# prints chedule forr all day
def daily_schedule(cur_stat):
    print("Loading today's schedule for %s station" % cur_stat)
    sleep(1)
    print("--")
    sleep(1)
    print("--"*2)
    sleep(1)
    print("--"*3)
    sleep(1)
    f = open("schedules/%s.txt" % cur_stat)
    print (f.read())
    f.close()


# prints chosen station schedule
def choose_schedule(STATIONS_DICT, f_stations):
    cur_stat = STATIONS_DICT[choose_station(STATIONS_DICT, f_stations)]
    welcome_screen()
    print("You have chosen %s station" % cur_stat)
    print("What do you want to check?\n")
    print("1. What is now on %s?" % cur_stat)
    print("2. Check TV program for specified hour.")
    print("3. See today's schedule.")
    print("4. Exit.")
    opt_choice = input("\nSelect number: ")
    c = True
    while c == True:
        if opt_choice == "1":
            now_schedule(cur_stat)
            c = False
        elif opt_choice == "2":
            specific_hour(cur_stat)
            c = False
        elif opt_choice == "3":
            daily_schedule(cur_stat)
            c = False
        elif opt_choice == "4":
            print("You chose not to watch TV.")
            print("Maby go swimming?")
            c = True
        else:
            c = True

def main():
    f_stations = "schedules/st_lst.txt"
    run = True
    STATIONS_DICT = count_lines(f_stations)
    while run == True:
        welcome_screen()
        choose_schedule(STATIONS_DICT, f_stations)
        cont = input("\nDo you want to check something else? [Y/N]")
        cont = cont.upper()
        if cont != "Y":
            break

main()


