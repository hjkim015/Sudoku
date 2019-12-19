
#https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python
from random import sample 
import numpy as np
from itertools import combinations
import copy 


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
			#print ("board",board)
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
		
		#board_with_zeros, board_true_solution = self.create_board()
		#board = np.array([
 	 	# 	 [0,0,1,0,0,0,0,0,0]
		# 	,[3,0,0,9,0,0,0,0,1]
		# 	,[9,0,0,0,0,0,0,0,0]
		# 	,[0,0,0,5,6,0,0,0,0]
		# 	,[5,6,0,0,0,0,0,0,0]
		# 	,[0,2,4,0,1,3,5,0,0]
		# 	,[0,0,5,0,0,7,0,0,0]
		# 	,[0,0,7,0,0,0,0,0,5]
		# 	,[0,0,0,0,0,5,6,0,7]])
		board = np.array([
 			 [4,0,1,0,5,0,9,0,0]
			,[3,0,0,9,0,0,0,0,1]
			,[9,0,2,0,0,1,0,5,0]
			,[8,0,3,5,6,0,7,0,4]
			,[5,6,0,7,0,4,0,1,0]
			,[0,2,4,0,1,3,5,0,0]
			,[0,0,5,0,0,7,0,4,0]
			,[0,0,7,0,0,8,0,0,5]
			,[0,4,0,1,0,5,6,0,7]])
		self.eliminated_list = []
		solving_dict = {}
		self.initialize_dict(board, solving_dict)
			#so we have a solution solving_dict to work with 
		self.col_list = []

	#def create_board(self):

	def initialize_dict(self, board, solving_dict):
		#this will create the first iteration of the solution
		#if there is a space with no # --> the solution will be 1-9
		for i in range(9):
			for j in range(9):
				self.space = board[i,j]
				if self.space == 0:
					solving_dict[(i,j)] = [1,2,3,4,5,6,7,8,9]
				else:
					solving_dict[(i,j)] = [self.space]

		return board, solving_dict
	def checkrow(self,i,j,board, solving_dict):
		row_nonzero_index = np.where(board[i,:]>0)
		#gives the index location of numbers already in the row
		if board[i,j] == 0:
			for index in range(len(row_nonzero_index[0])):
				self.eliminated_list.append(board[i,row_nonzero_index[0][index]])
				#will eliminate the nonzero number from the space's solution
		return i,j,board, solving_dict
	def checkcol(self,i,j, board, solving_dict):
		col_nonzero_index = np.where(board[:,j]>0)
		#gives the index location of numbers already in the column 
		#for i in range(9):
		if board[i,j] == 0:
			for index in range(len(col_nonzero_index[0])):
				self.eliminated_list.append(board[col_nonzero_index[0][index],j])	

		return board, solving_dict
		a = i/3
		b = j/3
		#this gives you the proper indexes for the boxes based on where the space is
		row_range = range(3*a,3*a+3)
		col_range = range(3*b,3*b+3)
		#these ranges give you the proper rows and columns in the box you need to look at. 
		box_nonzero_index = np.where(board[3*a:3*a+3,3*b:3*b+3]>0)
		
		
		if board[i,j] == 0:
			for x in range(len(box_nonzero_index[0])):
				self.eliminated_list.append(board[box_nonzero_index[0][x]+3*a,box_nonzero_index[1][x]+3*b])
				#add onto the list of numbers that need to be eliminated
				#for the space
		return i,j, board, solving_dict
	def checkbox(self,i,j, board, solving_dict):
		a = i/3
		b = j/3
		#this gives you the proper indexes for the boxes based on where the space is
		row_range = range(3*a,3*a+3)
		col_range = range(3*b,3*b+3)
		#these ranges give you the proper rows and columns in the box you need to look at. 
		box_nonzero_index = np.where(board[3*a:3*a+3,3*b:3*b+3]>0)
		
		
		if board[i,j] == 0:
			for x in range(len(box_nonzero_index[0])):
				self.eliminated_list.append(board[box_nonzero_index[0][x]+3*a,box_nonzero_index[1][x]+3*b])
				#add onto the list of numbers that need to be eliminated
				#for the space
		return i,j,board, solving_dict
	def checkspace(self,i,j, board, solving_dict):
		if board[i,j] == 0:

			i,j, board, solving_dict = self.checkrow(i,j, board, solving_dict) 
			i,j, board, solving_dict = self.checkcol(i,j, board, solving_dict)
			i,j, board, solving_dict = self.checkbox(i,j, board, solving_dict)
			#this will compile a list of all the numbers that need to be removed from the solution 
			#for the space that is being checked

			self.eliminated_list = list(dict.fromkeys(self.eliminated_list))
			#will give you only unique values (remove the duplicate numbers. )
			#this will remove any duplicates from the list of values that need to be removed. 
			#print(board)

			if len(self.eliminated_list) > 0:
				#basically if there are still numbers that need to be removed from the 
				#space's potential solution list.  
				for x in range(len(self.eliminated_list)):
					print(x, i,j,  self.eliminated_list, solving_dict.keys())
					if self.eliminated_list[x] in solving_dict[(i,j)]:
						solving_dict[(i,j)].remove(self.eliminated_list[x])
			#this will iterate the list of values that need to be removed and actually
			#Remove them from the solving_dict solutions.	
				
			self.eliminated_list = []
			#will need to reset the list because solutions very for each 
			#empty space.  
			if len(solving_dict[(i,j)]) == 1:
				board[i,j] = solving_dict[(i,j)][0]
				# print("i,j", i,j, solving_dict[i,j])
				# print(board)
				# raw_input("checkspace 218")

				board, solving_dict = self.every_space(board, solving_dict)
			#if there is already a solution, update the sudoku board a
			#and check every space of the board again. 
		return i,j, board, solving_dict
	def every_space(self, board, solving_dict): 
		for i in range(9):
			for j in range(9):
				i,j,board, solving_dict = self.checkspace(i,j, board, solving_dict)
		return board, solving_dict			
	def r_table(self, board, solving_dict):
	
		board, solving_dict = self.every_space(board, solving_dict)
		temp = []
		#this initializes the list of the values of potential solutions for a row
		empty_space = []
		#this initializes the list of values of the location of the column
		#in the truth table. 
		a_len = len(np.where(board[self.i,:] < 1)[0])
		#finds how many solutions NEED to be found in the row 
		#how: records the indexes of zero integers in the row and store in list
		#finds the length of that list. 
		truth_array = np.zeros([a_len,a_len])
		#initializes the truth_array to be all zeros
		#with dimensions based on how many solutions need to be found
		for j in range(9): 
			#iterate through each space of the row
			if board[(self.i,j)] == 0:
			#if the space has no solution yet
				temp.extend(solving_dict[(self.i,j)])
				#record the numbers that are potential solutions for that
				#whole entire row
				empty_space.append(j)
				#record the loctions by using column index of
				#spaces that still need solutions. 
		uni,count = np.unique(temp,return_counts = True)
		#will find the unique solutions and how many times they appea
	
		temp = uni

		
		#the final row of unique solutions for the truth table. 
		counter = 0
		for j in range(9):
		#this section of the code will put the needed 1s into the table
			if board[(self.i,j)] == 0:
			#if space has no solution yet	
				temp_sol = solving_dict[(self.i,j)]
				#set the temporary solution equal to what is in the 
				#solution solving_dict already 
				
				for k in range(len(temp_sol)):
					#iterate through the number of solutions in the solving_dict
					#ONLY for that space. 
					#this will look for where the potential solutions 
					#for the space match the the potential solutions for the row
					#this is because the potential solutiosn for the row are in order
					#for how the columns of the truth table are ordered. 
					index = np.where(uni == temp_sol[k])
					# print("i,j", self.i,j, temp_sol)
					# print(uni, "k", k, temp_sol, temp_sol[k], "index", index)
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
					# print("counter", counter)
					# print("index", index)
					# raw_input()
					#sets the appropriate places in the truth table to zerio
					#if there is already a solution. 	
					#counter gave us the row, index gives us the column
				counter += 1


		#after the truth table has been made:
		truth_array = np.array(truth_array)
		one_solution_col = np.sum(truth_array, axis = 0)
		#this will add up the columns of the truth _array
		where_one_col = np.where(one_solution_col == 1)
		#this will output the indices of where there is only one solution
		#based on the sums of the columns. 
		# print(one_solution_col, where_one_col)
		
		return truth_array, one_solution_col, where_one_col, empty_space, uni, a_len, temp, board, solving_dict
	def r_table_one(self, board, solving_dict):
		#will check for one solution pattern in truth table for row
		truth_array, one_solution_col, where_one_col, empty_space, uni, a_len, temp, board, solving_dict = self.r_table(board, solving_dict)
		

		if len(where_one_col[0]) > 0:
			#FOR THE DEFINITE ONE SOLUTION based on truth table columns
			#This chunk right here will replace the zero on the sudoku board
			#with the solution. 
			for loc in range(len(where_one_col[0])):
				column = truth_array[:,where_one_col[0][loc]]
				#the column that has one solution
				where_one_row = np.where(column == 1)[0][0]
				#the row index where that 1 is in the column 
				where_one_col_board = empty_space[where_one_row]
				#the actual "j_space" where the solution is 
				#if there is actually one solution in the truth table:
				one_sol = uni[where_one_col[0][loc]]
				one_sol_list = [one_sol]
				#the solution that needs to be put on the sudoku board. 
				board[(self.i, where_one_col_board)] = one_sol
				#this is changing the board which needs to be set to an integer
				#this will set the proper space on the sudoku board to its solution 
				solving_dict[(self.i,where_one_col_board)] = one_sol_list
				#changing the solving_dict so you need to utilize a list. 
			
			#updates the solving solving_dict's solutions 
			#remember, no need to revise the truth table because when 
			#the progrma iterates through, it creates a new truth table
			#based on the changed criteria outlines above. 
			self.every_space(board,solving_dict)
			truth_array, one_solution_col, where_one_col, empty_space, uni, a_len, temp, board, solving_dict = self.r_table(board, solving_dict)

			# print(board)
	
		return a_len, truth_array, empty_space, temp, board, solving_dict 
	def r_table_pair(self, board, solving_dict):
		a_len, truth_array, empty_space, temp, board, solving_dict = self.r_table_one(board,solving_dict)	
		pair_check_list = []
		pair_space_where = []
		for row in range(a_len): 
			row_sum = sum(truth_array[row])
			#check the sum of each row in the truth table.
			if row_sum == 2:
				pair_check_list.append(row)
				#add the index of that row in truth table to pair_check_list

		combination = list(combinations(range(len(pair_check_list)),2))
		
		#will output the indexes
		if len(combination) > 0 and len(combination[0])>1:
			for combo in combination:

				pair_value_list = []
				#going to be a list of the pair values!!!!!!!
				first_row = truth_array[pair_check_list[combo[0]]]
				second_row = truth_array[pair_check_list[combo[1]]]
				if (first_row == second_row).all():
				#uses the .all() because the stuff before it is a list of trues and falses. 
					non_pair_location = list(empty_space)
					for r in range(2):
						pair_value_index = np.where(np.array(first_row) == 1)[0][r]
						pair_value_list.append(temp[pair_value_index])
						#tells us the physical pair values. 
						pair_space_index = combo[r]
						pair_space_where.append(empty_space[pair_space_index])
						#tells us the j coordinates of the spaces that have the pairs
						non_pair_location.remove(pair_space_where[r])
						#tells us the j coordinates of the spaces that should not 
						#have the pair values in their potential solutions list. 
					#Go an remove those pair values form the non_pairs
					for space in range(len(non_pair_location)):
						removing_space = solving_dict[(self.i,non_pair_location[space])]
					#so for every space where the pair values need to be removed
						for v in range(len(pair_value_list)):
						#iterate through all the values that need to be removed.						
						#the current solutions for the space where values need to be removed. 
							if pair_value_list[v] in removing_space:
								removing_space.remove(pair_value_list[v])

					pair_space_where = []

					board, solving_dict = self.every_space(board,solving_dict)
		#print(board)
	def c_table(self, board, solving_dict):
		reverse_board = np.transpose(board)
		
		#this will transpose the oringinal sudoky board so that you can work 
		#with the columns for the truth array 
		board, solving_dict = self.every_space(reverse_board, solving_dict)
		temp = []
		#this initializes the list of the values of potential solutions for a row
		empty_space = []
		#this initializes the list of values of the location of the column
		#in the truth table. 
		a_len = len(np.where(reverse_board[self.i,:] < 1)[0])
		#finds how many solutions NEED to be found in the row 
		#how: records the indexes of zero integers in the row and store in list
		#finds the length of that list. 
		truth_array = np.zeros([a_len,a_len])
		#initializes the truth_array to be all zeros
		#with dimensions based on how many solutions need to be found

		for j in range(9): 
			#iterate through each space of the row
			if reverse_board[(self.i,j)] == 0:
			#if the space has no solution yet
				temp.extend(solving_dict[(j,self.i)])
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
			if reverse_board[(self.i,j)] == 0:
			#if space has no solution yet	
				temp_sol = solving_dict[(j,self.i)]
				#set the temporary solution equal to what is in the 
				#solution solving_dict already 
				for k in range(len(temp_sol)):
					#iterate through the number of solutions in the solving_dict
					#ONLY for that space. 
					#this will look for where the potential solutions 
					#for the space match the the potential solutions for the row
					#this is because the potential solutiosn for the row are in order
					#for how the columns of the truth table are ordered. 
					index = np.where(uni == temp_sol[k])
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
		one_solution_col = np.sum(truth_array, axis = 0)
		#print(one_solution_col)
		#this will add up the columns of the truth _array
		where_one_col = np.where(one_solution_col == 1)
		#this will output the indices of where there is only one solution 
		#based on the outputs of one_solution_col in array format

		
		
		return truth_array, one_solution_col, where_one_col, empty_space, uni, a_len, temp, board, reverse_board, solving_dict
	def c_table_one (self, board, solving_dict):
		truth_array, one_solution_col, where_one_col, empty_space, uni, a_len, temp, reverse_board, board, solving_dict = self.c_table(reverse_board, solving_dict)
		if len(where_one_col[0]) > 0:
				#FOR THE DEFINITE ONE SOLUTION based on truth table columns
				#print("before", board)
			
				#This chunk right here will replace the zero on the sudoku board
				#with the solution. 
			for loc in range(len(where_one_col[0])):
				column = truth_array[:,where_one_col[0][loc]]
				where_one_row = np.where(column == 1)[0][0]
				where_one_col_board = empty_space[where_one_row]
				#if there is actually one solution in the truth table:
				one_sol = uni[where_one_col[0][loc]]
				one_sol_list = [one_sol]
				self.reverse_board[(self.i, where_one_col_board)] = one_sol
				#this will set the proper space on the sudoku board to its solution 
				solving_dict[(self.i,where_one_col_board)] = one_sol_list
				#updates the solving solving_dict's solutions 
				#remember, no need to revise the truth table because when 
				#the progrma iterates through, it creates a new truth table
				#based on the changed criteria outlines above. 
			

			board, reverse_board, solvingd_dict = self.every_space(board, solving_dict)
		truth_array, one_solution_col, where_one_col, empty_space, uni, a_len, temp, reverse_board, board, solving_dict = self.c_table(board, solving_dict)			
		return a_len, truth_array, empty_space, temp, reverse_board, board 
	def c_table_pair(self, board, solving_dict):	
		a_len, truth_array, empty_space, temp, reverse_board, solving_dict = self.c_table_one(board, solving_dict)
		pair_check_list = []
		pair_space_where = []
		for row in range(a_len):
		#check the sum of each row in the truth table. 
			row_sum = sum(truth_array[row])
			if row_sum == 2:
				pair_check_list.append(row)
				#add the index of that row in truth table to pair_check_list
		combination = list(combinations(range(len(pair_check_list)),2))
		#will output the indexes
		if len(combination) > 0: 
			if len(combination[0])>1 and a_len > 2: 
				for combo in combination:
					pair_value_list = []
					#going to be a list of the pair values!!!!!!!
					first_row = truth_array[pair_check_list[combo[0]]]
					second_row = truth_array[pair_check_list[combo[1]]]

				
					if (first_row == second_row).all():
					#uses the .all() because the stuff before it is a list of trues and falses. 
						
						non_pair_location = list(empty_space)
						for r in range(2):
							# print("i", self.i)
							# print(truth_array)
							# print("combo", combo)
							# print("temporary solutions", temp)
							# print("location on board", empty_space)
							# print("passes pair test!", first_row, second_row)

							pair_value_index = np.where(np.array(first_row) == 1)[0][r]
							#Where the first 1 is in the row
							#print("pair_value index = the index of the first one by column", pair_value_index)

							pair_value_list.append(temp[pair_value_index])
							# print("pair_value_list", pair_value_list)
							#tells us the physical pair values. 
							pair_space_index = combo[r]
							#the index of the spaces that have the pair_values
							# print(empty_space)
							# print(combo)
							# print("pair_space_index", pair_space_index)
							# print(empty_space[pair_space_index])

							pair_space_where.append(empty_space[pair_space_index])
							
							# print("pair_space_where", pair_space_where)
							#tells us the j coordinates of the spaces that have the pairs
							non_pair_location.remove(pair_space_where[r])
							# print("non_pair_location", non_pair_location)
							#tells us the j coordinates of the spaces that should not 
							#have the pair values in their potential solutions list.
							# print("r =", r ) 
							# print("____________________________________________________________")
							# raw_input()


						#Go an remove those pair values form the non_pairs
						for l in range(len(non_pair_location)):
							removing_space = solving_dict[(non_pair_location[l], self.i)]
							# print("the values of the space where pairs need to be removed", removing_space)
						#so for every space where the pair values need to be removed
							# print("# in loop", l, removing_space)
							# raw_input()
							for v in range(len(pair_value_list)):
								# print("v =", v, removing_space)
								# print("pair values", pair_value_list)
							#iterate through all the values that need to be removed.						
							#the current solutions for the space where values need to be removed. 
								if pair_value_list[v] in removing_space:
									removing_space.remove(pair_value_list[v])
									
									raw_input()
						pair_space_where = []

						
						board, solving_dict = self.every_space(board, solving_dict)
			return board, solving_dict
	def initial_screening(self, board, solving_dict):
		for self.i in range(9):
			board, solving_dict = self.r_table_pair(board, solving_dict)
		for self.i in range(9):
			board, solving_dict = self.c_table_pair(board, solving_dict)
		board, solving_dict = self.every_space(board, solving_dict)
		return board, solving_dict
	def whatif(self, board, solving_dict):
		#use the most updated board! 
		board, solving_dict = self.initial_screening(board, solving_dict)
		
		#Make a copy of the solving solving_dict and sudoku board
		whatif_board = np.copy(board)
		whatif_solving_dict = copy.deepcopy(solving_dict)
		emptyspace_dict = {}
		
		
		#separate solving_dict for the empty spaces and their potential solutions
		for key in whatif_solving_dict:
			if len(whatif_solving_dict[key]) > 1:
				emptyspace_dict[key] = whatif_solving_dict[key]
		count = 0
		for key in emptyspace_dict:
			#change a blank space to one of the potential solutions
			print(whatif_board)
			print(key, emptyspace_dict[key])
			whatif_board[key] = emptyspace_dict[key][count]
			self.every_space(whatif_board, whatif_solving_dict) 
			#do I need to change every function to have a solving_dict and board argument?
			print(whatif_board)
			print("in progress")
			# for k in emptyspace_dict:
			# 	print("k", k, emptyspace_dict[k])

			# if len(whatif_solving_dict[key]).all() == 1:
			# 	print("solution!")
			# 	print(whatif_board)
			# 	break

			# elif len(whatif_solving_dict[key]).any() == 0:
			# 	count += 1
			# 	print("try another number")
			# 	whatif_board = np.copu(board)
			# 	whatif_board[key] = emptyspace_dict[key][count]
			# 	self.initial_screening(board, solving_dict)
			# 	print(whatif_board)

			# else:
			# 	print("not done yet")
			# 	print(whatif_board)
			# 	break
			


		
		#run every_space





		#if there are solutions in solving solving_dict that do not have 
		#any potential solutions, reset the board to the original
		#try a different space 
		#rinse and repeat unti you come across a scenario that leads to a 
		#completed sudoku board. 
	def solution_check(self, solving_dict):
		#MODIFY: will give you the potential solutions in order
		#given any solving_dict
		for v in range(9):
			for key in solving_dict:
				if key[v] == v:
					print(key, solving_dict[key])	
			raw_input()






game1 = sudoku()
#game1.checkrow(0,1, board, solving_dict)
#game1.checkcol(0,1)
#game1.checkbox(0,1)
#game1.checkspace(8,0)
#game1.initialize_dict()
#game1.every_space()
#game1.r_table()
#game1.r_table_one()
#game1.r_table_pair()
#game1.c_table_one()
#game1.c_table_pair()
#game1.solve()
#game1.solution_check(solving_dict)
#game1.initial_screening()
board = np.array([
 			 [4,0,1,0,5,0,9,0,0]
			,[3,0,0,9,0,0,0,0,1]
			,[9,0,2,0,0,1,0,5,0]
			,[8,0,3,5,6,0,7,0,4]
			,[5,6,0,7,0,4,0,1,0]
			,[0,2,4,0,1,3,5,0,0]
			,[0,0,5,0,0,7,0,4,0]
			,[0,0,7,0,0,8,0,0,5]
			,[0,4,0,1,0,5,6,0,7]])

solving_dict = {}
game1.whatif(board,solving_dict)
#ame1.solve(board, solving_dict)



  