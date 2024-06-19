import argparse
import re

# List of regex matchers
obj = re.compile('\{(.*?)\}',re.DOTALL)

def parseJson(fileName):
    f = open(fileName)
    contents = f.readlines()
    print(contents[0])
    if not obj.match(contents[0]) == None:
        
        return 0
    else:
        return 1

def main():
    parser = argparse.ArgumentParser('JSON File Parser','Allows you to parse a JSON file into a dictionary')
    parser.add_argument('filename',type=str,nargs=1)
    args = parser.parse_args()

    jsonObj = parseJson(args.filename[0])
    print(jsonObj)

main()