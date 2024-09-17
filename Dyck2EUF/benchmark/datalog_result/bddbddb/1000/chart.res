Initializing BDD library (500000 nodes, cache size 125000, min free 0.2%)
Could not load BDD package buddy: Can't load library: /home/dyd/project/Dyck2EUF/benchmark/libbuddy.so
Using BDD library JFactory 1.20
No machine learning library found, learning disabled.
Opening Datalog program "./bdd_AliasAnalysis/1000/chart.datalog"
1 field domains.
1003 relations.
45505 rules.
Splitting rules: done.
Initializing solver: Initializing value of special relation Z_eq_Z Z0,Z1
Garbage collection #1: 1009 nodes / 354 free / 0.003s / 0.003s total
Garbage collection #2: 1009 nodes / 0 free / 0.003s / 0.006s total
Resizing node table from 1009 to 2017
Garbage collection #3: 2017 nodes / 380 free / 0.002s / 0.008s total
Resizing node table from 2017 to 4027
Garbage collection #4: 4027 nodes / 764 free / 0.002s / 0.01s total
Resizing node table from 4027 to 8053
Garbage collection #5: 8053 nodes / 1532 free / 0.003s / 0.013s total
Resizing node table from 8053 to 16103
Garbage collection #6: 16103 nodes / 3068 free / 0.005s / 0.018s total
Resizing node table from 16103 to 32203
Garbage collection #7: 32203 nodes / 6140 free / 0.0s / 0.018s total
Resizing node table from 32203 to 64403
Garbage collection #8: 64403 nodes / 12284 free / 0.001s / 0.019s total
Resizing node table from 64403 to 114377
Garbage collection #9: 114377 nodes / 24572 free / 0.002s / 0.021s total
Garbage collection #10: 114377 nodes / 0 free / 0.002s / 0.023s total
Resizing node table from 114377 to 164377
Garbage collection #11: 164377 nodes / 49148 free / 0.002s / 0.025s total
Garbage collection #12: 164377 nodes / 0 free / 0.002s / 0.027s total
Resizing node table from 164377 to 214373
Garbage collection #13: 214373 nodes / 0 free / 0.004s / 0.031s total
Resizing node table from 214373 to 264371
Garbage collection #14: 264371 nodes / 0 free / 0.006s / 0.037s total
Resizing node table from 264371 to 314359
done.
Loading initial relations: done. (0 ms)
Stratifying: 
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.HashMap.newTreeNode(HashMap.java:1911)
	at java.base/java.util.HashMap$TreeNode.putTreeVal(HashMap.java:2156)
	at java.base/java.util.HashMap.putVal(HashMap.java:636)
	at java.base/java.util.HashMap.put(HashMap.java:610)
	at java.base/java.util.HashSet.add(HashSet.java:221)
	at jwutil.collections.HashWorklist.add(HashWorklist.java:79)
	at net.sf.bddbddb.IterationFlowGraph.constructRuleDependencies(IterationFlowGraph.java:76)
	at net.sf.bddbddb.IterationFlowGraph.constructDependencies(IterationFlowGraph.java:54)
	at net.sf.bddbddb.IterationFlowGraph.<init>(IterationFlowGraph.java:42)
	at net.sf.bddbddb.IterationFlowGraph.<init>(IterationFlowGraph.java:30)
	at net.sf.bddbddb.Solver.stratify(Solver.java:249)
	at net.sf.bddbddb.Solver.load(Solver.java:387)
	at net.sf.bddbddb.Solver.load(Solver.java:361)
	at net.sf.bddbddb.Solver.main2(Solver.java:448)
	at net.sf.bddbddb.Solver.main(Solver.java:1966)
