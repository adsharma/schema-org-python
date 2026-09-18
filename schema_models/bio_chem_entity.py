from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.thing import Thing


@dataclass
class BioChemEntity(Thing):
    """
    Any biological, chemical, or biochemical thing. For example: a protein; a gene; a chemical; a synthetic chemical.
    """

    associatedDisease: Optional[
        Union[
            "MedicalCondition",
            List["MedicalCondition"],
            "PropertyValue",
            List["PropertyValue"],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    bioChemInteraction: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = None
    bioChemSimilarity: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = None
    biologicalRole: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    funding: Optional[Union["Grant", List["Grant"]]] = None
    hasBioChemEntityPart: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = None
    hasMolecularFunction: Optional[
        Union[
            "DefinedTerm",
            List["DefinedTerm"],
            "PropertyValue",
            List["PropertyValue"],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    hasRepresentation: Optional[
        Union[
            "PropertyValue",
            List["PropertyValue"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    isEncodedByBioChemEntity: Optional[Union["Gene", List["Gene"]]] = None
    isInvolvedInBiologicalProcess: Optional[
        Union[
            "DefinedTerm",
            List["DefinedTerm"],
            "PropertyValue",
            List["PropertyValue"],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    isLocatedInSubcellularLocation: Optional[
        Union[
            "DefinedTerm",
            List["DefinedTerm"],
            "PropertyValue",
            List["PropertyValue"],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    isPartOfBioChemEntity: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = (
        None
    )
    taxonomicRange: Optional[
        Union[
            "DefinedTerm",
            List["DefinedTerm"],
            "Taxon",
            List["Taxon"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
