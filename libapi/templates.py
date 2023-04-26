from __future__ import annotations

from urllib.parse import quote

reserved_characters = 0x21232425262728292A2B2C2F3A3B3D3F405B5D.to_bytes(19, 'big')


def pct_encode(a: str, reserved_expansion=False) -> str:
    '''
    Percent-Encoding based on RFC 3986
    https://datatracker.ietf.org/doc/html/rfc3986#section-2.1
    '''
    return quote(a, safe=reserved_characters if reserved_expansion else b'', encoding='utf-8', errors='replace')


class URITemplate(str):
    '''
    RFC 6570 URI Template
    https://datatracker.ietf.org/doc/html/rfc6570
    '''

    def __new__(cls, a: str) -> URITemplate:
        this = super().__new__(cls, a)
        return this
