import math

def get_puzzle():
	print()
	dimensions = int(input('Sudoku Dimensions: '))
	print('Enter values, for an empty box just press enter')
	print()
	values = []
	for n in range(dimensions):
		for m in range(dimensions):
			value = input('Row ' + str(n+1) + ', Column ' + str(m+1) + ': ')
			try: 
				value = int(value)
				values.append(value)
			except ValueError:
				values.append(0)
	puzzle = []
	for n in range(dimensions):
		line = values[n * dimensions : (n+1) * dimensions]
		puzzle.append(line)
	return puzzle

def check_box(puzzle, row, column):
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


def solve_puzzle():
	#puzzle = get_puzzle()
	puzzle = [[1,0,2,0], [0,3,0,4], [0,2,4,0], [0,1,0,0]]
	finished = False
	while not finished:
		for i in range(len(puzzle)):
			for j in range(len(puzzle)):
				if puzzle[i][j] == 0:
					if len(check_box(puzzle, i, j)) == 1:
						puzzle[i][j] = check_box(puzzle, i, j)[0]
		values = []
		for i in range(len(puzzle)):
			for j in range(len(puzzle)):
				values.append(puzzle[i][j])
		finished = all(values)
	for i in range(len(puzzle)):
		print(puzzle[i])

solve_puzzle()

