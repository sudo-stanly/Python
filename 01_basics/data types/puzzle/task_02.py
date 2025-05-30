#[CHECK FOR DECIMAL NUMBER]:You are given a list of mysterious codes. Determine for each whether it consists solely of decimal characters.
    # codes = ["12345", "007", "9⅞", "42.0", "٣", ""]
    # print(codes[0].isdecimal(), codes[1].isdecimal(), codes[2].isdecimal(), codes[3].isdecimal(), codes[4].isdecimal(), codes[5].isdecimal())
    
#[WHISPER GAME]:A secret message list has been whispered in lowercase. Confirm whether each string is fully in lowercase, with no uppercase surprises.
    # messages = ["quiet", "LOUD", "whisPer", "shhh", "lower", ""]  # → ?
    # for i in range(0, 6):
    #     if(messages[i].islower()):
    #         print(messages[i])
    
#[SPACE]:A mysterious file stores records with hidden whitespace-only lines. Identify all the entries that contain only whitespace.
    # entries = ["   ", "\t\n", "data", "  .", "", " "]  # → ?
    # for i in range(0, 6):
    #     if(entries[i].isspace()):
    #         print(entries[i])
    
#[TITLE]:Each phrase below claims to be in “Title Case”. Use the appropriate method to reveal who’s lying.
    # titles = ["The Matrix", "lord Of The Rings", "A Beautiful Mind", "Catch-22", ""]
    # for i in range(0, 5):
    #     if not (titles[i].istitle()):
    #         print(titles[i])
    
#[ALPHA]: A group of password fragments needs testing. Identify which fragments contain only letters, no numbers or symbols.
    # fragments = ["Alpha", "123", "Test1", "clean", "🚀", ""]  # → ?
    # for i in range(0, 5):
    #     if(fragments[i].isalpha()):
    #         print(fragments[i])
