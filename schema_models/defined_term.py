from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.defined_term_set import DefinedTermSet
from schema_models.intangible import Intangible
from schema_models.thing import Thing


@dataclass
class DefinedTerm(Intangible):
    """
    A word, name, acronym, phrase, etc. with a formal definition. Often used in the context of category or subject classification, glossaries or dictionaries, product or creative work types, etc. Use the name property for the term being defined, use termCode if the term has an alpha-numeric code allocated, use description to provide the definition of the term. Use the about property to specify what the term is about.
    """

    about: Optional[Union[Thing, List[Thing]]] = None
    inDefinedTermSet: Optional[
        Union[DefinedTermSet, List[DefinedTermSet], HttpUrl, List[HttpUrl]]
    ] = None
    termCode: Optional[Union[str, List[str]]] = None
