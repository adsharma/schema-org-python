from typing import List, Optional, Union

from schema_models.taxon import Taxon
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.url import URL


class BioChemEntity(Thing):
    funding: Optional[Union["Grant", List["Grant"]]] = None
    hasMolecularFunction: Optional[Union[URL, List[URL]]] = None
    hasMolecularFunction: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    hasMolecularFunction: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    biologicalRole: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    bioChemSimilarity: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = None
    taxonomicRange: Optional[Union[Text, List[Text]]] = None
    taxonomicRange: Optional[Union[URL, List[URL]]] = None
    taxonomicRange: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    taxonomicRange: Optional[Union[Taxon, List[Taxon]]] = None
    isLocatedInSubcellularLocation: Optional[Union[URL, List[URL]]] = None
    isLocatedInSubcellularLocation: Optional[
        Union["DefinedTerm", List["DefinedTerm"]]
    ] = None
    isLocatedInSubcellularLocation: Optional[
        Union["PropertyValue", List["PropertyValue"]]
    ] = None
    hasRepresentation: Optional[Union[Text, List[Text]]] = None
    hasRepresentation: Optional[Union[URL, List[URL]]] = None
    hasRepresentation: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    bioChemInteraction: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = None
    isPartOfBioChemEntity: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = (
        None
    )
    hasBioChemEntityPart: Optional[Union["BioChemEntity", List["BioChemEntity"]]] = None
    associatedDisease: Optional[Union[URL, List[URL]]] = None
    associatedDisease: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    associatedDisease: Optional[Union["MedicalCondition", List["MedicalCondition"]]] = (
        None
    )
    isInvolvedInBiologicalProcess: Optional[
        Union["PropertyValue", List["PropertyValue"]]
    ] = None
    isInvolvedInBiologicalProcess: Optional[Union[URL, List[URL]]] = None
    isInvolvedInBiologicalProcess: Optional[
        Union["DefinedTerm", List["DefinedTerm"]]
    ] = None
    isEncodedByBioChemEntity: Optional[Union["Gene", List["Gene"]]] = None
