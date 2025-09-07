def calculate_love_score(name1,name2):
    total1 = 0
    int1 = 0
    int2 = ""
    word = "TRUE LOVE "
    names = name1.lower() + name2.lower()
    
    for letter in word:
        if letter != " ":
            for let in names:
                if letter.lower() == let:
                    total1 += 1
                    int1 += 1
            print(f"{letter} occurs {total1} times" )
            total1 = 0
        else:
            print(f"Total = {int1}")
            int2 += str(int1)
            int1 = 0
    
            
        
    print(f"Love Score = {int2}")    
    

calculate_love_score("Kanye West", "Kim Kardashian")
