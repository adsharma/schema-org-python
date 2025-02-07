from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity
from schema_models.number import Number
from schema_models.text import Text


class DrugCost(MedicalEntity):
    applicableLocation: Optional[
        Union["AdministrativeArea", List["AdministrativeArea"]]
    ] = None
    costOrigin: Optional[Union[Text, List[Text]]] = None
    costCurrency: Optional[Union[Text, List[Text]]] = None
    costCategory: Optional[Union["DrugCostCategory", List["DrugCostCategory"]]] = None
    costPerUnit: Optional[Union[Text, List[Text]]] = None
    costPerUnit: Optional[Union[Number, List[Number]]] = None
    costPerUnit: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    drugUnit: Optional[Union[Text, List[Text]]] = None
