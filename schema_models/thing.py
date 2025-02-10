from typing import List, Optional, Union

from fquery.pydantic import pydantic
from pydantic import HttpUrl


@pydantic
class Thing:
    """
    The most generic type of item.
    """

    subjectOf: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    subjectOf: Optional[Union["Event", List["Event"]]] = None
    alternateName: Optional[Union[str, List[str]]] = None
    additionalType: Optional[Union[str, List[str]]] = None
    additionalType: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    sameAs: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    identifier: Optional[Union[str, List[str]]] = None
    identifier: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    identifier: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    name: Optional[Union[str, List[str]]] = None
    url: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    description: Optional[Union[str, List[str]]] = None
    description: Optional[Union["TextObject", List["TextObject"]]] = None
    potentialAction: Optional[Union["Action", List["Action"]]] = None
    image: Optional[Union["ImageObject", List["ImageObject"]]] = None
    image: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    disambiguatingDescription: Optional[Union[str, List[str]]] = None
    mainEntityOfPage: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    mainEntityOfPage: Optional[Union[HttpUrl, List[HttpUrl]]] = None
