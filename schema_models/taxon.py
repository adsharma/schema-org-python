from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.thing import Thing


class Taxon(Thing):
    """
    A set of organisms asserted to represent a natural cohesive biological unit.
    """

    hasDefinedTerm: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    taxonRank: Optional[
        Union[
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
            "PropertyValue",
            List["PropertyValue"],
        ]
    ] = None
    childTaxon: Optional[
        Union[str, List[str], HttpUrl, List[HttpUrl], "Taxon", List["Taxon"]]
    ] = None
    parentTaxon: Optional[
        Union["Taxon", List["Taxon"], str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
