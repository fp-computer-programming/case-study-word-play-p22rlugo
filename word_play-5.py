# Ryan Lugo: RJL 3/14/22

def is_abecedarian():
    with open("words.txt") as infile:
        words_in_order = 0 
        found = False
        for l in infile:
             correct = "".join(sorted(l))
             correct = correct.replace("\n","")
             if l == correct:
                 words_in_order += 1

        if found == True:
            print(words_in_order)                
            return True


print(is_abecedarian())