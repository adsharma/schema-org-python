from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.structured_value import StructuredValue


class CDCPMDRecord(StructuredValue):
    cvdNumTotBeds: Optional[Union[float, List[float]]] = None
    datePosted: Optional[Union[datetime, List[datetime]]] = None
    datePosted: Optional[Union[date, List[date]]] = None
    cvdNumC19HOPats: Optional[Union[float, List[float]]] = None
    cvdFacilityCounty: Optional[Union[str, List[str]]] = None
    cvdNumVent: Optional[Union[float, List[float]]] = None
    cvdNumVentUse: Optional[Union[float, List[float]]] = None
    cvdNumBeds: Optional[Union[float, List[float]]] = None
    cvdNumC19Died: Optional[Union[float, List[float]]] = None
    cvdNumC19OverflowPats: Optional[Union[float, List[float]]] = None
    cvdNumICUBedsOcc: Optional[Union[float, List[float]]] = None
    cvdNumC19HospPats: Optional[Union[float, List[float]]] = None
    cvdCollectionDate: Optional[Union[datetime, List[datetime]]] = None
    cvdCollectionDate: Optional[Union[str, List[str]]] = None
    cvdNumC19MechVentPats: Optional[Union[float, List[float]]] = None
    cvdNumBedsOcc: Optional[Union[float, List[float]]] = None
    cvdNumC19OFMechVentPats: Optional[Union[float, List[float]]] = None
    cvdFacilityId: Optional[Union[str, List[str]]] = None
    cvdNumICUBeds: Optional[Union[float, List[float]]] = None
