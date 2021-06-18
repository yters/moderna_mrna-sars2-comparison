This repo contains some tools to convolve the Moderna mRNA sequence with the MERS, SARS and SARS2 virus sequence, and then visualize the best matches.



Matches between the Moderna mRNA sequence and the SARS-CoV-2 RNA.

```
$ time python3 code/convolve.py data/moderna_mrna1273.dna data/sars2.dna
21440 1946

real    0m55.264s
user    0m54.355s
sys     0m0.184s
$ python3 code/matches.py data/moderna_mrna1273.dna data/sars2.dna 21440
g-gaaa--a-----------a-----ag------t-t------c----------ac-atgtt-gt-tt-ct-gt--t--t
gcc-ct-gt----ag-cagtg-gt-aa-ct-ac-acc-g-ac-ca--t-cc-cc-gc-tacac-aa----ttcac-cg-g
g-gt-ta-taccc-gacaa-gt-ttc-g---c---gt--t-ca----ac-caggac-tgttc-t-cc-ttctt---caa-
gt-ac-tggttcca-gc-at-ca-gt----gg-accaa-gg-ac-aag-ggtt-ga-aaccc-gt-ct-cc-tt-aa-ga
-gg-gt-ta-tt-gc---cac-gagaag---aacat-at--g-ggctggat-tt-gg-ac-ac--t-ga----aagaccc
ag--cct-ct-at-gt-aataacgc-ac-aa-gt-gt-at-aa-gt-tg-ga-tt-ca-tt-tg-aa-ga-cc-tt--tg
gg-gt-ta-taccacaa-aacaacaa-ag-tggatgga-ag-gagttc-g-gt-ta----ag-gc-aa-aa-tgcac-tt
-ga-ta-gt----cagcc-tt-ct-atggacct-ga-gg-aa-caggg-aa-ttcaa-aa-ct--ggga-tt-gtgtt-a
agaa-at-ga-gg-ta-tt-aa-at-ta----aagcacac-cc-at-aa--t-gtgcg-gatct-cc-caggg-tt-tc-
gc--t-ga-cc--tggt-ga--tgcc-at-gg-at-aacatcac--ggtt-ca-ac--t-ct-gc--t-ca--g-ag-ta
--tgac-cc-gg-ga----------gg-tggacagc-gg-gc-gc-gctta-ta-gtggg-ta-ct-ca-cc--ggac-t
t-ct--t-aa-ta-aa-ga-aa-gg-accat-ac-ga-gc-gt-gactg-gc-ct-gaccctct----ga-ac-aagtg-
ac--tgaa---cttcac-gt-ga-aa-gg-atcta-ca-ac----aactt--g-gt-ca-cc-ac-ga----at-gt--g
-tt-cc-aa-at-ac-aac-tgtgccc-tt-gg-ga-gt-tt-aacgccacc-g-tt-gc----gt-ta-gc-tggaac-
ggaag-g-atcagcaactg-gt-gc-ga-ta----gt-ct-ta-aa---cgc----tt---cac-tt-aagtg-ta-gg-
gtg---cc-ac-aa--t-aa-ga-ct-tgctt-ac-aa-gt-ta-gc-ga----tt-gt-at--g-gg-ga-ga-gt--g
-ca-atcgc-cc-gg-ca-ac-gg-aagat-gc-ga-ta-aa-ta-aa--t-cc-ga-ga-tt-ac-ggctgcgt-at-g
c-tggaa----aacaa-ct-ga----aaggt-gg-gg-aa-ta-aa-tacctgta--g--tgtt--ggaag---aa-ct-
aa-cc-tt-gag-g-ga-at----ac-ga-atcta-ca-gccgg---cac-ccttg-aa-gg-gt-ga-gg-tt-aa-tg
-tactt-cct-t-ca----ta-gg-ttcca-cccac-aa-gg-gt-gg-tacca-cc-tac-g-gt-gt-gt-ct----t
t-ga-ct-ct-ca-gc-ccagc-ac-gt-tgtgg-cc-aa-aag---ac-aa--tggt-aa-aacaa-tg-gt-aa-ttc
aacttcaa-gg--t-ac-ggcac-gg-gt-ct-ac-gag---aacaa-aa-tt-ctgcc-tt-ca-ca-tt-ggc-g-ga
cat-gc-gacac-ac-ga-gctgt-cg-gatcc-cagac-ct-gagat-ct-gacat-ac-cc-tg----tt-gg-gg-g
t-ag-gt-at-ac-ccagg-ac-aa-ac----aaccaggt-gc-gt-ct-ta-cagga-gt-aactgcac-ga-gt-cc-
gt-gc-at-ca-gc-ga-ca-ct-ac-cc-ac-tggcg-gt-ta----ac-gg----aa-gt-tt-ca-ac-cg-gc-gg
-tg--t-at-gg-gc-ga-ca-gt-aacaac---ta-gagtg-gacat-cccat-gg-gc-gg-at-tg-gc-ag-ta-c
agac-cagac-aattc-cc-cgg-gggca-g-ag-gt-gc-ag-ca---catcat-gcctacac-atg---ct-gg-gc-
ga-aa----gt-gc-tac---aa-aac---at-gccat-cccac-aa-tt-ac-at-ag-gt-accac-ga-attct-cc
-gtg---atgaccaagac----gt-ga-tg-ac-atgtacat-tg-gg-ga----ac----------a-----t--t---
-----g----tt-t----c----t-aa-c-g--c-t-a-c-g-a----c-------------a-aa---cc--------t
t---c-------a----a--t---a-a-c-c--cca---a----tt--g--g-tt--a-tt---c---a---t--cc---
-cca-caa--cca---a---g--c-t----------------tt--a--a------c-----c-----c-g--t-----a
--------g----t--c---g---------c--c--g---c-----t----c---aa--t--a--g-c----c----t--
c--cc-t------c------a-------c--------c--c--c----t---cgg---ca----c--c-g-t-g----t-
-g-----g---c----t----a---cc-t---c------a--g-ct----g-t--a--g-----g------c----a---
-----------a-c--aa--t------c-a-c---t--a------c----g--a-a----------c-----c--c--c-
--a----c----g-aa-------------g---a-c--aa---c-----c-t-aa---c-------a------------c
-a-tt--g---ca----ca------t-aa-------c----c--g------c--------g-c---------a-------
g-t--------g-c-g------a---t------c--------c-------t-a----g--c--c---a-tc-g--c--c-
-c-a------c--c--c-a-a----c-------------g----a-caa---g------tt-t---g-aa-gg-------
--------c-ttccc-----c----cc----g--------t-ct---------ct-----ccc--c------aa--a--t
---ca-c--c-c---c---t---------g-aa---c----tt-cc--g----g-----t------caa--g---c----
-g-t----a-c-----g-a-tt-t------cc---a-------c--c----a---c-t------c-g--a----------
---a---g-a------a--a---c---t------cc-t-----cc----t------c-t--a-g--g---t-----a---
-tt--a--a------ca-c-cc----------t--g---------c-g-----a---c--c------aa-------aa--
--a-----c-gc---a----g----c-a--a--t-aa----a-c------------c---------g-aa----------
------aa---g-cc--g------t-g----g-tt------c-g-ct------c------a--g----ca--------t-
---------c---t--------t------a-gg----t----ct---g-a-c-------a--------g----c--c-c-
g--cc----c-c------g------tac--------t------a------ga-t-g------a-aa-----
```

