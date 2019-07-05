class Mem:
    def __init__(self, var_start, tmp_start):
        assert var_start < tmp_start, "variable space should be before temporary space"
        self.var = var_start
        self.tmp = tmp_start
        self.tmp_start = tmp_start
        self.type_dict = dict()

    def get_var(self, tp):
        self.type_dict[self.var] = tp
        self.var += 4
        if self.pointer >= self.tmp_start:
            raise Exception("Variable space is full.")
        return self.var - 4

    def get_tmp(self, tp):
        self.type_dict[self.tmp] = tp
        self.tmp += 4
        return self.tmp - 4

    def type_of(self, addr):
        return self.type_dict[addr]
