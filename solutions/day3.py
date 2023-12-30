# Imports from personal library
from utilities.vector import vector
import utilities.algos as algos
import utilities.io as io

# Imports from standard libraries I find myself using all the time
from collections import defaultdict
from collections import deque

try:
	input_lines = io.read_input_as_lines(3)
	example_lines = io.read_example_as_lines(3)
except:
	input_lines = ["Input Lines Not Found"]
	example_lines = ["Example"]

def do_part_one_for(lines):
	# Gamma rate is most common bit, epsilon rate is !Gamma
	bstr = ""
	for x in range(len(lines[0])):
		bit_count = {"0":0, "1":0}
		for y in range(len(lines)):
			bit_count[lines[y][x]] += 1
		bstr += max(bit_count.keys(), key=lambda k: bit_count[k])
	gamma = int("0b" + bstr, base=0)
	ep_str = "".join("1" if c == "0" else "0" for c in bstr)
	epsilon = int("0b" + ep_str, base=0)
	return gamma * epsilon


def do_part_two_for(lines):
	# To get the oxygen generator rating, prune out numbers without the most 
	# common bit at index 0. If you have only one left, then that number is the 
	# rating. "1" bits break ties. 
	oxygen_rating_strs = lines.copy()
	idx = 0
	while len(oxygen_rating_strs) > 1:
		bit_sort = {"0": [], "1": []}
		for ors in oxygen_rating_strs:
			bit_sort[ors[idx]].append(ors)
		def sortkey(num_list):
			return len(num_list) + (0.1 if num_list[0][idx] == "1" else 0.0)
		oxygen_rating_strs = max(bit_sort.values(), key=sortkey)
		idx += 1
	oxygen_generator_rating = int("0b" + oxygen_rating_strs[0], base=0)

	# CO2 scrubber rating is the reverse. 
	co2_rating_strs = lines.copy()
	idx = 0
	while len(co2_rating_strs) > 1:
		bit_sort = {"0": [], "1": []}
		for ors in co2_rating_strs:
			bit_sort[ors[idx]].append(ors)
		def sortkey(num_list):
			return len(num_list) + (0.1 if num_list[0][idx] == "1" else 0.0)
		co2_rating_strs = min(bit_sort.values(), key=sortkey)
		idx += 1
	co2_scrubber_rating = int("0b" + co2_rating_strs[0], base=0)

	return oxygen_generator_rating * co2_scrubber_rating


	

def solve_p1():
	print(f"PART ONE\n--------\n")
	print(f"Given the binary diagnostic report, what is the power consumption o"
       	  f"f your submarine?\n")

	results = do_part_one_for(example_lines)
	print(f"When we do part one for the example input:")
	print(f"\tThe power consumption is {results}")
	print(f"\tWe expected: 198\n")

	results = do_part_one_for(input_lines)
	print(f"When we do part one for the actual input:")
	print(f"\tThe power consumption is {results}\n")

def solve_p2():
	print(f"PART TWO\n--------\n")
	print(f"What is the life support rating?\n")

	results = do_part_two_for(example_lines)
	print(f"When we do part two for the example input:")
	print(f"\tThe life support rating is {results}")
	print(f"\tWe expected: 230\n")

	results = do_part_two_for(input_lines)
	print(f"When we do part two for the actual input:")
	print(f"\tThe life support rating is {results}\n")

def print_header():
	print("--- DAY 3: Binary Diagnostic ---\n")
