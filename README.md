# LC0

> Simplified LC0 with Python

Provides a simple interface around the original [LCZero python bindings](https://github.com/LeelaChessZero/lc0)

## Usage

````python
import lcz

lcz.eval(fens=[
    'rnbqkbnr/pp2pppp/2p5/3p4/3PP3/8/PPP2PPP/RNBQKBNR w KQkq - 0 3',
    'r2qkbnr/pp2pppp/2n5/3p1b2/3P1B2/5N2/PPP2PPP/RN1QKB1R w KQkq - 4 6'
], weights_path='/path/to/lcz.pb.gz') # if not specified, uses the pre-packaged 'maia-1900.pb.gz'

# [{'b1d2': 0.008045054972171783, # [0, 1] probabilities (softmaxed)
#   'b1a3': 5.8913348766509444e-05,
#   'b1c3': 0.21684584021568298,
#    ...
#   },
#   {'b1d2': 0.015918008983135223,
#    'b1a3': 0.0013550063595175743,
#    'b1c3': 0.09632844477891922,
#    ...
#   }]

```