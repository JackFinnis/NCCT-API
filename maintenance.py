# Get file extension
for i in range(1, 2):
    if i in range(1, 10):
        N = '0' + str(i)
    else:
        N = str(i)

    toWrite = ""
    churches = open(f'routes/route{N}/churches.txt').read().split('\n')
    for i in range(len(churches)):
        toWrite += churches[i] + "|" + str(i+1) + "\n"

    toWrite = toWrite[:-1]
    print(toWrite)
    file = open(f'routes/route{N}/churches.txt', "w")
    file.write(toWrite)
    file.close()


# Delete files
# import os
# os.remove('routes/route{0}/routeColour.txt'.format(N))