#!/usr/bin/python3


def main():

    choice_params = True

    while choice_params:
        beer = int(input("How many bottles of beer do we need? (must be < 100)"))
        if beer > 100:
            print("You can\'t have more than 100 beers!")
        else:
            choice_params = False

    for bottle in range(beer):
        print(f"{beer} bottles of beer on the wall!")
        print(f" {beer} bottles of beer!")

        beer -= 1
        print(f" You take one down, pass it around!")
        print(f"{beer} bottles of beer on the wall!")

if __name__ == "__main__":
    main()
