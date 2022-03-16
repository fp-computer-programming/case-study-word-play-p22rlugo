# Ryan Lugo: RJL 3/14/22

with open("words.txt") as infile:
    outfile = open("greater_than_20.txt","w")

    for l in infile:
        if len(l) > 21:
            outfile.write(l[:-1]+'\n')
