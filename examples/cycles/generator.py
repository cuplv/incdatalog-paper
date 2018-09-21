def make_cycle(n,output):
    for i in range(n):
        i_prime = (i+1) % n
        output.write("Edge(\"node" + str(i) + "\", \"node" + str(i_prime) + "\").")
               
for i in [10,25,50,75,100,125,150,175,200,225,250]:
    with open("cycle" + str(i) + ".flix", "w+") as f:
        make_cycle(i,f)
