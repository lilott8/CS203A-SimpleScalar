#!/usr/bin/python
#backup.py
import sys
import copy
import os
import re
import subprocess

def part1(cwd,dname):
    print "Starting paser for part1"
    fpath = cwd+"/../results/"+dname
    files = os.listdir(fpath)
    #print files
    #List of pattern to search for later on
    patterns = ["sim_cpi","sim_ipc","sim_cycle","sim_num_insn",
                "sim_num_refs","sim_num_loads","sim_num_stores",
                "mem.page_count","sim_total_loads",
                "sim_total_stores","sim_total_branches",
                "sim_elapsed_time","falu_power","alu_power",
                "regfile_power",
                "total_power","clock_power"]
    #List of contents to be written to a csv file later on
    #With the first line being specified
    contents = [["File Name","sim_cpi","sim_ipc","sim_cycle","sim_num_insn","sim_num_refs","sim_num_loads",
        "sim_num_stores","mem.page_count","sim_total_loads",
        "sim_total_stores","sim_total_branches","sim_elapsed_time",
        "FP ALU Power","Int Alu Power",
        "Register File Power Consumption",
        "Total Power Consumption","Total Clock Power"]]
    #Iterate through all the file in fpath
    #"""
    for f in files:
        if "." not in f:
            content = []
            content.append(f)
            path = fpath+"/"+f
            print path
            for p in patterns:
                cmd = "grep -i "+"\""+p+"\" " +path
                result = subprocess.Popen(str(cmd),shell = True,stdout = subprocess.PIPE,stderr=subprocess.PIPE).communicate()
                val =""
                if ":" in result[0]:
                    #val = result[0].split(":")[2].split()[0]
                    val = "?"
                else:
                    val = result[0].split()[1]
                content.append(val)
            contents.append(content)
    #"""
   
    #write conetents to csv file in ../report/+dname
    outpath = cwd+"/../report/"
    output_output = open(str(outpath+dname+".csv"),'wb')
    for items in contents:
        combine = ','.join(items)
        #print combine        
        output_output.write("%s\n" %combine)
    
    #close the corrected_file
    output_output.close()
    #if not then the program exits with an error message
    if not output_output.closed:
        sys.exit('File %s did not close properly. ' % output_file)
   
    return None

def part2(cwd,dname):
    print "Starting paser for part2"
    fpath = cwd+"/../results/"+dname
    files = os.listdir(fpath)
    #print files
    patterns = ["sim_cpi","sim_ipc","sim_cycle","bpred_power",
                "icache_power","sim_num_branches",
                "sim_total_branches",
                "total_power","clock_power"]
    contents = [["File Name","sim_cpi","sim_ipc","sim_cycle",
                 "Branch Predictor Power Consupmtion",
                 "Instruction Cache Power Consumption",
                 "Total number of branches committed",
                 "Total number of branches executed",
                 "Total Power Consumption","Total Clock Power"]]
    #Iterate through all the file in fpath
    # """
    for f in files:
        if "." not in f:
            content = []
            content.append(f)
            path = fpath+"/"+f
            print path
            for p in patterns:
                cmd = "grep -i "+"\""+p+"\" " +path
                result = subprocess.Popen(str(cmd),shell = True,stdout = subprocess.PIPE,stderr=subprocess.PIPE).communicate()
                val =""
                if ":" in result[0]:
                    #val = result[0].split(":")[2].split()[0]
                    val = "?"
                else:
                    #print result[0].split()[1]
                    val = result[0].split()[1]
                content.append(val)
            contents.append(content)
       
    #write conetents to csv file in ../report/+dname
    outpath = cwd+"/../report/"
    output_output = open(str(outpath+dname+".csv"),'wb')
    for items in contents:
        combine = ','.join(items)
        #print combine        
        output_output.write("%s\n" %combine)
    
    #close the corrected_file
    output_output.close()
    #if not then the program exits with an error message
    if not output_output.closed:
        sys.exit('File %s did not close properly. ' % output_file)
        # """
    return None

def part3(cwd,dname):
    print "Starting paser for part3"
    fpath = cwd+"/../results/"+dname
    files = os.listdir(fpath)
    #print files
    patterns = ["sim_cpi","sim_ipc","sim_cycle",
                "icache_power","dcache2_power",
                "resultbus_power",
                 "total_power","clock_power"]
    contents = [["File Name","sim_cpi","sim_ipc","sim_cycle",
                 "Instruction Power Consumption",
                 "Data Level 2 Cache Power Consumption",
                 "Result Bus Power Consumption",
                 "Total Power Consumption","Total Clock Power"]]
    #Iterate through all the file in fpath
    #"""
    for f in files:
        if "." not in f:
            content = []
            content.append(f)
            path = fpath+"/"+f
            print path
            for p in patterns:
                cmd = "grep -i "+"\""+p+"\" " +path
                result = subprocess.Popen(str(cmd),shell = True,stdout = subprocess.PIPE,stderr=subprocess.PIPE).communicate()
                val =""
                if ":" in result[0]:
                    #val = result[0].split(":")[2].split()[0]
                    val = "?"
                else:
                    val = result[0].split()[1]
                content.append(val)
            contents.append(content)
       
    #write conetents to csv file in ../report/+dname
    outpath = cwd+"/../report/"
    output_output = open(str(outpath+dname+".csv"),'wb')
    for items in contents:
        combine = ','.join(items)
        #print combine        
        output_output.write("%s\n" %combine)
    
    #close the corrected_file
    output_output.close()
    #if not then the program exits with an error message
    if not output_output.closed:
        sys.exit('File %s did not close properly. ' % output_file)
    #"""
    return None

def part4(cwd,dname):
    print "Starting paser for part4"
    return None

if __name__ == '__main__':
    print "Paser.py"
    directories = ['p1','p2','p3','p4']
    cwd = os.getcwd()
    for d in directories:
        if str(d) == "p1":
            part1(cwd,d)
            #tmp= ""
        elif str(d) == "p2":
            part2(cwd,d)
            #tmp= ""
        elif str(d) == "p3":
            part3(cwd,d)
            #tmp= ""
        elif str(d) == "p4":
            part4(cwd,d)
