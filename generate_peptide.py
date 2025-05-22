import random

AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"


def generate_peptide(length=15):
    """Generate a random peptide of given length using standard amino acids."""
    return ''.join(random.choice(AMINO_ACIDS) for _ in range(length))


if __name__ == "__main__":
    print(generate_peptide())
