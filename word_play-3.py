# Ryan Lugo: RJL 3/14/22

def avoid(string,letters):
    with open("words.txt") as infile:
        words_with = 0
        forbidden_letters = input("Input Letters that you do not want from the txt file: ")

        for l in infile:
            counter = 0

            for letter in l:
                if letter != forbidden_letters:
                    counter += 1
                    if counter == len(l):
                        words_with += 1
                        break

        for wordLetter in letters:
            counter = 0 
            found = False
            for letter in string:
                if letter != wordLetter:
                    counter += 1
                    if counter == len(string):
                        found = False
                else:
                    found = True

            if found == True:
                print(words_with)
                return True
        
        print(words_with)
    
     

print(avoid("yep", "yep"))
