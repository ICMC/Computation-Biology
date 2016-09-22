import Bio
from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls

#username = input("Plotly username: ")
#apiKey = input("Plotly API Key: ")

username= "pawpepe"
apiKey = "07lxwcy4d2"
tls.set_credentials_file(username, apiKey)

orfStart=[]
orfEnd=[]
path = input("path to the .fasta file: ")
for seq_record in SeqIO.parse(path,"fasta"):
    print(seq_record.id)
    sequence = str(seq_record.seq)
    print(len(seq_record))

    size = len(sequence)
    orfPortion= 0
    bigOrf = 0
    #iterating through the nucleotides bases to find the ORFs
    for i in range(0,size-3):

        #if the nucleotide is an "A", and the following two are "T" and "A" then register the position
        #and find stopping codon.
        if(sequence[i]=="A" and sequence[i+1]=="T" and sequence[i+2]=="A"):
            orfStart.append(i)

            #checking all the nucleitides that come after the starting codon "ATA"
            for j in range(i+2, size-3):


                if((sequence[j]=="A" and sequence[j+1]=="G" and sequence[j+2]=="A") or (sequence[j]=="A" and sequence[j+1]=="G" and sequence[j+2]=="G")):
                    aux = (j+2) - i
                    if aux > bigOrf:
                        bigOrf = aux
                    orfEnd.append(j+2)
                    orfPortion+= (j+2) - i
                    #i = j+2
                    break
                j+=2



    print(orfPortion)
    print("Bigger ORF Size: ", bigOrf)
    print("Percentage of All ORFs: ", (orfPortion/size))
    print("Percentage of the Bigger ORF: ",(bigOrf/size))
