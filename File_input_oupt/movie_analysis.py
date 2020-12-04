#read csv file
#q1 find year wise release count

f=open("movies.csv","r")
dict={}
for lines in f:

    data=lines.rstrip("\n").split(",")

    year=data[2]
    if year not in dict:
        dict[year]=1
    else:
        dict[year]+=1
print(dict["1992"])
#in which year highest number of movies released?
highest=max(dict,key=dict.get)
print(highest,dict[highest])

