# Imports from personal library
from utilities.vector import vector
import utilities.algos as algos
import utilities.io as io

# Imports from standard libraries I find myself using all the time
from collections import defaultdict
from collections import deque

try:
	input_lines = io.read_input_as_lines(14)
	example_lines = io.read_example_as_lines(14)
except:
	input_lines = ["Input Lines Not Found"]
	example_lines = ["Example"]

def do_part_soln_for(lines, step_count):
	start = lines[0]
	LEFTMOST, RIGHTMOST = (start[0], start[-1])
	pairs = defaultdict(int)
	for i in range(len(start)-1):
		pairs[start[i:i+2]] += 1
	
	reactions = {}
	for reaction_def in lines[2:]:
		a, b, c = algos.erase(reaction_def, [" -> "])
		reactions[f"{a}{b}"] = (f"{a}{c}", f"{c}{b}")
	
	for step in range(step_count):
		new_pairs = defaultdict(int)
		for pair, pcount in pairs.items():
			left, right = reactions[pair]
			new_pairs[left] += pcount
			new_pairs[right] += pcount
		pairs = new_pairs

	# Now that we've done all the stepping: Every instance of a pair has one of 
	# two repetitions of it's element, except for the leading pair and the final
	# pair. So, count the number of times each element appears in the pairs that
	# are in our final string, and integer divide them by 2. Add 1 back for the
	# head element and the tail element.
	element_counts = defaultdict(int)
	for pair, pcount in pairs.items():
		a, b = pair
		element_counts[a] += pcount
		element_counts[b] += pcount
	for element in element_counts:
		element_counts[element] //= 2
		if element in (LEFTMOST, RIGHTMOST):
			element_counts[element] += 1
	return max(element_counts.values()) - min(element_counts.values())

def solve_p1():
	print(f"PART ONE\n--------\n")
	print(f"This is the prompt for Part One of the problem.\n")

	results = do_part_soln_for(example_lines, 10)
	print(f"When we do part one for the example input:")
	print(f"\tThe <THING THEY WANT> is {results}")
	print(f"\tWe expected: 1588\n")

	results = do_part_soln_for(input_lines, 10)
	print(f"When we do part one for the actual input:")
	print(f"\tThe <THING THEY WANT> is {results}\n")

def solve_p2():
	print(f"PART TWO\n--------\n")
	print(f"This is the prompt for Part Two of the problem.\n")

	results = do_part_soln_for(example_lines, 40)
	print(f"When we do part two for the example input:")
	print(f"\tThe <THING THEY WANT> is {results}")
	print(f"\tWe expected: 2188189693529\n")

	results = do_part_soln_for(input_lines, 40)
	print(f"When we do part two for the actual input:")
	print(f"\tThe <THING THEY WANT> is {results}\n")

def print_header():
	print("--- DAY 14: <TITLE GOES HERE> ---\n")
