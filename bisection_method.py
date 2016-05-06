#!usr/bin/python

#############################################################################################################
#
# Author : P.C ROY
# Date & time : 06-05-2016 01:40:00
# Problem : Find the real root of equation x^3-x-4 = 0 using bisection method concept up to 3 decimal place
# Mathematical solution : https://www.youtube.com/watch?v=DMZj48icYnE
#
#############################################################################################################

from __future__ import division
import math   # This will import math module

# Bisection method
def bs_method():
	#a = input("Enter the value for a : ")
	#b = input("Enter the value for b : ")
	a = 1.701
	b = 1.801
	root = approximate_root(a, b)

	print("\n#########################################################################################################\n"
		  "# \t\t\t\t\tTable : Bisection table\t\t\t\t\t\t#"
		  "\n#########################################################################################################")
	print("\tn \t| a \t\t| b \t\t| x \t\t| fx\n"
		  "---------------------------------------------------------------------------------------------------------")

	count = 1
	while (count <= 11):
		fx = fx_func(root)
		print("\t{0} \t| {1} \t| {2} \t| {3} \t| {4}". format(count, a, b, round(root, 4), fx))

		if fx<0:
			x = approximate_root(root, b)
			a = round(root, 4)
			b = b
		else:
			x = approximate_root(a, root)
			a = a
			b = round(root, 4)

		print("---------------------------------------------------------------------------------------------------------")
		root = x
		count = count+ 1

# return the approximate root
def approximate_root(a, b):
	x = (a+b)/2
	return x

# return the value of x^3-x-4
def fx_func(x):
	fx = math.pow(x, 3)-x-4 #formula x^3-x-4 = 0
	return fx

bs_method()