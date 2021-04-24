import json
import ijson
import re

anarchistTrumpCount = 0
anarchistSubCount = 0
totalUpVotes = 0
totalTrumpVotes = 0
with open("clean_anarchist_november_2017.txt", "r") as ansubs_nov, open("clean_anarchist_december_2017.txt", "r") as ansubs_dec, open("clean_anarchist_january_2018.txt", "r") as ansubs_jan, open("clean_anarchist_february_2018.txt", "r") as ansubs_feb, open("clean_anarchist_march_2018.txt", "r") as ansubs_mar, open("clean_anarchist_april_2018.txt", "r") as ansubs_apr, open("clean_anarchist_may_2018.txt", "r") as ansubs_may, open("clean_anarchist_june_2018.txt", "r") as ansubs_june, open("clean_anarchist_july_2018.txt", "r") as ansubs_july, open("clean_anarchist_august_2018.txt", "r") as ansubs_aug, open("clean_anarchist_september_2018.txt", "r") as ansubs_sep, open("clean_anarchist_october_2018.txt", "r") as ansubs_oct:



    subCount = 0
    trumpCount = 0
    trumpVotes = 0
    votes = 0
    for line in ansubs_nov:
        newLine = re.split(r',(?=")', line)
        subCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        title = newLine[6]

        if "Trump" in title or "trump" in title:
            trumpCount+=1
            trumpVotes+= float(upVotes[1])


    print("November 2017 submissions to r/Anarchist: " + str(subCount))
    print("Mentions of Trump in Anarchist November: " + str(trumpCount))
    print("Average Post Score November: " + str((votes / subCount)))
    print("Average Trump Post Score November: " + str((trumpVotes / trumpCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalTrumpVotes+= trumpVotes
    anarchistSubCount+=subCount
    anarchistTrumpCount += trumpCount


    subCount = 0
    trumpCount = 0
    trumpVotes = 0
    votes = 0
    for line in ansubs_dec:
        newLine = re.split(r',(?=")', line)
        subCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        title = newLine[6]

        if "Trump" in title or "trump" in title:
            trumpCount+=1
            trumpVotes+= float(upVotes[1])


    print("December 2017 submissions to r/Anarchist: " + str(subCount))
    print("Mentions of Trump in Anarchist December: " + str(trumpCount))
    print("Average Post Score December: " + str((votes / subCount)))
    print("Average Trump Post Score December: " + str((trumpVotes / trumpCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalTrumpVotes+= trumpVotes
    anarchistSubCount+=subCount
    anarchistTrumpCount += trumpCount

    subCount = 0
    trumpCount = 0
    trumpVotes = 0
    votes = 0
    for line in ansubs_jan:
        newLine = re.split(r',(?=")', line)
        subCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        title = newLine[6]

        if "Trump" in title or "trump" in title:
            trumpCount+=1
            trumpVotes+= float(upVotes[1])


    print("January 2018 submissions to r/Anarchist: " + str(subCount))
    print("Mentions of Trump in Anarchist January: " + str(trumpCount))
    print("Average Post Score January: " + str((votes / subCount)))
    print("Average Trump Post Score January: " + str((trumpVotes / trumpCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalTrumpVotes+= trumpVotes
    anarchistSubCount+=subCount
    anarchistTrumpCount += trumpCount



    subCount = 0
    trumpCount = 0
    trumpVotes = 0
    votes = 0
    for line in ansubs_feb:
        newLine = re.split(r',(?=")', line)
        subCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        title = newLine[6]

        if "Trump" in title or "trump" in title:
            trumpCount+=1
            trumpVotes+= float(upVotes[1])


    print("February 2018 submissions to r/Anarchist: " + str(subCount))
    print("Mentions of Trump in Anarchist February: " + str(trumpCount))
    print("Average Post Score February: " + str((votes / subCount)))
    print("Average Trump Post Score February: " + str((trumpVotes / trumpCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalTrumpVotes+= trumpVotes
    anarchistSubCount+=subCount
    anarchistTrumpCount += trumpCount

    subCount = 0
    trumpCount = 0
    trumpVotes = 0
    votes = 0
    for line in ansubs_mar:
        newLine = re.split(r',(?=")', line)
        subCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        title = newLine[6]

        if "Trump" in title or "trump" in title:
            trumpCount+=1
            trumpVotes+= float(upVotes[1])


    print("March 2018 submissions to r/Anarchist: " + str(subCount))
    print("Mentions of Trump in Anarchist March: " + str(trumpCount))
    print("Average Post Score March: " + str((votes / subCount)))
    print("Average Trump Post Score March: " + str((trumpVotes / trumpCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalTrumpVotes+= trumpVotes
    anarchistSubCount+=subCount
    anarchistTrumpCount += trumpCount

    subCount = 0
    trumpCount = 0
    trumpVotes = 0
    votes = 0
    for line in ansubs_apr:
        newLine = re.split(r',(?=")', line)
        subCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        title = newLine[6]

        if "Trump" in title or "trump" in title:
            trumpCount+=1
            trumpVotes+= float(upVotes[1])


    print("April 2018 submissions to r/Anarchist: " + str(subCount))
    print("Mentions of Trump in Anarchist April: " + str(trumpCount))
    print("Average Post Score April: " + str((votes / subCount)))
    print("Average Trump Post Score April: " + str((trumpVotes / trumpCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalTrumpVotes+= trumpVotes
    anarchistSubCount+=subCount
    anarchistTrumpCount += trumpCount

    subCount = 0
    trumpCount = 0
    trumpVotes = 0
    votes = 0
    for line in ansubs_may:
        newLine = re.split(r',(?=")', line)
        subCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        title = newLine[6]

        if "Trump" in title or "trump" in title:
            trumpCount+=1
            trumpVotes+= float(upVotes[1])


    print("May 2018 submissions to r/Anarchist: " + str(subCount))
    print("Mentions of Trump in Anarchist May: " + str(trumpCount))
    print("Average Post Score May: " + str((votes / subCount)))
    print("Average Trump Post Score May: " + str((trumpVotes / trumpCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalTrumpVotes+= trumpVotes
    anarchistSubCount+=subCount
    anarchistTrumpCount += trumpCount

    subCount = 0
    trumpCount = 0
    trumpVotes = 0
    votes = 0
    for line in ansubs_june:
        newLine = re.split(r',(?=")', line)
        subCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        title = newLine[6]

        if "Trump" in title or "trump" in title:
            trumpCount+=1
            trumpVotes+= float(upVotes[1])


    print("June 2018 submissions to r/Anarchist: " + str(subCount))
    print("Mentions of Trump in Anarchist June: " + str(trumpCount))
    print("Average Post Score June: " + str((votes / subCount)))
    print("Average Trump Post Score June: " + str((trumpVotes / trumpCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalTrumpVotes+= trumpVotes
    anarchistSubCount+=subCount
    anarchistTrumpCount += trumpCount

    subCount = 0
    trumpCount = 0
    trumpVotes = 0
    votes = 0
    for line in ansubs_july:
        newLine = re.split(r',(?=")', line)
        subCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        title = newLine[6]

        if "Trump" in title or "trump" in title:
            trumpCount+=1
            trumpVotes+= float(upVotes[1])


    print("July 2018 submissions to r/Anarchist: " + str(subCount))
    print("Mentions of Trump in Anarchist July: " + str(trumpCount))
    print("Average Post Score July: " + str((votes / subCount)))
    print("Average Trump Post Score July: " + str((trumpVotes / trumpCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalTrumpVotes+= trumpVotes
    anarchistSubCount+=subCount
    anarchistTrumpCount += trumpCount

    subCount = 0
    trumpCount = 0
    trumpVotes = 0
    votes = 0
    for line in ansubs_aug:
        newLine = re.split(r',(?=")', line)
        subCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        title = newLine[6]

        if "Trump" in title or "trump" in title:
            trumpCount+=1
            trumpVotes+= float(upVotes[1])


    print("August 2018 submissions to r/Anarchist: " + str(subCount))
    print("Mentions of Trump in Anarchist August: " + str(trumpCount))
    print("Average Post Score August: " + str((votes / subCount)))
    print("Average Trump Post Score August: " + str((trumpVotes / trumpCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalTrumpVotes+= trumpVotes
    anarchistSubCount+=subCount
    anarchistTrumpCount += trumpCount

    subCount = 0
    trumpCount = 0
    trumpVotes = 0
    votes = 0
    for line in ansubs_sep:
        newLine = re.split(r',(?=")', line)
        subCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        title = newLine[6]

        if "Trump" in title or "trump" in title:
            trumpCount+=1
            trumpVotes+= float(upVotes[1])


    print("September 2018 submissions to r/Anarchist: " + str(subCount))
    print("Mentions of Trump in Anarchist September: " + str(trumpCount))
    print("Average Post Score September: " + str((votes / subCount)))
    print("Average Trump Post Score September: " + str((trumpVotes / trumpCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalTrumpVotes+= trumpVotes
    anarchistSubCount+=subCount
    anarchistTrumpCount += trumpCount

    subCount = 0
    trumpCount = 0
    trumpVotes = 0
    votes = 0
    for line in ansubs_oct:
        newLine = re.split(r',(?=")', line)
        subCount+=1
        upVotes = newLine[3].split(":")
        if(upVotes[0] != '"score"'):
            continue
        votes += float(upVotes[1])
        title = newLine[6]

        if "Trump" in title or "trump" in title:
            trumpCount+=1
            trumpVotes+= float(upVotes[1])

    print("September 2018 submissions to r/Anarchist: " + str(subCount))
    print("Mentions of Trump in Anarchist September: " + str(trumpCount))
    print("Average Post Score September: " + str((votes / subCount)))
    print("Average Trump Post Score September: " + str((trumpVotes / trumpCount)))
    print("\n")
    print("\n")
    totalUpVotes+= votes
    totalTrumpVotes+= trumpVotes
    anarchistSubCount+=subCount
    anarchistTrumpCount += trumpCount


    print("Total Anarchist Trump count: " + str(anarchistTrumpCount))
    print("Total Anarchist Submission count: " + str(anarchistSubCount))
    print("Average Post Score: " + str(totalUpVotes/anarchistSubCount))
    print("Average Trump Post Score: " + str(totalTrumpVotes/anarchistTrumpCount))
