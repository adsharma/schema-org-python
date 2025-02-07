from typing import List, Optional, Union

from schema_models.medical_risk_estimator import MedicalRiskEstimator
from schema_models.text import Text


class MedicalRiskScore(MedicalRiskEstimator):
    algorithm: Optional[Union[Text, List[Text]]] = None
