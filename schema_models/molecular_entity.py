from typing import List, Optional, Union

from schema_models.bio_chem_entity import BioChemEntity
from schema_models.defined_term import DefinedTerm


class MolecularEntity(BioChemEntity):
    """
    Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity.
    """

    chemicalRole: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    inChIKey: Optional[Union[str, List[str]]] = None
    molecularWeight: Optional[
        Union[str, List[str], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    molecularFormula: Optional[Union[str, List[str]]] = None
    inChI: Optional[Union[str, List[str]]] = None
    iupacName: Optional[Union[str, List[str]]] = None
    smiles: Optional[Union[str, List[str]]] = None
    monoisotopicMolecularWeight: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"], str, List[str]]
    ] = None
    potentialUse: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
