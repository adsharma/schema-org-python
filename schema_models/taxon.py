from typing import List, Optional, Union

from schema_models.defined_term import DefinedTerm
from schema_models.property_value import PropertyValue
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.url import URL


class Taxon(Thing):
    hasDefinedTerm: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    taxonRank: Optional[Union[Text, List[Text]]] = None
    taxonRank: Optional[Union[URL, List[URL]]] = None
    taxonRank: Optional[Union[PropertyValue, List[PropertyValue]]] = None
    childTaxon: Optional[Union[Text, List[Text]]] = None
    childTaxon: Optional[Union[URL, List[URL]]] = None
    childTaxon: Optional[Union["Taxon", List["Taxon"]]] = None
    parentTaxon: Optional[Union["Taxon", List["Taxon"]]] = None
    parentTaxon: Optional[Union[Text, List[Text]]] = None
    parentTaxon: Optional[Union[URL, List[URL]]] = None
