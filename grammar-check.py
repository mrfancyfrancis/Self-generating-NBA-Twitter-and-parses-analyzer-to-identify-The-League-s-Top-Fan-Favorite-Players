import en_core_web_sm
import csv
# load en_core_web_sm of English for vocabluary, syntax & entities
nlp = en_core_web_sm.load()

#  "nlp" Objectis used to create documents with linguistic annotations.
lines = [line.rstrip('\n') for line in open('tweets.txt')]
players = [""]
ranking = [["Player","Mentions","Likeability"]]
for line in lines:
    docs = nlp(line)
    positivity = 1
    name = str(docs[0])+" "+str(docs[1])
    for word in docs:
        #print(word.text,word.pos_,word.dep_)
        if(word.dep_ == "neg"):
            positivity*=(-1)
        elif(word.dep_ == "acomp"):
            positivity*=1
    #print("Player:",name)
    #print("Positivity:",positivity)
    if name in players:
        ranking[players.index(name)][1]+=1
        ranking[players.index(name)][2]+=positivity
    else:
        players.append(name)
        ranking.append([name,1,positivity])
print(ranking)
with open('popularity.csv', mode='w') as csv_file:
    csv_file = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in ranking:
        csv_file.writerow(i)
'''docs = nlp("Michael Jordan and Andre Kirilenko is good in Basketball")
positivity = 1
name = str(docs[0])+" "+str(docs[1])
for word in docs:
    if(word.dep_ == "neg"):
        positivity*=1
    elif(word.dep_ == "acomp"):
        positivity*=1
print("Player:",name)
print("Positivity:",positivity)'''