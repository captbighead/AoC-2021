# Imports from personal library
from utilities.vector import vector
import utilities.algos as algos
import utilities.io as io

# Imports from standard libraries I find myself using all the time
from collections import defaultdict
from collections import deque

try:
	input_lines = io.read_input_as_lines(5)
	example_lines = io.read_example_as_lines(5)
except:
	input_lines = ["Input Lines Not Found"]
	example_lines = ["Example"]

def tween(a, b):
	dx = b[0] - a[0]
	dy = b[1] - a[1]
	d = max(abs(dx), abs(dy))
	twn = [a]
	step_x = dx//abs(dx) if dx else 0
	step_y = dy//abs(dy) if dy else 0
	for diff in range(d):
		twn.append((twn[-1][0] + step_x, twn[-1][1] + step_y))
	return twn

def do_all(function, iterable):
	for i in iterable: function(i)

def do_solution_for(segment_defs, is_part_one=True):
	sea_floor = defaultdict(int)
	def count_point(p):
		sea_floor[p] += 1

	for sd in segment_defs:
		a, b = [tuple(int(n) for n in pt.split(",")) for pt in sd.split(" -> ")]
		if is_part_one and all(ai != bi for ai, bi in zip(a, b)): 
			continue
		do_all(count_point, tween(a, b))
	return sum(1 for n in sea_floor if sea_floor[n] > 1)

def solve_p1():
	print(f"PART ONE\n--------\n")
	print(f"We need to avoid travelling over some dangerous spots, identified b"
       	  f"y the intersections of a series of overlapping coordinates. For Par"
		  f"t One, we ignore diagonal segments.\n")

	results = do_solution_for(example_lines)
	print(f"When we do part one for the example input:")
	print(f"\tThe number of intersections (without diagonals) is {results}")
	print(f"\tWe expected: 5\n")

	results = do_solution_for(input_lines)
	print(f"When we do part one for the actual input:")
	print(f"\tThe number of intersections (without diagonals) is {results}\n")

def solve_p2():
	print(f"PART TWO\n--------\n")
	print(f"For Part 2, we don't ignore diagonal segments.\n")

	results = do_solution_for(example_lines, False)
	print(f"When we do part two for the example input:")
	print(f"\tThe number of intersections is {results}")
	print(f"\tWe expected: 12\n")

	results = do_solution_for(input_lines, False)
	print(f"When we do part two for the actual input:")
	print(f"\tThe number of intersections is {results}\n")

def print_header():
	print("--- DAY 5: Hydrothermal Venture ---\n")
