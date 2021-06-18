import sys

dna0 = open(sys.argv[1]).read()
dna1 = open(sys.argv[2]).read()
results_file = None
if len(sys.argv) > 3:
    results_file = open(sys.argv[3], 'w')

if len(dna0) > len(dna1):
    dna1, dna0 = dna0, dna1

results = []
for i in range(len(dna1)-len(dna0)):
    matches = 0
    for j in range(len(dna0)):
        if dna0[j] == dna1[i+j]:
            matches += 1
    results += [matches]

if results_file:
    for i, result in enumerate(results):
        results_file.write(str(result)+'\n')
    results_file.close()
print(results.index(max(results)), max(results))
