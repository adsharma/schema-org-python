from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.administrative_area import AdministrativeArea
from schema_models.creative_work import CreativeWork
from schema_models.defined_term import DefinedTerm
from schema_models.organization import Organization
from schema_models.rating import Rating
from schema_models.thing import Thing


class Certification(CreativeWork):
    hasMeasurement: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    certificationRating: Optional[Union[Rating, List[Rating]]] = None
    expires: Optional[Union[date, List[date]]] = None
    expires: Optional[Union[datetime, List[datetime]]] = None
    about: Optional[Union[Thing, List[Thing]]] = None
    datePublished: Optional[Union[date, List[date]]] = None
    datePublished: Optional[Union[datetime, List[datetime]]] = None
    validIn: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    issuedBy: Optional[Union[Organization, List[Organization]]] = None
    certificationIdentification: Optional[Union[str, List[str]]] = None
    certificationIdentification: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    auditDate: Optional[Union[datetime, List[datetime]]] = None
    auditDate: Optional[Union[date, List[date]]] = None
    certificationStatus: Optional[
        Union["CertificationStatusEnumeration", List["CertificationStatusEnumeration"]]
    ] = None
    logo: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    logo: Optional[Union["ImageObject", List["ImageObject"]]] = None
    validFrom: Optional[Union[datetime, List[datetime]]] = None
    validFrom: Optional[Union[date, List[date]]] = None
