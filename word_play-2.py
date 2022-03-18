# Ryan Lugo: RJL 3/14/22

def no_e():
    with open("words.txt") as infile:
        outfile = open("words_without_e.txt","w")
        total_words = 0
        words_without_e = 0

        for l in infile:
            not_e = False
            counter = 0

            total_words += 1

            for letter in l:
                if letter != "e":
                    counter += 1
                    if counter == len(l):
                        words_without_e += 1
                        not_e = True
                        break
            if not_e == True:
                outfile.write(l[:-1]+'\n')
    
        print("Percentage of words that don't have E in it:",(words_without_e / total_words) * 100)

no_e()
