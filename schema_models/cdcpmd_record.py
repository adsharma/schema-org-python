from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.structured_value import StructuredValue


@dataclass
class CDCPMDRecord(StructuredValue):
    """
    A CDCPMDRecord is a data structure representing a record in a CDC tabular data format
          used for hospital data reporting. See [documentation](/docs/cdc-covid.html) for details, and the linked CDC materials for authoritative
          definitions used as the source here.

    """

    cvdCollectionDate: Optional[Union[datetime, List[datetime], str, List[str]]] = None
    cvdFacilityCounty: Optional[Union[str, List[str]]] = None
    cvdFacilityId: Optional[Union[str, List[str]]] = None
    cvdNumBeds: Optional[Union[float, List[float]]] = None
    cvdNumBedsOcc: Optional[Union[float, List[float]]] = None
    cvdNumC19Died: Optional[Union[float, List[float]]] = None
    cvdNumC19HOPats: Optional[Union[float, List[float]]] = None
    cvdNumC19HospPats: Optional[Union[float, List[float]]] = None
    cvdNumC19MechVentPats: Optional[Union[float, List[float]]] = None
    cvdNumC19OFMechVentPats: Optional[Union[float, List[float]]] = None
    cvdNumC19OverflowPats: Optional[Union[float, List[float]]] = None
    cvdNumICUBeds: Optional[Union[float, List[float]]] = None
    cvdNumICUBedsOcc: Optional[Union[float, List[float]]] = None
    cvdNumTotBeds: Optional[Union[float, List[float]]] = None
    cvdNumVent: Optional[Union[float, List[float]]] = None
    cvdNumVentUse: Optional[Union[float, List[float]]] = None
    datePosted: Optional[Union[date, List[date], datetime, List[datetime]]] = None
