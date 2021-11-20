def main():
    print("It’s time to go on a scavenger hunt!")
    print("You'd be amazed how many things can go wrong!")
    time = float(input("Please enter how long you want to travel for:"))
    initialPos = 7.0
    velocity = 5.0
    acceleration = 1.0
    position = initialPos + velocity * time + float(1 / 2) * acceleration * time ** 2
    
    print(position)
    
main()