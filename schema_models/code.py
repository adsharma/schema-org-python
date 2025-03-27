from dataclasses import dataclass

from schema_models.creative_work import CreativeWork


@dataclass
class Code(CreativeWork):
    """
    Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates.
    """
