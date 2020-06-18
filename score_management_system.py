from score import Score

def key_rank(item):
    return item[1].sum
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

    def _make_cars_string(self, score,order_key,order_way):
        result = ""
        temp_sum=0
        if order_way== 'asc':
            num =1
        elif order_way=='des':
            num = len(score)
        
        for key, item in score:
            result = result + str(item.no) +','
            result = result + item.name +','
            result = result +str(int(item.kor)) +','
            result = result + str(int(item.eng)) +','
            result = result + str(int(item.math)) + ','
            result = result + str(int(item.sum)) + ','
            if item.avg % 1 >0 :
                result = result + str(round(item.avg,2)) + ','
            elif item.avg % 1 ==0:
                result = result + str(int(item.avg)) + ','
            
            if item.sum!=temp_sum:
                same_num = num

            if order_key =='register':
                result = result + str(key) + '\n'
            elif order_way== 'asc':
                result = result + str(same_num) + '\n'
                num +=1
            elif order_way== 'des':
                result = result + str(same_num) + '\n'
                num -=1

            temp_sum = item.sum
            temp_num = num
            
        return result.strip()
    


    def sort(self, order_key="register", order_way = "asc"):
        if order_key == "register" and order_way == "asc":
            sorted_score = sorted(self._score.items())
        elif order_key == "register" and order_way == "des":
            sorted_score = sorted(self._score.items() , reverse = True)
        elif order_key == "rank" and order_way == "asc":
            sorted_score = sorted(self._score.items(),key = key_rank, reverse = True)
        elif order_key == "rank" and order_way == "des":
            sorted_score = sorted(self._score.items(),key = key_rank )

        result = self._make_cars_string(sorted_score,order_key,order_way)
        return result

    def write(self,file_name,order_key='register',order_way='asc'):
        with open(file_name, 'wt', encoding= 'utf-8') as fo:
            result = self.sort(order_key,order_way)
            fo.write(result)
