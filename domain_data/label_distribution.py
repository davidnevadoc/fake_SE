#!/usr/bin/env python3


import csv

    
"""
-----------------------------------------------------------------------
Reports the distribution of labels for the panels as contained in each
CSV.
-----------------------------------------------------------------------
"""




def show_distribution(filename):
    fd = open(filename, "r") 
    reader = csv.reader(fd, delimiter=',')
    labelcount = dict()
    for line in reader:
        if line[1] in labelcount:
            labelcount[line[1]] += 1
        else:
            labelcount[line[1]] = 1
    
    sortedcount = [(labelcount[key], key) for key in labelcount]
    sortedcount.sort()
    sortedcount.reverse()
    
    for s in sortedcount: print(str(s))
    
    fd.close()


"""
---------------------------------------------------------------------------
Main
---------------------------------------------------------------------------
"""
def main():

    print("[*] SYMANTEC\n")
    show_distribution("symantec_panels.csv")
    print("\n[*] MCAFEE\n")
    show_distribution("mcafee_panels.csv")
    print("\n[*] FORTIGUARD\n")
    show_distribution("fortiguard_panels.csv")
    print("\n[*] OPENDNS\n")
    show_distribution("opendns_panels.csv")



if __name__ == "__main__":
    main()

        

