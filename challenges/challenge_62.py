#!/usr/bin/python3

def main():

    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    for farm in farms:
        animals= farm.get("agriculture")
        print(animals)

        print(farms.get("name"))
        usr_choice = input("Type a farm above to see the animals they have!")

        if usr_choice in farms["name"]:
            print(farms.get("agriculture"))










if __name__ == "__main__":
    main()
