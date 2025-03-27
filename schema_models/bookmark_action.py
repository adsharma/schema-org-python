from dataclasses import dataclass

from schema_models.organize_action import OrganizeAction


@dataclass
class BookmarkAction(OrganizeAction):
    """
    An agent bookmarks/flags/labels/tags/marks an object.
    """
