# Ryan Lugo: RJL 3/14/22

def uses_only(string,letters):
    with open("words.txt") as infile:
        words_with = 0
        wanted_letters = input("Input Letters that you want from the txt file: ")

        for l in infile:
            counter = 0

            for letter in l:
                if letter == wanted_letters:
                    counter += 1
                    words_with += 1
                    break

        for wordLetter in letters:
            counter = 0 
            found = False
            for letter in string:
                if letter == wordLetter:
                    counter += 1
                    if counter == len(string):
                        found = False
                else:
                    found = True

            if found == True:
                print(words_with)
                return True
        
        print(words_with)
    
     

print(uses_only("yep", "yep"))
