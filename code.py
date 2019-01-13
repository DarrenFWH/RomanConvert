import sys

class RomanTranslator(object):
	"""docstring for RomanTranslator"""
	def __init__(self, inputStr, size):
		self.inputStr = inputStr
		self.size = size
		self.Num_0 = [1,2,0,2,1]
		self.Num_1 = [0,3,0,3,0]
		self.Num_2 = [1,3,1,4,1]
		self.Num_3 = [1,3,1,3,1]
		self.Num_4 = [0,2,1,3,0]
		self.Num_5 = [1,4,1,3,1]
		self.Num_6 = [1,4,1,2,1]
		self.Num_7 = [1,3,0,3,0]
		self.Num_8 = [1,2,1,2,1]
		self.Num_9 = [1,2,1,3,1]
		self.Num_10 = [[1],[4],[1],[4],[1]]
		self.li = []
		self.Roman_letter = ['I','V','X','L','C','D','M']
		self.Roman_Int = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
		self.result = self.RomanConvert()
		self.seed = 3
		if self.size == 1:
			self.seed = 3
		elif self.size == 2:
			self.seed = 4
		else:
			self.seed = self.size + 2

		for num in str(self.result):
			exec('self.li.append(self.Num_{})'.format(num))
		# list转置
		self.li = list(map(list,zip(*self.li)))

		# output
		self.printer()
		

	def RomanConvert(self):
		input_list = []
		for l in self.inputStr:
			input_list.append(l)

		# error
		if len(self.Roman_letter) != len(list(set(input_list+self.Roman_letter))):
			self.error_printer()
			print("Error, please try again.")
			sys.exit(0)
			
		sum = 0
		for i in range(len(self.inputStr)-1):
			# plus if next string is >= current one
			if self.Roman_Int[self.inputStr[i]] >= self.Roman_Int[self.inputStr[i+1]]:
				sum += self.Roman_Int[self.inputStr[i]]
			else:
				sum -= self.Roman_Int[self.inputStr[i]]

		return sum + self.Roman_Int[self.inputStr[-1]]

	def pattern0(self):
		print(' '*self.seed, end='')

	# '-'
	def pattern1(self):
		print(' '+'_'*self.size+' ', end='')

	# '| |'
	def pattern2(self):
		print('|%s|' % (' '*self.size), end='')

	# ' |'
	def pattern3(self):
		print(' '*self.size+' |', end='')

	# '| '
	def pattern4(self):
		print('| '+' '*self.size, end='')

    # when size is bigger than 1
	def handler(self, list_):
		list_1 = [list_]*self.size
		for i in range(len(list_1)):
			for j in list_1[i]:
				exec('self.pattern{}()'.format(j))
			print()
    
	def key_loop(self,list_):
		for i in range(len(list_)):
			for j in list_[i]:
				if i%2 == 0:
					exec('self.pattern{}()'.format(j))
					#print_Y(size,exec('pattern{}()'.format(j)))
				else:
					self.handler(list_[i])
					break
			print()

    # print the shape of number
	def printer(self):
		self.key_loop(self.li)
	
	def error_printer(self):
		self.key_loop(self.Num_10)

if __name__ == '__main__':
	input_letter = input("Please enter a Roman number: ")
	input_size = input("Please enter a size: ")
	RomanTranslator(input_letter.upper(),int(input_size))
				