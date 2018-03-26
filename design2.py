#!/bin/env python2
# coded by sachin
def sanj(): 
 import os

 print ""
 print " If dia is not given assume .."
 print ""
 d = input("\033[1;34m Enter diameter of bolt d :- ")
 t = input("\033[1;34m Enter least thickness t :- ")
 if d < 16:
	 do = d+1.0
	 print "\033[1;32m d not is ", do,"mm"
 elif d > 24:
	 do = d+3.0
	 print "\033[1;32m d not is ", do,"mm"
 else:
	 do = d+2.0
	 print "\033[1;32m d not is ", do,"mm"
 selc = raw_input("Edge distance is given y/n :-  ")
 selt = raw_input("Pitch is given p y/n :-        ")
 sect = raw_input("factor load given y/n :-       ")
 scet = raw_input("area of plate given y/n :-     ")
 stec = raw_input("Number of bolt is given y/n :- ")
 if selc == "y":
	 e = input("\033[1;34m Enter edge distance or assume e :- ")
 else:
	 if d >= 16:
	 	e1 = 1.5*do
	 	print "\033[1;32m Value of e is :- ", e1,"mm"
	 	e = input("\033[1;34m Make 'e' nearly equal to :- ")
	 	print "\033[1;32m Edge distance e is ", e,"mm"
	 else:
		e1 = 1.7*do
		print "\033[1;32m Value of e is :- ", e1,"mm"
		e = input("\033[1;34m Make 'e' nearly equal to :- ")
		print "\033[1;32m Edge distance e is ", e,"mm"
 if selt == "y":
	 p = input("\033[1;34m Enter pitch value or assume p :- ")
 else:
	 p1 = 2.5*d
	 print "\033[1;32m Value of p is :- ", p1,"mm"
	 p = input("\033[1;34m Make 'p' nearly equal to :- ")
	 print "\033[1;32m Pitch p is :- ", p,"mm"
 fub = input("\033[1;34m Enter property class fub :- ")
 print ""
 print "fu is not given assume 410 n/mm square "
 print ""
 fu = input("\033[1;34m Enter fu value :- ")
 if sect == "y":
	 print "-----------------------"
	 print "1 - factor load"
	 print "2 - unfactor load"
	 print ""
	 sanj = input("Select :- ")
	 if sanj == 1:
		 Fu = input("\033[1;34m Enter factor load :- ")
	 elif sanj == 2:
		 print "\033[1;32m Refer page no 29 "
		 print "table number 4 "
		 print "   (1)     (2)  (3)  (4)  (5) (6) (7) (8) (9) (10)"
		 print "DL+LL+CL   1.5  1.5  1.05  _   _  1.0 1.0 1.0  _"
		 print "DL+LL+CL+  1.2  1.2  1.05 0.6  _  1.0 1.8 0.8 0.8"
		 print "WL/EL      1.2  1.2  0.53 1.2"
		 print "DL+WL/EL    _    _    _   1.5  _  1.0  _   _   1.0"
		 print "DL+ER       _    1.2  _    _ "
		 print "DL+LL+AL   1.0  0.35 0.35  _  1.0"
		 print ""
		 o = input("Select from table :- ")
		 uFu1 = input("unfactored load :- ")
		 uFu = uFu1*o
		 print "\033[1;32m Therefore ", uFu,"kN"
 elif sect == "n":
	 print "continued ...."
 if scet == "y":
	 l = input("\033[1;34m Enter length :- ")
	 b = input("\033[1;34m Enter breadth :- ")
	 ag =l*b
	 print "\033[1;32m therefore area of plate is :-", ag,"mm square"
 else:
	 print ""

 print "a) shear capacity of bolt "
 print ""
 nn = input("\033[1;34m Enter nn value :- ")
 ns = input("\033[1;34m Enter ns value :- ")
 asb = (3.142*d*d)/4
 anb = 0.78*asb
 vnsb = (fub/3**0.5)*((nn*anb)+(ns*asb))
 gama_mb = 1.25
 vdsb1 = vnsb/gama_mb
 vdsb5 = vdsb1/1000
 redu = raw_input("reduction factor y/n :- ")
 if stec == "y":
	 boltz = input("\033[1;34m Enter number of bolt :- ")
	 vdsb = vdsb5*boltz
	 print "\033[1;32m therefore vdsb is :- ", vdsb,"kN"
