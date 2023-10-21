# 100-prisoners-riddle

Simulates the 100 prisoners riddle

After watching the [Veritasium video](https://www.youtube.com/watch?v=iSNsgj1OCLA), I made a poorly optimized simulation tool to see how well the strategy works.

# Usage

```
$ python3 prisoners.py --help
usage: LinkedPrisoners [-h] [-i ITERATIONS] [-p PRISONERS] [-s {linked,random}]

Simulates linked prisoner dilemma

optional arguments:
  -h, --help            show this help message and exit
  -i ITERATIONS, --iterations ITERATIONS
                        Number of simulation tests to run
  -p PRISONERS, --prisoners PRISONERS
                        Number of prisoners in each simulation
  -s {linked,random}, --simulation {linked,random}
                        Type of simulation
```

# Examples

Using the random strategy

```
$ python3 prisoners.py --iterations 10000 --prisoners 100 --simulation random
{'success': 0, 'fail': 10000}
10000 random simulations of 100 prisoners in 1.75 seconds
```

Using the linked strategy

```
$ python3 prisoners.py --iterations 10000 --prisoners 100 --simulation linked
{'success': 3145, 'fail': 6855}
10000 linked simulations of 100 prisoners in 4.51 seconds
```
