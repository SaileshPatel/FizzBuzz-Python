# using a 'for-loop' to check each number from 1 to 100
for i in range(1, 101):
	# if the number is divisble by three with no remainder
	if i % 3 == 0:
		# 'Fizz' is printed in place of the number
		print "Fizz"

	# if the number is divisible by 5 with no remainder
	elif i % 5 == 0:
		# 'Buzz' is printed in place of the number
		print "Buzz"

	# if the number is divisible by 15 (LCM of 3 + 5) with no remainder
	elif i % 15 == 0:
		# 'FizzBuzz' is printed in place of the number
		print "FizzBuzz"

	# if the number isn't divisible by any of the following numbers
	else:
		# the number is printed
		print i