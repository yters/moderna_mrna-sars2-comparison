import sys

dna0 = open(sys.argv[1]).read()
dna1 = open(sys.argv[2]).read()
pos = int(sys.argv[3])

if len(dna0) > len(dna1):
    dna0, dna1 = dna1, dna0

line_break = 80
for i in range(0, len(dna0)):
    if dna0[i] == dna1[pos+i]:
        print(dna0[i], end='')
    else:
        print('-', end='')
        #print('*'+dna0[i].upper()+'/'+dna1[pos+i].upper()+'*', end='')
    if ((i+1) % line_break) == 0:
        print()
print()
