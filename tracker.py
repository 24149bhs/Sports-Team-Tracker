#docstring Christchurch Tigers-players database application
#imports
import sqlite3

#contant and variables
DATABASE = "team"
#functions
def print_all_playername():
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
#main code
print_all_playername()