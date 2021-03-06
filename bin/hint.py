try:
    import binutil  # required to import from dreamcoder modules
except ModuleNotFoundError:
    import bin.binutil  # alt import if called as module

from dreamcoder.domains.hint.main import main, list_options
from dreamcoder.dreamcoder import commandlineArguments
from dreamcoder.utilities import numberOfCPUs


if __name__ == '__main__':
    args = commandlineArguments(
        enumerationTimeout=1000, activation='tanh', iterations=20, recognitionTimeout=3600,
        a=3, maximumFrontier=15, topK=2, pseudoCounts=30.0,
        helmholtzRatio=0.5, structurePenalty=1.,
        CPUs=numberOfCPUs(),
        extras=list_options)
    main(args)
