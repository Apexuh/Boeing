import copy


class Boeing737:
    business_class = [[' '] + ['.' for _ in range(4)] + [' '] for _ in range(2)]
    economy_class = [['.' for _ in range(6)] for _ in range(18)]
    scheme_airplane = business_class + economy_class

    def print_scheme(self):
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

    def request_with_all_wishes(self, line):
        req = [i for i in line.split()]
        req_dict = {a: req.count(a) for a in req}
        req_dict_final = {}
        for i, v in req_dict.items():
            if v > 1:
                return 'Please input correct information'
            elif i.isnumeric():
                if 6 < int(i) or int(i) < 0:
                    return 'Please input correct information'
                else:
                    req_dict_final['count_of_buyers'] = int(i)
            elif i in ['left', 'right']:
                req_dict_final['side'] = i
            elif i in ['aisle', 'window']:
                req_dict_final['place'] = i
            if i == 'business':
                req_dict_final['business'] = 1
        if len(req_dict_final) == 0:
            return 'Please input correct information'
        return req_dict_final

    def seating(self, inp):
        # todo бизнес-класс. запрос на этапе ввода данных с предложением мест.
        request = self.request_with_all_wishes(inp)
        scheme = self.scheme_airplane
        print_scheme = self.print_scheme
        # print(request)
        if 'side' not in request and 'place' not in request:
            self.seating_only_places(request)


    def seating_only_places(self, count_of_buyers_list):
        """Только с указанным количеством мест."""
        # print(self.scheme_airplane)
        # print(count_of_buyers_list)
        count_of_buyers = count_of_buyers_list['count_of_buyers']
        if 'business' in count_of_buyers_list:
            range_of_rows = self.scheme_airplane[:2]
            index_place_plus = -1
            index_plus = 0
        else:
            range_of_rows = self.scheme_airplane[2:]
            index_place_plus = 0
            index_plus = 2
        buyers_list = ['.'] * count_of_buyers
        for index, row in enumerate(range_of_rows):
            if '.' in row:
                for index_place, place in enumerate(row):
                    if index_place != -count_of_buyers:
                        seats = row[index_place:index_place + count_of_buyers]
                        if seats == buyers_list:
                            row[index_place:index_place + count_of_buyers] = ['X'] * count_of_buyers
                            index_place_plus += index_place
                            index_plus += index
                            request_places = ' '.join([str(index_plus + 1) + chr(index_place_plus + i + 65) for i in range(count_of_buyers)])
                            return print(f'Find a seats: {request_places}')
        return print('Seats not found')

    def empty_seats(self):
        """Количество свободных мест по классам"""
        empty_seats_business = 0
        empty_seats_economy = 0
        for index_row, row in enumerate(self.scheme_airplane):
            for j in row:
                if j == '.' and index_row < 2:
                    empty_seats_business += 1
                elif j == '.' and index_row > 1:
                    empty_seats_economy += 1
        return print(f'''Empty places in our airplane: Business - {empty_seats_business}, Economy - {empty_seats_economy}.\nTotal - {empty_seats_economy + empty_seats_business}''')








# todo изучить вариант записи в nosql(или csv) для хранения наполненности салона


if __name__ == '__main__':
    boeing = Boeing737()
    # boeing.seating('2 left aisle')
    # boeing.print_scheme()
    # print(boeing.request_with_all_wishes('2 left aisle'))
    boeing.seating('2')
    boeing.seating('2')
    boeing.seating('business 2')
    for i in range(40):
        boeing.seating('3')
    boeing.print_scheme()
    boeing.empty_seats()

# boeing.print_scheme()
# [print(*i) for i in boeing.scheme_airplane]
# print(boeing.request_with_all_wishes('2 left left')) # Проверит если ввели повторные значения
# print(boeing.request_with_all_wishes('2 left aisle'))
