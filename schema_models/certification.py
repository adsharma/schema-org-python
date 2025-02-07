from typing import List, Optional, Union

from schema_models.administrative_area import AdministrativeArea
from schema_models.creative_work import CreativeWork
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.defined_term import DefinedTerm
from schema_models.organization import Organization
from schema_models.rating import Rating
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.url import URL


class Certification(CreativeWork):
    hasMeasurement: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    certificationRating: Optional[Union[Rating, List[Rating]]] = None
    expires: Optional[Union[Date, List[Date]]] = None
    expires: Optional[Union[DateTime, List[DateTime]]] = None
    about: Optional[Union[Thing, List[Thing]]] = None
    datePublished: Optional[Union[Date, List[Date]]] = None
    datePublished: Optional[Union[DateTime, List[DateTime]]] = None
    validIn: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    issuedBy: Optional[Union[Organization, List[Organization]]] = None
    certificationIdentification: Optional[Union[Text, List[Text]]] = None
    certificationIdentification: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    auditDate: Optional[Union[DateTime, List[DateTime]]] = None
    auditDate: Optional[Union[Date, List[Date]]] = None
    certificationStatus: Optional[
        Union["CertificationStatusEnumeration", List["CertificationStatusEnumeration"]]
    ] = None
    logo: Optional[Union[URL, List[URL]]] = None
    logo: Optional[Union["ImageObject", List["ImageObject"]]] = None
    validFrom: Optional[Union[DateTime, List[DateTime]]] = None
    validFrom: Optional[Union[Date, List[Date]]] = None
