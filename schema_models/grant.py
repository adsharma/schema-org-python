from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.bio_chem_entity import BioChemEntity
from schema_models.creative_work import CreativeWork
from schema_models.event import Event
from schema_models.intangible import Intangible
from schema_models.medical_entity import MedicalEntity
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.product import Product


class Grant(Intangible):
    sponsor: Optional[Union[Person, List[Person]]] = None
    sponsor: Optional[Union[Organization, List[Organization]]] = None
    funder: Optional[Union[Person, List[Person]]] = None
    funder: Optional[Union[Organization, List[Organization]]] = None
    fundedItem: Optional[Union[Person, List[Person]]] = None
    fundedItem: Optional[Union[Organization, List[Organization]]] = None
    fundedItem: Optional[Union[BioChemEntity, List[BioChemEntity]]] = None
    fundedItem: Optional[Union[Event, List[Event]]] = None
    fundedItem: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
    fundedItem: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    fundedItem: Optional[Union[Product, List[Product]]] = None
