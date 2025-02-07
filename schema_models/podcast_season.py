from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_validator, ConfigDict, Field, HttpUrl
from schema_models.creative_work_season import CreativeWorkSeason


class PodcastSeason(CreativeWorkSeason):
    pass
