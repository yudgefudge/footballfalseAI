import time

clubs = ["Manchester United", "Manchester City", "Chelsea", "Tottenham", "Arsenal", "Liverpool"]

def manunited():
    print ("Ah! You've chosen the Red Devils, as they are fondly called!")
    time.sleep(0.5)
    while True:
        inquiry2 = input("What would you like to inquire about?\n(1) The manager\n(2) The players\n(3) The number of trophies\n(4) The club itself\nPut your answer here! ")
        if inquiry2 == "1":
            manutdman()
        elif inquiry2 == "manager":
            manutdman()
        elif inquiry2 == "the manager":
            manutdman()
        elif inquiry2 == "baldie":
            manutdman()
        elif inquiry2 == "walter white":
            manutdman()
        elif inquiry2 == "players":
            manutdply()
        else:
            print ("Not what I asked for.")
            time.sleep(1)
    return;

def manutdman():
    print ("Man United's manager is Erik Ten Hag; he originally coached the Dutch club Ajax, and consistently won the Eredivisie, the Dutch national league. Erik is Dutch himself.")
    time.sleep(3)

def manutdply():
    print ("Man United has a multitude of players! I'd like to to choose a specific one, if that's okay? Give a second to gather my notes...")
    time.sleep(1.3)
    while True:
        inquiry3 = input("Alright, choose a player! ")
        if inquiry3 == "Rashford":
            print ("Best player.")
        elif inquiry3 == "Hojlund":
            print ("Hojlundinfo")
        elif inquiry3 == "Eriksen":
            print ("Erikseninfo")
        elif inquiry3 == "Martial":
            print ("Martialinfo")
        elif inquiry3 == "Onana":
            print ("Onanainfo")
        elif inquiry3 == "
        else:
            print ("Not a United player.")
            
print ("Waking up...")
time.sleep(1.5)
print ("Hi! My name is FootyAI! I'm here to answer your questions about football clubs.")
time.sleep(1.5)
print ("Currently, my database contains information on the following clubs:", (clubs), "Apologies for the silly brackets and apostrophes. My use of the English language is only so limited...")
time.sleep(3)
inquiry1 = input("What team would you like to ask about? ")
if inquiry1 == "Man U" or "Manchester United" or "Man Utd" or "man u" or "manchester united" or "man utd" or "MUN" or "mun":
    manunited()
elif inquiry1 == "Treble winners" or "treble winners" or "Treble Winners" or "TREBLEWINNERS" or "TREBLE WINNERS":
    treblewinners = input("Ah, which ones? ")
    if treblewinners == "Man U" or "Manchester United" or "Man Utd" or "man u" or "manchester united" or "man utd" or "MUN" or "mun":
        manunited()
else:
    print ("That's not what I asked about, come on!")
        
        
