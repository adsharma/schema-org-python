from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.thing import Thing


@dataclass
class Certification(CreativeWork):
    """
    A Certification is an official and authoritative statement about a subject, for example a product, service, person, or organization. A certification is typically issued by an indendent certification body, for example a professional organization or government. It formally attests certain characteristics about the subject, for example Organizations can be ISO certified, Food products can be certified Organic or Vegan, a Person can be a certified professional, a Place can be certified for food processing. There are certifications for many domains: regulatory, organizational, recycling, food, efficiency, educational, ecological, etc. A certification is a form of credential, as are accreditations and licenses. Mapped from the [gs1:CertificationDetails](https://www.gs1.org/voc/CertificationDetails) class in the GS1 Web Vocabulary.
    """

    about: Optional[Union[Thing, List[Thing]]] = None
    auditDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    certificationIdentification: Optional[
        Union["DefinedTerm", List["DefinedTerm"], str, List[str]]
    ] = None
    certificationRating: Optional[Union["Rating", List["Rating"]]] = None
    certificationStatus: Optional[
        Union["CertificationStatusEnumeration", List["CertificationStatusEnumeration"]]
    ] = None
    datePublished: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    expires: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    hasMeasurement: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    issuedBy: Optional[Union[Organization, List[Organization]]] = None
    logo: Optional[
        Union["ImageObject", List["ImageObject"], HttpUrl, List[HttpUrl]]
    ] = None
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    validIn: Optional[Union["AdministrativeArea", List["AdministrativeArea"]]] = None
