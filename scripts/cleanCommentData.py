import json
import ijson
import re

with open("comments_conservative_march_2018.txt", "r") as infile, open("clean_comments_conservative_march_2018.txt", "w") as outfile:

    for line in infile:
        newLine = re.split(r',(?=")', line)
        counter = 0
        newString = ""
        while counter < len(newLine):
                category = newLine[counter].split(":")
                if category[0] == '{"author"':
                    newString = newString + newLine[counter] + ","

                if category[0] == '"created_utc"':
                    newString = newString + newLine[counter] + ","

                if category[0] == '"score"':
                    newString = newString + newLine[counter] + ","

                if category[0] == '"subreddit"':
                    newString = newString + newLine[counter]

                if category[0] == '"body"':
                    newString = newString + newLine[counter] + ","


                counter = counter+1
        newString = newString + "}" + "\n"
        outfile.write(newString)
