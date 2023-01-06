#!/usr/bin/python3

def main(): 

    grappling_match = True

    defense = {
            "standing": "close the distance, establish control, and stabilize your base", 
            "open guard": "use your legs to keep distance, control your opponent with feet on their hips or hooks",
            "closed guard": "break your opponent\'s posture, establish your grips, and close their distance from you",
            "side control": "establish your frames on the hip and neck, stay off your back, and create space with your hips", 
            "full mount": "get frames on your opponents hips, prevent them from inching up, destabilize their base",
            "back control": "protect your neck, remain calm, and try to turn to face your opponent"
            }

    while grappling_match:
        try:
            continue_advice = True
            print(list(defense.keys()))
            position = input("\nWhat BJJ defensive position would you like advice on from the list above? ").lower()
            if defense.get(position.lower()):
               print("\n" + str(defense.get(position)).capitalize())
               print("\n")
            else:
                print("Can\'t find anything on: " + position + "\n")
        except TypeError as invalid_key:

            print("The defensive position, " + position + " was not found. Please try again.\n")

        while continue_advice:
            try: 
                ask_again = input("\nWould you like to hear advice on anything else? (y/n)\n")
                if "n" in ask_again.lower():
                    grappling_match = False
                    continue_advice = False
                elif "y" in ask_again.lower():
                    continue_advice = False
                else:
                    print("I don\'t recognize your answer. Please try again.\n")

            except: 
                print("Hmm something went wrong, we\'ll look into it.")

if __name__ == "__main__": 
    main()

