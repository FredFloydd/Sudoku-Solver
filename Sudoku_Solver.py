import math
import copy

def get_puzzle(values):
	dimensions = int(len(values) ** 0.5)
	puzzle = []
	for n in range(dimensions):
		line = values[n * dimensions : (n+1) * dimensions]
		puzzle.append(line)
	return puzzle

def check_cell(puzzle, row, column):
	dimensions = len(puzzle)
	options = []
	sqrtdimensions = int(dimensions ** 0.5)
	box_row = math.floor(row / sqrtdimensions)
	box_column = math.floor(column / sqrtdimensions)
	box = []
	for n in range(sqrtdimensions):
		for m in range(sqrtdimensions):
			box.append(puzzle[box_row * sqrtdimensions + n][box_column * sqrtdimensions + m])
	for o in range(dimensions):
		a = True
		b = True
		c = True
		for i in puzzle[row]:
			if i == o+1:
				a = False
		for j in range(dimensions):
			if puzzle[j][column] == o+1:
				b = False
		for k in range(dimensions):
			if box[k] == o+1:
				c = False
		if a and b and c:
			options.append(o+1)
	return options

def check_box(puzzle, box_row, box_column, number):
	dimensions = len(puzzle)
	sqrtdimensions = int(dimensions ** 0.5)
	box = []
	for n in range(sqrtdimensions):
		for m in range(sqrtdimensions):
			box.append(puzzle[box_row * sqrtdimensions + n][box_column * sqrtdimensions + m])
	if number not in box:
		possible_locations = []
		for i in range(len(box)):
			if box[i] == 0:
				a = False
				b = False
				if number not in puzzle[sqrtdimensions * box_row + math.floor(i / sqrtdimensions)]:
					a = True
				column = []
				for j in range(dimensions):
					column.append(puzzle[j][sqrtdimensions * box_column + (i % sqrtdimensions)])
				if number not in column:
					b = True
				if a and b:
					possible_locations.append(i)
		if len(possible_locations) == 1:
			puzzle[sqrtdimensions * box_row + math.floor(possible_locations[0] / sqrtdimensions)][sqrtdimensions * box_column + (possible_locations[0] % sqrtdimensions)] = number
		return puzzle
	else:
		return puzzle

def check_row(puzzle, row, number):
	dimensions = len(puzzle)
	sqrtdimensions = int(dimensions ** 0.5)
	if number not in puzzle[row]:
		possible_locations = []
		for i in range(dimensions):
			if puzzle[row][i] == 0:
				a = False
				b = False
				box = []
				box_row = math.floor(row / sqrtdimensions)
				box_column = math.floor(i / sqrtdimensions)
				for n in range(sqrtdimensions):
					for m in range(sqrtdimensions):
						box.append(puzzle[box_row * sqrtdimensions + n][box_column * sqrtdimensions + m])
				if number not in box:
					a = True
				column = []
				for j in range(dimensions):
					column.append(puzzle[j][i])
				if number not in column:
					b = True
				if a and b:
					possible_locations.append(i)
		if len(possible_locations) == 1:
			puzzle[row][possible_locations[0]] = number
		return puzzle
	else:
		return puzzle

def check_column(puzzle, column, number):
	dimensions = len(puzzle)
	sqrtdimensions = int(dimensions ** 0.5)
	col = []
	for j in range(dimensions):
		col.append(puzzle[j][column])
	if number not in col:
		possible_locations = []
		for i in range(dimensions):
			if col[i] == 0:
				a = False
				b = False
				box = []
				box_row = math.floor(i / sqrtdimensions)
				box_column = math.floor(column / sqrtdimensions)
				for n in range(sqrtdimensions):
					for m in range(sqrtdimensions):
						box.append(puzzle[box_row * sqrtdimensions + n][box_column * sqrtdimensions + m])
				if number not in box:
					a = True
				if number not in puzzle[i]:
					b = True
				if a and b:
					possible_locations.append(i)
		if len(possible_locations) == 1:
			puzzle[possible_locations[0]][column] = number
		return puzzle
	else:
		return puzzle

def solve_puzzle(values):
	puzzle = get_puzzle(values)
	finished = False
	dimensions = len(puzzle)
	count = 0
	guesses = []
	while not finished:
	
		options = []
		puzzlecopy = copy.deepcopy(puzzle)

		for i in range(len(puzzle)):
			for j in range(len(puzzle)):
				if puzzle[i][j] == 0:
					line = []
					line.append(dimensions * i + j)
					line.append(check_cell(puzzle, i, j))
					options.append(line)
		for cell in options:
			if len(cell[1]) == 1:
				puzzle[math.floor(cell[0] / len(puzzle))][cell[0] % len(puzzle)] = cell[1][0]
				del cell
		for i in range(int(len(puzzle) ** 0.5)):
			for j in range(int(len(puzzle) ** 0.5)):
				for k in range(len(puzzle)):
					puzzle = check_box(puzzle, i, j, k+1)
		for i in range(len(puzzle)):
			for j in range(len(puzzle)):
				puzzle = check_row(puzzle, i, j+1)
				puzzle = check_column(puzzle, i, j+1)
		for i in range(len(options)):
			if len(options[i][1]) == 0:
				restored = guesses.pop()
				puzzle = restored[1]
				count += 1
				break
		if puzzlecopy == puzzle:
			info = min(options, key=lambda u: len(u[1]))
			guessed_cell = info[0]
			choices = info[1]
			for i in range(len(choices)):
				puzzlecopy[math.floor(guessed_cell / len(puzzle))][guessed_cell % len(puzzle)] = choices[i]
				situation = []
				situation.append(guessed_cell)
				situation.append(copy.deepcopy(puzzlecopy))
				guesses.append(situation)
			puzzle = puzzlecopy
		values = []
		for i in range(len(puzzle)):
			for j in range(len(puzzle)):
				values.append(puzzle[i][j])
		finished = all(values)
	print()
	for i in range(len(puzzle)):
		line = '| '
		line2 = '--'
		for j in range(len(puzzle)):
			line += str(puzzle[i][j]) + ' | '
			line2 += '----'
		print(line)
		print(line2)
	print()
	print(str(count) + ' Guesses Needed')

values = []
line = '000000396700000000000208000000009670800306009040000000300005000005020700900070410'
for i in range(len(line)):
	values.append(int(line[i]))

solve_puzzle(values)

