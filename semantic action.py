from enum import Enum

name = "if"
inp = "dummy"


errors = {
    'No Void Main Function Error.',
    'Illegal type error.',
    'ID is not fine',
    'Value error, value not found.'
}


class VariableType(Enum):
    BOOLEAN = "BOOLEAN"
    INT = "INT"
    CLASS = "CLASS"
    METHOD = "METHOD"
    NONE = "NONE"


class ErrorType(Enum):
    Semantic = "SEMANTIC"
    Pars = "PARS"


class Stack:
    def __init__(self):
        self.list = []

    def push(self, a):
        self.list.append(a)

    def pop(self, i):
        self.list = self.list[:-i]

    def top(self):
        return len(self.list) - 1


stack = Stack()

PB = []
i = 0


class Operator:
    def __init__(self, name, arg1, arg2, arg3):
        self.name = name
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3


<<<<<<< HEAD
def findaddr(inp):
    pass


def gettemp():
    pass


if name == 'pid':
     p = findaddr(inp)
     stack.push(p)

if name == 'add':
    t = gettemp()
    PB[i] = Operator("add", ('', stack.list[stack.top()]), ('', stack.list[stack.top() - 1]), ('',t))
    i = i + 1
    stack.pop(2)
    stack.push(t)

if name == 'sub':
    t = gettemp()
    PB[i] = Operator("sub", ('', stack.list[stack.top()]), ('', stack.list[stack.top() - 1]), ('', t))
    i = i + 1
    stack.pop(2)
    stack.push(t)

if name == 'mult':
    t = gettemp()
    PB[i] = Operator("mult", ('', stack.list[stack.top()]), ('', stack.list[stack.top() - 1]), ('', t))
    i = i + 1
    stack.pop(2)
    stack.push(t)

if name == 'equal':
    t = gettemp()
    PB[i] = Operator("eq", ('', stack.list[stack.top()]), ('', stack.list[stack.top() - 1]), ('', t))
    i = i + 1
    stack.pop(2)
    stack.push(t)

if name == 'less':
    t = gettemp()
    PB[i] = Operator("lt", ('', stack.list[stack.top()]), ('', stack.list[stack.top() - 1]), ('', t))
    i = i + 1
    stack.pop(2)
    stack.push(t)

if name == 'not':
    t = gettemp()
    PB[i] = Operator("lt", ('', stack.list[stack.top()]), ('', t), None)
    i = i + 1
    stack.pop(1)
    stack.push(t)

if name == 'assign':
    PB[i] = Operator("assign", ('', stack.list[stack.top()]), ('', stack.list[stack.top() - 1]), None)
    i = i + 1
    stack.pop(2)

if name == 'save':
    stack.push(i)
    i = i +1

if name == 'while':
    PB[stack.list[stack.top()]] = Operator("jpf", ('', stack.list[stack.top() - 1]), ('#', i + 1), None)
    PB[i] = Operator("jp", ('', stack.list[stack.top() - 2]), None, None)
    i = i + 1
    stack.pop(3)


if name == 'jpf_save':
    PB[stack.list[stack.top()]] = Operator('jpf', ('', stack.list[stack.top() - 1]), ('#', i + 1), None)
    stack.pop(2)
    stack.push(i)
    i = i + 1

if name == 'jp':
    PB[stack.list[stack.top()]] = Operator('jp', ('#', i), None, None)
    stack.pop(1)
    i = i + 1

if name == 'jp2':
    PB[stack.list[stack.top() - 1]] = Operator('jp', ('#', i), None, None)
    s = stack.list[-1]
    stack.pop(2)
    stack.push(s)
    i = i + 1

if name == 'jpf':
    PB[stack.list[stack.top()]] = Operator('jpf', ('', stack.list[stack.top() - 1]), ('#', i), None)
    stack.pop(2)
=======
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


mem = Mem(0, 1000)


