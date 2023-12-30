# Imports from personal library
from utilities.vector import vector
import utilities.algos as algos
import utilities.io as io

# Imports from standard libraries I find myself using all the time
from collections import defaultdict
from collections import deque

try:
	input_lines = io.read_input_as_lines(8)
	example_lines = io.read_example_as_lines(8)
except:
	input_lines = ["Input Lines Not Found"]
	example_lines = ["Example"]

#	 * 		   		 * 		 * 		   		 * 		 * 		 * 		 * 		 * 
#	* *		  *		  *		  *		* *		*  		*  		  *		* *		* *
#	   		   		 * 		 * 		 * 		 * 		 * 		   		 * 		 * 
#	* *		  *		*  		  *		  *		  *		* *		  *		* *		  *
#	 * 		   		 * 		 * 		   		 * 		 * 		   		 * 		 * 
#
#	 6		  2		 5		 5		 4		 5		 6		 3		 7		 6

def do_part_one_for(lines):
	summation = 0
	for line in lines:
		digit_defs, out_digits = line.split(" | ")
		for d in out_digits.split():
			summation += 1 if len(d) in (2, 3, 4, 7) else 0
	return summation

def process_line(def_str):
	catalog, output = def_str.split(" | ")
	trivial = lambda s: (1 if len(s) in (2, 3, 4, 7) else 10) * len(s)
	catalog = sorted(catalog.split(), key=trivial)

	# Catalog has the digit representations of 1, 7, 4, 8, followed by 2, 3, 5 
	# in some order, followed by 0, 6, 9 in some order. 
	segs = {n: set(catalog[s]) for n, s in zip([1, 7, 4, 8], range(4))}
	cat_235 = [set(s) for s in catalog[4:7]]
	cat_069 = [set(s) for s in catalog[7:]]
	not_4 = segs[8].difference(segs[4])

	# 2, 3, 5 all have the middle segments in common. Not 4 and 7 Have the top 
	# and bottom segments, so the difference between the intersection of 
	# {2, 3, 5} and {~4, 7} is the center. 
	middle = cat_235[0].intersection(cat_235[1]).intersection(cat_235[2])
	center = middle.difference(segs[7]).difference(not_4)
	
	# The topmost segment is the difference between 1 and 7
	top = not_4.intersection(segs[7])

	# Which makes the bottom segment the difference between mid and the known 
	# top and bottom. 
	bottom = middle.difference(top.union(center))

	# The bottom left is ~4 - bottom - top
	bleft = not_4.difference(bottom).difference(top)

	# With the pieces we've unearthed:
	segs[0] = segs[8].difference(center)
	segs[9] = segs[8].difference(bleft)
	segs[3] = segs[1].union(middle)

	# Because we know 3 now, we can remove it from 2, 3, 5:
	cat_235.remove(segs[3])

	# Which means that 2 is the only one remaining that has bleft
	segs[2] = cat_235[0] if cat_235[0].intersection(bleft) else cat_235[1]
	cat_235.remove(segs[2])

	# Which means 5 is the only one left!
	segs[5] = cat_235.pop()

	# And that leaves only 6 as undefined, but it's just 5 with bleft in it.
	segs[6] = segs[5].union(bleft)

	# Now if we sort the component string, we can store the number it represents
	# in a way that's easily looked up:
	translation = {"".join(sorted(segs[n])): n for n in segs}
	pow = 3
	val = 0
	for d in output.split():
		d = "".join(sorted(d))
		val += (10 ** pow) * translation[d]
		pow -= 1
	return val

def do_part_two_for(lines):
	return sum(process_line(l) for l in lines)

def solve_p1():
	print(f"PART ONE\n--------\n")
	print(f"We need to interpret a set of scrambled 7-segment displays. For Par"
       	  f"t 1, we want to count the occurrences of all digits 1, 4, 7, or 8 i"
		  f"n our outputs.\n")

	results = do_part_one_for(example_lines)
	print(f"When we do part one for the example input:")
	print(f"\tThe number of 1s, 4s, 7s, or 8s in the output is {results}")
	print(f"\tWe expected: 26\n")

	results = do_part_one_for(input_lines)
	print(f"When we do part one for the actual input:")
	print(f"\tThe number of 1s, 4s, 7s, or 8s in the output is {results}\n")

def solve_p2():
	print(f"PART TWO\n--------\n")
	print(f"What is the sum of the numbers displayed in the output? \n")

	results = do_part_two_for(example_lines)
	print(f"When we do part two for the example input:")
	print(f"\tThe sum of the output displays is {results}")
	print(f"\tWe expected: 61229\n")

	results = do_part_two_for(input_lines)
	print(f"When we do part two for the actual input:")
	print(f"\tThe sum of the output displays is {results}\n")

def print_header():
	print("--- DAY 8: Seven-Segment Search ---\n")
