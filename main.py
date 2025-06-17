import random

n = random.randint(1,100)
a = 0
guesses = 1

print("--- GUESS THE NUMBER GAME ---")
print("I'm thinking of a number between 1 and 100. Try to guess it!\n")
while(a!=n):
    a = int(input("Enter a Number :"))
    

    if (a < 1 or a > 100):
        print("⚠️ Number out of range! Enter a number between 1 and 100.")
        continue
    
    elif(a<n):
        print("🔼 Higher number Please!")
        guesses += 1
        
    elif(a>n):
        print("🔽 Lower number Please!")
        guesses += 1 

print(f"🎉 Congratulations! You guessed the right number {n} in {guesses} attempts")
