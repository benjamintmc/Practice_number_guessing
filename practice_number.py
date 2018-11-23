# Generate random integer from 1 - 100
# Let the user guess and tell them the answer is larger or smaller if the answer was wrong
# Let the user know when the answer was correct

import random

ans = random.randint(1, 100)
time = 0

while True:
	guess = input('Try your guess: ')
	guess = int(guess)
	time += 1
	if guess == ans:
		print('How smart!')
		print('You tried', time, 'times to get the answer!')
		break
	elif guess > ans:
		print('Too big')
	elif guess < ans:
		print('Too small')
	print('This is your guess no.', time, '.')