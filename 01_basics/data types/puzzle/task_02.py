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