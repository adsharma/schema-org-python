from typing import List, Optional, Union

from schema_models.bio_chem_entity import BioChemEntity
from schema_models.defined_term import DefinedTerm


class ChemicalSubstance(BioChemEntity):
    """
    A chemical substance is 'a portion of matter of constant composition, composed of molecular entities of the same type or of different types' (source: [ChEBI:59999](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=59999)).
    """

    potentialUse: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    chemicalComposition: Optional[Union[str, List[str]]] = None
    chemicalRole: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
