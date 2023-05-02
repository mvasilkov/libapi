from __future__ import annotations


def escape(a: str) -> str:
    '''
    Escape a JSON Pointer (RFC 6901) reference token.
    '''
    return a.replace('~', '~0').replace('/', '~1')


def unescape(a: str) -> str:
    '''
    Unescape a JSON Pointer (RFC 6901) reference token.
    '''
    return a.replace('~1', '/').replace('~0', '~')
