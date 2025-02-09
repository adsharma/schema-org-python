from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.anatomical_system import AnatomicalSystem
from schema_models.bio_chem_entity import BioChemEntity
from schema_models.defined_term import DefinedTerm


class Gene(BioChemEntity):
    hasBioPolymerSequence: Optional[Union[str, List[str]]] = None
    encodesBioChemEntity: Optional[Union[BioChemEntity, List[BioChemEntity]]] = None
    alternativeOf: Optional[Union["Gene", List["Gene"]]] = None
    expressedIn: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = None
    expressedIn: Optional[Union[AnatomicalSystem, List[AnatomicalSystem]]] = None
    expressedIn: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    expressedIn: Optional[Union[BioChemEntity, List[BioChemEntity]]] = None
