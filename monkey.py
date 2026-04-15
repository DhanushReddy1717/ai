def monkey_banana():
    
    monkey = input("Enter monkey position: ")
    box = input("Enter box position: ")
    banana = input("Enter banana position: ")
    print("\nInitial State:")
    print("Monkey:", monkey, "| Box:", box, "| Banana:", banana)
    print("\nSteps:\n")
    if monkey != box:
        print("Step 1: Monkey moves from", monkey, "to", box)
        monkey = box
    if box != banana:
        print("Step 2: Monkey pushes box from", box, "to", banana)
        box = banana
    print("Step 3: Monkey climbs onto the box")

    
    print("Step 4: Monkey grabs the banana")
    print("\nGoal Achieved: Monkey got the banana!")

monkey_banana()
