from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.thing import Thing


class Taxon(Thing):
    hasDefinedTerm: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    taxonRank: Optional[Union[str, List[str]]] = None
    taxonRank: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    taxonRank: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    childTaxon: Optional[Union[str, List[str]]] = None
    childTaxon: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    childTaxon: Optional[Union["Taxon", List["Taxon"]]] = None
    parentTaxon: Optional[Union["Taxon", List["Taxon"]]] = None
    parentTaxon: Optional[Union[str, List[str]]] = None
    parentTaxon: Optional[Union[HttpUrl, List[HttpUrl]]] = None
