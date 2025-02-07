from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_validator, ConfigDict, Field, HttpUrl
from schema_models.user_interaction import UserInteraction


class UserTweets(UserInteraction):
    pass
