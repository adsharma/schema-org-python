from dataclasses import dataclass

from schema_models.local_business import LocalBusiness


@dataclass
class GovernmentOffice(LocalBusiness):
    """
    A government office&#x2014;for example, an IRS or DMV office.
    """
