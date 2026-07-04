#!/usr/bin/env python3

import os
import sys
import csv

username = os.environ['username']
password = os.environ['password']

with open("users", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ":")
    for row in file_reader:
        if row[0] == username and row[1] == password and row[0] != "":
            sys.exit(0)

sys.exit(1)
