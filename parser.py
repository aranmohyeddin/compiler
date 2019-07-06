terminals = [
    "EOF",
    "ID",
    "NUM",
    "int",
    "void",
    "continue",
    "break",
    "if",
    "while",
    "else",
    "return",
    "switch",
    "case",
    "default",
    ";",
    ",",
    ":",
    "+",
    "=",
    "==",
    "<",
    "-",
    "*",
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
]


class Rule:
    def __init__(self, lhs, rhs):
        self.rhs = rhs
        self.lhs = lhs

    def __str__(self):
        return self.lhs + "→" + str(self.rhs)


def read_grammer(gram_dir):
    grammer = {}
    f = open(gram_dir, "r")
    gram = f.readlines()
    for rule in gram:
        words = rule.split()
        lhs = words[0]
        grammer[lhs] = []
        words = words[2:]
        words.append("|")
        while len(words) > 0:
            i = words.index("|")
            grammer[lhs].append(words[:i])
            words = words[i + 1 :]

    return grammer


grammar = read_grammer("Grammar")
# print(grammar)


def unique(list1):
    list_set = set(list1)
    unique_list = list(list_set)
    return unique_list


first = {}

for a in terminals + ["Ïµ"]:
    first[a] = [a]


def calc_first(alpha):
    # print(alpha)
    if alpha in first:
        return
    first[alpha] = []

    for _ in range(2):
        # print(alpha)
        for lhs in grammar[alpha]:
            if (not lhs[0] in first) and lhs[0] != alpha:
                calc_first(lhs[0])

            first[alpha] = first[alpha] + first[lhs[0]]
            first[alpha] = unique(first[alpha])
            i = 0

            while "Ïµ" in first[lhs[0]] and i < len(lhs) - 1:
                i = i + 1
                if (not (lhs[i] in first)) and lhs[i] != alpha:
                    calc_first(lhs[i])

                first[alpha] = first[alpha] + first[lhs[i]]
                first[alpha] = unique(first[alpha])


# for a in grammar.keys():
#     calc_first(a)


follow = {}

follow["program"] = ["$"]


def calc_follow(alpha):
    # print(alpha)
    if alpha in follow:
        return
    follow[alpha] = []

    for _ in range(2):
        # print(alpha)
        for lhs in grammar[alpha]:
            for i in range(len(lhs) - 1):
                if not (lhs[i] in follow):
                    follow[lhs[i]] = []
                follow[lhs[i]] = follow[lhs[i]] + list(
                    set(first[lhs[i + 1]]) - set("Ïµ")
                )
                follow[lhs[i]] = unique(follow[lhs[i]])
                j = i + 1
                while "Ïµ" in first[lhs[j]] and j < len(lhs) - 1:
                    j = j + 1
                    follow[lhs[i]] = follow[lhs[i]] + list(
                        set(first[lhs[j]]) - set("Ïµ")
                    )
                    follow[lhs[i]] = unique(follow[lhs[i]])

            i = -1

            while "Ïµ" in first[lhs[i]] and i > -len(lhs) + 1:
                i = i - 1
                if (not (lhs[i] in follow)) and lhs[i] != alpha:
                    calc_follow(lhs[i])

                follow[alpha] = follow[alpha] + follow[lhs[i]]
                follow[alpha] = unique(follow[alpha])


# for a in grammar.keys():
#     calc_follow(a)

# print(follow)

Table = {}


# for a in grammar.keys():
#     for lhs in grammar[a]:
#         i = 0
#         for t in first[lhs[0]]:
#             Table[a, t] = lhs
#
#         if 'Ïµ' in first[lhs[i]] and i < len(lhs) - 1:
#             i = i + 1
#
#             for t in first[lhs[i]]:
#                 Table[a, t] = lhs

<<<<<<< HEAD
=======
        if "Ïµ" in first[lhs[i]] and i < len(lhs) - 1:
            i = i + 1
>>>>>>> c255c9749e46807c92fcc8591782b8c48006e44c



# stack = []
#
# stack.append('program')
# stack.append('$')
#
# def next_action(token):
#     if stack[0] in terminals:
#         if stack[0] == token:
#             stack = stack[1:]
#


<<<<<<< HEAD
stack.push("program")
stack.push("$")
=======
>>>>>>> 71b95eac67855c2803de6e0bae3788f32bae9e5c

print('Void main function error')