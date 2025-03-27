from dataclasses import dataclass

from schema_models.organization import Organization


@dataclass
class WorkersUnion(Organization):
    """
    A Workers Union (also known as a Labor Union, Labour Union, or Trade Union) is an organization that promotes the interests of its worker members by collectively bargaining with management, organizing, and political lobbying.
    """
