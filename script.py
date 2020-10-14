ejercicio biopython
from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation, SeqFeature
from Bio.SeqRecord import SeqRecord
def summarize_contents(filename):
  record = SeqIO.read(filename, "genbank")
  print("Name: ", record.name)
  record = list(SeqIO.parse("filename" , "genbank"))
  print("found % records" % len(records))
  records = list(SeqIO.parse("filename", "genbank"))
  len(records) print(records[1].id)
