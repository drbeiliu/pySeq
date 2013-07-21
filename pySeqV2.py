##############
# QLFLVFF
from Bio import SeqIO
#from Bio.Seq import Seq
#from Bio.Alphabet import IUPAC
import re

# generate pattern
# Here is some example
#  'LFLVFF',
#  'LF(LV){0,10}FF', will match LFFF,LFLVFF, LFLVLVFF, LFLVLVLVFF....
#  'LF([LFV]{1,5}D){1,10}FF', with match LFLDFF,LFLDLDFF,...LFFDFF,LFVDFF 
myseq = 'ALEPFPV'
seqfile = "uniprot-Homo sapiens (Human) [9606]"


################################################
pp = re.compile(myseq)
foundSeq = []
foundID  = []
##     Calculete item numbers
#seq_iterator = SeqIO.parse(seqfilt, "fasta")
#print sum(1 for e in seq_iterator)
#############################################
seq_iterator = SeqIO.parse(seqfile+'.fasta', "fasta")
item_num = 0
n = 0
f = open(seqfile+'_Pattern_'+myseq+'.txt','wb')
for each_item in seq_iterator:
    item_num += 1
    mall = pp.findall(str(each_item.seq))
    if mall:
        miter = pp.finditer(str(each_item.seq))
        n = n + 1
        f.write('#'*10+'\r\n')
        f.write("ID : %s \r\n " % each_item.id)
        f.write("Discription : %s \r\n " % each_item.discription)
        print each_item.id
        foundSeq.append(each_item)
        foundID.append(each_item.id)
        for i in miter:
            #f.write("span from %s \r\n" % i.span()) 
            f.write(" ".join(map(lambda x: str(x), i.span())))
            f.write(" %s \r\n" % i.group())
            print i.group(), 'span from: ', i.span()       
print item_num, n
# save whole sequence content
SeqIO.write(foundSeq,seqfile+'_foundSeq.fasta','fasta')
# save ID
f.close