There is some kind of offset.

```
$ python3 code/matches.py data/moderna_mrna1273.dna data/sars2.dna 21441
-g-aaa-aa-agag-----a----ta---a------t---a-c-------cg--------tt--t-ttc-tg-t------
-c-c--g--------c-------t-a-c-t-----c------c-a----cc-c-----------a-----t----c--gg
---t------cc-----aag-t-t------------t------------c--g------t-----c--t--tt----a--
-t-----g-t-c--------c---------gg--c-a--g-----a---g-tt----a-cc--------c--tt-a----
-g---t----tt-------------a-----a----------gg---g--t-tt-g----------g----g-a---cc-
----c----t--t--t-a--a--------a---tg-t--t-aag-------a-ttc-a-tt----a----cc--tt---g
g---t------c---aa-a--a--aa-----g---g-a-------t----g-t-------------a--a--------tt
--a---------c---c--ttc-t---g--c-tg-agg--aa---gg--a--t--aa-a-c-t--gg-a-tt----tt-a
--a---t----g-----tt-aa----------a-------cc-a-t-a----g-----g------c-c--gg--tt----
-----g-a-c----g--g------c-----g---t-a---------g-ttc-a--------tg-----------------
------cc--g--------------g---g-------g----g-----t--------gg----c-t--a-c---g----t
tc------aa----a---a-a--g---c--t------------g--------c-tg--cc---------a----a-----
------aa----t-------g-a-aagg-------c-a-------a--tt---g----a-c------a-----t--t---
-ttcc--a---t----a-------cc--tt-g---ag-t-tt-a---c--c----tt--------t--------g-a---
g-a-----------a------tg---------------------a-----------tt-------tt-a--------g--
-----cc-----aa----a----c------tt----a-----------------tt-----t----g------ag-----
--a-------c--ggc-a----g--a---t----------a-----aa----c--------tt----g------t-----
---g-a-----a--a-c-t-------a-g-tgg--g--a-----a----c------------tt--g-a-----a-c---
aa-c--tt------g----t--------a------c----c-g---c---cc-t---a--g---tg-agg--tt-a----
----ttcc-t----a-------g--t-c-a-cc----a--g---tgg----c-a-c-------g--g--g----t----t
t--a--t---------cc---------t----g-cc--aa-a--------a----g-t-aa-a--aa-------a--t--
a--t--a--g--------g-----g---t--t----------a--aa-a--ttc---c--t---a--a-tt-g----g--
--t------------------------g---c-c-----c-tg----tc-tg----t---cc-t------tt-g--g---
------t------cc--g-----a--------a-c--g-tg----t--t---c--g----t-a---------ag---c--
-tg----tc--------c-a--t----c------g---g-t----------g-----a---t-ttc-a---c--g---g-
t---------gg-----a-------a--a-------------------ccc--t-g-----g----------------c-
----c------a-t---c-c-g--gg-----------g-----c-a--------t--c------------c-tgg-----
-a-a------tg---------a--a------t--c---ccc----a--tt-----t-----t--c-----a--t----c-
-----------c-a----------g----------------t----g-----------a-tgcagcaa-ct--tg-tgca
-ta-ggcag-tt-tg-ac-ca--t-aaccg-gc--t-ac-gg-at-gc-gt-ga-ca-gacaa-aacaccca-ga-gt-t
t-gc-ca-gt-aa-ca-at-tacaa-ac-cc-cc-at-aa-ga-tt-gg-gg-tt-aa-tt----ca-at--t-cc-ga-
cc----aa-cc-agcaag-gg---tt-at-ga-ga-ct-ct-ttcaacaa-gtgac-ct-gc-ga-gc-ggcttcatcaa
-ca-ta-gg-ga-tgcct-gg-ga-at-gc-gc--g-gacct-at-tg-gc-ca-aagtt-aacggcct-ac-gt--tgc
c-cc--tgct-ac-ga-ga-atgat-gc-ca-tacac----gc-ctgttagc-gg-ac-atcac----gg-tggac-tt-
gg-gc-gg-gc-gc--t-ca-at-cc-tt-gc-atgca-atggc-ta--ggtt-aa-gg-at-gg-gt-ac-cagaa-gt
-ct-ta-gagaacca-aa--tgat-gccaacca-tt-aa-ag-gc-at-ggcaa-at-ca-gac---ct------cac-g
c-ag-gc-ct-gg-aa-ct-ca-ga-gtggt-aacca-aa-gc-ca-gc--t-aacac-ct-gt-aa-ca-ct-agc--c
aa-tt-gg-gc-at----ag-gt--t-aa-ga-atcct----cg-ct-gac------gaggc-ga-gtgca-at-ga--g
g-tgatcac-ggc-g-ct-ca-ag--tgcagac-ta-gtgac-ca-ca--t-at--g-gc-gc-ga-at--g-gc----g
c-aa-ct-gc-gc-ac-aa-atg---gagtg-gt-ct-gg-ca----aa--g-gt-ga-tt-tg-gg-aagggcta-ca-
ct-atg--ctt-cc-cag---gcacc-ca-gg-gt-gt-ttc-tgca-gtgac-ta-gt-cc-gc-ca-ga-aagaactt
cac-ac-gc-cc-gccat-tg-ca-ga-gg-aa-gc-cactttcc-cg-ga-gg-gt-tt-gt----aa-ggcac-cact
ggtt-gt-ac-ca--ggaa-tt-ta-ga-cc-ca-atcat-ac-ac-gacaacac-tt-gtg---gg-aactg-ga-gt-
gt-at-gg-at-gt-aacaacac-gt-ta-gatcc--tgca-cc-ga--t-gac---ttcaaggaggag-t-ga-aa-ta
-tt-aagaatca-ac----cc-ga-gt-ga--t-gg-gacatc---ggcat-aa-gc----gt-gt-aacat-ca-aa-g
a-at-ga-cg-ct-aa-gaggt-gccaagaa--t-aa-ga----ct-atcga-ct-ca-ga-ct-gg-aagta-gagcag
ta-at-aa-tggcc-tggtacat-tggct-gg-tt-at-gc-ggc-tgat-gccat-gt-atggtgac-at-atgct-tg
ctg-atgaccag-tgctg-ag-tg-ct-aagggctgttg----tg-gg---ctgctgcaa------tg-------c-c--
--cc------c--------ca--------------------a-----t-----tg------a-aa------
```

