from typing import List, Optional, Union

from schema_models.bio_chem_entity import BioChemEntity


class Protein(BioChemEntity):
    """
    Protein is here used in its widest possible definition, as classes of amino acid based molecules. Amyloid-beta Protein in human (UniProt P05067), eukaryota (e.g. an OrthoDB group) or even a single molecule that one can point to are all of type :Protein. A protein can thus be a subclass of another protein, e.g. :Protein as a UniProt record can have multiple isoforms inside it which would also be :Protein. They can be imagined, synthetic, hypothetical or naturally occurring.
    """

    hasBioPolymerSequence: Optional[Union[str, List[str]]] = None
