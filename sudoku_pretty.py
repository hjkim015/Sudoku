#https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python



from random import sample 
import numpy as np

base  = 3  # Will generate any size of random sudoku board in O(n^2) time
side  = base*base

'''
nums  = sample(range(1,side+1),side) # random numbers
	#This generates a random list of numbers between 1-9 
	#Translates to sample(range(1,10),9)
	#sample cannot repeat numbers
	#THIS IS THE MASTER LIST OF NUMBERS THAT GIVES PROGRAM RANDOM ABILITY
board = [[nums[(base*(r%base)+r//base+c)%side] for c in range(side)] for r in range(side)]
	#HOW DOES THE EQUATION GIVE YOU THE SPECIFIC INDEXES BELOW? 	
	#This gives you the actual board of the sudoko. A list of lists representing a row.
	#What happens is that the numbers are generated based on an index pattern that fits 
	#the sudoku pattern below:
		#|0|1|2|3|4|5|6|7|8|
		#|3|4|5|6|7|8|0|1|2|
		#|6|7|8|0|1|2|3|4|5|
		#|1|2|3|4|5|6|7|8|0|
		#|4|5|6|7|8|0|1|2|3|
		#|7|8|0|1|2|3|4|5|6|
		#|2|3|4|5|6|7|8|0|1|
		#|5|6|7|8|0|1|2|3|4|
		#|8|0|1|2|3|4|5|6|7|
	#BREAKING IT DOWN: print the following code
		# print("nums", nums)
		# for r in range(side):
		# 	print("r", r)
		# 	for i in board:
		# 		print("board",i)
		# 	for c in range(side):
		# 		print("c", c)
		# 		print("base",base)
		# 		print(base*(r%base))
		# 		print(r//base)
		# 		print((base*(r%base)+r//base+c))
		# 		print((base*(r%base)+r//base+c)%side)
		# 		print("nums[]",nums[(base*(r%base)+r//base+c)%side])
		# 		raw_input()
squares = side*side
empties = squares * 3//4
for p in sample(range(squares),empties):
    board[p//side][p%side] = 0
def expandLine(line):
    return (line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13])
line0  = expandLine(" ___ ___ ____")
line1  = expandLine("| . | . | . |")
line2  = expandLine("|___|___|___|")
line3  = expandLine("|___|___|___|")
line4  = expandLine("|___|___|___|")
#________________________________________________________________________________
symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums   = [[""]+[symbol[n] for n in line] for line in board ]
	#what is happening with the "nums" variable: 
		#it takes the board with zeros
		#If n = 0, aka if the program reaches a spot on the board that is zero,
		#it will print [''] 
		#empty space of symbol. Because symbol[n] when n=0 is ''
		#IF n=another number, program will print [ 'another number']
		#BREAKING IT DOWN: print this code to see what's going on in the loop
#			print ("board",board)
				# for line in board:
				# 	print("line",line)
				# 	print("")
				# 	for n in line:
				# 		print("n", n)
				# 		print([symbol[n]])
				# 	print("this is nums", nums)
				# 	raw_input()
#________________________________________________________________________________
#in our case r will iterate through the sequence [1,2,3,4,5,6,7,8,9]
for r in range(1,side+1):
	print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) ) #columns
# # 		#WHAT IS HAPPENING: this makes all the numbers of the board appear 
# # 			#Let's BREAK IT DOWN: print the following code: 
# # 				# for r in range(1,side+1):
# # 				# 	print("r", r)
# # 				# 	print(nums)
# # 				# 	print("nums:these are the numbers/blank spots on the sudoku board",nums[r-1])
# # 				# 	print("line1: these are the pipes of the sudoku board", line1.split("."))
# # 				# 	zipping = zip(nums[r-1], line1.split("."))
# # 				# 	print("this is zip's final list of tuples that joined nums and line1", zipping)
# # 				# 	print("joining everything", "".join(n+s for n,s in zipping))
# # 				# 	raw_input()
 	print([line2,line3,line4][(r%side==0)+(r%base==0)])
# # 		#WHAT IS HAPPENING:Makes horizontal separators on the board appear 
# # 		#The modulo here is actually unnesscary. 
# # 		#if you put print(line2), it yields the same sudoku board
# 		#Mod was there becaue the original code had non aSCII symbols 
# 			
		#and wanted to control the 3*3 boxes within the sudoku board. 
	#TO UNDERSTAND THIS WHOLE ENTIRE FOR LOOP: Joining the "floors",#s, and pipes
	#Run this code to get a better idea of what is going on: 
	#notice how the individual spaces have a height of two pipes, not one. 
	#This occurs because you are stacking lines on top of each other. 
		# for r in range(1,side+1):
		# 	print("row", "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
		# 	raw_input()
		# 	print("floor",line2)
		# 	raw_input()
		# 	print("".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
		# 	print(line2)
		# 	raw_input()

'''


