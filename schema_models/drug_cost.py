from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


class DrugCost(MedicalEntity):
    applicableLocation: Optional[
        Union["AdministrativeArea", List["AdministrativeArea"]]
    ] = None
    costOrigin: Optional[Union[str, List[str]]] = None
    costCurrency: Optional[Union[str, List[str]]] = None
    costCategory: Optional[Union["DrugCostCategory", List["DrugCostCategory"]]] = None
    costPerUnit: Optional[Union[str, List[str]]] = None
    costPerUnit: Optional[Union[float, List[float]]] = None
    costPerUnit: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    drugUnit: Optional[Union[str, List[str]]] = None
