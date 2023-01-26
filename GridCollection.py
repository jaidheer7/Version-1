from functools import cached_property

class Grid1:
    def __init__(self, **kwargs):
        try:
            self.__npgrid = kwargs['npgrid'] 
            self.__updateFunction = kwargs.get('updateFunction')
            self.__updateFunctionParameters = {}
            self.__updateFunctionParameters['fPath'] = kwargs['fPath']
            self.__updateFunctionParameters['zFactor'] = kwargs.get('zFactor', 1) 

            for (k, v) in kwargs.items():
                if k.startswith('ufp_') and len(k) > 4:
                    self.__updateFunctionParameters[k[4:]] = v
        except KeyError as ke:
            raise Exception('Missing main value', ke)

    def get(self, coordinates):
        return self.__npgrid[coordinates]

    def set(self, coordinates, value):

        self.__npgrid[coordinates] = value

        if self.__updateFunction is not None:
            return self.__updateFunction(self.__updateFunctionParameters)
        return None

    # @cached_property
    def getShape(self): 
        return self.__npgrid.shape