from dataclasses import dataclass

from schema_models.aggregate_rating import AggregateRating


@dataclass
class EmployerAggregateRating(AggregateRating):
    """
    An aggregate rating of an Organization related to its role as an employer.
    """
