from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.thing import Thing


@dataclass
class Taxon(Thing):
    """
    A set of organisms asserted to represent a natural cohesive biological unit.
    """

    childTaxon: Optional[
        Union["Taxon", List["Taxon"], str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
    hasDefinedTerm: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    parentTaxon: Optional[
        Union["Taxon", List["Taxon"], str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
    taxonRank: Optional[
        Union[
            "PropertyValue",
            List["PropertyValue"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
