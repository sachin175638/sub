#/bin/env python2
import os
import dss
import dessign
import design2
import zig

while 1:
 try:
	os.system("clear")
	print "\033[1;31m -------------------------------------------"
	os.system("figlet =+DSS+=")
	print "\033[1;31m -------------------------------------------"
	print "\033[1;32m       coded by sachin mmct"
	print ""
	print "1 - basics"
	print "2 - design"
	print "3 - design2"
	print "4 - exit"
	print ""
	select = input("Select your option :- ")
	#if select == "":
	#	print "ENTER the value.."
	#	print ""
	#	san = raw_input("Press enter to continue ..")
	if select == 1:
		dss.ajay()
		san = raw_input("Press enter to continue ..")
	elif select == 2:
		dessign.sachin()
		san = raw_input("Press enter to continue ..")
	elif select == 3:
		while 2:
			os.system("clear")
			print "==========================="
			print "1 - lap&butt"
			print "2 - zizag bolt"
			print "3 - menue"
			print ""
			selectt = input("select :- ")
			if selectt == 1:
				design2.sanj()
				san = raw_input("Press enter to continue ..")
			elif selectt == 2:
				zig.amma()
				san = raw_input("Press enter to continue ..")
			elif selectt == 3:
				break
			else:
				print "wrong selection..."
				os.system("sleep 1")
		san = raw_input("Press enter to continue ..")
	elif select == 4:
		print "bye bye .."
		break
	else:
		print "wrong selection..."
		os.system("sleep 1")
 except SyntaxError:
  print ""
  xx = raw_input(" you entered nothing..>> press enter ")
