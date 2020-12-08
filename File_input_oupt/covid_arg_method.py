f=open("covid_19_india.csv")

# 3st,thcured,7death,8thconfim

covid_data={}
for lines in f:
    data=lines.rstrip("\n").lower().split(",")
    state=data[3].rstrip("***")
    if state=="Telengana":
        state="Telangana"
    cured=data[6]
    death=data[7]
    confirmed=data[8]
    covid_data[state]={

        "state":state,
        "confirmed":confirmed,
        "cured":cured,
        "death":death
    }
for k,v in covid_data.items():
    print(k,v)



def print_covid_data(**kwargs):
    #fetcting value state
    state=kwargs["state"]
    if state in covid_data:
        print(state,",",covid_data[state]["confirmed"])
    else:
        print("you given invalid state")


print_covid_data(state="kerala")





