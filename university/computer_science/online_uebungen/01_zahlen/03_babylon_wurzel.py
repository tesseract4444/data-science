def babylonian_root(number: float, count: int) -> float:
        if not isinstance(count, int):
            raise Exception('count muss ein Integer sein!!!')

        if count < 0:
            raise Exception('Die Zahl für count muss größer als 0 sein!')

        if not isinstance(number, int):
            raise Exception('Die Zahl für number muss ein Integer oder float sein')

        if number <= 0:
            raise Exception('Die Zahl für number muss größer als 0 sein!')

        sqr: float = number

        for i in range(count): #count < 3 => 2
            sqr = 1/2 * (sqr + (number / sqr))

        return sqr

print(babylonian_root(3,2))
'''
sqr(1) = 0.5 * (1 + 3/1) = 0.5 * 4 = 2.0 = neues sqr        #count = 1
neues sqr = 0.5 * (2.0 + 3/2) = 0.5 * 3.5 = 1.75            #count = 2
'''