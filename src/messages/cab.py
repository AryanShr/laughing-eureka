from uagents import Model
from enum import Enum
from typing import Optional, List
from pydantic import Field

class Cab(Model):
  from_address: str = Field(description="Describes the address where user wants to start the activity from. For example: 123 Main Street, London")
  to_address: str = Field(description="Describes the address where user wants to go to. For example: 123 Main Street, London")
  time: str = Field(description="Describes the time when user wants to start the activity. For example: 10:00 AM")
  date: str = Field(description="Describes the date when user wants to start the activity. For example: 10/10/2020")
  passengers: int = Field(description="Describes the number of passengers. For example: 2")