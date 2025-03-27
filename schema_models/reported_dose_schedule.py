from dataclasses import dataclass

from schema_models.dose_schedule import DoseSchedule


@dataclass
class ReportedDoseSchedule(DoseSchedule):
    """
    A patient-reported or observed dosing schedule for a drug or supplement.
    """
