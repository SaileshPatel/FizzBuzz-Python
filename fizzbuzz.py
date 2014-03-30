
# created variable 'keepProgramRunning' with boolean value of 'True'
keepProgramRunning = True
# created while loop, which will keep the program running unless the value of 'keepProgramRunning' is 'False'
while keepProgramRunning:
	# using a 'for-loop' to run numbers from 1 to 100
	for i in range(1, 101):
		# if the number is divisible by three with no remainder
		if i % 3 == 0:
			# 'Fizz'is printed in place of the number
			print "Fizz"
		# if the number is divisible by 5 with no remainder	
		elif i % 5 == 0:
			# 'Buzz' is printed in place of the number
			print "Buzz"
		# if the number is divisible by 15 (LCM of 3 & 5) with no remainder
		elif i % 15 == 0:
			# 'FizzBuzz' is printed in place of the number
			print "FizzBuzz"
		# if the number isn't divisible by any other the following numbers
		else:
			# the number is printed
			print i

	# printing string
	print "Select an option!"
	# printing string
	print "1: Close the program"
	# printing string
	print "Press any other key to restart"
	# assigning user inputted string to the variable 'choice'
	choice = raw_input()

	# if the value of choice is '1'
	if choice == '1':
		# printing string
		print "Goodbye!"
		# the value of 'keepProgramRunning' is changed to 'False'
		keepProgramRunning = False
	# if any other value is entered
	else:
		# restarting the program 
		keepProgramRunning = True