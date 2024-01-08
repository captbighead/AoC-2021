# Imports from personal library
from utilities.vector import vector
import utilities.algos as algos
import utilities.io as io

# Imports from standard libraries I find myself using all the time
from collections import defaultdict
from collections import deque

try:
	input_lines = io.read_input_as_lines(10)
	example_lines = io.read_example_as_lines(10)
except:
	input_lines = ["Input Lines Not Found"]
	example_lines = ["Example"]

def score_chunkset(chunkstr):
	bracket_match = {}
	lefts = "([{<"
	rights = ")]}>"
	for lft, rht in zip(lefts, rights):
		bracket_match[lft] = rht
		bracket_match[rht] = lft
	scores = {end: val for end, val in zip(rights, [3, 57, 1197, 25137])}
	
	chunkstack = []
	for c in chunkstr:
		# It's always okay to open a new chunk
		if c in lefts:
			chunkstack.append(c)
			continue

		# If we find a right-hand bracket that doesn't match the last chunk open
		# character, it's a corrupted value
		if c in rights and c != bracket_match[chunkstack[-1]]:
			return scores[c]
		
		# Otherwise, we completed the most recent open chunk.
		chunkstack.pop()

	# This is guaranteed to happen: we are given that all lines are either 
	# incomplete or corrupted. Getting here means that we weren't corrupted.
	if chunkstack:
		return 0
	else:
		raise ValueError("This isn't supposed to happen!")

def autocomplete(chunkstr):
	bracket_match = {}
	lefts = "([{<"
	rights = ")]}>"
	for lft, rht in zip(lefts, rights):
		bracket_match[lft] = rht
		bracket_match[rht] = lft
	
	chunkstack = []
	for c in chunkstr:
		# It's always okay to open a new chunk
		if c in lefts:
			chunkstack.append(c)
			continue

		# If we find a right-hand bracket that doesn't match the last chunk open
		# character, it's a corrupted value
		if c in rights and c != bracket_match[chunkstack[-1]]:
			return None
		
		# Otherwise, we completed the most recent open chunk.
		chunkstack.pop()

	# Getting here means that we weren't corrupted.
	autostr = ""
	while chunkstack:
		autostr += bracket_match[chunkstack.pop()]
	return autostr

def score_autocomplete_str(ac_str):
	rubrik = {c: s for c, s in zip(")]}>", range(1, 5))}
	score = 0
	for c in ac_str:
		score *= 5
		score += rubrik[c]
	return score

def do_part_one_for(lines):
	return sum(score_chunkset(ln) for ln in lines)

def do_part_two_for(lines):
	scores = []
	for chunkstr in lines: 
		ac = autocomplete(chunkstr)
		if ac == None:
			continue
		scores.append(score_autocomplete_str(ac))
	scores.sort()
	return scores[len(scores)//2]



def solve_p1():
	print(f"PART ONE\n--------\n")
	print(f"Find the aggregate corruption score for the lines in the input.\n")

	results = do_part_one_for(example_lines)
	print(f"When we do part one for the example input:")
	print(f"\tThe corruption score is {results}")
	print(f"\tWe expected: 26397\n")

	results = do_part_one_for(input_lines)
	print(f"When we do part one for the actual input:")
	print(f"\tThe corruption score is {results}\n")

def solve_p2():
	print(f"PART TWO\n--------\n")
	print(f"What is the middle auto-completion score for the auto-completion st"
       	  f"rings needed to close the unfinished lines?\n")

	results = do_part_two_for(example_lines)
	print(f"When we do part two for the example input:")
	print(f"\tThe middle auto-completion score is {results}")
	print(f"\tWe expected: 288957\n")

	results = do_part_two_for(input_lines)
	print(f"When we do part two for the actual input:")
	print(f"\tThe middle auto-completion score is {results}\n")

def print_header():
	print("--- DAY 10: <TITLE GOES HERE> ---\n")
