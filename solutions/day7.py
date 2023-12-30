# Imports from personal library
from utilities.vector import vector
import utilities.algos as algos
import utilities.io as io

# Imports from standard libraries I find myself using all the time
from collections import defaultdict
from collections import deque
 
try:
	input_lines = io.read_input_as_lines(7)
	example_lines = io.read_example_as_lines(7)
except:
	input_lines = ["Input Lines Not Found"]
	example_lines = ["Example"]

def do_part_one_for(lines):
	init_posns = sorted([int(n) for n in lines[0].split(",")])
	midpoint = init_posns[len(init_posns) // 2]
	if (not len(init_posns)) and init_posns[len(init_posns)//2+1] != midpoint:
		raise AssertionError(f"The arrangement is even and the middle two posit"
		    				 f"ions aren't equal.")
	return sum(abs(n - midpoint) for n in init_posns)

def do_part_two_for(lines):
	posns = sorted([int(n) for n in lines[0].split(",")])
	pos_counts = {n: posns.count(n) for n in posns}
	posns = sorted(list(pos_counts.keys()))
	mid = posns[len(posns) // 2]

	def fcost(s, e):
		d = abs(s - e)
		return (d * d + d) // 2

	fc_mid = sum(k * fcost(p, mid) for p, k in pos_counts.items())
	fc_lft = sum(k * fcost(p, mid-1) for p, k in pos_counts.items())
	fc_rgt = sum(k * fcost(p, mid+1) for p, k in pos_counts.items())
	while not (fc_lft > fc_mid and fc_rgt > fc_mid):
		mid += (-1 if fc_lft < fc_mid else 1)
		fc_mid = sum(k * fcost(p, mid) for p, k in pos_counts.items())
		fc_lft = sum(k * fcost(p, mid-1) for p, k in pos_counts.items())
		fc_rgt = sum(k * fcost(p, mid+1) for p, k in pos_counts.items())
	return fc_mid

def solve_p1():
	print(f"PART ONE\n--------\n")
	print(f"Which point of alignment for the crabs will require the least overa"
       	  f"ll fuel for them?\n")

	results = do_part_one_for(example_lines)
	print(f"When we do part one for the example input:")
	print(f"\tThe best fuel cost is {results}")
	print(f"\tWe expected: 37\n")

	results = do_part_one_for(input_lines)
	print(f"When we do part one for the actual input:")
	print(f"\tThe best fuel cost is {results}\n")

def solve_p2():
	print(f"PART TWO\n--------\n")
	print(f"What about when fuel costs are linear over the distance travelled?"
       	  f"\n")

	results = do_part_two_for(example_lines)
	print(f"When we do part two for the example input:")
	print(f"\tThe new best fuel cost is {results}")
	print(f"\tWe expected: 168\n")

	results = do_part_two_for(input_lines)
	print(f"When we do part two for the actual input:")
	print(f"\tThe new best fuel cost is {results}\n")

def print_header():
	print("--- DAY 7: The Treachery of Whales ---\n")
