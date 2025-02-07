from typing import List, Optional, Union

from schema_models.bio_chem_entity import BioChemEntity
from schema_models.defined_term import DefinedTerm
from schema_models.text import Text


class ChemicalSubstance(BioChemEntity):
    potentialUse: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    chemicalComposition: Optional[Union[Text, List[Text]]] = None
    chemicalRole: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