class sudoku:
	def __init__(self):
		
		#self.board_with_zeros, self.board_true_solution = self.create_board()
		# self.board = np.array([
 	# 		 [0,0,1,0,0,0,0,0,0]
		# 	,[3,0,0,9,0,0,0,0,1]
		# 	,[9,0,0,0,0,0,0,0,0]
		# 	,[0,0,0,5,6,0,0,0,0]
		# 	,[5,6,0,0,0,0,0,0,0]
		# 	,[0,2,4,0,1,3,5,0,0]
		# 	,[0,0,5,0,0,7,0,0,0]
		# 	,[0,0,7,0,0,0,0,0,5]
		# 	,[0,0,0,0,0,5,6,0,7]])
		self.board = np.array([
 			 [0,0,1,0,0,0,0,0,0]
			,[3,0,0,9,0,0,0,0,1]
			,[9,0,0,0,0,0,0,0,0]
			,[8,0,0,5,6,0,7,0,4]
			,[5,6,0,7,0,4,0,1,0]
			,[7,2,4,0,1,0,5,0,0]
			,[0,0,5,0,0,7,0,0,0]
			,[0,0,7,0,0,0,0,0,5]
			,[0,0,0,0,0,5,6,0,7]])

		self.eliminated_list = []
		self.initialize_dict()
		self.col_list = []

		

	def initialize_dict(self):
		self.solving_dict = {}
		
		for i in range(9):
			for j in range(9):
				self.space = self.board[i,j]
				if self.space == 0:
					self.solving_dict[(i,j)] = [1,2,3,4,5,6,7,8,9]
				else:
					self.solving_dict[(i,j)] = [self.space]


	def checkrow(self,i,j):
		row_nonzero_index = np.where(self.board[i,:]>0)
		#gives the index location of numbers already in the row
		#for j in range(9):
		if self.board[i,j] == 0:
			for index in range(len(row_nonzero_index[0])):
				self.eliminated_list.append(self.board[i,row_nonzero_index[0][index]])
	

	def checkcol(self,i,j):
		col_nonzero_index = np.where(self.board[:,j]>0)
		#gives the index location of numers already in the column 
		#for i in range(9):
		if self.board[i,j] == 0:
			for index in range(len(col_nonzero_index[0])):
				self.eliminated_list.append(self.board[col_nonzero_index[0][index],j])



	def checkbox(self,i,j):
		a = i/3
		b = j/3
		#this gives you the proper indexes for the boxes based on where the space is
		row_range = range(3*a,3*a+3)
		col_range = range(3*b,3*b+3)
		#these ranges give you the proper rows and columns in the box you need to look at. 
		box_nonzero_index = np.where(self.board[3*a:3*a+3,3*b:3*b+3]>0)
		
		
		if self.board[i,j] == 0:
			self.checkrow(i,j)
			self.checkcol(i,j)

			for x in range(len(box_nonzero_index[0])):

				self.eliminated_list.append(self.board[box_nonzero_index[0][x]+3*a,box_nonzero_index[1][x]+3*b])


		
	def checkspace(self,i,j):
		if self.board[i,j] == 0:
			self.checkrow(i,j) 
			self.checkcol(i,j)
			self.checkbox(i,j)
			#this will compile a list of all the numbers that need to be removed from the solution 
			#for the space that is being checked
			self.eliminated_list = list(dict.fromkeys(self.eliminated_list))
			#this will remove any duplicates from the list of values that need to be removed. 
			for x in range(len(self.eliminated_list)):
				self.solving_dict[(i,j)].remove(self.eliminated_list[x])
			self.eliminated_list = []
			#this will iterate the list of values that need to be removed and actually
			#Remove them from the dictionary solutions. 
			#print(self.solving_dict[(i,j)])
		if len(self.solving_dict[(i,j)]) == 1:
			self.board[i,j] = self.solving_dict[(i,j)][0]
		
		#print("solution",self.solving_dict[(i,j)])

	def every_space(self): 
		for i in range(9):
			for j in range(9):
				#print("i,j",[i,j])
				self.checkspace(i,j)
				# print((i,j),self.solving_dict[(i,j)])
				# #print("____________________________________________________")

		# raw_input()
		# print(self.board)
		# print(self.solving_dict)



	def col_most_nonzero(self):
		#this function will find the column with the most solutions 
		for j in range(9):
			col_array = np.where(self.board[:,j]>0)
			col_count = len(col_array[0])
			self.col_list.append(col_count)
		maxpos = self.col_list.index(max(self.col_list)) 
		self.col_location = self.board[:,maxpos]
		print(self.col_location)

	def col_pairs(self):
		#this function will look for the "pairs" in a column 
		#then take out the solutions from other numbers in the same box. 

		#making the solutions based on rows and columns
		self.col_most_nonzero()
		self.checkcol(i,self.col_location)
		self.checkrow(i,self.col_location)
		print(solving_dict[(i,self.col_location)])

		#identifying the pair
		#identifying what box the pair is in
		#taking out the pair solutions from the other numbers already in the box


	def truth_table(self):
		#the truth table is a table that shows the #s that are in a space in the rows
		#and how many time a number appears as a potential solution in columns
		#in the form of a 1 of 0
		#patterns found in this table can help eliminate more potential solutions 

		self.every_space()

		#print(self.board)
		for i in range(3,6):
			#print(i)
			self.temp = []
			#this initializes the list of the values of potential solutions for a row
		
			a_len = len(np.where(self.board[i,:] < 1)[0])
			#print("a_len", a_len)
			#Based on the row, this will find the length of the list that
			#of the number of blank spaces.
			#aka the # of blank spaces = the length of the list 

			truth_array = np.zeros([a_len,a_len])
			#this will initialize a truth_array that is all zeros 
			#based on the number of blank spaces there are in the current 
			#row the program is checking. 
			#print(truth_array)

			
			for j in range(9): 
				#this loop will go through all of the spaces in the row
				if self.board[(i,j)] == 0: 
					#if the space is blank, then it will add the potential 
					#solutions of that space to a longer list of potential solutions
					#of the whole row 
					self.temp.extend(self.solving_dict[(i,j)])
					#print(self.temp)

			uni,count = np.unique(self.temp,return_counts = True)
			#this line of code will give you two lists in an array
			#the first list will give you "unique solutions." 
			#[1,1,1,1,2,2,2] --> [1,2]
			#the second list will give you "count": how many of each number was in self.temp
			#[1,1,1,1,2,2,2] --> [4,3]

			# print(uni)
			# print(count)

			counter = 0
			#We need to set counter to zero here because it will help us 




			for j in range(9):
				#this will iterate through each space in the row
				if self.board[(i,j)] == 0:	
					temp_sol = self.solving_dict[(i,j)]
					#print(self.solving_dict[(i,j)])
					#if the space is blank, temp_sol will be replaced with the 
					#potential solutions of that space
					

					for k in range(len(temp_sol)):
						#this will itereate through the lenth of the potential solutions
						#for the space you are checking.
						#the main objective is to add ones to the truth table 
						#when appropriate 
						print("temp_sol", temp_sol)
						print("iterating through",range(len(temp_sol)))
						print("k",k)
						index = np.where(uni == temp_sol[k])
						#This will output the indexes of the number 
						print(temp_sol[k])
						print("uni",uni)
						print(uni==temp_sol[k])
						print("index", index)
						truth_array[counter][index] = 1
						print(truth_array)
						raw_input()

						#print(truth_array)
					counter += 1
						# raw_input()
			raw_input()
			print("i", i)
			print(self.board[i])
			print(truth_array)
			#for column in truth_array:
				#iterate through each column of truth array
				#find columns that have the EXACT same pattern
				#if three columns have the same patter, they must each have three ones
				#if two columns have the same pattern, they must each have two ones. 

			print("temp",self.temp)
			print("potential",uni,"choices",count)







game1 = sudoku()
#game1.checkrow(0,1)
#game1.checkcol(0,1)
#game1.checkbox(0,1)
#game1.checkspace(1,2)
#game1.initialize_dict()
#game1.every_space()
#game1.col_most_nonzero()
#game1.col_pairs()
game1.truth_table()