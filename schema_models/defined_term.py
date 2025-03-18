from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


class DefinedTerm(Intangible):
    """
    A word, name, acronym, phrase, etc. with a formal definition. Often used in the context of category or subject classification, glossaries or dictionaries, product or creative work types, etc. Use the name property for the term being defined, use termCode if the term has an alpha-numeric code allocated, use description to provide the definition of the term.
    """

    inDefinedTermSet: Optional[
        Union[HttpUrl, List[HttpUrl], "DefinedTermSet", List["DefinedTermSet"]]
    ] = None
    termCode: Optional[Union[str, List[str]]] = None
