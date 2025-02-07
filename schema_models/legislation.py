from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.administrative_area import AdministrativeArea
from schema_models.category_code import CategoryCode
from schema_models.creative_work import CreativeWork
from schema_models.date import Date
from schema_models.legal_force_status import LegalForceStatus
from schema_models.legislation import Legislation
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.text import Text
from schema_models.url import URL


class Legislation(CreativeWork):
    legislationTransposes: Optional[Union["Legislation", List["Legislation"]]] = None
    legislationPassedBy: Optional[Union[Person, List[Person]]] = None
    legislationPassedBy: Optional[Union[Organization, List[Organization]]] = None
    legislationLegalForce: Optional[Union[LegalForceStatus, List[LegalForceStatus]]] = (
        None
    )
    jurisdiction: Optional[Union[Text, List[Text]]] = None
    jurisdiction: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    legislationJurisdiction: Optional[Union[Text, List[Text]]] = None
    legislationJurisdiction: Optional[
        Union[AdministrativeArea, List[AdministrativeArea]]
    ] = None
    legislationConsolidates: Optional[Union["Legislation", List["Legislation"]]] = None
    legislationResponsible: Optional[Union[Person, List[Person]]] = None
    legislationResponsible: Optional[Union[Organization, List[Organization]]] = None
    legislationDateVersion: Optional[Union[Date, List[Date]]] = None
    legislationApplies: Optional[Union["Legislation", List["Legislation"]]] = None
    legislationDate: Optional[Union[Date, List[Date]]] = None
    legislationIdentifier: Optional[Union[Text, List[Text]]] = None
    legislationIdentifier: Optional[Union[URL, List[URL]]] = None
    legislationType: Optional[Union[CategoryCode, List[CategoryCode]]] = None
    legislationType: Optional[Union[Text, List[Text]]] = None
    legislationChanges: Optional[Union["Legislation", List["Legislation"]]] = None
