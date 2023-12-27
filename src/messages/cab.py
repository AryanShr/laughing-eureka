from uagents import Model
from enum import Enum
from typing import Optional, List
from pydantic import Field

class Cab(Model):
    distance_from_source: int = Field(description="The distance from the source location to the destination location.")
    distance_for_travel: int = Field(description="The distance that the user is willing to travel to reach the destination.")

class CabSelection(Model):
    is_available: bool = Field(description="The field expresses whether the cab is available or not.")
    fare: int = Field(description="The fare of the cab.")
    arrival_time: int = Field(description="The time taken by the cab to reach the user.")