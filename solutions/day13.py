# Imports from personal library
from utilities.vector import vector
import utilities.algos as algos
import utilities.io as io

# Imports from standard libraries I find myself using all the time
from collections import defaultdict
from collections import deque

try:
	input_lines = io.read_input_as_lines(13)
	example_lines = io.read_example_as_lines(13)
except:
	input_lines = ["Input Lines Not Found"]
	example_lines = ["Example"]

def preprocess(lines):
	dots = set()
	for idx, dot_def in enumerate(lines, 1):		
		if dot_def == "":
			break
		dots.add(tuple([int(n) for n in dot_def.split(",")]))
	folds = lines[idx:]
	return dots, folds

def fold(dots_orig: set, axis, val):
	dots = dots_orig.copy()
	change_ind = 0 if axis == "x" else 1
	check_op = int.__gt__ if change_ind else int.__lt__
	for dot in dots_orig:
		x, y = dot
		if check_op(dot[change_ind], val):
			delta = abs(dot[change_ind] - val)
			delta *= -2 if change_ind else 2
			dots.remove(dot)
			new_dot = (x + delta, y) if not change_ind else (x, y + delta)
			dots.add(new_dot)
	
	# If we folded from left to right, we need to realign the left edge:
	dots = list(dots)
	if not change_ind:
		for i in range(len(dots)):
			dots[i] = (dots[i][0] - (val + 1), dots[i][1])
	return set(dots)

def do_part_one_for(lines):
	dots, folds = preprocess(lines)
	axis, val = algos.erase(folds[0], ["fold along "]).split("=")
	val = int(val)
	return len(fold(dots, axis, val))

def do_part_two_for(lines):
	dots, folds = preprocess(lines)
	for fold_str in folds:
		axis, val = algos.erase(fold_str, ["fold along "]).split("=")
		val = int(val)
		dots = fold(dots, axis, val)
	mapping = defaultdict(lambda: " ")
	for x, y in dots:
		mapping[vector(x, y)] = "#"
	algos.print_map(mapping, bounds=1080)

def solve_p1():
	print(f"PART ONE\n--------\n")
	print(f"We need to fold a piece of transparent paper covered in dots. After"
       	  f" the first fold, how many dots are visible (counting dots that over"
		  f"lap each other as a single dot)?\n")

	results = do_part_one_for(example_lines)
	print(f"When we do part one for the example input:")
	print(f"\tThe number of visible dots after a single fold is {results}")
	print(f"\tWe expected: 17\n")

	results = do_part_one_for(input_lines)
	print(f"When we do part one for the actual input:")
	print(f"\tThe number of visible dots after a single fold is {results}\n")

def solve_p2():
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
	print("--- DAY 13: Transparent Origami ---\n")
