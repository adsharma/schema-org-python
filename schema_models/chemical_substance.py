from typing import List, Optional, Union

from schema_models.bio_chem_entity import BioChemEntity
from schema_models.defined_term import DefinedTerm


class ChemicalSubstance(BioChemEntity):
    potentialUse: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    chemicalComposition: Optional[Union[str, List[str]]] = None
    chemicalRole: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
