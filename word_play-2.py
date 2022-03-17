# Ryan Lugo: RJL 3/14/22

def no_e():
    with open("words.txt") as infile:
        outfile = open("words_without_e.txt","w")

        for l in infile:
            not_e = True
            for letter in l:
                if letter != "e":
                    not_e = False
                    break
            if not_e == True:
                outfile.write(l[:-1]+'\n')

no_e()
print("poggers")
