from __future__ import annotations

import re
from urllib.parse import quote

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


class URITemplate(str):
    '''
    RFC 6570 URI Template (Levels 1 and 2)
    https://datatracker.ietf.org/doc/html/rfc6570
    '''

    def __new__(cls, a: str) -> URITemplate:
        this = super().__new__(cls, a)
        return this
