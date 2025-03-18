from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


class DrugCost(MedicalEntity):
    """
    The cost per unit of a medical drug. Note that this type is not meant to represent the price in an offer of a drug for sale; see the Offer type for that. This type will typically be used to tag wholesale or average retail cost of a drug, or maximum reimbursable cost. Costs of medical drugs vary widely depending on how and where they are paid for, so while this type captures some of the variables, costs should be used with caution by consumers of this schema's markup.
    """

    applicableLocation: Optional[
        Union["AdministrativeArea", List["AdministrativeArea"]]
    ] = None
    costOrigin: Optional[Union[str, List[str]]] = None
    costCurrency: Optional[Union[str, List[str]]] = None
    costCategory: Optional[Union["DrugCostCategory", List["DrugCostCategory"]]] = None
    costPerUnit: Optional[
        Union[
            str,
            List[str],
            float,
            List[float],
            "QualitativeValue",
            List["QualitativeValue"],
        ]
    ] = None
    drugUnit: Optional[Union[str, List[str]]] = None
