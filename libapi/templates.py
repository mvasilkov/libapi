from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import re
from typing import Any
from urllib.parse import quote

__all__ = ['pct_encode', 'URITemplate']

# TODO RFC 6570 Reserved Expansion only accepts % in pct-encoded triplets
reserved_characters = 0x21232425262728292A2B2C2F3A3B3D3F405B5D.to_bytes(19, 'big')

# Accept zero-length variables. This is not in the RFC
expression_pattern = re.compile(r'\{([+#]?)(.*?)\}')


def pct_encode(a: str, reserved_expansion=False) -> str:
    '''
    Percent-Encoding based on RFC 3986
    https://datatracker.ietf.org/doc/html/rfc3986#section-2.1
    '''
    return quote(a, safe=reserved_characters if reserved_expansion else b'', encoding='utf-8', errors='replace')


@dataclass
class Variable:
    operator: str
    start: int
    end: int


class URITemplate(str):
    '''
    RFC 6570 URI Template (Levels 1 and 2)
    https://datatracker.ietf.org/doc/html/rfc6570
    '''

    variables: defaultdict[str, list[Variable]]

    def __new__(cls, a: str) -> URITemplate:
        self = super().__new__(cls, a)

        self.variables = defaultdict(list)

        for exp in expression_pattern.finditer(self):
            operator = exp.group(1)
            variable = exp.group(2)
            start, end = exp.span()
            self.variables[variable].append(Variable(operator, start, end))

        return self

    def expand(self, values: dict[str, Any]) -> str:
        pass
