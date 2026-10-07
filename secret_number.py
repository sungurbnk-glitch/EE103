SecretNumber = 27
YourNumber = int(input("Guess the secret number: "))
while True:
    if YourNumber == SecretNumber:
        print("\n !! You guessed it right !!")
        break
    else:
        print("You are not from Gaziantep...")
    YourNumber = int(input("\n Guess the secret number one more time: "))
    
