import abc
class ClusterAlgorithm(object, metaclass=abc.ABCMeta):
    def __init__(self, params):
        assert isinstance(params, dict), "params must be a dictionary!"
        self.params = params

        #assert "X" in params, "X the features matrix must be in params"
        #self.X = float(None)#params["X"]

    def add_to_params(self, key, val):
        self.params.update({key: val})

    @abc.abstractmethod
    def run(self, plot=False):
        raise NotImplementedError('run must be implemented!')
