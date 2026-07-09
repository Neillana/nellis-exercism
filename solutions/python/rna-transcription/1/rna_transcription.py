"""Module to determine the RNA complement of a given DNA sequence.
"""


def to_rna(dna_strand):
    """Transpose a DNA strand into its RNA complement.

    The function maps each DNA nucleotide to its complementary RNA nucleotide:
    - G -> C
    - C -> G
    - T -> A
    - A -> U

    Args:
        dna_strand: The string representing the DNA sequence to transpose.

    Returns:
        The complementary RNA sequence as a string.

    Examples:
        >>> to_rna("GCTA")
        'CGAU'
    """
    dna_to_rna = {"G": "C", "C": "G", "T": "A", "A": "U"}
    dna_strand = dna_strand.upper()
    rna_sequence = []

    for char in dna_strand:
        if char in dna_to_rna:
            rna_sequence.append(dna_to_rna[char])

    return "".join(rna_sequence)