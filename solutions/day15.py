# Imports from personal library
from utilities.vector import vector
import utilities.algos as algos
import utilities.io as io

# Imports from standard libraries I find myself using all the time
from collections import defaultdict
from collections import deque
import heapq

try:
	input_lines = io.read_input_as_lines(15)
	example_lines = io.read_example_as_lines(15)
except:
	input_lines = ["Input Lines Not Found"]
	example_lines = ["Example"]

class Graph: 

	def __init__(self, line_defs, extended) -> None:
		dflt = lambda: 10
		self.base_grid = algos.vector_map_from_string_list(line_defs, dflt, int)
		self.base_size = len(line_defs)
		self.size = self.base_size * (5 if extended else 1)
		self.extended = extended
	
	def neighbours(self, position: vector, cost: int):
		options = []
		for v in position.adjacents:
			# If out of bounds, it's undefined. 
			if min(v.x, v.y) < 0 or max(v.x, v.y) >= self.size:
				continue

			v_tile = vector(v.x // self.base_size, v.y // self.base_size)
			tile_dist = v_tile.distance(vector())

			if tile_dist > 0:
				asdf = "asdf"

			v_relative = v.congruent(self.base_size)
			v_base_cost = self.base_grid[v_relative]
			v_cost = (v_base_cost + tile_dist) % 9
			v_cost = 9 if not v_cost else v_cost

			options.append((v, cost + v_cost))
		return options


def do_soln_for(lines, extended):
	ENTRIES = 1
	graph = Graph(lines, extended)
	destination = (vector(1, 1) * graph.size) - vector(1, 1)
	prique = []
	heapq.heappush(prique, (0, 0, vector()))
	visited = set()

	while prique:
		running_cost, eid, posn = heapq.heappop(prique)
		if posn in visited:
			continue
		visited.add(posn)

		if posn == destination:
			return running_cost

		for next_posn, next_cost in graph.neighbours(posn, running_cost):
			heapq.heappush(prique, (next_cost, ENTRIES, next_posn))
			ENTRIES += 1
	
	raise LookupError("Couldn't find a path to the destination.")

def solve_p1():
	print(f"PART ONE\n--------\n")
	print(f"This is the prompt for Part One of the problem.\n")

	results = do_soln_for(example_lines, False)
	print(f"When we do part one for the example input:")
	print(f"\tThe <THING THEY WANT> is {results}")
	print(f"\tWe expected: 40\n")

	results = do_soln_for(input_lines, False)
	print(f"When we do part one for the actual input:")
	print(f"\tThe <THING THEY WANT> is {results}\n")

def solve_p2():
	print(f"PART TWO\n--------\n")
	print(f"This is the prompt for Part Two of the problem.\n")

	results = do_soln_for(example_lines, True)
	print(f"When we do part two for the example input:")
	print(f"\tThe <THING THEY WANT> is {results}")
	print(f"\tWe expected: 315\n")

	results = do_soln_for(input_lines, True)
	print(f"When we do part two for the actual input:")
	print(f"\tThe <THING THEY WANT> is {results}\n")

def print_header():
	print("--- DAY 15: <TITLE GOES HERE> ---\n")
