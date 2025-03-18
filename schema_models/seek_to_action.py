from typing import List, Optional, Union

from schema_models.action import Action


class SeekToAction(Action):
    """
    This is the [[Action]] of navigating to a specific [[startOffset]] timestamp within a [[VideoObject]], typically represented with a URL template structure.
    """

    startOffset: Optional[
        Union["HyperTocEntry", List["HyperTocEntry"], float, List[float]]
    ] = None
