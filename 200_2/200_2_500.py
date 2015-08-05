class GravityBomb:

	def aftermath(self, string_tuple):
		height = len(string_tuple)
		if height ==  0:
			return ()
		width = len(string_tuple[0])
		counts = [0] * width
		for string in string_tuple:
			print string
			for i in xrange(width):
				if string[i] == 'X':
					print i
					counts[i] += 1
		
		min_count = min(counts)
		for i in xrange(len(counts)):
			counts[i] -= min_count
			
		print counts	
		result = ""
		result = [result] * height 

		max_count = max(counts)
		for i in reversed(xrange(height-1)):
			for j in xrange(width):
				if counts[j] > 0:
					counts[j] -= 1
					result[i] += 'X'
				else:
					result[i] += '.'
					
		return result
			
