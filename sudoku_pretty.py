#https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python



from random import sample 
import numpy as np
from itertools import combinations

base  = 3  # Will generate any size of random sudoku board in O(n^2) time
side  = base*base

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
# #in our case r will iterate through the sequence [1,2,3,4,5,6,7,8,9]
# for r in range(1,side+1):
# 	print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) ) #columns
# # # 		#WHAT IS HAPPENING: this makes all the numbers of the board appear 
# # # 			#Let's BREAK IT DOWN: print the following code: 
# # # 				# for r in range(1,side+1):
# # # 				# 	print("r", r)
# # # 				# 	print(nums)
# # # 				# 	print("nums:these are the numbers/blank spots on the sudoku board",nums[r-1])
# # # 				# 	print("line1: these are the pipes of the sudoku board", line1.split("."))
# # # 				# 	zipping = zip(nums[r-1], line1.split("."))
# # # 				# 	print("this is zip's final list of tuples that joined nums and line1", zipping)
# # # 				# 	print("joining everything", "".join(n+s for n,s in zipping))
# # # 				# 	raw_input()
#  	print([line2,line3,line4][(r%side==0)+(r%base==0)])
# # # 		#WHAT IS HAPPENING:Makes horizontal separators on the board appear 
# # # 		#The modulo here is actually unnesscary. 
# # # 		#if you put print(line2), it yields the same sudoku board
# # 		#Mod was there becaue the original code had non aSCII symbols 
# # 			
# 		#and wanted to control the 3*3 boxes within the sudoku board. 
# 	#TO UNDERSTAND THIS WHOLE ENTIRE FOR LOOP: Joining the "floors",#s, and pipes
# 	#Run this code to get a better idea of what is going on: 
# 	#notice how the individual spaces have a height of two pipes, not one. 
# 	#This occurs because you are stacking lines on top of each other. 
# 		# for r in range(1,side+1):
# 		# 	print("row", "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
# 		# 	raw_input()
# 		# 	print("floor",line2)
# 		# 	raw_input()
# 		# 	print("".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
# 		# 	print(line2)
# 		# 	raw_input()




