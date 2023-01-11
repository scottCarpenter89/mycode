!/usr/bin/python3
import requests
import os 
## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    nasacreds = os.getenv("nasa_creds", default="DEMO_KEY")
    nasacreds = "api_key=" + nasacreds
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    ##  nasacreds = returncreds()
    nasacreds = returncreds()
    ## update the date below, if you like
    
    start_date = ""
    while start_date == "":
       start_date = input("what is the start date YYYY-MM-DD?")
    
    startdate = "start_date=" + start_date
    
    
    end_date = input("What is the end date YYYY-MM-DD (press ENTER to skip)?")
    if end_date:
        end_date = "end_date=" + end_date

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    urltolookup = f'{NEOURL}{start_date}&{nasacreds}'

    if end_date: 
        urltolookup = f'{urltolookup}&{end_date}' 

    # make a request with the request library
    neowrequest = requests.get(urltolookup)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()