# redu = raw_input("reduction factor y/n :- ")
 elif redu == "y":
	 tpk = input("\033[1;34m Enter packing plate value tpk :- ")
	 x = 15*d
	 y = 5*d
	 w = 1-0.0125*tpk
	 print " 1 - 15xd = ", x,"mm"
	 print " 2 - 5xd = ", y,"mm"
	 print " 3 - beta_pk = ", w,"mm"
	 print ""
	 q = input("select value :- ")
	 vdsb2 = vdsb5
	 vdsb = vdsb2*q
	 print "\033[1;32m therefore vdsb value is :- ", vdsb,"kN"
 else:
	vdsb = vdsb5 
	print "therefore vdsb is : ", vdsb,"kN"

 print ""
 print "b) Bearing capacity"
 kb1 = e/(3*do)
 kb2 = (p/(3*do))-0.25
 kb3 = fub/fu
 kb4 = 1
 print "  kb = ", kb1
 print "  kb = ", kb2
 print "  kb = ", kb3
 print "  kb = ", kb4
 print ""
 kb = input("Select kb value :- ")
 vnpb = 2.5*kb*t*d*fub
 vdpb1 = vnpb/gama_mb
 if stec == "y":
	 boltz = input("Enter number of bolt :- ")
	 vdpb2 = vdpb1/1000
	 vdpb = vdpb2*boltz
	 print "\033[1;32m vdpb value is :- ", vdpb,"kN"
 else:
	 vdpb = vdpb1/1000
	 print "\033[1;32m vdpb value is :- ", vdpb,"kN"
 if stec == "n":
	 if sect == "y":
		 if sanj == 1:
			 if vdsb < vdpb:
				 bolt1 = Fu/vdsb
				 print "\033[1;32m no of bolt is :- ", bolt1
				 boltz = input("make nearly equal to :- ")
			 else:
				 bolt1 = Fu/vdpb
				 print "\033[1;32m no of bolt is :- ", bolt1
				 boltz = input("make nearly equal to :- ")
		 elif sanj == 2:
			 if vdsb < vdpb:
				 bolt1 = uFu/vdsp
				 print "\033[1;32m no of bolt is :- ", bolt1
				 boltz = input("make nearly equal to :- ")
			 else:
				 bolt1 = uFu/vdpb
				 print "\033[1;32m no of bolt is :- ", bolt1
				 boltz = input("make nearly equal to :- ")

 print ""
 print "Tensile strength of joint "
 print "refer page no 32"
 gama_m1 = 1.25
 bb = input("\033[1;34m analyse edge and pitch :- ")
 AN = (bb-boltz*do)*t
 Tdn1 = (0.9*AN*fu)/gama_m1
 Tdn = Tdn1/1000
 print ""
 print "\033[1;32m therefore Tdn is :- ", Tdn ,"kN"
 print ""
 print "Strength of solid plate"
 print ""
 ANN = bb*t
 Tdnn1 = (0.9*fu*ANN)/gama_m1
 Tdnn = Tdnn1/1000
 print "\033[1;32m therefore Tdn is :- ", Tdnn ,"kN"
 #print "Efficiency"
 if vdsb < vdpb:
	 eff = (vdsb/Tdnn)*100
	 print "\033[1;32m Efficiency is :- ", eff,"%"
 else:
	 eff = (vdpb/Tdnn)*100
	 print "\033[1;32m Efficiency is :- ", eff,"%"
 print ''
 check = raw_input("Want to check strength of individual bolt y/n :- ")
 if sect == "y":
	if check == "y":
		if sanj == 1:
			strength = Fu/boltz
			print "Strength of individual bolt is : ", strength,"kN"
		elif sanj == 2:
			strength = uFu/boltz
			print "Strength of individual bolt is : ", strength,"kN"
