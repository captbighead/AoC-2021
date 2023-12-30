# Imports from personal library
from utilities.vector import vector
import utilities.algos as algos
import utilities.io as io

# Imports from standard libraries I find myself using all the time
from collections import defaultdict
from collections import deque

try:
	input_lines = io.read_input_as_lines(2)
	example_lines = io.read_example_as_lines(2)
except:
	input_lines = ["Input Lines Not Found"]
	example_lines = ["Example"]

def do_part_one_for(lines):
	position = vector()
	dirs = {"f": vector.RIGHT(), "u": vector.UP(), "d": vector.DOWN()}
	for inst in lines:
		bearing, distance = inst.split()
		position += dirs[bearing[0]] * int(distance)
	return position.x * position.y


def do_part_two_for(lines):
	position = vector()
	aim = vector()
	dirs = {"f": vector.RIGHT(), "u": vector.UP(), "d": vector.DOWN()}
	for inst in lines:
		bearing, distance = algos.erase(inst, ["orward", "p", "own"]).split()
		if bearing in "ud":
			aim += dirs[bearing] * int(distance)
		else:
			position += (dirs[bearing] * int(distance)) + (aim * int(distance))
	return position.x * position.y

def solve_p1():
	print(f"PART ONE\n--------\n")
	print(f"what is the product of the x and y values after you follow the subm"
       	  f"arine driving instructions provided?\n")

	results = do_part_one_for(example_lines)
	print(f"When we do part one for the example input:")
	print(f"\tThe product of x and y for your destination is {results}")
	print(f"\tWe expected: 150\n")

	results = do_part_one_for(input_lines)
	print(f"When we do part one for the actual input:")
	print(f"\tThe product of x and y for your destination is {results}\n")

def solve_p2():
	print(f"PART TWO\n--------\n")
	print(f"What about if up/down instructions change your pitch instead?\n")

	results = do_part_two_for(example_lines)
	print(f"When we do part two for the example input:")
	print(f"\tThe x, y product is {results}")
	print(f"\tWe expected: 900\n")

	results = do_part_two_for(input_lines)
	print(f"When we do part two for the actual input:")
	print(f"\tThe x, y product is {results}\n")

def print_header():
	print("--- DAY 2: Dive! ---\n")
