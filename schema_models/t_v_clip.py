from typing import List, Optional, Union

from schema_models.clip import Clip
from schema_models.t_v_series import TVSeries


class TVClip(Clip):
    partOfTVSeries: Optional[Union[TVSeries, List[TVSeries]]] = None
