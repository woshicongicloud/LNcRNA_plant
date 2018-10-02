# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 13:12:51 2018

@author: woshicong
"""
lnc_file = 'step3_ID.out'
gtf_name = 'stringie_merged.gtf'
Lnc_ID = [ ]
LncRNA_gtf = open("LncRNA.gtf","w")
def get_lncGTF(lncID,total_gtf):
    #主要是将lncID存入列表，然后再将存在于总lncRNA抓取出来
    with open (lncID) as a:
        for i in a:
            Lnc_ID.append(i.strip())
        #print(len(Lnc_ID))
    with open(total_gtf) as b:
        for j in b:
            if not j.startswith("#"):
                                #print (j.split("\t")[8].split('"')[1])
                                gene_id = j.split("\t")[8].split('"')[3]
                                if gene_id in Lnc_ID:
                                    LncRNA_gtf.write(j)
if __name__ == "__main__":
    
    get_lncGTF(lncID=lnc_file,total_gtf=gtf_name)
    LncRNA_gtf.close()