import csv
import sys

#sequence é o arquivo txt; subsequence é um dos STR
def longest_match(sequence, subsequence):

  longest_run = 0
  len_sub = len(subsequence)
  len_seq = len(sequence)

  for i in range(len_seq):
    #conta de STR consecutivos
    count = 0

    while True:

      start = i + count * len_sub
      end = start + len_sub

      if sequence[start:end] == subsequence:
        count +=1

      else:
        break
    longest_run = max(longest_run, count)

  return longest_run


def main():
    #command line usage
  if len(sys.argv) != 3:
      print("Usage: python dna.py data.csv sequence.txt")
      sys.exit(1)

  #read database into a variablepython dna.py
  #database é meu arquivo csv em formato de dicionário nome:valor dentro da lista
  database = []
  with open(sys.argv[1], 'r') as file:
      reader = csv.DictReader(file)
      for row in reader:
          database.append(row)
  #print(database)

  #read sequence file into a variable
  with open(sys.argv[2], 'r') as file:
      dna_sequence = file.read()
  #print(dna_sequence)

  #find longest match of each STR in DNA sequence
  subsequences = list(database[0].keys())[1:]
  #subsequences = AGATC,TTTTTTCT,AATG,TCTAG,GATA,TATC,GAAA,TCTG or AGATC,AATG,TATC
  #print(len(subsequences))
  results = {}
  for i in subsequences:
      results[i] = longest_match(dna_sequence, i)
  #print(results)

  #check database to match profiles
  no_match = 0
  for i in database:
      count = 0
      for j in subsequences:
          if int(i[j]) == results[j]:
              count += 1

      if count == len(subsequences):
          print(i["name"])
          break

      if count != len(subsequences) and i  == database[-1]:
          no_match += 1
          print("no match")

main()
