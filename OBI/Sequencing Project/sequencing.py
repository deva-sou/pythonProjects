import random
# Génération des données de test
def create_readset_file(fasta_file,N,L):
	return

def read_fasta(fasta_file):
	fasta_file = open("test.fasta")
	with open('test.fasta','r') as file:
	    content = file.readlines()[1:]
	output="".join(content)
	return output

def generate_reads(sequence,N,L): 
	listetest =[]
	for i in range (0, N): 
		listetest.append(sequence[i:i+L])
	return listetest

def qualities(L): 
	
	return

fasta_file = open('test.fasta')
output = read_fasta(fasta_file)
cut = generate_reads(output, 3, 2)
print(cut)
