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
    """
    A Certification is an official and authoritative statement about a subject, for example a product, service, person, or organization. A certification is typically issued by an indendent certification body, for example a professional organization or government. It formally attests certain characteristics about the subject, for example Organizations can be ISO certified, Food products can be certified Organic or Vegan, a Person can be a certified professional, a Place can be certified for food processing. There are certifications for many domains: regulatory, organizational, recycling, food, efficiency, educational, ecological, etc. A certification is a form of credential, as are accreditations and licenses. Mapped from the [gs1:CertificationDetails](https://www.gs1.org/voc/CertificationDetails) class in the GS1 Web Vocabulary.
    """

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
