from schema_models.dose_schedule import DoseSchedule


class MaximumDoseSchedule(DoseSchedule):
    """
    The maximum dosing schedule considered safe for a drug or supplement as recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.
    """
