from typing import List, Optional, Union

from fquery.pydantic import pydantic
from pydantic import ConfigDict

from schema_models.text import Text


@pydantic
class Thing:
    model_config = ConfigDict(arbitrary_types_allowed=True)

    subjectOf: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    subjectOf: Optional[Union["Event", List["Event"]]] = None
    alternateName: Optional[Union[Text, List[Text]]] = None
    additionalType: Optional[Union[Text, List[Text]]] = None
    additionalType: Optional[Union["URL", List["URL"]]] = None
    sameAs: Optional[Union["URL", List["URL"]]] = None
    identifier: Optional[Union[Text, List[Text]]] = None
    identifier: Optional[Union["URL", List["URL"]]] = None
    identifier: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    name: Optional[str] = None
    url: Optional[Union["URL", List["URL"]]] = None
    description: Optional[Union[Text, List[Text]]] = None
    description: Optional[Union["TextObject", List["TextObject"]]] = None
    potentialAction: Optional[Union["Action", List["Action"]]] = None
    image: Optional[Union["ImageObject", List["ImageObject"]]] = None
    image: Optional[Union["URL", List["URL"]]] = None
    disambiguatingDescription: Optional[Union[Text, List[Text]]] = None
    mainEntityOfPage: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    mainEntityOfPage: Optional[Union["URL", List["URL"]]] = None
