from typing import List, Optional, Union

from schema_models.clip import Clip
from schema_models.tv_series import TVSeries


class TVClip(Clip):
    partOfTVSeries: Optional[Union[TVSeries, List[TVSeries]]] = None
