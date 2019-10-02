#https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python



from random import sample 

base  = 3  # Will generate any size of random sudoku board in O(n^2) time
side  = base*base
nums  = sample(range(1,side+1),side) # random numbers
	#This generates a random list of numbers between 1-9 
	#Translates to sample(range(1,10),9)
	#This is what the sample function does: 
	#cannot repeat numbers
board = [[nums[(base*(r%base)+r//base+c)%side] for c in range(side) ] for r in range(side)]
rows  = [ r for g in sample(range(base),base) for r in sample(range(g*base,(g+1)*base),base) ] 
cols  = [ c for g in sample(range(base),base) for c in sample(range(g*base,(g+1)*base),base) ] 
board = [[board[r][c] for c in cols] for r in rows]


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




# #________________________________________________________________________________
# symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# nums   = [[""]+[symbol[n] for n in line] for line in board ]
# nums2   = [[symbol[n] for n in line] for line in board ]
# 	#what is happening with the "nums" variable: 
# 		#it takes the board with zeros
# 		#If n = 0, aka if the program reaches a spot on the board that is zero,
# 		#it will print [''] 
# 		#empty space of symbol. Because symbol[n] when n=0 is ''
# 		#IF n=another number, program will print [ 'another number']
# 		#BREAKING IT DOWN: print this code to see what's going on in the loop
# #			print ("board",board)
# 				# for line in board:
# 				# 	print("line",line)
# 				# 	print("")
# 				# 	for n in line:
# 				# 		print("n", n)
# 				# 		print([symbol[n]])
# 				# 	print("this is nums", nums)
# 				# 	raw_input()
# #________________________________________________________________________________


# #in our case r will iterate through the sequence [1,2,3,4,5,6,7,8,9]
# for r in range(1,side+1):
# 	print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) ) #columns
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

# 	print([line2,line3,line4][(r%side==0)+(r%base==0)])
# # 		#WHAT IS HAPPENING:Makes horizontal separators on the board appear 
# # 		#The modulo here is actually unnesscary. 
# # 		#if you put print(line2), it yields the same sudoku board
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




	











