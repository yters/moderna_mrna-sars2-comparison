import sys

dna = ''
with open(sys.argv[1]) as f:
    for line in f.readlines():
        line = line.strip().lower()
        tmp = ''
        for c in line:
            if not c in 'gtca 1234567890':
                tmp = ''
                break
            elif c in 'gtca':
                tmp += c
        dna += tmp
print(dna)
