#!/usr/bin/python3

import pandas as pd

def main():

    csv = pd.read_csv("~/mycode/data_sets/pandas/5movies.csv")

    json = json.to_json("5movies_translated_from_csv_to_json.json")

    print(json)

if __name__ == "__main__":
    main()
