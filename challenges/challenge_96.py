#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import html

URL= "https://opentdb.com/api.php?amount=10&category=11&difficulty=medium&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data = requests.get(URL).json()
    # print(data)

    for trivia in data['results']:
        question = html.unescape(trivia['question'])
        correct = html.unescape(trivia['correct_answer'])
        incorrect00 = html.unescape(trivia['incorrect_answers'][0])
        incorrect01 = html.unescape(trivia['incorrect_answers'][1])
        incorrect02 = html.unescape(trivia['incorrect_answers'][2])
        
        formatted_question = f'''{question}
                                 '''
                                 

if __name__ == "__main__":
    main()

