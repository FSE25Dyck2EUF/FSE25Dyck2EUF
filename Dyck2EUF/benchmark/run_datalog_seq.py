import time
import os
import subprocess

bdd_alias_time = [0.0]*11
bdd_dd_time = [0.0]*15

bdd_alias_time_query = [0.0]*11
bdd_dd_time_query = [0.0]*15

souffle_alias_time = [0.0]*11
souffle_dd_time = [0.0]*15

souffle_alias_time_query = [0.0]*11
souffle_dd_time_query = [0.0]*15

AliasAnalysis=[
'antlr',
'bloat',
'chart',
'eclipse',
'fop',
'hsqldb',
'jython',
'luindex',
'lusearch',
'pmd',
'xalan'
]

DataDep = [
'btree',
'check',
'compiler',
'compress',
'crypto',
'derby',
'helloworld',
'mpegaudio',
'mushroom',
'parser',
'sample',
'scimark',
'startup',
'sunflow',
'xml'
]

analysis_Type = [
    "AliasAnalysis",
    "DataDepAnalysis"
]

for analysisType in analysis_Type:
    if analysisType == "AliasAnalysis":
        benchmarks = AliasAnalysis
    elif analysisType == "DataDepAnalysis":
        benchmarks = DataDep
    for j in range(2):
        for num in range(3):
            bm_num = 0
            for bm in benchmarks:
                time_start = time.time()
                #os.system(f"java -jar ../bddbddb_test/bddbddb-full.jar ./bdd_{analysisType}/{j*1000}/{bm}.datalog")
                with open(f'./datalog_result/bddbddb/{j*1000}/{bm}.res', 'w') as outfile:
                     process = subprocess.Popen(
                          ['java', '-jar', '../bddbddb_test/bddbddb-full.jar', f'./bdd_{analysisType}/{j*1000}/{bm}.datalog'],
                          stdout=outfile,
                          stderr=outfile

                     )
                     stdout, stderr = process.communicate()
                time_end = time.time()
                print(f"{j*1000}===============================")
                print(time_end - time_start)
                print(bm)
                if j == 0 and analysisType == "AliasAnalysis":
                    bdd_alias_time[bm_num] += time_end - time_start
                if j == 0 and analysisType == "DataDepAnalysis":
                    bdd_dd_time[bm_num] += time_end - time_start
                if j == 1 and analysisType == "AliasAnalysis":
                    bdd_alias_time_query[bm_num] += time_end - time_start
                if j == 1 and analysisType == "DataDepAnalysis":
                    bdd_dd_time_query[bm_num] += time_end - time_start

                print(f"{j*1000}===============================")
                print(bm)
                time_start = time.time()
                os.system(f"../souffle_test/souffle -D ./datalog_result/souffle/{j*1000}/ ./dl_{analysisType}/{j*1000}/{bm}.dl")
                time_end = time.time()
                if j == 0 and analysisType == "AliasAnalysis":
                    souffle_alias_time[bm_num] += time_end - time_start
                if j == 0 and analysisType == "DataDepAnalysis":
                    souffle_dd_time[bm_num] += time_end - time_start
                if j == 1 and analysisType == "AliasAnalysis":
                    souffle_alias_time_query[bm_num] += time_end - time_start
                if j == 1 and analysisType == "DataDepAnalysis":
                    souffle_dd_time_query[bm_num] += time_end - time_start
                bm_num += 1

with open(f'./datalog_result/result.txt','w') as f_out:
    f_out.write("bddbddb alias analysis time:\n")
    for item in bdd_alias_time:
        f_out.write(f"{round(item/3, 4)}\n")
    f_out.write("bddbddb alias analysis query time:\n")
    for item in bdd_alias_time_query:
        f_out.write(f"{round(item/3, 4)}\n")
    f_out.write("souffle alias analysis time:\n")
    for item in souffle_alias_time:
        f_out.write(f"{round(item/3, 4)}\n")
    f_out.write("souffle alias analysis query time:\n")
    for item in souffle_alias_time_query:
        f_out.write(f"{round(item/3, 4)}\n")

    f_out.write("bdd data dependence analysis time:\n")
    for item in bdd_dd_time:
        f_out.write(f"{round(item/3, 4)}\n")
    f_out.write("bdd data dependence analysis query time:\n")
    for item in bdd_dd_time_query:
        f_out.write(f"{round(item/3, 4)}\n")
    f_out.write("souffle data dependence analysis:\n")
    for item in souffle_dd_time:
        f_out.write(f"{round(item/3, 4)}\n")
    f_out.write("souffle data dependence analysis query time:\n")
    for item in souffle_dd_time_query:
        f_out.write(f"{round(item/3, 4)}\n")
