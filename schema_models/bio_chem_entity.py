from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.taxon import Taxon
from schema_models.thing import Thing


class BioChemEntity(Thing):
    """
    Any biological, chemical, or biochemical thing. For example: a protein; a gene; a chemical; a synthetic chemical.
    """

    funding: Optional[Union["Grant", List["Grant"]]] = None
    hasMolecularFunction: Optional[
        Union[
            HttpUrl,
            List[HttpUrl],
            "DefinedTerm",
            List["DefinedTerm"],
            "PropertyValue",
            List["PropertyValue"],
        ]
    ] = None
    biologicalRole: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    bioChemSimilarity: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = None
    taxonomicRange: Optional[
        Union[
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
            "DefinedTerm",
            List["DefinedTerm"],
            Taxon,
            List[Taxon],
        ]
    ] = None
    isLocatedInSubcellularLocation: Optional[
        Union[
            HttpUrl,
            List[HttpUrl],
            "DefinedTerm",
            List["DefinedTerm"],
            "PropertyValue",
            List["PropertyValue"],
        ]
    ] = None
    hasRepresentation: Optional[
        Union[
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
            "PropertyValue",
            List["PropertyValue"],
        ]
    ] = None
    bioChemInteraction: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = None
    isPartOfBioChemEntity: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = (
        None
    )
    hasBioChemEntityPart: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = None
    associatedDisease: Optional[
        Union[
            HttpUrl,
            List[HttpUrl],
            "PropertyValue",
            List["PropertyValue"],
            "MedicalCondition",
            List["MedicalCondition"],
        ]
    ] = None
    isInvolvedInBiologicalProcess: Optional[
        Union[
            "PropertyValue",
            List["PropertyValue"],
            HttpUrl,
            List[HttpUrl],
            "DefinedTerm",
            List["DefinedTerm"],
        ]
    ] = None
    isEncodedByBioChemEntity: Optional[Union["Gene", List["Gene"]]] = None
