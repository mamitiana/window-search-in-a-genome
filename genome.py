from Bio import SeqIO

class Genome:

  def __init__(self, file):

    self.file = file
    self.dict_genome = None

  def read_fasta(self):
    """
    Reads a fasta file using SeqIO
    """
    self.dict_genome = SeqIO.to_dict(SeqIO.parse(self.file, "fasta"))

  def check_position_sequence_in_genome(self, genome, seq):
    """
    Returns a dictionary containing the start
    and end of each sequence inside genome.
    """
    result = dict()

    for s in seq:

      intermediate_list = []

      for i in range(0, len(genome), 1):
        if genome[i:len(s) + i] == s:
          intermediate_list.append((s, i, len(s) + i))

      result[s] = intermediate_list

    return result

  def scan_genome_given_seq(self, genome, motif_list, window_lenght=200, stride=1, thrsehold=2):

    """
      input :
        - genome : string representing the long string which is the genome
        - motif_list : list of "motif" to check if it exists in a window
        - window_lenght : length of the window where we must check the "motifs"
        - stride : window displacement stride

      Returns the window whose number of sequences present is greater than a certain threshold.
    """

    list_result = list()

    lenght_result = ((len(genome) - window_lenght) / stride) + 1

    for i in range(int(lenght_result)):

      nb_motif_checked = 0

      for motif in motif_list:
        if motif in genome[i:window_lenght + i]:
          nb_motif_checked += 1

      if thrsehold == nb_motif_checked:
        list_result.append((i, window_lenght + i))

    return list_result

if __name__ == "__main__":
  g = Genome('rmark3.fa')
  g.read_fasta()
  genome = g.dict_genome['rmark1'].seq
  # a recuperer à partir d un fichier
  sequence = ["GAG", "AUG"]
  print(g.scan_genome_given_seq(genome, sequence))


