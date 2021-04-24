import json
import ijson
import re


anarchistSwearCount = 0
anarchistCommCount = 0
totalUpVotes = 0
totalSwearVotes = 0
with open("clean_comments_anarchist_november_2017.txt", "r") as comms_nov, open("clean_comments_anarchist_december_2017.txt", "r") as comms_dec, open("clean_comments_anarchist_january_2018.txt", "r") as comms_jan, open("clean_comments_anarchist_february_2018.txt", "r") as comms_feb, open("clean_comments_anarchist_march_2018.txt", "r") as comms_mar, open("clean_comments_anarchist_april_2018.txt", "r") as comms_apr, open("clean_comments_anarchist_may_2018.txt", "r") as comms_may, open("clean_comments_anarchist_june_2018.txt", "r") as comms_june, open("clean_comments_anarchist_july_2018.txt", "r") as comms_july, open("clean_comments_anarchist_august_2018.txt", "r") as comms_aug, open("clean_comments_anarchist_september_2018.txt", "r") as comms_sep, open("clean_comments_anarchist_october_2018.txt", "r") as comms_oct:



    commentCount = 0
    swearCount = 0
    swearVotes = 0
    votes = 0
    for line in comms_nov:
        newLine = re.split(r',(?=")', line)
        commentCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        body = newLine[1]

        if "Fuck" in body or "fuck" in body or "Shit" in body or "shit" in body or "Cunt" in body or "cunt" in body or "Damn" in body or "damn" in body or "Asshole" in body or "asshole" in body:
            swearCount+=1
            swearVotes+= float(upVotes[1])


    print("November 2017 comments to r/Anarchist: " + str(commentCount))
    print("Comments with swearwords in Anarchist November: " + str(swearCount))
    print("Average Comment Score November: " + str((votes / commentCount)))
    print("Average Swearing Comment Score November: " + str((swearVotes / swearCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalSwearVotes+= swearVotes
    anarchistCommCount+=commentCount
    anarchistSwearCount += swearCount


    commentCount = 0
    swearCount = 0
    swearVotes = 0
    votes = 0
    for line in comms_dec:
        newLine = re.split(r',(?=")', line)
        commentCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        body = newLine[1]

        if "Fuck" in body or "fuck" in body or "Shit" in body or "shit" in body or "Cunt" in body or "cunt" in body or "Damn" in body or "damn" in body or "Asshole" in body or "asshole" in body:
            swearCount+=1
            swearVotes+= float(upVotes[1])


    print("December 2017 comments to r/Anarchist: " + str(commentCount))
    print("Comments with swearwords in Anarchist December: " + str(swearCount))
    print("Average Comment Score December: " + str((votes / commentCount)))
    print("Average Swearing Comment Score December: " + str((swearVotes / swearCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalSwearVotes+= swearVotes
    anarchistCommCount+=commentCount
    anarchistSwearCount += swearCount

    commentCount = 0
    swearCount = 0
    swearVotes = 0
    votes = 0
    for line in comms_jan:
        newLine = re.split(r',(?=")', line)
        commentCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        body = newLine[1]

        if "Fuck" in body or "fuck" in body or "Shit" in body or "shit" in body or "Cunt" in body or "cunt" in body or "Damn" in body or "damn" in body or "Asshole" in body or "asshole" in body:
            swearCount+=1
            swearVotes+= float(upVotes[1])


    print("January 2018 comments to r/Anarchist: " + str(commentCount))
    print("Comments with swearwords in Anarchist January: " + str(swearCount))
    print("Average Comment Score January: " + str((votes / commentCount)))
    print("Average Swearing Comment Score January: " + str((swearVotes / swearCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalSwearVotes+= swearVotes
    anarchistCommCount+=commentCount
    anarchistSwearCount += swearCount



    commentCount = 0
    swearCount = 0
    swearVotes = 0
    votes = 0
    for line in comms_feb:
        newLine = re.split(r',(?=")', line)
        commentCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        body = newLine[1]

        if "Fuck" in body or "fuck" in body or "Shit" in body or "shit" in body or "Cunt" in body or "cunt" in body or "Damn" in body or "damn" in body or "Asshole" in body or "asshole" in body:
            swearCount+=1
            swearVotes+= float(upVotes[1])


    print("February 2018 comments to r/Anarchist: " + str(commentCount))
    print("Comments with swearwords in Anarchist February: " + str(swearCount))
    print("Average Comment Score February: " + str((votes / commentCount)))
    print("Average Swearing Comment Score February: " + str((swearVotes / swearCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalSwearVotes+= swearVotes
    anarchistCommCount+=commentCount
    anarchistSwearCount += swearCount

    commentCount = 0
    swearCount = 0
    swearVotes = 0
    votes = 0
    for line in comms_mar:
        newLine = re.split(r',(?=")', line)
        commentCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        body = newLine[1]

        if "Fuck" in body or "fuck" in body or "Shit" in body or "shit" in body or "Cunt" in body or "cunt" in body or "Damn" in body or "damn" in body or "Asshole" in body or "asshole" in body:
            swearCount+=1
            swearVotes+= float(upVotes[1])


    print("March 2018 comments to r/Anarchist: " + str(commentCount))
    print("Comments with swearwords in Anarchist March: " + str(swearCount))
    print("Average Comment Score March: " + str((votes / commentCount)))
    print("Average Swearing Comment Score March: " + str((swearVotes / swearCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalSwearVotes+= swearVotes
    anarchistCommCount+=commentCount
    anarchistSwearCount += swearCount

    commentCount = 0
    swearCount = 0
    swearVotes = 0
    votes = 0
    for line in comms_apr:
        newLine = re.split(r',(?=")', line)
        commentCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        body = newLine[1]

        if "Fuck" in body or "fuck" in body or "Shit" in body or "shit" in body or "Cunt" in body or "cunt" in body or "Damn" in body or "damn" in body or "Asshole" in body or "asshole" in body:
            swearCount+=1
            swearVotes+= float(upVotes[1])


    print("April 2018 comments to r/Anarchist: " + str(commentCount))
    print("Comments with swearwords in Anarchist April: " + str(swearCount))
    print("Average Comment Score April: " + str((votes / commentCount)))
    print("Average Swearing Comment Score April: " + str((swearVotes / swearCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalSwearVotes+= swearVotes
    anarchistCommCount+=commentCount
    anarchistSwearCount += swearCount

    commentCount = 0
    swearCount = 0
    swearVotes = 0
    votes = 0
    for line in comms_may:
        newLine = re.split(r',(?=")', line)
        commentCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        body = newLine[1]

        if "Fuck" in body or "fuck" in body or "Shit" in body or "shit" in body or "Cunt" in body or "cunt" in body or "Damn" in body or "damn" in body or "Asshole" in body or "asshole" in body:
            swearCount+=1
            swearVotes+= float(upVotes[1])


    print("May 2018 comments to r/Anarchist: " + str(commentCount))
    print("Comments with swearwords in Anarchist May: " + str(swearCount))
    print("Average Comment Score May: " + str((votes / commentCount)))
    print("Average Swearing Comment Score May: " + str((swearVotes / swearCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalSwearVotes+= swearVotes
    anarchistCommCount+=commentCount
    anarchistSwearCount += swearCount

    commentCount = 0
    swearCount = 0
    swearVotes = 0
    votes = 0
    for line in comms_june:
        newLine = re.split(r',(?=")', line)
        commentCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        body = newLine[1]

        if "Fuck" in body or "fuck" in body or "Shit" in body or "shit" in body or "Cunt" in body or "cunt" in body or "Damn" in body or "damn" in body or "Asshole" in body or "asshole" in body:
            swearCount+=1
            swearVotes+= float(upVotes[1])


    print("June 2018 comments to r/Anarchist: " + str(commentCount))
    print("Comments with swearwords in Anarchist June: " + str(swearCount))
    print("Average Comment Score June: " + str((votes / commentCount)))
    print("Average Swearing Comment Score June: " + str((swearVotes / swearCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalSwearVotes+= swearVotes
    anarchistCommCount+=commentCount
    anarchistSwearCount += swearCount

    commentCount = 0
    swearCount = 0
    swearVotes = 0
    votes = 0
    for line in comms_july:
        newLine = re.split(r',(?=")', line)
        commentCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        body = newLine[1]

        if "Fuck" in body or "fuck" in body or "Shit" in body or "shit" in body or "Cunt" in body or "cunt" in body or "Damn" in body or "damn" in body or "Asshole" in body or "asshole" in body:
            swearCount+=1
            swearVotes+= float(upVotes[1])


    print("July 2018 comments to r/Anarchist: " + str(commentCount))
    print("Comments with swearwords in Anarchist July: " + str(swearCount))
    print("Average Comment Score July: " + str((votes / commentCount)))
    print("Average Swearing Comment Score July: " + str((swearVotes / swearCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalSwearVotes+= swearVotes
    anarchistCommCount+=commentCount
    anarchistSwearCount += swearCount

    commentCount = 0
    swearCount = 0
    swearVotes = 0
    votes = 0
    for line in comms_aug:
        newLine = re.split(r',(?=")', line)
        commentCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        body = newLine[1]

        if "Fuck" in body or "fuck" in body or "Shit" in body or "shit" in body or "Cunt" in body or "cunt" in body or "Damn" in body or "damn" in body or "Asshole" in body or "asshole" in body:
            swearCount+=1
            swearVotes+= float(upVotes[1])


    print("August 2018 comments to r/Anarchist: " + str(commentCount))
    print("Comments with swearwords in Anarchist August: " + str(swearCount))
    print("Average Comment Score August: " + str((votes / commentCount)))
    print("Average Swearing Comment Score August: " + str((swearVotes / swearCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalSwearVotes+= swearVotes
    anarchistCommCount+=commentCount
    anarchistSwearCount += swearCount

    commentCount = 0
    swearCount = 0
    swearVotes = 0
    votes = 0
    for line in comms_sep:
        newLine = re.split(r',(?=")', line)
        commentCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        body = newLine[1]

        if "Fuck" in body or "fuck" in body or "Shit" in body or "shit" in body or "Cunt" in body or "cunt" in body or "Damn" in body or "damn" in body or "Asshole" in body or "asshole" in body:
            swearCount+=1
            swearVotes+= float(upVotes[1])


    print("September 2018 comments to r/Anarchist: " + str(commentCount))
    print("Comments with swearwords in Anarchist September: " + str(swearCount))
    print("Average Comment Score September: " + str((votes / commentCount)))
    print("Average Swearing Comment Score September: " + str((swearVotes / swearCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalSwearVotes+= swearVotes
    anarchistCommCount+=commentCount
    anarchistSwearCount += swearCount

    commentCount = 0
    swearCount = 0
    swearVotes = 0
    votes = 0
    for line in comms_oct:
        newLine = re.split(r',(?=")', line)
        commentCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        body = newLine[1]

        if "Fuck" in body or "fuck" in body or "Shit" in body or "shit" in body or "Cunt" in body or "cunt" in body or "Damn" in body or "damn" in body or "Asshole" in body or "asshole" in body:
            swearCount+=1
            swearVotes+= float(upVotes[1])

    print("September 2018 comments to r/Anarchist: " + str(commentCount))
    print("Comments with swearwords in Anarchist September: " + str(swearCount))
    print("Average Comment Score September: " + str((votes / commentCount)))
    print("Average Swearing Comment Score September: " + str((swearVotes / swearCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalSwearVotes+= swearVotes
    anarchistCommCount+=commentCount
    anarchistSwearCount += swearCount


    print("Total Anarchist Swear count: " + str(anarchistSwearCount))
    print("Total Anarchist Comment count: " + str(anarchistCommCount))
    print("Average Comment Score: " + str(totalUpVotes/anarchistCommCount))
    print("Average Swearing Comment Score: " + str(totalSwearVotes/anarchistSwearCount))
