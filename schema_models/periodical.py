from dataclasses import dataclass

from schema_models.creative_work_series import CreativeWorkSeries


@dataclass
class Periodical(CreativeWorkSeries):
    """
    A publication in any medium issued in successive parts bearing numerical or chronological designations and intended to continue indefinitely, such as a magazine, scholarly journal, or newspaper.

    See also [blog post](https://blog.schema.org/2014/09/02/schema-org-support-for-bibliographic-relationships-and-periodicals/).
    """
