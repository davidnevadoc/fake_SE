#!/usr/bin/env python3


import json
import os
from statistics import mean, median


    
"""
-----------------------------------------------------------------------
Read all JSON files and return a list of JSON
-----------------------------------------------------------------------
"""
def read_JSON_files (directory):

    jlist = []
    for entry in os.scandir(directory):
        if (entry.path.endswith(".json")):
            with open(entry.path) as f:
                jlist.append(json.load(f))
     
    return jlist


"""
-----------------------------------------------------------------------
HTTPS certificate issuers
-----------------------------------------------------------------------
"""
def cert_issuers (jlist):

    cert_issuers = dict()
    for j in jlist:
        try:
            issuer = j['data']['attributes']['last_https_certificate']['issuer']['O']
            if issuer in cert_issuers:
                cert_issuers[issuer] += 1
            else:
                cert_issuers[issuer] = 1
        except KeyError:
             continue

    sorted_dict = [(cert_issuers[key], key) for key in cert_issuers]
    sorted_dict.sort()
    sorted_dict.reverse()

    for s in sorted_dict: print(str(s))



"""
-----------------------------------------------------------------------
HTTPS certificate versions
-----------------------------------------------------------------------
"""
def cert_versions (jlist):

    cert_versions = dict()
    for j in jlist:
        try:
            version = j['data']['attributes']['last_https_certificate']['version']
            if version in cert_versions:
                cert_versions[version] += 1
            else:
                cert_versions[version] = 1
        except KeyError:
             continue

    sorted_dict = [(cert_versions[key], key) for key in cert_versions]
    sorted_dict.sort()
    sorted_dict.reverse()

    for s in sorted_dict: print(str(s))




"""
-----------------------------------------------------------------------
Domain registrars
-----------------------------------------------------------------------
"""
def domain_registrars (jlist):

    regs = dict()
    for j in jlist:
        try:
            r = j['data']['attributes']['registrar']
            if r in regs:
                regs[r] += 1
            else:
                regs[r] = 1
        except KeyError:
             continue

    sorted_dict = [(regs[key], key) for key in regs]
    sorted_dict.sort()
    sorted_dict.reverse()

    for s in sorted_dict: print(str(s))


"""
-----------------------------------------------------------------------
Alexa ranks
-----------------------------------------------------------------------
"""
def alexa (jlist):

    ranking = []
    for j in jlist:
        try:        
            pos = j['data']['attributes']['popularity_ranks']['Alexa']['rank']
            ranking.append(pos)
        except KeyError:
             continue

    print("[*] Alexa rankings:\n")
    print("  mean: " + str(mean(ranking)) + "\n")
    print("median: " + str(median(ranking)) + "\n")
    print("   min: " + str(min(ranking)) + "\n")
    print("   max: " + str(max(ranking)) + "\n")
      

"""
-----------------------------------------------------------------------
Statvoo ranks
-----------------------------------------------------------------------
"""
def statvoo (jlist):

    ranking = []
    for j in jlist:
        try:        
            pos = j['data']['attributes']['popularity_ranks']['Statvoo']['rank']
            ranking.append(pos)
        except KeyError:
             continue

    print("[*] Statvoo rankings:\n")
    print("  mean: " + str(mean(ranking)) + "\n")
    print("median: " + str(median(ranking)) + "\n")
    print("   min: " + str(min(ranking)) + "\n")
    print("   max: " + str(max(ranking)) + "\n")
      


"""
---------------------------------------------------------------------------
Main
---------------------------------------------------------------------------
"""
def main():

    jlist = read_JSON_files("./results_vt")

    # Print VT engines analysis results
    #for j in jlist:
    #    print(j['data']['attributes']['last_analysis_stats'])

    print("[*] HTTPS certificate issuers\n")
    cert_issuers(jlist)

    print("[*] HTTPS certificate versions\n")
    cert_versions(jlist)

    print("[*] Domain registrars\n")
    domain_registrars(jlist)
    

    alexa(jlist)

    statvoo(jlist)

if __name__ == "__main__":
    main()

        

