from score import Score

class ScoreManagementSystem:
    def __init__(self):
        self._score={}

    def read(self, score_data_file):
        if self._score != None :
            self._score={}
        
        with open(score_data_file, 'rt', encoding='utf-8') as fo:
            data =fo.read()
            lines = data.strip().split('\n')

        num = 0
        for line in lines:
            num += 1
            self._score[num] = Score(line.strip())
        return len(self._score)