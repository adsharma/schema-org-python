from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.taxon import Taxon
from schema_models.thing import Thing


class BioChemEntity(Thing):
    funding: Optional[Union["Grant", List["Grant"]]] = None
    hasMolecularFunction: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    hasMolecularFunction: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    hasMolecularFunction: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    biologicalRole: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    bioChemSimilarity: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = None
    taxonomicRange: Optional[Union[str, List[str]]] = None
    taxonomicRange: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    taxonomicRange: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    taxonomicRange: Optional[Union[Taxon, List[Taxon]]] = None
    isLocatedInSubcellularLocation: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    isLocatedInSubcellularLocation: Optional[
        Union["DefinedTerm", List["DefinedTerm"]]
    ] = None
    isLocatedInSubcellularLocation: Optional[
        Union["PropertyValue", List["PropertyValue"]]
    ] = None
    hasRepresentation: Optional[Union[str, List[str]]] = None
    hasRepresentation: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    hasRepresentation: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    bioChemInteraction: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = None
    isPartOfBioChemEntity: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = (
        None
    )
    hasBioChemEntityPart: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = None
    associatedDisease: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    associatedDisease: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    associatedDisease: Optional[Union["MedicalCondition", List["MedicalCondition"]]] = (
        None
    )
    isInvolvedInBiologicalProcess: Optional[
        Union["PropertyValue", List["PropertyValue"]]
    ] = None
    isInvolvedInBiologicalProcess: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    isInvolvedInBiologicalProcess: Optional[
        Union["DefinedTerm", List["DefinedTerm"]]
    ] = None
    isEncodedByBioChemEntity: Optional[Union["Gene", List["Gene"]]] = None
