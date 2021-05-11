
#Кодирование строки "по Хаффману".

from collections import Counter, deque


class Coding():
    def __init__(self, string):
        self.s = string
        self.code = {}
        self._sort(self.s)

    def _sort(self, item):
        self.count = Counter(item)
        self.sort_item = deque(sorted(self.count.items(), key=lambda i: i[1]))
        self.res = self._processing(self.sort_item)
        self.created_tabs(self.res)

    def _processing(self, obj):
        if len(obj) != 1:
            weight = obj[0][1] + obj[1][1]
            comb = {0: obj.popleft()[0],
                    1: obj.popleft()[0]}
            for inx, el in enumerate(obj):
                if weight != el[1]:
                    continue
                else:
                    obj.insert(inx, (comb, weight))
                    break
            else:
                obj.append((comb, weight))
            return self._processing(obj)
        else:
            return obj[0][0]

    def created_tabs(self, item, code=''):
        if not isinstance(item, dict):
            self.code[item] = code
        else:
            self.created_tabs(item[0], code=f'{code}0')
            self.created_tabs(item[1], code=f'{code}1')

    def __str__(self):
        self.result = ''
        for el in self.s:
            self.result += str(self.code[el]) + ' '
        return self.result

    def decoding(self, item):
        check_list = item.split(' ')
        res = ''
        for char in check_list:
            for el in self.code.items():
                if char in el:
                    res += el[0]
        return res


s = "tic tac toe!"
a = Coding(s)
print(a.count)
print(a.code)
print(a)
print(a.decoding(str(a)))

"""
Вывод в консоли:
Counter({'t': 3, 'c': 2, ' ': 2, 'i': 1, 'a': 1, 'o': 1, 'e': 1, '!': 1})
{' ': '00', '!': '010', 'o': '0110', 'e': '0111', 't': '10', 'i': '1100', 'a': '1101', 'c': '111'}
10 1100 111 00 10 1101 111 00 10 0110 0111 010 
tic tac toe!


Итоги: интересный алгоритм и довольно простой в реализации и понимании. Однако подобный метод шифрования
не всегда хорош. Нашел информацию (в которой сам убедился на опытах), что кодирование по Хоффану не очень эффективно
для большого количества редких элементов в огромном объеме текста. Однако эффективно для работы с документами, изображениями и т.д.
"""
