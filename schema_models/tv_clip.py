from typing import List, Optional, Union

from schema_models.clip import Clip
from schema_models.tv_series import TVSeries


class TVClip(Clip):
    """
    A short TV program or a segment/part of a TV program.
    """

    partOfTVSeries: Optional[Union[TVSeries, List[TVSeries]]] = None
