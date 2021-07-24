#!/usr/bin/python3.6
#!/usr/bin/env python3.6
# coding: utf-8

import subprocess
import pandas as pd

inputFileName = 'FINAL_FROM_DF.csv'
outputFileName = 'FINAL_FROM_DF_SERIES.csv'
inputHdfsFilePath = '/user/hadoop/'+inputFileName
outputHdfsFilePath = '/user/hadoop/EQ/'+outputFileName
inputLocalFilePath = '/home/hadoop/Shasank/case_study4/'+inputFileName
outputLocalFilePath = '/home/hadoop/Shasank/case_study4/'+outputFileName
def run_cmd(args_list):
    print('Running system command: {0}'.format(' '.join(args_list)))
    proc = subprocess.Popen(args_list, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    (output, errors) = proc.communicate()
    if proc.returncode:
        raise RuntimeError(
            'Error running command: %s. Return code: %d, Error: %s' % (
                ' '.join(args_list), proc.returncode, errors))
    return (output, errors)

# copying hdfs file to local
(out, errors)= run_cmd(['hdfs', 'dfs', '-copyToLocal', '-f', inputHdfsFilePath])

# processing csv file using pandas
data = pd.read_csv(inputLocalFilePath)
data.columns = [column.replace(" ", "_") for column in data.columns]
# filtering with query method
data.query('SERIES == "EQ"', inplace = True)
export_csv = data.to_csv(outputLocalFilePath, index=False)

# creating EQ directory
(out, errors)= run_cmd(['hdfs', 'dfs', '-mkdir', '-p', '/user/hadoop/EQ'])

# copying local file to hdfs
(out, errors)= run_cmd(['hdfs', 'dfs', '-copyFromLocal', '-f', outputLocalFilePath, outputHdfsFilePath])