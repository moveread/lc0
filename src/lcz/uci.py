from typing import Annotated

Uci = Annotated[str, 'uci']

def lcz2uci(lcz_uci: str) -> Uci:
    """The lcz people have decided to encode castles as `e1h1, e8h8, e1a1, e8a8`, so we gotta fix it to `e1g1, e8g8, e1c1, e8c8`"""
    match lcz_uci:
        case "e1h1":
            return "e1g1"
        case "e8h8":
            return "e8g8"
        case "e1a1":
            return "e1c1"
        case "e8a8":
            return "e8c8"
        case uci:
            return uci