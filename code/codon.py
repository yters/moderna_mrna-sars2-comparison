import sys

aa2cdn = {
    'A': set(['gct', 'gcc', 'gca', 'gcg']),
    'I': set(['att', 'atc', 'ata']),
    'R': set(['cgt', 'cgc', 'cga', 'cgg', 'aga', 'agg']),
    'L': set(['ctt', 'ctc', 'cta', 'ctg', 'tta', 'ttg']),
    'N': set(['aat', 'aac']),
    'K': set(['aaa', 'aag']),
    'D': set(['gat', 'gac']),
    'M': set(['atg']),
#    'B': set(['aat', 'aac', 'gat', 'gac']),
    'F': set(['ttt', 'ttc']),
    'C': set(['tgt', 'tgc']),
    'P': set(['cct', 'ccc', 'cca', 'ccg']),
    'Q': set(['caa', 'cag']),
    'S': set(['tct', 'tcc', 'tca', 'tcg', 'agt', 'agc']),
    'E': set(['gaa', 'gag']),
    'T': set(['act', 'acc', 'aca', 'acg']),
#    'Z': set(['caa', 'cag', 'gaa', 'gag']),
    'W': set(['tgg']),
    'G': set(['ggt', 'ggc', 'gga', 'ggg']),
    'Y': set(['tat', 'tac']),
    'H': set(['cat', 'cac']),
    'V': set(['gtt', 'gtc', 'gta', 'gtg']),
    'START': set(['atg']),
    'STOP': set(['taa', 'tga', 'tag']),
}

cdn2aa = {}
for k, v in aa2cdn.items():
    for c in v:
        cdn2aa[c] = k

dna = open(sys.argv[1]).read()

pos = 0
transcribing = False
transcription_start = 0
transcription = ''
proteins = []
false_starts = 0
false_stops = 0
while pos < len(dna)-3:
    cdn = dna[pos:pos+3]
    if cdn in aa2cdn['START']:
        if not transcribing:
            transcribing = True
            transcription_start = pos
            print('starting')
            transcription = ''
        else:
            transcription += 'M'
        pos += 3
    elif cdn in aa2cdn['STOP']:
        if transcribing:
            transcribing = False
            proteins += [(transcription_start, transcription)]
            print('stopping')
        else:
            false_stops += 1
            print('false stop')
        pos += 3
    elif transcribing:
        transcription += cdn2aa[cdn]
        pos += 3
    else:
        pos += 1

for protein in proteins:
    print(protein)
print(false_starts, false_stops)

    
