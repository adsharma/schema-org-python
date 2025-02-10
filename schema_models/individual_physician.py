from typing import List, Optional, Union

from schema_models.medical_organization import MedicalOrganization
from schema_models.physician import Physician


class IndividualPhysician(Physician):
    """
    An individual medical practitioner. For their official address use [[address]], for affiliations to hospitals use [[hospitalAffiliation]].
    The [[practicesAt]] property can be used to indicate [[MedicalOrganization]] hospitals, clinics, pharmacies etc. where this physician practices.
    """

    practicesAt: Optional[Union[MedicalOrganization, List[MedicalOrganization]]] = None
