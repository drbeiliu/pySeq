##############
# QLFLVFF
from Bio import SeqIO
#from Bio.Seq import Seq
#from Bio.Alphabet import IUPAC
import re

# generate pattern
# Here is some example
#  'LFLVFF',
#  'LF(LV){1,10}FF', will match LFLVFF, LFLVLVFF, LFLVLVLVFF....
#  'LF([LFV]D){1,10}FF', with match LFLDFF,LFFDFF,LFVDFF 
myseq = 'VFYLKMK'
pp = re.compile(myseq)

seqfilt = "uniprot-Homo sapiens (Human) [9606].fasta"
foundSeq = []
##     Calculete item numbers
#seq_iterator = SeqIO.parse(seqfilt, "fasta")
#print sum(1 for e in seq_iterator)
#############################################
seq_iterator = SeqIO.parse(seqfilt, "fasta")
item_num = 0
n = 0
for each_item in seq_iterator:
    item_num += 1
    m = pp.search(str(each_item.seq))
    if not m == None:
        n = n + 1
        print each_item.id
        print each_item.description
        print m.group()
        print m.span()
        foundSeq.append(each_item)
print item_num, n
#SeqIO.write(foundSeq,'foundSeq.fasta','fasta')
