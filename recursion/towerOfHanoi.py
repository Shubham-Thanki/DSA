def tower(n, pos1, pos2, pos3):
    if n > 0:
        tower(n-1, pos1, pos3, pos2)
        print("{} ---------> {}".format(pos1, pos3))
        tower(n-1, pos2, pos1, pos3)


tower(3, 1, 2, 3)
# tower(source,using,destination)
