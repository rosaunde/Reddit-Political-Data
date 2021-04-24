import json
import ijson
import re

with open("RS_2017_11.txt", "r") as infile, open("anarchist_november_2017.txt", "w") as anfile, open("communist_november_2017.txt", "w") as commfile, open("libertarian_november_2017.txt", "w") as liberfile, open("liberal_november_2017.txt", "w") as liberfile, open("conservative_november_2017.txt", "w") as confile:
    count = 0;
    for line in infile:
        newLine = re.split(r',(?=")', line)
        counter = 0
        while counter < len(newLine):
                if newLine[counter] == '"subreddit":"Anarchism"':
                    anfile.write(newLine)
                if newLine[counter] == '"subreddit":"communism"':
                    commfile.write(newLine)
                if newLine[counter] == '"subreddit":"Libertarian"':
                    liberfile.write(newLine)
                if newLine[counter] == '"subreddit":"Liberal"':
                    libfile.write(newLine)
                if newLine[counter] == '"subreddit":"Conservative"':
                    confile.write(newLine)



                counter = counter+1
        count = count + 1
print(count)
