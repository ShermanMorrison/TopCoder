class WindowManager:

	def screen(self, height, width, window_tuples):
		
		# make an output [list of char lists]
		self.output = self.string_to_window("0 0 " + str(height) + " " + str(width) + " " + "X", " ")
		# make a list of input [list of char lists]'s
		for window_tuple in window_tuples:
			self.project(self.output, self.string_to_window(window_tuple))
		
		return tuple(["".join(row) for row in self.output.matrix]) 

	# write a function which takes a window_tuple and returns a Window (y, x, matrix)
	def string_to_window(self, window_tuple, *args):
		window_tuple_list = window_tuple.split(" ")
		y = int(window_tuple_list[0])
		x = int(window_tuple_list[1])
		height = int(window_tuple_list[2])
		width = int(window_tuple_list[3])
		if (args):
			letter = args[0]
		else:
			letter = window_tuple_list[4]
		# create window matrix
		top_row = ["+"] + (["-"] * (width - 2)) + ["+"]
		mid_matrix_rows = ["|"] +  [letter] * (width - 2)  + ["|"]
		mid_matrix_rows = [mid_matrix_rows] * (height - 2)
		matrix = [top_row] + mid_matrix_rows + [top_row]
		
		return Window(y, x, height, width, matrix)

	# write function taking an output window and input window which puts the input list on top of the output list
	def project(self, output, input):
		
		# x range: max(0, input.x) to min(width, input.x + input.width)
		
		y_min = max(0, input.y)
		y_lim = min(output.height, input.y + input.height)
		x_min = max(0, input.x)
		x_lim = min(output.width, input.x + input.width)
		
		for y in xrange(y_min, y_lim):
			for x in xrange(x_min, x_lim):
				output.matrix[y][x] = input.matrix[y - y_min][x - x_min]
		
	
class Window:
	
	def __init__(self, y, x, height, width, matrix):
		self.y = y
		self.x = x
		self.height = height
		self.width = width
		self.matrix = matrix