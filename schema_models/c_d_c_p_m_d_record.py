from typing import List, Optional, Union

from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.number import Number
from schema_models.structured_value import StructuredValue
from schema_models.text import Text


class CDCPMDRecord(StructuredValue):
    cvdNumTotBeds: Optional[Union[Number, List[Number]]] = None
    datePosted: Optional[Union[DateTime, List[DateTime]]] = None
    datePosted: Optional[Union[Date, List[Date]]] = None
    cvdNumC19HOPats: Optional[Union[Number, List[Number]]] = None
    cvdFacilityCounty: Optional[Union[Text, List[Text]]] = None
    cvdNumVent: Optional[Union[Number, List[Number]]] = None
    cvdNumVentUse: Optional[Union[Number, List[Number]]] = None
    cvdNumBeds: Optional[Union[Number, List[Number]]] = None
    cvdNumC19Died: Optional[Union[Number, List[Number]]] = None
    cvdNumC19OverflowPats: Optional[Union[Number, List[Number]]] = None
    cvdNumICUBedsOcc: Optional[Union[Number, List[Number]]] = None
    cvdNumC19HospPats: Optional[Union[Number, List[Number]]] = None
    cvdCollectionDate: Optional[Union[DateTime, List[DateTime]]] = None
    cvdCollectionDate: Optional[Union[Text, List[Text]]] = None
    cvdNumC19MechVentPats: Optional[Union[Number, List[Number]]] = None
    cvdNumBedsOcc: Optional[Union[Number, List[Number]]] = None
    cvdNumC19OFMechVentPats: Optional[Union[Number, List[Number]]] = None
    cvdFacilityId: Optional[Union[Text, List[Text]]] = None
    cvdNumICUBeds: Optional[Union[Number, List[Number]]] = None
