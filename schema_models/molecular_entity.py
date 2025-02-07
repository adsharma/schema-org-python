from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.bio_chem_entity import BioChemEntity
from schema_models.defined_term import DefinedTerm
from schema_models.quantitative_value import QuantitativeValue
from schema_models.text import Text


class MolecularEntity(BioChemEntity):
    chemicalRole: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    inChIKey: Optional[Union[Text, List[Text]]] = None
    molecularWeight: Optional[Union[Text, List[Text]]] = None
    molecularWeight: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    molecularFormula: Optional[Union[Text, List[Text]]] = None
    inChI: Optional[Union[Text, List[Text]]] = None
    iupacName: Optional[Union[Text, List[Text]]] = None
    smiles: Optional[Union[Text, List[Text]]] = None
    monoisotopicMolecularWeight: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    monoisotopicMolecularWeight: Optional[Union[Text, List[Text]]] = None
    potentialUse: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
