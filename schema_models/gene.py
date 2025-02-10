from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.anatomical_system import AnatomicalSystem
from schema_models.bio_chem_entity import BioChemEntity
from schema_models.defined_term import DefinedTerm


class Gene(BioChemEntity):
    """
    A discrete unit of inheritance which affects one or more biological traits (Source: [https://en.wikipedia.org/wiki/Gene](https://en.wikipedia.org/wiki/Gene)). Examples include FOXP2 (Forkhead box protein P2), SCARNA21 (small Cajal body-specific RNA 21), A- (agouti genotype).
    """

    hasBioPolymerSequence: Optional[Union[str, List[str]]] = None
    encodesBioChemEntity: Optional[Union[BioChemEntity, List[BioChemEntity]]] = None
    alternativeOf: Optional[Union["Gene", List["Gene"]]] = None
    expressedIn: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = None
    expressedIn: Optional[Union[AnatomicalSystem, List[AnatomicalSystem]]] = None
    expressedIn: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    expressedIn: Optional[Union[BioChemEntity, List[BioChemEntity]]] = None
