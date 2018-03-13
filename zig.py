#!/bin/env python2
def amma():
 import os
 
 print ""
 d = input("\033[1;34m Enter dia of bolt in mm :- ")
 t = input("\033[1;34m Enter least thickness :- ")
 psi = input("\033[1;34m Enter psi value :- ")
 boltz = input("\033[1;34m Enter number of bolts :- ")
 fub = input("\033[1;34m Entet fub :- ")
 print ""
 print "If fu is not given assume 410 n/mm square "
 fu = input("\033[1;34m Enter fu value :- ")
 if d < 16:
	 do = d+1.0
	 print "\033[1;32m d not 'do' = ", do,"mm"
 elif d > 24:
	 do = d+3.0
	 print "\033[1;32m d not is ", do,"mm"
 else:
	 do = d+2.0
	 print "\033[1;32m d not is ", do,"mm"
 edge = raw_input("\033[1;34m Edge distance is given y/n :- ")
 pitch = raw_input("\033[1;34m Pitch distance is given y/n :- ")
 if edge == "y":
	 e = input("\033[1;34m Enter edge distance :- ")
 else:
	 if d >= 16:
		 e1 = 1.5*do
		 print "edge distance e is :- ", e1,"mm"
		 e = input("\033[1;32m Make nearly equal to :- ")
	 else:
		 e1 = 1.7*do
		 print "edge distance e is :- ", e1,"mm"
		 e = input("\033[1;32m Make nearly equal to :- ")
 if pitch == "y":
	 p = input("\033[1;34m Enter pitch value :- ")
 else:
	 p1 = 2.5*d
	 print ""
	 print "pitch value p ie :-", p1,"mm"
	 p = input("\033[1;32m Make it nearly equal to :- ")
 print ""
 print "\033[1;34m a) Shear strength of bolt"
 nn = input("\033[1;34m Enter nn value :- ")
 ns = input("\033[1;34m Enter ns value :- ")
 selt = raw_input("\033[1;34m Factor load is given y/n :- ")
 Asb = (3.142*d*d)/4
 Anb = 0.78*Asb
 vnsb = (fub/3**0.5)*((nn*Anb)+(ns*Asb))
 gama_mb = 1.25
 vdsb1 = vnsb/gama_mb
 vdsb2 = vdsb1/1000
 vdsb = vdsb2*boltz
 print "\033[1;32m Therefore number of bolts is :- ", vdsb,"kN"
 print ""
 print "\033[1;34m Bearing capacity "
 kb1 = e/(3*do)
 kb2 = (p/(3*do))-0.25
 kb3 = fub/fu
 kb4 = 1
 print "  kb = ", kb1
 print "  kb = ", kb2
 print "  kb = ", kb3
 print "  kb = ", kb4
 print ""
 kb = input("\033[1;34m Select kb value :- ")
 vnpb = 2.5*kb*t*d*fu
 vdpb1 = vnpb/gama_mb
 vdpb2 = vdpb1/1000
 vdpb = vdpb2*boltz
 print "\033[1;32m therfore vdpb is :- ", vdpb,"kN" 
 print ""
 print "\033[1;34m c) Tensile strength of joint "
 print ''
 b = input("\033[1;34m Enter b value :- ")
 g = input("\033[1;34m Enter g value :- ")
 while 1:
 	print "\033[1;34m Failure end section "
 	print "------------------- "
 	print " 1 try full section "
 	print " 2 finish "
 	print ""
 	select = input("select your option :- ")
 	if select == 1:
# 		b = input("Enter b value :- ")
 		zig = input("Enter number of zig :- ")
 		n = input("Enter n value :- ")
 		AN = (b-(n*do)+((zig*psi*psi)/(4*g)))*t
 		gama_m1=1.25
 		Td1 = (0.9*AN*fu)/gama_m1
 		Td2 = Td1/1000
 		Td = Td2
		print "\033[1;33m therefore Td is :- ", Td,"kN"
 		xx = raw_input("\033[1;34m Press enter .. ")
 	elif select==2:
 		Td = input("\033[1;34m select least Td :- ")
 		break
 print "Strength of solid plate "
 ANN = b*t
 Tdn1 = (0.9*ANN*fu)/gama_m1
 Tdn = Tdn1/1000
 print "\033[1;32m Therefore Tdn is :- ", Tdn,"kN"
 eff = (Td/Tdn)*100
 print "\033[1;32m Therfore efficiency is :- ", eff,"%"
 print ""
 if selt == "y":
 	Fu = input("\033[1;34m Enter factor load :- ")
 	strength = Fu/boltz
 	print "\033[1;32m Strength of individual bolt is :- ", strength,"kN"
 