For comparison, here is the match with random data.

```
$ python3 code/matches.py data/moderna_mrna1273.dna data/random.dna 21441
-g---at-------------a----a-----------a-----c---c---g---c----t-c-----c-----g--g--
-c-cctgg--ag--gcca--------acc-g-ccac-cg---cc---------------acac-aa------------g-
g---c--c----c-g--------t-----a----c-tc---c-c-g--cc----acct----c----c-------gca--
---a----g------g----cc--g-g------a-c----gc----a--g--t----a----c-tg--------ca----
-g--g---ac-------------ag--------c-t-a---------g----t--g-c-------t---c-g--aga-cc
-------gc----cg-ga--a----ca---a---g-------a--------a--t------c-g-a---------tc--g
--c---ta-t-------g--caa-aa-------a--------g--------gtgt--------g---a---c--------
c----a----a--cagcc-----t--t------gg--g-c---c-------c---aag---c------------t-t---
a-a--------gg------c-ag-t------c-a-ca--cc---------c--gt---------g---c---------c-
---c---a---c-tgg-g-------cc-----ca-c-a---c-c---g---c-----c--c--------c---gga--t-
-c-g-c-c----c--ca--a-c-g-g-g-----a--------g---------t----gg---ac--g--g--c-----ct
-c--gct-aag--c------a--g---c------cg-cg-c-t-ga-t-----c-ggac--t---a-c----cc------
-c---------ct-------g-a--a-g--a-----c---c---c---tt--g-g--ca-------g-g--c--c--g-g
--t----a-----a----c-t-t---c-t--g--g-----t-c-ac-------g-----c-----t--------g---cc
g-a---g------c---------g--g-c--c----t---g--c----gc---ag--t-a--ac--t---gt--------
g-----cc-------ct-a-------g--c-t----aa----ta--c--ac--c------a--cg--gc----a---g--
g--g-----------c--g----gc--ga--g-----t-ca----c------c-cg-c-ac---a--g------tg--c-
----ga------a-a--------a-c-a--tg--c--------c----a--t-------ct--t---g------aac---
a-------c-------a-a-c-g-a-----at---c---gc----t-ca-c-c-----ac-------aggg--------g
---c--ccc------g--c---gg-t-----cc--c-------------t-------c-ac-g----------c--a---
t--a---g-t--ac---c--g--a-c--g--t---cc---g--------ca-c-t--tg--ga---a---cg-----t--
-a---caa---c-t--cc----c-----tg-t-----------a------att--------tt---c----------g--
-a------a------------t-tgc-g--tc------------------------t-ac---tt-----t-------cg
--a------tc-cc---gg------cac--g-a---ag-t-----------a------c-t----------g-------c
-----------c-------a--t------c-cc---------t-c------gg--gc---gt--t-----c---gg-c--
--------------c--a--a-g----caa----t-c---t--g--------a-----g-----a---------------
-g-c---ga-c-at------cg-----ca---a------cc--c--g--------c----a---c-t----c---gc-cc
g-g-------tggc-t----c-----c-g-------at-c-----a----ca--at-------ac--c-------c---c
---g---at-ac--a-----g--tgga-t-ca--------a---------------c-----cag-a-c-----g----a
gt-c-----ct-c-gc-------t------g-c---g---gg--tcg-c-tg--------c-----c-c---------g-
-c----------a----------a-g-----t-----ca---a-ttc-gc-----------c-----g---------ga-
-------------g--a-------------------------t--------g--a---t--c---c-------t--tc--
g-------gc-a---------c---a-a---g--cg----c-g--c--c-c-ca--a-t--------c---c-gt----c
-t-ccct-ct--------------t----ca-------a--------t-------aa-c------a-----tg--c-tt-
gg----g---c-g----gc-g--------------------------c---t-c--c-g--t------g---c------t
g-tg--c----a------gc-g-t---c-a--ag------a--gc---c----ag-tc-----c-g------cag---c-
c---cg--c-g-g-aa-c----------g----a---g------c--gc----aa-a---t-----ag-a-------a-c
-a--------c-a--------g---t--a-----tc-t--gc---c----------c----c-ga---------c----g
------c--t------c-g-------t-----c----------c----g--------g---g--g--a-t--g-----c-
------t---------ca------gc------gt---------g-g-aag-g---g--------c-g-a----c---c--
-----------t--------c-------a--------tgt-cc---------c---------------g--g------t-
---c-c--c-c----ca-----------g----g---------c--------g--g-gtt----ag---cg--a----c-
ggt-c-t----------a--------ga------g------a--a-c---aa---c-----ga--------tg-------
gt--t------c----a-a-c-c-----a--atc--c-----c-c---ctgga--g-ttc-a-----a-----aca----
-t----g-a---c--c-----c--c-tg--c--ggg----a--a-c------a-c---a--g------a---c-a---g-
-ga--g-tc----gaa------g---a---a-c--a--g--a---t----g---tgc-g-----ggg-a------ag-a-
t----c-------c-t-gt-c----g----g--t-c------g-------------c-t-a-gg-----at-a------g
c--------c-gc--c------t-c--------c------a--t---g---------c-a---c---gg---t------a
--c--t-c------tcct---c----------gg----tg----aagt-tg-g---g-------aa-----
```