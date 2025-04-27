# Importing the required class from Biopython
from Bio.Seq import Seq

# Defining the DNA sequence
DNA = Seq("ATGCGTACGTTAG")

# Displaying the original DNA sequence
print("Original DNA sequence:", DNA)

# Displaying the complement of the DNA sequence
print("Complement of DNA:", DNA.complement())

# Displaying the reverse complement of the DNA sequence
print("Reverse complement of DNA:", DNA.reverse_complement())

# Transcribing DNA to RNA
print("Transcribed RNA sequence:", DNA.transcribe())

# Translating DNA to protein (amino acids)
print("Translated Protein sequence:", DNA.translate())

# Reversing the DNA sequence manually
print("Manually reversed DNA sequence:", DNA[::-1])

# Counting occurrences of each nucleotide
print("Count of 'A' in DNA:", DNA.count("A"))
print("Count of 'G' in DNA:", DNA.count("G"))
print("Count of 'T' in DNA:", DNA.count("T"))

# Replacing 'T' with 'U' (another way to mimic RNA transcription)
print("DNA sequence with T replaced by U:", DNA.replace("T", "U"))

# Calculating GC content
GC_count = DNA.count("G") + DNA.count("C")
print("Total G and C bases (GC Count):", GC_count)

# Calculating total number of bases
total_bases = len(DNA)
print("Total number of bases in DNA:", total_bases)

# Showing the incorrect string attempt (for learning purpose)
GC_content_str = 'GC_count/total_bases*100'
print("GC Content formula as string:", GC_content_str)

# Correct calculation of GC content as a percentage
GC_content = (GC_count / total_bases) * 100
print("GC Content calculated (in %):", GC_content, type(GC_content))

# Displaying GC content with 2 decimal places
print(f"GC Content (formatted to 2 decimal places): {GC_content:.2f}%")

# Searching for a specific subsequence in the DNA
subseq = "CGTA"
if subseq in DNA:
    print(f"Subsequence '{subseq}' found in DNA sequence.")
else:
    print(f"Subsequence '{subseq}' not found in DNA sequence.")

# Comparing two DNA sequences
Sequence1 = Seq("ATGCGTACGTTAG")
Sequence2 = Seq("ATGCGTACGATAG")

# Checking if the two sequences are identical
if Sequence1 == Sequence2:
    print("The two sequences are identical.")
else:
    print("The two sequences are not identical.")

# Counting the number of matching bases between two sequences
matches = sum(1 for original, compared in zip(Sequence1, Sequence2) if original == compared)
print("Number of matching bases:", matches)

# Calculating the matching percentage
matching_percentage = (matches / len(Sequence1)) * 100
print(f"Matching percentage between the two sequences: {matching_percentage:.2f}%")