class sudoku:
	def __init__(self):
		
		#self.board_with_zeros, self.board_true_solution = self.create_board()
		#self.board = np.array([
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
			,[0,2,4,0,1,3,5,0,0]
			,[0,0,5,0,0,7,0,0,0]
			,[0,0,7,0,0,0,0,0,5]
			,[0,0,0,0,0,5,6,0,7]])
		self.eliminated_list = []
		self.initialize_dict()
			#so we have a solution dictionary to work with 
		self.col_list = []
		self.iteration = 1
		#print(self.solving_dict)

	
	#def create_board(self):
		

	def initialize_dict(self):
		#this will create the first iteration of the solution
		#if there is a space with no # --> the solution will be 1-9
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
				#will eliminate the nonzero number from the space's solution

	def checkcol(self,i,j):
		col_nonzero_index = np.where(self.board[:,j]>0)
		#gives the index location of numbers already in the column 
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
			for x in range(len(box_nonzero_index[0])):
				self.eliminated_list.append(self.board[box_nonzero_index[0][x]+3*a,box_nonzero_index[1][x]+3*b])
				#add onto the list of numbers that need to be eliminated
				#for the space

	def checkspace(self,i,j):

		if self.board[i,j] == 0:

			self.checkrow(i,j) 
			self.checkcol(i,j)
			self.checkbox(i,j)
			#this will compile a list of all the numbers that need to be removed from the solution 
			#for the space that is being checked
			self.eliminated_list = list(dict.fromkeys(self.eliminated_list))
			#this will remove any duplicates from the list of values that need to be removed. 
			#print(self.board)

			if len(self.eliminated_list) > 0:
				#basically if there are still numbers that need to be removed from the 
				#space's potential solution list.  
				for x in range(len(self.eliminated_list)):
					if self.eliminated_list[x] in self.solving_dict[(i,j)]:
						self.solving_dict[(i,j)].remove(self.eliminated_list[x])

					# print("i,j",i,j)
					# print("eliminate list",self.eliminated_list)
					# print("range",range(len(self.eliminated_list)))
					# print("x", x)
					# print("dictionary", self.solving_dict[(i,j)])
					# raw_input()
			#this will iterate the list of values that need to be removed and actually
			#Remove them from the dictionary solutions.	
				
			self.eliminated_list = []
			#will need to reset the list because solutions very for each 
			#empty space.  
			
			if len(self.solving_dict[(i,j)]) ==1:
				self.board[i,j] = self.solving_dict[(i,j)][0]
				self.every_space()
			#if there is already a solution, update the sudoku board a
			#and check every space of the board again. 

	def every_space(self): 
		#print("before", self.board)
		for i in range(9):
			for j in range(9):
				self.checkspace(i,j)
		# dot = 1
		# for key in self.solving_dict:
		# 	if len(self.solving_dict[key]) == 1:
		# 		print("solution!", key, self.solving_dict[key], "count", dot)
		# 		dot +=1

		#print("after", self.board)

	def truth_table_row(self):
		#After going through the process of checking screening the solutions
		#for basic columns,boxes, and rows,
		#this function will check paterns in temporary solutions to 
		#further narrow down the solutions by making truth tables for each row

		self.every_space()
		print(self.board)
		#print("before", self.board)

		for i in range(9):
		#this will iterate through all the rows
			temp = []
			#this initializes the list of the values of potential solutions for a row
			empty_space = []
			#this initializes the list of values of the location of the column
			#in the truth table. 
			a_len = len(np.where(self.board[i,:] < 1)[0])
			#finds how many solutions NEED to be found in the row 
			#how: records the indexes of zero integers in the row and store in list
			#finds the length of that list. 
			# print(i)
			# print(self.board[i,:])
			# print(self.board[i,:] < 1)
			# print(np.where(self.board[i,:] < 1))
			# print(np.where(self.board[i,:] < 1)[0])
			# print("alen", a_len)
			truth_array = np.zeros([a_len,a_len])
			#print(truth_array)
			#initializes the truth_array to be all zeros
			#with dimensions based on how many solutions need to be found
			#print(truth_array)

			for j in range(9): 
				#iterate through each space of the row
				if self.board[(i,j)] == 0:
				#if the space has no solution yet
					temp.extend(self.solving_dict[(i,j)])
					#record the numbers that are potential solutions for that
					#whole entire row
					empty_space.append(j)
					#record the loctions by using column index of
					#spaces that still need solutions. 


			uni,count = np.unique(temp,return_counts = True)
			#will find the unique solutions and how many times they appear
			temp = uni
			#the final row of unique solutions for the truth table. 
			
			counter = 0
			for j in range(9):
			#iterate through each space in that row. 
			#this section of the code will put the needed 1s into the table
				if self.board[(i,j)] == 0:
				#if space has no solution yet	
					temp_sol = self.solving_dict[(i,j)]
	
					#set the temporary solution equal to what is in the 
					#solution dictionary already 
					for k in range(len(temp_sol)):
						#iterate through the number of solutions in the dictionary
						#ONLY for that space. 
						#this will look for where the potential solutions 
						#for the space match the the potential solutions for the row
						#this is because the potential solutiosn for the row are in order
						#for how the columns of the truth table are ordered. 
						index = np.where(uni == temp_sol[k])
						#Example:
							#temp_sol = [1,3,9]
							#uni = [1,2,3,9]
							#Iterating through range [0,1,2]
							#Program will go to k = 0
							#program will see where temp_sol[k] == uni
							#in other words, where does 1 appear in uni?
							#program will spit out the index based on uni
	
						#where does the solution in our dictinary
						#match the unique solutions of truth table? 
						#trying to find the column location of where the 
						#number can be a solution for the space in truth table
						truth_array[counter][index] = 1
						# print(truth_array)
						# print("i =", i)
						# raw_input()
						#sets the appropriate places in the truth table to zerio
						#if there is already a solution. 	
						#counter gave us the row, index gives us the column
					counter += 1

		#after the truth table has been made:
			truth_array = np.array(truth_array)
			# print(truth_array)
			#print("i",i,"iteration", self.iteration)
			# print("row")
			# print("(i,j",i,j)
			# print(uni)
			# print(temp_sol)
			# print(truth_array)
			# raw_input()

			one_solution_col = np.sum(truth_array, axis = 0)
			#print(one_solution_col)
			#this will add up the columns of the truth _array
			where_one_col = np.where(one_solution_col == 1)

			#this will output the indices of where there is only one solution 
			#based on the outputs of one_solution_col in array format
		
 			 #_----------------------------------------------------------------
			if len(where_one_col[0]) > 0:
				

				#FOR THE DEFINITE ONE SOLUTION based on truth table columns
				#print("before", self.board)

				#This chunk right here will replace the zero on the sudoku board
				#with the solution. 
				for loc in range(len(where_one_col[0])):
					column = truth_array[:,where_one_col[0][loc]]
					where_one_row = np.where(column == 1)[0][0]
					#print("row", where_one_row)
					where_one_col_board = empty_space[where_one_row]
					# print("column",column)
					# print("where", where_one_row)
				#if there is actually one solution in the truth table:
				one_sol = uni[where_one_col][0]
				#print("one",one_sol)
				self.board[(i, where_one_col_board)] = one_sol
				#this will set the proper space on the sudoku board to its solution 
				self.solving_dict[(i,where_one_col_board)] = one_sol
				self.every_space()
				#updates the solving dictionary's solutions 

				#remember, no need to revise the truth table because when 
				#the progrma iterates through, it creates a new truth table
				#based on the changed criteria outlines above. 

			#for the pairs in column/row case:



				#iterate through the combination way:
					#if the sum brings two 2s in the same place,
					#eliminate the pairs from all other spaces. 


			# print("iteratoin", self.iteration, "i",i, truth_array)
			# print("uni", uni, "location", empty_space)
			# print("4,2",self.solving_dict[(4,2)], "3,2",self.solving_dict[(3,2)])
			# print(self.board)
			# raw_input()

	def truth_table_col(self):
		reverse_board = np.transpose(self.board)
		#this will transpose the oringinal sudoky board so that you can work 
		#with the columns for the truth array 

		#After going through the process of checking screening the solutions
		#for basic columns,boxes, and rows,
		#this function will check paterns in temporary solutions to 
		#further narrow down the solutions by making truth tables for each row

		self.every_space()
		#print(reverse_board)
	

		for i in range(2,3):
		#this will iterate through all the rows
			temp = []
			#this initializes the list of the values of potential solutions for a row
			empty_space = []
			#this initializes the list of values of the location of the column
			#in the truth table. 
			a_len = len(np.where(reverse_board[i,:] < 1)[0])

			#finds how many solutions NEED to be found in the row 
			#how: records the indexes of zero integers in the row and store in list
			#finds the length of that list. 
			# print(i)
			# print(self.board[i,:])
			# print(self.board[i,:] < 1)
			# print(np.where(self.board[i,:] < 1))
			# print(np.where(self.board[i,:] < 1)[0])
			# print("alen", a_len)
			truth_array = np.zeros([a_len,a_len])
			#print(truth_array)
			#initializes the truth_array to be all zeros
			#with dimensions based on how many solutions need to be found
			#print(truth_array)

			for j in range(9): 
				#iterate through each space of the row
				if reverse_board[(i,j)] == 0:
				#if the space has no solution yet
					temp.extend(self.solving_dict[(j,i)])
					#record the numbers that are potential solutions for that
					#whole entire row
					empty_space.append(j)
					#record the loctions by using column index of
					#spaces that still need solutions. 


			uni,count = np.unique(temp,return_counts = True)
			#will find the unique solutions and how many times they appear
			temp = uni

			#the final row of unique solutions for the truth table. 
			
			counter = 0
			for j in range(9):
			#iterate through each space in that row. 
			#this section of the code will put the needed 1s into the table
				if reverse_board[(i,j)] == 0:
				#if space has no solution yet	
					temp_sol = self.solving_dict[(j,i)]

	
					#set the temporary solution equal to what is in the 
					#solution dictionary already 
					for k in range(len(temp_sol)):
						#iterate through the number of solutions in the dictionary
						#ONLY for that space. 

						#this will look for where the potential solutions 
						#for the space match the the potential solutions for the row
						#this is because the potential solutiosn for the row are in order
						#for how the columns of the truth table are ordered. 
						index = np.where(uni == temp_sol[k])
						#Example:
							#temp_sol = [1,3,9]
							#uni = [1,2,3,9]
							#Iterating through range [0,1,2]
							#Program will go to k = 0
							#program will see where temp_sol[k] == uni
							#in other words, where does 1 appear in uni?
							#program will spit out the index based on uni
	
						#where does the solution in our dictinary
						#match the unique solutions of truth table? 
						#trying to find the column location of where the 
						#number can be a solution for the space in truth table
						truth_array[counter][index] = 1
						#sets the appropriate places in the truth table to zerio
						#if there is already a solution. 	
						#counter gave us the row, index gives us the column
					counter += 1

		#after the truth table has been made:
			truth_array = np.array(truth_array)
			# print("i",i,"iteration", self.iteration)
			# print("col")
			# print(truth_array)
			# raw_input()
			print("col")
			print("(i,j",i,j)
			print(uni)
			print(temp_sol)
			print(truth_array)
			raw_input()
			

			one_solution_col = np.sum(truth_array, axis = 0)
			#print(one_solution_col)
			#this will add up the columns of the truth _array
			where_one_col = np.where(one_solution_col == 1)

			#this will output the indices of where there is only one solution 
			#based on the outputs of one_solution_col in array format
		
 			 #_----------------------------------------------------------------
			if len(where_one_col[0]) > 0:
				#FOR THE DEFINITE ONE SOLUTION based on truth table columns
				#print("before", self.board)

				#This chunk right here will replace the zero on the sudoku board
				#with the solution. 
				for loc in range(len(where_one_col[0])):
					column = truth_array[:,where_one_col[0][loc]]
					where_one_row = np.where(column == 1)[0][0]
					#print("row", where_one_row)
					where_one_col_board = empty_space[where_one_row]
					# print("column",column)
					# print("where", where_one_row)
				#if there is actually one solution in the truth table:
				one_sol = uni[where_one_col][0]
				#print("one",one_sol)
				self.reverse_board[(i, where_one_col_board)] = one_sol
				#this will set the proper space on the sudoku board to its solution 
				self.solving_dict[(i,where_one_col_board)] = one_sol
				self.every_space()
				#updates the solving dictionary's solutions 
				#remember, no need to revise the truth table because when 
				#the progrma iterates through, it creates a new truth table
				#based on the changed criteria outlines above. 
			#------------------------------------------------------------------

			combination = list(combinations(truth_array,2))
			print(truth_array)
			print("length", len(combination))
			print(combination)
			#raw_input()

			#for combo in combination:
		

			for combo in combination:
				pair_check = []
				for element in range(a_len):
					pair_check.append(combo[0][a_len] + combo[1][a_len])






			print("should equal= [1]",combination[0][0][0])
			print("should equal= [1]",combination[0][1][0])
			print(combination[0][0][0] + combination[0][1][0])
				#for element in range(a_len):        
					# 
					# print(a_len)





		
	
	




			
	def truth_table(self):
		self.truth_table_row()
		self.truth_table_col()

	def solve(self):
		self.truth_table()
		self.iteration += 1
		self.truth_table()
		self.iteration += 1
		self.truth_table()
		print(self.board)




game1 = sudoku()
#game1.checkrow(0,1)
#game1.checkcol(0,1)
#game1.checkbox(0,1)
#game1.checkspace(3,1)
#game1.initialize_dict()
#game1.every_space()
#game1.truth_table_row()
game1.truth_table_col()
#game1.truth_table()
#game1.solve()