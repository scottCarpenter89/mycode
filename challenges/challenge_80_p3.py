#!/usr/bin/python3

import pandas as pd

def main():

    json = pd.read_json("~/mycode/data_sets/pandas/5movies.json")

    json.to_xlsx("5movies_translated_from_json_to_xlxs.xlsx")


if __name__ == "__main__":
    main()
