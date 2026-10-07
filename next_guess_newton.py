x = float(input("What x to find the square root of? ")) 
guess = float(input("What guess to start with? "))
print("Current estimate square:", guess**2)
next_guess = guess - (guess**2 - x) / (2 * guess)
print("Next guess:", next_guess)

