#Do you play the Banjo? If your name starts with r, you do.
def areYouPlayingBanjo(name):
    if name[0] == "r" or name[0] == "R":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


#Alternate solution
def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";