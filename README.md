# Admix4Pop

Admixture estimation for population.

## Data

* populations.txt: allele frequencies for each reference population
* mixture.txt: allele frequncies for mixture population (to be analyzed)

## Result

The program will calculate fraction of each reference population for the mixture population.

## Run

```
python3 admix.py --tolerance=1e-3 --population=population.txt --mixture=mixture.txt
```
