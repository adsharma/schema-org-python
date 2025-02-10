from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class Thesis(CreativeWork):
    """
    A thesis or dissertation document submitted in support of candidature for an academic degree or professional qualification.
    """

    inSupportOf: Optional[Union[str, List[str]]] = None
