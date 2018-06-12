#!usr/bin/python
import time
import os
import commands
import webbrowser

x ='''
Press 1 :  To check current time and date
Press 2 :  To create a  file 
Press 3 :  To create  a directory  
Press 4 :  To logout system
Press 5 :  To search something on google 
Press 6 :  To reboot your OS  
Press 7 :  To check Internet connection
Press 8 :  To login whatsapp on browser
press 9  : to check all connected  IP in your network
'''
print x

choice = int(raw_input("Enter your choice "))

if choice == 1 :
    print "Showing date and time...", time.ctime().split()[2],time.ctime().split()[1] ,time.ctime().split()[3]

elif choice == 2:
    file = raw_input("Enter the name of new file  ")
    print "Creating a new file...",commands.getoutput('touch ' + file)

elif choice == 3:
    file1 = raw_input("Enter the name of new directory  ")
    print "Creating a new directory...",commands.getoutput('mkdir ' + file1)

elif choice == 4:
   print "Logging out..."
   time.sleep(3)
   commands.getoutput('gnome-session-quit')

elif choice == 5:
   msg = raw_input("Enter to search on google  ")
   webbrowser.open_new_tab("https://www.google.com/search?q="+msg)
   
elif choice == 6:
   print "Rebooting..."
   time.sleep(3)
   os.system("reboot")

elif choice == 7:
   print "Checking internet connection..."
   webbrowser.open_new_tab("https://www.google.com")

elif choice == 8:
   webbrowser.open_new_tab("https://web.whatsapp.com/")

elif choice == 9:
   os.system(" sudo nmap -sn 192.168.0.0/24")

else :
   print "Wrong choice" 
