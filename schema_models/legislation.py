from dataclasses import dataclass
from datetime import date
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.person import Person


@dataclass
class Legislation(CreativeWork):
    """
    A legal document such as an act, decree, bill, etc. (enforceable or not) or a component of a legal act (like an article).
    """

    jurisdiction: Optional[
        Union["AdministrativeArea", List["AdministrativeArea"], str, List[str]]
    ] = None
    legislationAmends: Optional[Union["Legislation", List["Legislation"]]] = None
    legislationApplies: Optional[Union["Legislation", List["Legislation"]]] = None
    legislationChanges: Optional[Union["Legislation", List["Legislation"]]] = None
    legislationCommences: Optional[Union["Legislation", List["Legislation"]]] = None
    legislationConsolidates: Optional[Union["Legislation", List["Legislation"]]] = None
    legislationCorrects: Optional[Union["Legislation", List["Legislation"]]] = None
    legislationCountersignedBy: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    legislationDate: Optional[Union[date, List[date]]] = None
    legislationDateOfApplicability: Optional[Union[date, List[date]]] = None
    legislationDateVersion: Optional[Union[date, List[date]]] = None
    legislationEnsuresImplementationOf: Optional[
        Union["Legislation", List["Legislation"]]
    ] = None
    legislationIdentifier: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = (
        None
    )
    legislationJurisdiction: Optional[
        Union["AdministrativeArea", List["AdministrativeArea"], str, List[str]]
    ] = None
    legislationLegalForce: Optional[
        Union["LegalForceStatus", List["LegalForceStatus"]]
    ] = None
    legislationPassedBy: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    legislationRepeals: Optional[Union["Legislation", List["Legislation"]]] = None
    legislationResponsible: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    legislationTransposes: Optional[Union["Legislation", List["Legislation"]]] = None
    legislationType: Optional[
        Union["CategoryCode", List["CategoryCode"], str, List[str]]
    ] = None