class Semantic:
    def __init__(self):
        self.i = 0

    def pid(self):
        p = mem.get_var(inp)
        stack.push(p)

    def add(self):
        t = mem.get_tmp()
        PB[i] = Operator(
            "add",
            ("", stack.list[stack.top()]),
            ("", stack.list[stack.top() - 1]),
            ("", t),
        )
        self.i += 1
        stack.pop(2)
        stack.push(t)

    def sub(self):
        t = mem.get_tmp()
        PB[i] = Operator(
            "sub",
            ("", stack.list[stack.top()]),
            ("", stack.list[stack.top() - 1]),
            ("", t),
        )
        self.i += 1
        stack.pop(2)
        stack.push(t)

    def mult(self):
        t = mem.get_tmp()
        PB[i] = Operator(
            "mult",
            ("", stack.list[stack.top()]),
            ("", stack.list[stack.top() - 1]),
            ("", t),
        )
        self.i += 1
        stack.pop(2)
        stack.push(t)

    def equal(self):
        t = mem.get_tmp()
        PB[i] = Operator(
            "eq",
            ("", stack.list[stack.top()]),
            ("", stack.list[stack.top() - 1]),
            ("", t),
        )
        self.i += 1
        stack.pop(2)
        stack.push(t)

    def less(self):
        t = mem.get_tmp()
        PB[i] = Operator(
            "lt",
            ("", stack.list[stack.top()]),
            ("", stack.list[stack.top() - 1]),
            ("", t),
        )
        self.i += 1
        stack.pop(2)
        stack.push(t)

    def nott(self):
        t = mem.get_tmp()
        PB[i] = Operator("lt", ("", stack.list[stack.top()]), ("", t), None)
        self.i += 1
        stack.pop(1)
        stack.push(t)

    def assign(self):
        PB[i] = Operator(
            "assign",
            ("", stack.list[stack.top()]),
            ("", stack.list[stack.top() - 1]),
            None,
        )
        self.i += 1
        stack.pop(2)

    def save(self):
        stack.push(i)
        self.i += 1

    def whilee(self):
        PB[stack.list[stack.top()]] = Operator(
            "jpf", ("", stack.list[stack.top() - 1]), ("#", i + 1), None
        )
        PB[i] = Operator("jp", ("", stack.list[stack.top() - 2]), None, None)
        self.i += 1
        stack.pop(3)

    def jpf_save(self):
        PB[stack.list[stack.top()]] = Operator(
            "jpf", ("", stack.list[stack.top() - 1]), ("#", i + 1), None
        )
        stack.pop(2)
        stack.push(i)
        self.i += 1

    def jp(self):
        PB[stack.list[stack.top()]] = Operator("jp", ("#", i), None, None)
        stack.pop(1)
        self.i += 1

    def jpf(self):
        PB[stack.list[stack.top()]] = Operator(
            "jpf", ("", stack.list[stack.top() - 1]), ("#", i), None
        )
        stack.pop(2)

    def set_local_search(self, current_token):
        self.symbol_table.local_search = True

    def reset_local_search(self, current_token):
        self.symbol_table.local_search = False

    def remove_last(self, current_token):
        self.semantic_stack.pop(1)

    def remove_prev(self, current_token):
        tmp = self.semantic_stack[-1]
        self.semantic_stack.pop(2)
        self.semantic_stack.push(tmp)

    def identifier(self, current_token):
        if self.symbol_table.local_search:
            # we know type of current token, we have already define this variable in this scope
            if current_token[1].tp is not None:
                self.error_handler.rasie_error(
                    ErrorType.Semantic,
                    "A variable or method by name {} is already define in the scope".format(
                        current_token[1].name
                    ),
                )
            else:
                current_token[1].tp = self.semantic_stack.top()
                self.semantic_stack.pop()

                if current_token[1].tp is VariableType.METHOD:
                    current_token[1].return_type = self.semantic_stack.top()
                    current_token[1].return_address = (
                        self.memory_manager.saved_pc_address + self.method_cnt * 4
                    )
                    self.method_cnt = self.method_cnt + 1
                    self.semantic_stack.pop()

                if (
                    current_token[1].tp is not VariableType.CLASS
                    and current_token[1].tp is not VariableType.METHOD
                ):
                    current_token[1].address = self.memory_manager.get_variable(
                        current_token[1].tp
                    )

                if current_token[1].tp is VariableType.METHOD:
                    current_token[1].address = self.memory_manager.get_variable(
                        current_token[1].return_type
                    )

        else:
            # we don't know type of current token, we didn't define this variable in this scope
            if current_token[1] is None:
                self.error_handler.rasie_error(
                    ErrorType.Semantic, "Can not resolve symbol @"
                )

    def add_row(self, current_token):
        self.semantic_stack.push(0)

    def identifier_parameter(self, current_token):
        identifier = self.semantic_stack[-1]
        number = self.semantic_stack[-2]
        self.semantic_stack.pop(2)
        self.semantic_stack.push(identifier)
        self.semantic_stack.push(number + 1)

    def end_parameter(self, current_token):
        current_line = self.semantic_stack.top()
        self.semantic_stack.pop(1)

        number = self.semantic_stack.top()
        self.semantic_stack.pop()
        ls = []

        for i in range(number):
            ls.append(self.semantic_stack[-1].address)

            self.semantic_stack.pop(1)

        self.semantic_stack.top().parameters = list(reversed(ls))
        self.semantic_stack.top().line = current_line

    def create_extend(self, current_token):
        self.symbol_table.extend_flag = True

    def start_scope(self, current_token):
        self.symbol_table.start_scope(current_token[1].name)

    def end_scope(self, current_token):
        self.symbol_table.end_scope()

    def identifier_int(self, current_token):
        self.semantic_stack.push(VariableType.INT)

    def identifier_boolean(self, current_token):
        self.semantic_stack.push(VariableType.BOOLEAN)

    def identifier_method(self, current_token):
        self.semantic_stack.push(VariableType.METHOD)

    def identifier_class(self, current_token):
        self.semantic_stack.push(VariableType.CLASS)

    def set_search_scope(self, current_token):
        self.semantic_stack.push(self.symbol_table.current)
        self.symbol_table.current = self.symbol_table.get_class_table(
            self.semantic_stack[-2]
        )

    def reset_search_scope(self, current_token):
        tmp = self.semantic_stack[-1]
        self.symbol_table.current = self.semantic_stack[-2]
        self.semantic_stack.pop(3)
        self.semantic_stack.push(tmp)

    def add_zero(self, current_token):
        self.semantic_stack.push(0)

    def save_argument(self, current_token):
        tmp = self.semantic_stack[-1]
        ted = self.semantic_stack[-2] + 1
        self.semantic_stack.pop(2)
        self.semantic_stack.push(tmp)
        self.semantic_stack.push(ted)

    def return_assign(self, current_token):
        if len(self.semantic_stack) < 2:
            self.error_handler.rasie_error(
                ErrorType.Semantic, "Expected return at the end of method"
            )
        return_type = self.semantic_stack[-2].return_type.value
        value_type = self.get_type(self.semantic_stack[-1])

        if return_type != value_type:
            self.error_handler.rasie_error(
                ErrorType.Semantic,
                "Incompatible types. \n Required: {} \n Found: {}".format(
                    return_type, value_type
                ),
            )

    def call_method(self, current_token):
        ted = self.semantic_stack[-1]
        self.semantic_stack.pop(1)
        if ted > 0:
            args = self.semantic_stack[-ted:]
        else:
            args = []

        if len(args) < len(self.semantic_stack[-1 - ted].parameters):
            self.error_handler.rasie_error(
                ErrorType.Semantic, "Expected more arguments"
            )
        if len(args) > len(self.semantic_stack[-1 - ted].parameters):
            self.error_handler.rasie_error(
                ErrorType.Semantic, "Expected less arguments"
            )

        for i in range(len(args)):
            arg_type = self.get_type(args[i])
            return_type = self.get_type(self.semantic_stack[-1 - ted].parameters[i])
            if arg_type != return_type:
                self.error_handler.rasie_error(
                    ErrorType.Semantic,
                    "Wrong {}st argument type.Found: {}, requierd: {}".format(
                        i + 1, arg_type, return_type
                    ),
                )

        self.semantic_stack.push(ted)

    # def assign(self, last_token):
    #     first_type = self.get_type(self.semantic_stack[-1])
    #     second_type = self.get_type(self.semantic_stack[-2])

    #     if first_type == second_type:
    #         return

    #     self.error_handler.rasie_error(
    #         ErrorType.Semantic,
    #         "Incompatible types. \n Required: {} \n Found: {}".format(
    #             second_type, first_type
    #         ),
    #     )

    def not_bool_less(self, last_token):
        first_type = self.get_type(self.semantic_stack[-1])
        second_type = self.get_type(self.semantic_stack[-2])

        if (
            first_type == VariableType.BOOLEAN.value
            or second_type == VariableType.BOOLEAN.value
        ):
            self.error_handler.rasie_error(
                ErrorType.Semantic, "< operation can't be applied to boolean"
            )

    def not_int_and(self, last_token):
        first_type = self.get_type(self.semantic_stack[-1])
        second_type = self.get_type(self.semantic_stack[-2])

        if (
            first_type == VariableType.INT.value
            or second_type == VariableType.INT.value
        ):
            self.error_handler.rasie_error(
                ErrorType.Semantic, " && operation can't be applied to int"
            )

    def not_bool_add(self, last_token):
        first_type = self.get_type(self.semantic_stack[-1])
        second_type = self.get_type(self.semantic_stack[-2])

        if (
            first_type == VariableType.BOOLEAN.value
            or second_type == VariableType.BOOLEAN.value
        ):
            self.error_handler.rasie_error(
                ErrorType.Semantic, " + operation can't be applied to boolean"
            )

    def not_bool_mult(self, last_token):
        first_type = self.get_type(self.semantic_stack[-1])
        second_type = self.get_type(self.semantic_stack[-2])

        if (
            first_type == VariableType.BOOLEAN.value
            or second_type == VariableType.BOOLEAN.value
        ):
            self.error_handler.rasie_error(
                ErrorType.Semantic, "* operation can't be applied to boolean"
            )

    def not_bool_minus(self, last_token):
        first_type = self.get_type(self.semantic_stack[-1])
        second_type = self.get_type(self.semantic_stack[-2])

        if (
            first_type == VariableType.BOOLEAN.value
            or second_type == VariableType.BOOLEAN.value
        ):
            self.error_handler.rasie_error(
                ErrorType.Semantic, " - operation can't be applied to boolean"
            )

    def get_type(self, value):
        if isinstance(value, str):
            if value.startswith("#"):
                type = VariableType.INT
            else:
                type = VariableType.BOOLEAN
        else:
            type = self.memory_manager.get_tp(value)
>>>>>>> c255c9749e46807c92fcc8591782b8c48006e44c

        return type.value
