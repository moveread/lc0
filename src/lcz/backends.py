from typing import Annotated
from functools import cache
import lczero.backends as lcz

Backend = Annotated[str, 'backend']
@cache
def cached_backend(weights_path: str, backend: Backend = 'eigen') -> lcz.Backend:
    w = lcz.Weights(weights_path)
    return lcz.Backend(weights=w, backend=backend)

def available_backends() -> list[Backend]:
    return lcz.Backend.available_backends()