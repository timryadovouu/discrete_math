import itertools


class TableKeli:
    def __init__(self, operation, data):
        """На вход операция и список чисел"""
        self.operation = operation
        self.data = data
        self.table = [[(self.data[i] + self.data[j]) % 5 for j in range(len(self.data))] for i in
                      range(len(self.data))]  # условие: свое
        # self.table = [[eval(f"{self.data[j]}{self.operation}{self.data[i]}") for j in range(len(self.data))] for i in
        #               range(len(self.data))]  # условие: a*b=a{операция}b
        self.flag_a = False
        self.flag_c = False
        self.ne = None
        self.ie = None

    def __str__(self):
        return f"Operation: {self.operation}\nData(set): {self.data}"

    def __repr__(self):
        return "\n".join(["".join([str(item).rjust(4) for item in line]) for line in
                          [[self.operation, *self.data]] + [[self.data[i]] + self.table[i] for i in
                                                            range(len(self.table))]])

    @property
    def commutativity(self):
        self.flag_c = all(
            self.table[i][j] == self.table[j][i] for i in range(len(self.table)) for j in range(len(self.table[i])))
        return f"Commutativity check: {self.flag_c}"

    @property
    def associativity(self):
        self.flag_a = [eval(f"({tpl[0]}{self.operation}{tpl[1]}){self.operation}{tpl[2]}")
                       ==
                       eval(f"{tpl[0]}{self.operation}({tpl[1]}{self.operation}{tpl[2]})")
                       for tpl in itertools.combinations(self.data, r=3)]
        return f"Associativity check: {all(self.flag_a)}"

    @property
    def neutral_element(self):
        # print(self.table)
        cols = [[line[i] for line in self.table] for i in range(len(self.table))]
        for i in range(len(self.table)):
            if self.table[i] == self.data and cols[i] == self.data:
                self.ne = self.table[i][i]
        return f"Neutral element: {self.ne}"

    @property
    def inverse_element(self):
        if self.ne is not None:
            cols = [[line[i] for line in self.table] for i in range(len(self.table))]
            self.ie = all(self.ne in line for line in self.table) and all(self.ne in line for line in cols)
        return f"Inverse element exists for all elements: {self.ie}"

    @property
    def normal_subgroups(self):
        all_sg = []
        res = []
        for r_i in range(1, len(self.data) + 1):
            [all_sg.append(lst) for lst in map(list, itertools.combinations(self.data, r=r_i))]
        for H in all_sg:
            if all(x * h * (-x) in H for h in H for x in self.data):
                res.append(H)
        return res


# test = TableKeli(input("Ведите операцию: "), list(map(int, input("Введите данные: ").split())))
test = TableKeli("+", [0, 1, 2, 3, 4])

print(test)
print(repr(test))
print(test.commutativity)
print(test.associativity)
print(test.neutral_element)
print(test.inverse_element)
print(test.normal_subgroups)
