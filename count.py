import sys

inpt = ""
alphabet = digit = simbol = 0

for line in sys.stdin:
    inpt = line
    for x in range(len(inpt)):
        if((inpt[x] >= 'a' and inpt[x] <= 'z') or (inpt[x] >= 'A' and inpt[x] <= 'Z')): 
            alphabet = alphabet + 1 
        elif(inpt[x] >= '0' and inpt[x] <= '9'):
            digit = digit + 1
        else:
            simbol = simbol + 1

sys.stdout.write("Total angka: " + str(digit))
sys.stdout.write('\n')
sys.stdout.write("Total huruf: " + str(alphabet))
sys.stdout.write('\n')
sys.stdout.write("Total simbol: " + str(simbol))
sys.stdout.write('\n')
