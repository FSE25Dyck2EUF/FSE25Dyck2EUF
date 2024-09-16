# Artifact description
This is the artifact of submission #847 (**SMT-based Solving Dyck-Reachability with Applications to Static Analysis**) in FSE 2025.


# Prerequisites
+ Hardware: ~2.50 GHz CPU (all experiments were performed on a desktop with 11th Gen Intel(R) Core(TM) i5-1155G7 @ 2.50GHz 2.50 GHz), 16GB RAM.
+ Unix / Linux OS: We have validated the artifact on Ubuntu system
+ Python3
+ Java >= 1.8

# Running the artifact
We assume that the following commands are run in sudo mode.

**Run each tool individually**
We first introduce the method for running each tool individually. Before running the experiments, it is necessary to ensure that each tool is functioning properly.

`Optimal`

```sh
cd /Dyck2EUF/Graph-Reach_test/
./main.out example.spg example.seq
```

`CVC5`

```sh
cd /Dyck2EUF/cvc5_test/
./cvc5 example.smt2 --incremental
```

`Z3`

```sh
cd /Dyck2EUF/z3_test/
./z3 example.smt2
```

`Yices`

```sh
cd /Dyck2EUF/Yices_test/
./yices-smt2 example.smt2 --incremental
```

`Plat-smt`

```sh
cd /Dyck2EUF/platsmt_test/
./plat-smt example.smt2
```

`Bddbddb`

```sh
cd /Dyck2EUF/bddbddb_test/
java -jar bddbddb-full.jar example.datalog
```

`Soufflé`

```sh
cd /Dyck2EUF/souffle_test/
./souffle example.dl
```
**Reproduction of the experimental results in the main text**
First, we need to generate a total of 10 query sequences with lengths ranging from 1,000 to 10,000, with an increment of 1,000. You can choose to regenerate them or use the existing data. To regenerate the query sequences, run the following code (this step takes approximately 6 minutes on my machine):

```sh
cd /Dyck2EUF/benchmark/
python3 trans.py
```

Next, run Optimal, Z3, CVC5, Yices, and Plat-smt on the benchmark using the following command (this step takes approximately 18 minutes on my machine):

```sh
cd /Dyck2EUF/benchmark/
python3 run.py
```
Run the following command to check if the results obtained from different tools are consistent:

```sh
cd /Dyck2EUF/benchmark/total_result/
python3 check.py
```

Run the following command to perform statistical analysis on the experimental results. The results from $\bf{Section\ 4.2}$ are in $\bf{/benchmark/total\_result/}$, with $\bf{AliasAnalysis\_result.txt}$ and $\bf{DataDepAnalysis\_result.txt}$ respectively storing the results of alias analysis and data dependence analysis. The experimental results from  $\bf{Section\ 4.3}$ are in folders $\bf{AliasAnalysis\_query}$ and $\bf{DataDepAnalysis\_result}$, saved in $\bf{.dat}$ format (all results are the average of three runs):

```sh
cd /Dyck2EUF/benchmark/total_result/
python3 get_result.py
```

**Reproducing the experimental results of the Datalog tool in the appendix**
Run the following command to generate a query sequence with a length of 1,000 for each program:

```sh
cd /Dyck2EUF/benchmark/
python3 trans_datalog.py
```
Run the following command to evaluate the performance of the Datalog tools Bddbddb and Soufflé on this benchmark:

```sh
cd /Dyck2EUF/benchmark/
python3 run_datalog_seq.py
```
The run results are in the folder $\bf{/benchmark/datalog\_result}$. The runtime statistics are in $\bf{result.txt}$ (the average of three runs).