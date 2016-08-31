import Bio
from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC

for seq_record in SeqIO.parse("sequence.fasta","fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
    print("Whole Sequence: " + str(seq_record.seq.count('CG')))
    print("porcentage: " + str((seq_record.seq.count('CG'))/len(seq_record)) + "\n")
    print("slice seq[4:30]: " + str(seq_record[4:300].seq.count('CG')))
    print("porcentage: " + str((seq_record[4:300].seq.count('CG'))/len(seq_record)) + "\n")
    print("slice seq[1:100]: " + str(seq_record[1:100].seq.count('CG')))
    print("porcentage: " + str(seq_record[1:100].seq.count('CG')/len(seq_record)) + "\n")
    print("slice seq[100:10000]" + str(seq_record[100:10000].seq.count('CG')))
    print("porcentage: " + str((seq_record[100:10000].seq.count('CG'))/len(seq_record))+ "\n")
    print("slice seq[10000:40000]: " + str(seq_record[10000:40000].seq.count('CG')))
    print("porcentage: " + str((seq_record[10000:40000].seq.count('CG'))/len(seq_record)) + "\n")
    print("slice seq[40000:48500]: " + str(seq_record[40000:48500].seq.count('CG')))
    print("porcentage: " + str((seq_record[40000:48500].seq.count('CG'))/len(seq_record)) + "\n")
