class Score:

    def __init__(self,data):
        items = data.split(',')
        self._no = int(items[0])
        self._name = items[1]
        self._kor = float(items[2])
        self._eng = float(items[3])
        self._math = float(items[4])

    @property
    def no(self):
        return self._no

    @property
    def name(self):
        return self._name

    @property
    def kor(self):
        return self._kor
    
    @property
    def eng(self):
        return self._eng
    
    @property
    def math(self):
        return self._math

    @property
    def sum(self):
        return self._kor+self._eng+self._math
    
    @property
    def avg(self):
        return round(self.sum/3,2)