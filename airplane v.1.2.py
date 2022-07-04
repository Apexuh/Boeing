import copy


class Boeing737:
    business_class = [[' '] + ['.' for _ in range(4)] + [' '] for _ in range(2)]
    economy_class = [['.' for _ in range(6)] for _ in range(18)]
    scheme_airplane = business_class + economy_class

    @staticmethod
    def print_scheme():
        scheme = copy.deepcopy(Boeing737.scheme_airplane)
        for i in range(len(scheme)):
            scheme[i].insert(3, str(i + 1))
        scheme.insert(0, [' ', 'A', 'B', ' ', 'C', 'D', ' '])
        scheme.insert(3, ['A', 'B', 'C', ' ', 'D', 'E', 'F'])
        scheme.insert(10, ['#'] * 7)
        rotated = list(zip(*scheme))[::-1]
        for i in rotated:
            for j in i:
                j = j.rjust(2)
                print(j, end=' ')
            print()

    @staticmethod
    def request_with_all_wishes(line):
        req = [i for i in line.split()]
        req_dict = {a: req.count(a) for a in req}
        req_dict_final = {}
        for i, v in req_dict.items():
            if i.isnumeric() and 6 < int(i) < 0 or v > 1:
                return 'Please input correct information'
            elif i.isnumeric():
                req_dict_final['count_of_buyers'] = int(i)
            elif i in ['left', 'right']:
                req_dict_final['side'] = i
            elif i in ['aisle', 'window']:
                req_dict_final['place'] = i
        return req_dict_final

    def seating(self, inp):
        #todo написать функцию посадки пассажиров с рамдомным предложением мест
        # и в зависимости от того, насколько заявка полная. То есть если ввели: 2. Надо дать абсолютно рандомные 2 места
        #todo бизнес-класс. запрос на этапе ввода данных с предложением мест.
        #todo если количество мест > 3 , то предлагать варианты рассадки поблизости
        # (4 места: 3 места + 1 чререз проход в одном ряду или 3 места + 1 в другом. или 2 +2 по такому же принципу)

        request = self.request_with_all_wishes(inp)
        scheme = self.scheme_airplane
        print_scheme = self.print_scheme



#todo изучить вариант записи в nosql(или csv) для хранения наполненности салона









boeing = Boeing737()
# boeing.print_scheme()
# [print(*i) for i in boeing.scheme_airplane]
# print(boeing.request_with_all_wishes('2 left left')) # Проверить если ввели повторные значения
# print(boeing.request_with_all_wishes('2 left aisle'))


boeing.seating('2 left aisle')
