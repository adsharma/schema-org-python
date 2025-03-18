from typing import List, Optional, Union

from schema_models.bio_chem_entity import BioChemEntity
from schema_models.creative_work import CreativeWork
from schema_models.event import Event
from schema_models.intangible import Intangible
from schema_models.medical_entity import MedicalEntity
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.product import Product


class Grant(Intangible):
    """
    A grant, typically financial or otherwise quantifiable, of resources. Typically a [[funder]] sponsors some [[MonetaryAmount]] to an [[Organization]] or [[Person]],
        sometimes not necessarily via a dedicated or long-lived [[Project]], resulting in one or more outputs, or [[fundedItem]]s. For financial sponsorship, indicate the [[funder]] of a [[MonetaryGrant]]. For non-financial support, indicate [[sponsor]] of [[Grant]]s of resources (e.g. office space).

    Grants support  activities directed towards some agreed collective goals, often but not always organized as [[Project]]s. Long-lived projects are sometimes sponsored by a variety of grants over time, but it is also common for a project to be associated with a single grant.

    The amount of a [[Grant]] is represented using [[amount]] as a [[MonetaryAmount]].

    """

    sponsor: Optional[Union[Person, List[Person], Organization, List[Organization]]] = (
        None
    )
    funder: Optional[Union[Person, List[Person], Organization, List[Organization]]] = (
        None
    )
    fundedItem: Optional[
        Union[
            Person,
            List[Person],
            Organization,
            List[Organization],
            BioChemEntity,
            List[BioChemEntity],
            Event,
            List[Event],
            MedicalEntity,
            List[MedicalEntity],
            CreativeWork,
            List[CreativeWork],
            Product,
            List[Product],
        ]
    ] = None
