from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.bio_chem_entity import BioChemEntity


@dataclass
class Gene(BioChemEntity):
    """
    A discrete unit of inheritance which affects one or more biological traits (Source: [https://en.wikipedia.org/wiki/Gene](https://en.wikipedia.org/wiki/Gene)). Examples include FOXP2 (Forkhead box protein P2), SCARNA21 (small Cajal body-specific RNA 21), A- (agouti genotype).
    """

    alternativeOf: Optional[Union["Gene", List["Gene"]]] = None
    encodesBioChemEntity: Optional[Union[BioChemEntity, List[BioChemEntity]]] = None
    expressedIn: Optional[
        Union[
            "AnatomicalStructure",
            List["AnatomicalStructure"],
            "AnatomicalSystem",
            List["AnatomicalSystem"],
            BioChemEntity,
            List[BioChemEntity],
            "DefinedTerm",
            List["DefinedTerm"],
        ]
    ] = None
    hasBioPolymerSequence: Optional[Union[str, List[str]]] = None
