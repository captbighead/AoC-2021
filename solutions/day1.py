# Imports from personal library
from utilities.vector import vector
import utilities.algos as algos
import utilities.io as io

# Imports from standard libraries I find myself using all the time
from collections import defaultdict
from collections import deque

try:
	input_lines = io.read_input_as_lines(1)
	example_lines = io.read_example_as_lines(1)
except:
	input_lines = ["Input Lines Not Found"]
	example_lines = ["Example"]

def do_part_one_for(lines):
	return sum([1 for i, n in enumerate(lines[1:]) if int(n) > int(lines[i])])

def do_part_two_for(lines):
	scan = [int(n) for n in lines]
	scan_agg = [sum(scan[i-2:i+1]) for i in range(2, len(scan))]
	return sum([1 for i, n in enumerate(scan_agg[1:]) if n > scan_agg[i]])

def solve_p1():
	print(f"PART ONE\n--------\n")
	print(f"We're given a sonar scan and need to report the number of times the"
       	  f" depth of the scan increases from line to line.\n")

	results = do_part_one_for(example_lines)
	print(f"When we do part one for the example input:")
	print(f"\tThe number of depth increases in our sonar scan is {results}")
	print(f"\tWe expected: 7\n")

	results = do_part_one_for(input_lines)
	print(f"When we do part one for the actual input:")
	print(f"\tThe number of depth increases in our sonar scan is {results}\n")

def solve_p2():
	print(f"PART TWO\n--------\n")
	print(f"To eliminate the noise, we're checking the depth increases on slidi"
       	  f"ng windows of length 3 instead.\n")

	results = do_part_two_for(example_lines)
	print(f"When we do part two for the example input:")
	print(f"\tThe new number of depth increases in our sonar scan is {results}")
	print(f"\tWe expected: 5\n")

	results = do_part_two_for(input_lines)
	print(f"When we do part two for the actual input:")
	print(f"\tThe new number of depth increases in our sonar scan is {results}"
       	  f"\n")

def print_header():
	print("--- DAY 1: Sonar Sweep ---\n")
