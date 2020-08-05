'''
 # @ Project: Chat
 # @ Author: Spinda Máté
 # @ Create Time: 2020-08-05 18:51:15
 # @ Email: mate.spinda01@gmail.com
 # @ GitHub: https://github.com/matespinda01/Chat
 # @ Licence: MIT

 # @ Description: Starting
 """[Command-line interface]"""


 '''

import curses
import sys
import math




"""[Define backspace and enter just in case]
"""
class KEYS: 
    BS = [curses.KEY_BACKSPACE, curses.KEY_DC, 127]
    ENTER = [curses.KEY_ENTER, 10, 13]
    isRunning = False
   

"""[Screen setup]"""


screen = curses.initscr()
screen.scrollok(1)
max_y,max_x = screen.getmaxyx()
curses.newwin(0,0,max_y,max_x)
curses.setsyx(0,12)
screen.refresh()
screen.addstr(1,12,'Welcome\n\n')

screen.refresh()



def helpMsg():
    """[Display the help message]
    """
    for i in range(max_y):
        screen.addch("=")
    screen.addstr("\n\n")
    screen.addstr("Start the server type: !start\n")
    screen.addstr("Stop the server: !stop\n")
    screen.addstr("Send message to all rooms: !broadcast <msg>\n")
    screen.addstr("Reload the server: !reload\n")
    screen.addstr("Display this message: !help\n")
    screen.addstr("\n")
   
    
    screen.refresh()
    for i in range(max_y):
        screen.addch("=")
    
    screen.refresh()
    screen.addstr("\n\n")
screen.refresh()

helpMsg()
def start():
    screen.addstr("Starting the server...\n")
    #TODO: Try run a server, if fails throw error and set isRunning to false
    screen.refresh()
    isRunning = True
    
#TODO: Methods for the remaining commands
#TODO: !!! IMPORT THE SERVER IF DONE
run = True
while run:
    def command(args):
        if(str(args) == "!start"):
            if(KEYS.isRunning == True):
                screen.addstr("Server is already running!\n")
                screen.refresh()
            else:
                KEYS.isRunning = True
                start()
                
           
        elif(args == "!reload"):
            reloadServer()
           
        elif(args == "!stop"):
            serverStop()
            
        elif(args == "!broadcast" or args == "!bc"):
            broadcast()
            
        elif(args == "!help"):
            helpMsg()
        else:
            screen.addstr("Invalid input, to see the full list of commands: !help\n")
        
            screen.refresh()
    
        

    userInput = screen.getstr().decode("utf-8") # Waiting for input
    command(userInput)

        

screen.refresh()

curses.endwin()



    
        


