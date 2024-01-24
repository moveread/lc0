from typing import Annotated
import lczero.backends as lcz
from .uci import Uci, lcz2uci
from .backends import Backend, cached_backend
from .weights import MAIA_PATH

Prob = Annotated[float, 'probability']

def preds(game: lcz.GameState, y: lcz.Output) -> dict[Uci, Prob]:
    return {
        lcz2uci(pred): prob
        for pred, prob in zip(game.moves(), y.p_softmax(*game.policy_indices()))
    }

def eval(fens: list[str], weights_path: str = MAIA_PATH, backend: Backend = 'eigen') -> list[dict[Uci, Prob]]:
    """Given a batch of positions `fens`, returns a batch of dictionaries of uci moves to probabilities
    - e.g. `result[0] = { "g1f3": 0.4, "e2e4" : 0.5, ... }` (per each `fen` in `fens`)
    """
    bk = cached_backend(weights_path, backend=backend)
    games: list[lcz.GameState] = [lcz.GameState(fen) for fen in fens]
    X: list[lcz.Input] = [game.as_input(bk) for game in games]
    Y: list[lcz.Output] = bk.evaluate(*X)
    return [preds(game, y) for game, y in zip(games, Y)]