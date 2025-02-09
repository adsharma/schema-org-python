from typing import List, Optional, Union

from schema_models.medical_risk_estimator import MedicalRiskEstimator


class MedicalRiskScore(MedicalRiskEstimator):
    algorithm: Optional[Union[str, List[str]]] = None
