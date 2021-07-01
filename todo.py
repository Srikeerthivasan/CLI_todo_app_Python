
### This is code is done by SRIKEERTHIVASAN SA and tested in Windows ###


import sys
import os
from datetime import date
import re

def g_help():                                                                                           # Function to get help
   print("Usage :-\n" + 
            "$ ./todo add \"todo item\"  # Add a new todo\n" +
            "$ ./todo ls               # Show remaining todos\n"+
            "$ ./todo del NUMBER       # Delete a todo\n"+
            "$ ./todo done NUMBER      # Complete a todo\n"+
            "$ ./todo help             # Show usage\n"+
            "$ ./todo report           # Statistics"
        )
def add(new_task):                                                                                      # Function that adds a new task
        if os.path.exists("todo.txt") == False:
                with open("todo.txt","w") as file:
                        file.write(new_task+'\n');
                print('Added todo: '+'"'+new_task+'"')
        else:
                with open("todo.txt","a") as file:
                        file.write(new_task+'\n');
                print('Added todo: '+'"'+new_task+'"')

def ls():                                                                                               # Function to print remaining tasks
        count = 0
        if os.path.exists("todo.txt") == False:
                print("There are no pending todos!")
        else:
                with open("todo.txt") as file:
                        lines = file.readlines()
                        for line in lines:
                                count += 1;
                        if count == 0:
                                print("There are no pending todos!")
                        else:
                                for line in reversed(lines):
                                        print(('[' + str(count) + ']' + ' ' +line),end='')
                                        count -= 1
def delete(ln_num):                                                                                     # Function to delete a task
        count = 0
        with open("todo.txt","r") as file:
                lines = file.readlines()
                for line in lines:
                        count += 1
        if ln_num > count or ln_num <= 0:
                print("Error: todo #" + str(ln_num) + " does not exist. Nothing deleted.")
        else:
                del lines[ln_num-1];
                with open("todo.txt","w") as file:
                        for line in lines:
                                file.write(line)
                        print("Deleted todo #" + str(ln_num))
def done(ln_num):                                                                                       # Function to mark a task as done
        today = date.today()
        d = today.strftime("%Y-%m-%d")
        count = 0
        with open("todo.txt","r") as file:
                lines = file.readlines()
                for line in lines:
                        count += 1
        if ln_num > count or ln_num <= 0:
                print("Error: todo #" + str(ln_num) + " does not exist.")
        else:
                if os.path.exists("done.txt") == False:
                        with open("done.txt","w") as file:
                                file.write("x " + d + ' ' +lines[ln_num-1]);
                        print("Marked todo #" + str(ln_num) + " as done.")
                else:
                        with open("done.txt","a") as file:
                                file.write("x " + d + ' ' +lines[ln_num-1]);
                        print("Marked todo #" + str(ln_num) + " as done.")
        del lines[ln_num-1];
        with open("todo.txt","w") as file:
                for line in lines:
                        file.write(line)
def report():                                                                                           # Function to give statistics
        ct_pending=0
        ct_completed=0
        global lat_date
        with open("todo.txt","r") as file:
                lines = file.readlines()
                for line in lines:
                        ct_pending += 1
        with open("done.txt","r") as file:
                lines1 = file.readlines()
                for line in lines1:
                        ct_completed += 1
        result = re.search(r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", lines1[ct_completed-1])
        print(result[1] + " Pending : " + str(ct_pending) + " Completed : " + str(ct_completed))

        
def main():                                                                                             # Driver function
        if len(sys.argv) <= 1:
                g_help()
        else:
                function = sys.argv[1];

                if (function == "help"):
                        g_help()
                elif (function == "add"):
                        if len(sys.argv) <= 2:
                                print ("Error: Missing todo string. Nothing added!");
                        else:
                                add(sys.argv[2])
                elif (function == "ls"):
                        ls()
                elif (function == "del"):
                        if len(sys.argv) <= 2:
                                print ("Error: Missing NUMBER for deleting todo.");
                        else:
                                delete(int(sys.argv[2]))
                elif (function == "done"):
                        if len(sys.argv) <= 2:
                                print ("Error: Missing NUMBER for marking todo as done.");
                        else:
                                done(int(sys.argv[2]))
                elif (function == "report"):
                        report()

if (__name__ == "__main__"):
        main();
