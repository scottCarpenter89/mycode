#!/usr/bin/python3

"""Challenge 67 - Looping Vampires"""

def vampytimes_maker(line):
    """write lines into a file if they containvampire"""

    line = line.rstrip()
    line = line + "\n"

    with open("vampytimes.txt", "a") as vamp_file:
        vamp_file.write(line)

        return line

def main(): 

    count_dracula = 0

    with open("dracula.txt") as dracula:
        for line in dracula:
            if "vampire" in line.lower():
                count_dracula += 1 
                #  print(line)

                print(vampytimes_maker(line), end="")

    print("\nTotal number of lines with the work vampire: ", count_dracula)


if __name__ == "__main__":
    main()
