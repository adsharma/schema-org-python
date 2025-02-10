from typing import List, Optional, Union

from schema_models.medical_risk_estimator import MedicalRiskEstimator


class MedicalRiskScore(MedicalRiskEstimator):
    """
    A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score.
    """

    algorithm: Optional[Union[str, List[str]]] = None
