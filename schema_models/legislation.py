from datetime import date
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.administrative_area import AdministrativeArea
from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.person import Person


class Legislation(CreativeWork):
    """
    A legal document such as an act, decree, bill, etc. (enforceable or not) or a component of a legal act (like an article).
    """

    legislationTransposes: Optional[Union["Legislation", List["Legislation"]]] = None
    legislationPassedBy: Optional[Union[Person, List[Person]]] = None
    legislationPassedBy: Optional[Union[Organization, List[Organization]]] = None
    legislationLegalForce: Optional[
        Union["LegalForceStatus", List["LegalForceStatus"]]
    ] = None
    jurisdiction: Optional[Union[str, List[str]]] = None
    jurisdiction: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    legislationJurisdiction: Optional[Union[str, List[str]]] = None
    legislationJurisdiction: Optional[
        Union[AdministrativeArea, List[AdministrativeArea]]
    ] = None
    legislationConsolidates: Optional[Union["Legislation", List["Legislation"]]] = None
    legislationResponsible: Optional[Union[Person, List[Person]]] = None
    legislationResponsible: Optional[Union[Organization, List[Organization]]] = None
    legislationDateVersion: Optional[Union[date, List[date]]] = None
    legislationApplies: Optional[Union["Legislation", List["Legislation"]]] = None
    legislationDate: Optional[Union[date, List[date]]] = None
    legislationIdentifier: Optional[Union[str, List[str]]] = None
    legislationIdentifier: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    legislationType: Optional[Union["CategoryCode", List["CategoryCode"]]] = None
    legislationType: Optional[Union[str, List[str]]] = None
    legislationChanges: Optional[Union["Legislation", List["Legislation"]]] = None
