from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork


class PublicationVolume(CreativeWork):
    pagination: Optional[Union[str, List[str]]] = None
    volumeNumber: Optional[Union[str, List[str]]] = None
    volumeNumber: Optional[Union[int, List[int]]] = None
    pageEnd: Optional[Union[int, List[int]]] = None
    pageEnd: Optional[Union[str, List[str]]] = None
    pageStart: Optional[Union[str, List[str]]] = None
    pageStart: Optional[Union[int, List[int]]] = None
