handle = open("batman.txt", 'a')
for x in range(9999999999,6000000000,-1):
    handle.write(str(x)+"\n")

handle.close()
