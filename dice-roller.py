import random

def roll_dice(sides, rolls):
    results = []
    for _ in range(rolls):
        roll = random.randint(1, sides)
        results.append(roll)
    return results

def main():
    print("Welcome to the Dice Rolling Simulator!")
    sides = int(input("Enter the number of sides on the dice: "))
    rolls = int(input("Enter the number of rolls: "))
    
    print("\nRolling the dice...\n")
    results = roll_dice(sides, rolls)
    
    print(f"Results of rolling a {sides}-sided dice {rolls} times:")
    for i, result in enumerate(results, 1):
        print(f"Roll {i}: {result}")

if __name__ == "__main__":
    main()
