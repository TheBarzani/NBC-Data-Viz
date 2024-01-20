
# Python program to read
# json file
 
import json

def main():
    # Opening JSON file
    e1 = open('data/Exchange_1.json')
    e2 = open('data/Exchange_2.json')
    e3 = open('data/Exchange_3.json')
    # returns JSON object as 
    # a dictionary
    data = json.load(e1)
    
    # Iterating through the json
    # list
    for i in data:
        print(i["TimeStamp"])
    
    # Closing file
    e1.close()
    e2.close()
    e3.close()

if __name__ == "__main__":
    main()