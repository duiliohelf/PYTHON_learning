#This finds out what number you are thinking about in a range of 0 to 100.
#It uses a bisectin method.


sec = 100
epsilon = 0.01
num_guesses = 0
low = 0
high = sec
guess = (high + low)/2.0
c = guess

print('Please think of a number between 0 and 100!')
print('Is your secret number '+ str(guess) + '?')

qst = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.: "))


while qst != 'c':
    if qst == 'h' or qst == 'l':
        if qst == 'h':
            high = guess
        else:
            low = guess

        guess = (high + low) // 2
        int(guess)
        num_guesses += 1
    else:
        print("You have typed a wrong letter!")

    print('Is your secret number ' + str(guess) + '?')

    qst = str(input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.: "))

print('Game over. Your secret number was: ' + str(guess))




