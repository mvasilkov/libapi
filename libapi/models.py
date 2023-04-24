from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class DescriptionLanguage(StrEnum):
    OpenAPI = 'OpenAPI'
    'OpenAPI Specification'
    RAML = 'RAML'
    'RESTful API Modeling Language'


@dataclass
class APISpecification:
    spec_language: DescriptionLanguage
    spec_language_version: str

    title: str | None
