# Imports from personal library
from utilities.vector import vector
import utilities.algos as algos
import utilities.io as io

# Imports from standard libraries I find myself using all the time
from collections import defaultdict
from collections import deque

try:
	input_lines = io.read_input_as_lines(12)
	example_lines = io.read_example_as_lines(12)
except:
	input_lines = ["Input Lines Not Found"]
	example_lines = ["Example"]

class PartOneGraph: 

	def __init__(self, edge_list) -> None:
		self.lookup = defaultdict(set)
		self.small_bitvals = {}
		defined = set()
		bval = 1

		for edge_def in edge_list:
			v, w = edge_def.split("-")
			self.lookup[v].add(w)
			self.lookup[w].add(v)

			if v not in defined and v.islower():
				defined.add(v)
				self.small_bitvals[v] = bval
				bval *= 2
			
			if w not in defined and w.islower():
				defined.add(w)
				self.small_bitvals[w] = bval
				bval *= 2
	
	def get_neighbours(self, cave, small_bitmap):
		if cave == "end":
			return []
		
		options = []
		for next_cave in self.lookup[cave]:
			next_bmp = self.small_bitvals.get(next_cave, 0)
			if not small_bitmap & next_bmp:
				options.append((next_cave, next_bmp | small_bitmap))
		return options


class PartTwoGraph: 

	def __init__(self, edge_list) -> None:
		self.lookup = defaultdict(set)
		self.small_bitvals = {}
		defined = set()
		bval = 1

		for edge_def in edge_list:
			v, w = edge_def.split("-")
			self.lookup[v].add(w)
			self.lookup[w].add(v)

			if v not in defined and v.islower():
				defined.add(v)
				self.small_bitvals[v] = bval
				bval *= 2
			
			if w not in defined and w.islower():
				defined.add(w)
				self.small_bitvals[w] = bval
				bval *= 2
	
	def get_neighbours(self, cave, small_bmp, special, sp_done):
		if cave == "end":
			return []
		
		options = []
		for nxt_cave in self.lookup[cave]:
			nxt_bmp = self.small_bitvals.get(nxt_cave, 0)

			# If the next cave is our special cave and we haven't been already,
			# we can go, and we don't add it to the bmp, but we do track that
			# we've been there already.
			if nxt_cave == special and not sp_done:
				options.append((nxt_cave, small_bmp, special, True))

			# Otherwise, we check the cave like before:
			elif not small_bmp & nxt_bmp:
				options.append((nxt_cave, nxt_bmp|small_bmp, special, sp_done))
		return options

def do_part_one_for(lines):
	graph = PartOneGraph(lines)
	queue = deque([("start", graph.small_bitvals["start"], ["start"])])
	final_paths = []
	while queue:
		cave, small_map, path = queue.popleft()

		if cave == "end":
			final_paths.append(path)

		for nxt_cave, nxt_bmp in graph.get_neighbours(cave, small_map):
			nxt_path = path.copy()
			nxt_path.append(nxt_cave)
			queue.append((nxt_cave, nxt_bmp, nxt_path))

	final_paths = set([tuple(p) for p in final_paths])

	return len(final_paths)

def do_part_two_for(lines):
	graph = PartTwoGraph(lines)
	s = "start"
	sbmp = graph.small_bitvals[s]
	spath = [s]

	queue = deque()
	for small in graph.small_bitvals:
		if small in ("start", "end"):
			continue
		
		queue.append((s, sbmp, small, False, spath))

	final_paths = []
	while queue:
		cave, small_map, small, small_once, path = queue.popleft()

		if cave == "end":
			final_paths.append(path)

		for nxt in graph.get_neighbours(cave, small_map, small, small_once):
			nxt_cave, nxt_bmp, sml, nxt_done = nxt
			nxt_path = path.copy()
			nxt_path.append(nxt_cave)
			queue.append((nxt_cave, nxt_bmp, sml, nxt_done, nxt_path))

	final_paths = set([tuple(p) for p in final_paths])

	return len(final_paths)

def solve_p1():
	print(f"PART ONE\n--------\n")
	print(f"Given a series of caves, how many paths through the caves exist whe"
       	  f"re you can only visit a small cave once?\n")

	results = do_part_one_for(example_lines)
	print(f"When we do part one for the example input:")
	print(f"\tThe number of paths is {results}")
	print(f"\tWe expected: 226\n")

	results = do_part_one_for(input_lines)
	print(f"When we do part one for the actual input:")
	print(f"\tThe number of paths is {results}\n")

def solve_p2():
	print(f"PART TWO\n--------\n")
	print(f"This is the prompt for Part Two of the problem.\n")

	results = do_part_two_for(example_lines)
	print(f"When we do part two for the example input:")
	print(f"\tThe <THING THEY WANT> is {results}")
	print(f"\tWe expected: 3509\n")

	results = do_part_two_for(input_lines)
	print(f"When we do part two for the actual input:")
	print(f"\tThe <THING THEY WANT> is {results}\n")

def print_header():
	print("--- DAY 12: <TITLE GOES HERE> ---\n")
