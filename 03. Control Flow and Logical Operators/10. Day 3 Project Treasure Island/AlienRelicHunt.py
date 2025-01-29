print('''
                           *     .--.
                                / /  `
               +               | |
                      '         \ \__,
                  *          +   '--'  *
                      +   /\
         +              .'  '.   *
                *      /======\      +
                      ;:.  _   ;
                      |:. (_)  |
                      |:.  _   |
            +         |:. (_)  |          *
                      ;:.      ;
                    .' \:.    / `.
                   / .-'':._.'`-. \
                   |/    /||\    \|
                 _..--"""````"""--.._
           _.-'``                    ``'-._
         -'                                '-

''')
print("Welcome to Alien Relic Hunt.")
print("Your mission is to find the ancient alien relic.")

# First Decision
choice1 = input('Your spaceship approaches an alien planet. Choose a landing site: "Crimson Canyons" or "Frosted Wastes". Type "crimson" or "frosted"\n').lower()

if choice1 == "crimson":
    # Second Decision
    choice2 = input("You land in the Crimson Canyons. A massive sandstorm approaches! Type 'shelter' to take cover, 'drive' to speed away, or 'scan' to look for structures.\n").lower()
    
    if choice2 == "shelter":
        # Third Decision
        choice3 = input("You find a cave with glowing crystals: red, yellow, and blue. Touch one to activate a portal. Which color?\n").lower()
        
        if choice3 == "red":
            print("A laser beam activates, vaporizing you. Game over.")
        elif choice3 == "yellow":
            # Fourth Decision
            choice4 = input("The portal opens to a chamber! Two relics appear: one glowing, one humming. Which do you take? Type 'glowing' or 'humming'\n").lower()
            if choice4 == "glowing":
                print("It's a holographic decoy! Security drones activate. Game over.")
            elif choice4 == "humming":
                # Fifth Decision
                choice5 = input("The relic hums with power! Activate it here or take it home? Type 'activate' or 'return'\n").lower()
                print("You successfully return the relic to Earth! You win!" 
                if choice5 == "return" 
                else "Uncontrolled energy release destroys the planet. Game over.")
            else:
                print("Indecision triggers security systems. Game over.")
                
        elif choice3 == "blue":
            print("The cave floods with toxic gas. Game over.")
        else:
            print("You stumble and trigger a trap. Game over.")
            
    elif choice2 == "drive":
        # Alternate Third Decision
        choice3 = input("You find a canyon crossing: 'accelerate' over the gap or 'detour' around it?\n").lower()
        print("You overshoot and crash! Game over." if choice3 == "accelerate" else "The detour leads into quicksand. Game over.")
        
    elif choice2 == "scan":
        # Alternate Third Decision
        choice3 = input("You detect a buried structure. 'Dig' manually or 'blast' it open?\n").lower()
        print("Ancient defense systems annihilate you." if choice3 == "blast" else "You unearth... nothing but rocks. Supplies run out. Game over.")
    
    else:
        print("The sandstorm overtakes you. Game over.")

else:  # Frosted Wastes path
    # Second Decision
    choice2 = input("You land in the Frosted Wastes. Sensors detect thermal vents. Type 'follow' heat signatures or 'dig' near strange markings.\n").lower()
    
    if choice2 == "follow":
        # Third Decision
        choice3 = input("You find a frozen structure! Enter through 'main' gate or 'vent' shaft?\n").lower()
        
        if choice3 == "main":
            print("Ancient security systems activate. Game over.")
        elif choice3 == "vent":
            # Fourth Decision
            choice4 = input("Inside, find two chambers: 'left' with strange sounds or 'right' glowing softly.\n").lower()
            
            if choice4 == "right":
                print("You discover the relic... but it's frozen in ice! Use 'laser' to cut it out or 'wait' for thaw.\n").lower()
                print("Laser damages the relic!" if choice4 == "laser" else "The ice never melts. Game over.")
            else:
                print("You awaken a frozen predator. Game over.")
    
    elif choice2 == "dig":
        # Alternate Third Decision
        choice3 = input("You uncover alien machinery! 'Touch' the controls or 'document' it first?\n").lower()
        print("The machine activates and disintegrates you!" if choice3 == "touch" else "A ice avalanche buries the site. Game over.")
    
    else:
        print("Hypothermia sets in. Game over.")