from typing import List, Optional, Union

from fquery.pydantic import pydantic
from pydantic import HttpUrl


@pydantic
class Thing:
    """
    The most generic type of item.
    """

    additionalType: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    alternateName: Optional[Union[str, List[str]]] = None
    description: Optional[Union[str, List[str], "TextObject", List["TextObject"]]] = (
        None
    )
    disambiguatingDescription: Optional[Union[str, List[str]]] = None
    identifier: Optional[
        Union[
            "PropertyValue",
            List["PropertyValue"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    image: Optional[
        Union["ImageObject", List["ImageObject"], HttpUrl, List[HttpUrl]]
    ] = None
    mainEntityOfPage: Optional[
        Union["CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]
    ] = None
    name: Optional[Union[str, List[str]]] = None
    owner: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    potentialAction: Optional[Union["Action", List["Action"]]] = None
    sameAs: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    subjectOf: Optional[
        Union["CreativeWork", List["CreativeWork"], "Event", List["Event"]]
    ] = None
    url: Optional[Union[HttpUrl, List[HttpUrl]]] = None
