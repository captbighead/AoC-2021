# Imports from personal library
from utilities.vector import vector
import utilities.algos as algos
import utilities.io as io

# Imports from standard libraries I find myself using all the time
from collections import defaultdict
from collections import deque

try:
	input_lines = io.read_input_as_lines(4)
	example_lines = io.read_example_as_lines(4)
except:
	input_lines = ["Input Lines Not Found"]
	example_lines = ["Example"]

class bingo_card:

	def __init__(self, def_strs) -> None:
		self.card = {}
		for y, row in enumerate(def_strs):
			for x, num in enumerate(row.split()):
				self.card[int(num)] = vector(x, y)
		self.sum_unmarked = sum(self.card.keys())
		self.y_scores = [0] * 5
		self.x_scores = [0] * 5
		self.last_dabbed = -1
	
	def dab(self, number):
		# 'dabs' a spot on the bingo card, adding to its score for that 
		# row/column. If either score becomes 5, a Bingo is achieved. This 
		# method returns True if bingo was achieved, otherwise False.
		if number in self.card.keys():
			self.last_dabbed = number
			self.sum_unmarked -= number
			v = self.card[number]
			self.y_scores[v.y] += 1
			self.x_scores[v.x] += 1
			return 5 in (self.x_scores[v.x], self.y_scores[v.y])
		return False

	def score(self):
		return self.sum_unmarked * self.last_dabbed

def do_part_one_for(lines):
	lines = lines.copy() + [""]
	bingo_nums = deque([int(n) for n in lines[0].split(",")])
	bingo_cards = []
	card_in_progress = []
	for row in lines[2:]:
		if row == "":
			bingo_cards.append(bingo_card(card_in_progress))
			card_in_progress = []
			continue
		card_in_progress.append(row)

	bingo = False
	while bingo_nums and not bingo:
		num = bingo_nums.popleft()
		for card in bingo_cards:
			bingo = bingo or card.dab(num)
			if bingo:
				return card.score()
	
	raise ValueError("There are no winners in Bingo.")

	

		


def do_part_two_for(lines):
	lines = lines.copy() + [""]
	bingo_nums = deque([int(n) for n in lines[0].split(",")])
	bingo_cards = []
	card_in_progress = []
	for row in lines[2:]:
		if row == "":
			bingo_cards.append(bingo_card(card_in_progress))
			card_in_progress = []
			continue
		card_in_progress.append(row)

	last_winner = None
	while bingo_nums and bingo_cards:
		num = bingo_nums.popleft()
		for card in bingo_cards.copy():
			if card.dab(num):
				bingo_cards.remove(card)
				last_winner = card
	return last_winner.score()

def solve_p1():
	print(f"PART ONE\n--------\n")
	print(f"What is the winning score for the first bingo card to win?\n")

	results = do_part_one_for(example_lines)
	print(f"When we do part one for the example input:")
	print(f"\tThe winning score is {results}")
	print(f"\tWe expected: 4512\n")

	results = do_part_one_for(input_lines)
	print(f"When we do part one for the actual input:")
	print(f"\tThe winning score is {results}")
	print(f"\tWe expected: 33462 (we solved it years ago)\n")

def solve_p2():
	print(f"PART TWO\n--------\n")
	print(f"What's the score of the last card to win?\n")

	results = do_part_two_for(example_lines)
	print(f"When we do part two for the example input:")
	print(f"\tThe score of the final, losing card is {results}")
	print(f"\tWe expected: 1924\n")

	results = do_part_two_for(input_lines)
	print(f"When we do part two for the actual input:")
	print(f"\tThe score of the final, losing card is {results}\n")

def print_header():
	print("--- DAY 4: Giant Squid ---\n")
