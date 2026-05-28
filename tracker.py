#docstring Christchurch Tigers-players database application
#imports
import sqlite3

#contant and variables
DATABASE = "team"
#functions
#when user input 1.
def print_all_player():
    '''print all the playername nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from players;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"Name                          Date           Attendance     Score")
    for player in results:
        print(f"{player[1]:<30}{player[2]:<15}{player[3]:<15}{player[4]:<6}")
    #loop finish here
    db.close()
#when user input 2.
def print_all_player_by_name():
    '''print all the players stored by name'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from players order by playername desc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"Name                          Date           Attendance     Score")
    for player in results:
        print(f"{player[1]:<30}{player[2]:<15}{player[3]:<15}{player[4]:<6}")
    #loop finish here
    db.close()
#when user input 3.
def print_all_player_by_attendance():
    '''print all the players stored by attendance'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from players order by attendance desc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"Name                          Date           Attendance     Score")
    for player in results:
        print(f"{player[1]:<30}{player[2]:<15}{player[3]:<15}{player[4]:<6}")
    #loop finish here
    db.close()
#when user input 4.
def print_all_player_by_score():
    '''print all the players stored by point scored'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from players order by pointscored desc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"Name                          Date           Attendance     Score")
    for player in results:
        print(f"{player[1]:<30}{player[2]:<15}{player[3]:<15}{player[4]:<6}")
    #loop finish here
    db.close()

#main code
while True:
    user_input = input(
'''
What would you like to do. Please input number 1 ~ 5
1. Print all players
2. Print all players by names
3. Print all players by attendance
4. Print all players by point scored
5. Exit
'''
    )
    if user_input == "1":
        print_all_player()
    elif user_input == "2":
        print_all_player_by_name()
    elif user_input == "3":
        print_all_player_by_attendance()
    elif user_input == "4":
        print_all_player_by_score()
    elif user_input == "5":
        break
    else:
        print("That was not an opition\n")