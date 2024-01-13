# Imports from personal library
from utilities.vector import vector
import utilities.algos as algos
import utilities.io as io

# Imports from standard libraries I find myself using all the time
from collections import defaultdict
from collections import deque

import math
import itertools

try:
	input_lines = io.read_input_as_lines(17)
	example_lines = io.read_example_as_lines(17)
except:
	input_lines = ["Input Lines Not Found"]
	example_lines = ["Example"]

def do_part_one_for(lines):
	bound_def = algos.erase(lines[0], ["target area: x=", ",", "y="])
	xbound = ([int(n) for n in bound_def.split(" ")[0].split("..")])
	ybound = ([int(n) for n in bound_def.split(" ")[1].split("..")])

	# The function to define the probe's position after each step is:
	#
	#	Let vx be the initial x velocity, vy the initial y velocity, t be the 
	# 	time 
	#
	#		Sum of i in [0, n] is n * (n + 1) // 2
	#
	#		xt = x0 + max(vx - (t * (t + 1)) // 2), 0)
	#
	#		x0 = x
	#		x1 = x0 + vx
	#		x2 = x1 + vx - 1
	#		x3 = x2 + vx - 2


	#		x3 = ((x0 + vx) + vx - 1) + vx - 2
	#		x3 = x0 + 3vx - 3
	
	#
	#		xt = x0 + (t * vx) - max((t * (t + 1)) // 2), t * vx)

	# Range of x:	v.x + (t * v.x - t * (t + 1) // 2) for t in range(v.x)
	#
	# MAX X = X + (tX - t * (t + 1) / 2) => X + X^2 - (X^2 + X) / 2 = DX
	#  => 2X + 2X^2 - (X^2 + X) = DX
	#  => 2X + 2X^2 - X^2 - X = DX
	#  => X^2 + X = DX
	#
	# So if X is an integer and X^2 + X = [value in range of x], then it could
	# be what we want.

	# The x value X of locations in the probe's arc is given by the function:
	# vx + vx^2 - vx(vx + 1)/2, where vx is the chosen x velocity. We know that 
	# we want X to be in a specific range; so if we iterate over that range and
	# use the quadratic formula to solve for vx, we can see at which X values vx
	# would be an integer.
	x_vals = []
	for dest_x in range(xbound[0], xbound[1] + 1):
		x = (-1 + math.sqrt(1 + 8 * dest_x)) / 2
		if int(x) == x:
			x_vals.append(x)

	# The best y value we can get for this arc can be found by using the 
	# derivative: 2x - 1 / x + 1. When d/dx = 0, y is at it's peak.
	#
	#	(2dx - 1)/2 + 1 = 0
	#	(2dx - 1)/2 = -1
	#	2dx - 1 = -2
	#	2dx = -1
	#	dx = -1/2
	#	
	# 	So the highest point in each arc is where:
	# 		vy = -1/2 (vx + vx^2 - vx(vx + 1)/2)
	#
	#	For given vx values. 
	for 

	print()
	
	#plot = defaultdict(lambda: " ")
	#plot[vector()] = "S"
	#for x, y in itertools.product(range(20, 31), range(-10, -4)):
	#	plot[vector(x, y)] = "T"
	#
	#init_vel = vector(7, 2)
	#for t in range(10):
	#	T = min(t, init_vel.x)
	#	dx = T * init_vel.x - T * (T + 1) // 2
	#	dy = t * init_vel.y - t * (t + 1) // 2
	#	dv = vector(dx, dy) + init_vel
	#	plot[dv] = "#"
	#
	#new_plot = defaultdict(lambda: " ")
	#for v in plot:
	#	new_plot[vector(v.x, -v.y)] = plot[v]
	#plot = new_plot
	#
	#algos.print_map(plot, bounds=800)

	

def do_part_two_for(lines):
	pass

def solve_p1():
	print(f"PART ONE\n--------\n")
	print(f"What is the best starting velocity that you can use to cause a prob"
       	  f"e to be within a specified region at the end of an integer step?\n")

	results = do_part_one_for(example_lines)
	print(f"When we do part one for the example input:")
	print(f"\tThe <THING THEY WANT> is {results}")
	print(f"\tWe expected: <SOLUTION THEY WANT>\n")

	results = do_part_one_for(input_lines)
	print(f"When we do part one for the actual input:")
	print(f"\tThe <THING THEY WANT> is {results}\n")

def solve_p2():
	return
	print(f"PART TWO\n--------\n")
	print(f"This is the prompt for Part Two of the problem.\n")

	results = do_part_two_for(example_lines)
	print(f"When we do part two for the example input:")
	print(f"\tThe <THING THEY WANT> is {results}")
	print(f"\tWe expected: <SOLUTION THEY WANT>\n")

	results = do_part_two_for(input_lines)
	print(f"When we do part two for the actual input:")
	print(f"\tThe <THING THEY WANT> is {results}\n")

def print_header():
	print("--- DAY 17: <TITLE GOES HERE> ---\n")
