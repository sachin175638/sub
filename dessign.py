#!/bin/env python2
def sachin():
 import os

 #os.system("clear")
 #print "\033[1;31m -------------------------------------------"
 #os.system("figlet =+DSS+=")
 #print "\033[1;31m -------------------------------------------"
 #print "\033[1;32m       coded by sachin mmct"
 print "VTU -- Module 2"
 print "\033[1;34m code book : IS800:2007"
 select = raw_input("area is given y/n :")
 if select == "y":
  l = input("Enter length :- ")
  b = input("Enter bredth :- ")
  ag = l*b
  print "Area of plate = ", ag,"mm square"
 else:
  print "continued"
 Fu1 = input("Enter factorial load :- ")
 Fu = Fu1*1000
 d = input("Entet dia of bolt d :- ")
 fub = input("Enter property class fub :- ")
 print "if fu is not given take 410 n/mm square "
 fu = input("Enter strength of plate fu :- ")
 os.system("sleep 2")
 print " ------------------------------"
 print "|standard clearance in diameter|"
 print "|and width of slot             |"
 print " ------------------------------"
 print "refer page no 73"
 #os.system("clear")
 print "Note: 12 - 14 is 1.0"
 print "Note: 16 - 22 is 2.0"
 print "Note: >24 is     3.0"
 su = input("Select clearance :- ")
 do = d+su
 print "-----------------------------------"
 print "\033[1;32m diameter of hole do is :- ",do ,"mm"
 print "-----------------------------------"
 if d >= 16:
	 e = 1.5*do
	 print "------------------------------"
	 print "\033[1;32m edge distance e is : ", e ,"mm"
	 print "------------------------------"
 else:
	 e = 1.7*do
	 print "------------------------------"
	 print "\033[1;32m edge distance e is : ", e ,"mm"
	 print "------------------------------"
 p = 2.5*d
 print "----------------------"
 print "\033[1;32m pitch p is : ", p ,"mm"
 print "----------------------"
 os.system("sleep 2")
 print "\033[1;34m a) Shear capicity of the bolt "
 print "refer page no 75 "
 nn = input("Enter the value of nn : ")
 ns = input("Enter the value of ns : ")
 Asb = (3.142*d*d)/4
 print "---------------------"
 print "\033[1;32m Asb is ", Asb ,"mm*mm"
 print "---------------------"
 Anb = (0.78*3.142*d*d)/4
 print "\033[1;32m Asb is ", Anb ,"mm*mm"
 vnsb = (fub/3**0.5)*((nn*Anb)+(ns*Asb))
 vnsb1 = vnsb/1000
 print "-------------------"
 print "\033[1;32m vnsb is = : ", vnsb1,"KN"
 print "-------------------"
 os.system("sleep 2")

 print "now refer page no 30 "
 gama_m0 = 1.10
 gama_m1 = 1.25
 gama_mb = 1.25
 gama_ml = 1.25
 gama_mf = 1.25
 gama_mw = 1.25
 vdsb = vnsb/gama_mb
 vdsb1 = vdsb/1000
 print "--------------"
 print "\033[1;32m vdsb : ", vdsb1,"KN"
 print "--------------"
 os.system("sleep 2")
 print "\033[1;34m b) bearing strength of bolt"
 kb1 = e/(3*do)
 kb2 = p/(3*do)-0.25
 kb3 = fub/fu
 kb4 = 1
 print " kb =",kb1
 print " kb =",kb2
 print " kb =",kb3
 print " kb =",kb4
 kb = input("select least value of kb : ")
 print "if thickness is not given assume your self "
 t = input("select least thickness : ")
 vnpb = 2.5*kb*d*t*fu
 vnpb1 = vnpb/1000
 print "------------------------"
 print "\033[1;32m value of vnpb is : ", vnpb1,"KN"
 print "------------------------"
 vdpb = vnpb/gama_mb
 vdpb1 = vdpb/1000
 print "--------------------------"
 print "\033[1;32m value of vdpb is : ", vdpb1,"KN"
 print "--------------------------"
 print ""
 print "Number of bolt required "
 if vdsb < vdpb:
 	bolt1 = Fu/vdsb
 	print "No of bolt is ", bolt1
 	bolt = input("no of bolt nearly equal to :- ")
 	print " therefore number of bolt is :- ",bolt
 else:
	bolt1 = Fu/vdpb
	print "No of bolt is ", bolt1
	bolt = input("no of bolt nearly equal to :- ")
	print " therefore number of bolt is :- ",bolt
 if select == "y":
	 print "Design strength of the solid plate"
	 print "Refer page no 30 "
	 sp1 = (fu*ag)*gama_m0
	 sp = sp1/1000
	 print ""
	 print "strength of solid plate is :", sp,"KN"
	 print ""
	 eff = vdsb/sp
	 print "efficiency of the joint is :- ", eff,"%"

