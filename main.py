from database import *
from fingerprint import match_fingerprint
import os

create_table()

def register():
    name = input("Enter name: ")
    fp = input("Enter fingerprint image path: ")

    filename = os.path.basename(fp)
    os.system(f"copy {fp} fingerprints/{filename}")

    add_voter(name, filename)
    print("Voter Registered Successfully!")

def vote():
    fp = input("Enter fingerprint image path: ")
    match = match_fingerprint(fp)

    if not match:
        print("Fingerprint not recognized!")
        return

    voters = get_voters()

    for v in voters:
        if v[2] == match:
            if v[3] == 1:
                print("Already voted!")
                return

            print(f"Welcome {v[1]}")
            print("1. Party A\n2. Party B")
            choice = input("Enter choice: ")

            mark_voted(v[0])
            print("Vote cast successfully!")
            return

    print("No voter found!")

def menu():
    while True:
        print("\n1. Register\n2. Vote\n3. Exit")
        ch = input("Choice: ")

        if ch == '1':
            register()
        elif ch == '2':
            vote()
        else:
            break

menu()
