#/bin/env python2
import os
import dss
import dessign

while 1:
	os.system("clear")
	print "\033[1;31m -------------------------------------------"
	os.system("figlet =+DSS+=")
	print "\033[1;31m -------------------------------------------"
	print "\033[1;32m       coded by sachin mmct"
	print ""
	print "1 - basics"
	print "2 - design"
	print "3 - exit"
	print ""
	select = input("Select your option :- ")
	if select == 1:
		dss.ajay()
		san = raw_input("Press enter to continue ..")
	elif select == 2:
		dessign.sachin()
		san = raw_input("Press enter to continue ..")
	elif select == 3:
		print "bye bye .."
		break
	else:
		print "wrong selection..."

