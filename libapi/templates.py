from __future__ import annotations

from urllib.parse import quote


def pct_encode(a: str) -> str:
    '''
    Percent-Encoding based on RFC 3986
    https://datatracker.ietf.org/doc/html/rfc3986#section-2.1
    '''
    return quote(a, safe='', encoding='utf-8', errors='replace')


class URITemplate:
    '''
    RFC 6570 URI Template
    https://datatracker.ietf.org/doc/html/rfc6570
    '''

    pass
