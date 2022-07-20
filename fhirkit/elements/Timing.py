from datetime import datetime
from typing import Optional, Sequence, Union

from pydantic import PositiveInt, validator
from fhirkit.elements import (
    BackboneElement,
    CodeableConcept,
    Duration,
    Element,
    Period,
    Range,
)
from fhirkit.primitive_datatypes import dateTime, decimal, Code
from fhirkit.choice_type import deterimine_choice_type


class TimingRepeat(Element):
    bounds: Optional[Union[Duration, Range, Period]] = None

    @validator("bounds", pre=True, always=True, allow_reuse=True)
    def validate_bounds(cls, value, values, field):
        return deterimine_choice_type(cls, value, values, field)

    count: Optional[PositiveInt] = None
    countMax: Optional[PositiveInt] = None
    duration: Optional[decimal] = None
    durationMax: Optional[decimal] = None
    durationUnit: Optional[Code] = None
    frequency: Optional[PositiveInt] = None
    frequencyMax: Optional[PositiveInt] = None
    period: Optional[decimal] = None
    periodMax: Optional[decimal] = None
    periodUnit: Optional[Code] = None
    dayOfWeek: Sequence[Code] = []
    timeOfDay: Sequence[Code] = []
    when: Sequence[Code] = []


TimingRepeat.update_forward_refs()


class Timing(BackboneElement):
    event: Sequence[datetime] = []
    repeat: Optional[TimingRepeat] = None
    code: Optional[CodeableConcept] = None


Timing.update_forward_refs()
