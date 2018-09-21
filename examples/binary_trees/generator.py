def make_tree(depth,prefix,output):
    if depth == 0:
        return
    for choice in ["0","1"]:
        output.write("Edge(\"" + prefix + "\", \"" + prefix + choice + "\").")
        make_tree(depth-1, prefix+choice, output)
               
for i in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    print i 
    with open("tree" + str(i) + ".flix", "w+") as f:
        make_tree(i,"node",f)
