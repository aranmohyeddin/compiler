import string
from collections import defaultdict

with open("program.d", "r") as inn:
    program = inn.read()

keywords = [
    "if",
    "else",
    "void",
    "int",
    "while",
    "break",
    "continue",
    "switch",
    "default",
    "case",
    "return",
]
letters = string.ascii_letters
digits = string.digits
symbols = "()[]{};:<,+-*="
whitespace = string.whitespace  # ' \t\n\r\x0b\x0c'

state = "START"
COMMENT_FSM = {
    "/": {"/": "//", "*": "/*..."},
    "//": defaultdict(lambda: "//", {"\n": "START"}),
    "/*...": defaultdict(lambda: "/*...", {"*": "/*...*", "\n": "/*...\n"}),
    "/*...*": defaultdict(lambda: "/*...", {"/": "START", "\n": "/*...\n"}),
}

FSM = {
    "START": {
        **dict.fromkeys(whitespace, "START"),
        **dict.fromkeys(symbols, "SYMBOL"),
        **dict.fromkeys(letters, "ID"),
        **dict.fromkeys(digits, "NUM"),
        "=": "=",
        "/": "COMMENT",
        "\n": "STOP",
    },
    "ID": {
        **dict.fromkeys(whitespace + symbols, "STOP"),
        **dict.fromkeys(digits + letters, "ID"),
    },
    "NUM": {
        **dict.fromkeys(whitespace + symbols, "STOP"),
        **dict.fromkeys(letters, "ERROR"),
        **dict.fromkeys(digits, "NUM"),
    },
    "SYMBOL": {**dict.fromkeys(letters + digits + whitespace + symbols, "STOP")},
    "=": {**dict.fromkeys(letters + digits + whitespace + symbols, "STOP"), "=": "=="},
    "==": {**dict.fromkeys(letters + digits + whitespace + symbols, "STOP")},
    "ERROR": None,
    "STOP": None,
    "COMMENT": None,  # We either have an error or
}  # manage comments out of FSM


def panic(msg):
    return "({}, invalid input)".format(msg)


def output(token, token_type):
    return "({}, {})".format(token_type, token)


def get_next_token(prog, out="", err="", look_ahead=""):
    token = ""
    if not look_ahead:
        token += next(prog)
    else:
        token += look_ahead
    # first character of token in place
    # if token[-1] == "/":
    #     look_ahead = next(prog)
    #     if look_ahead == "*":
    #         try:
    #             # this is some genius that just skips all chars until it finds '*/'
    #             while next(prog) != "*" or next(prog) != "/":
    #                 pass
    #         except StopIteration:
    #             return "", panic("/*")
    #         return get_next_token(prog)
    #     elif look_ahead == "/":
    #         return out, err
    #     else:
    #         err += panic(token)
    #         return get_next_token(prog, err=err, look_ahead=look_ahead)
    # # comments handled
    # else:
    initial_state = state = FSM["START"].get(token[-1], "ERROR")
    if state == "ERROR":
        return panic(token)
    while state != "STOP":
        token += next(prog)
        # remember to remove the last element of token if there is no error, this is probably the best way to do it, think before changing.
        state = FSM[state].get(token[-1], "ERROR")
    if state == "ERROR":
        return panic(token)
    else:
        look_ahead = token[-1]
        token = token[:-1]
        # removed the last element of token, token is clean now.
        out += str((initial_state, token))


with open("scanner.txt", "w") as out, open("lexical_errors.txt", "w") as err:
    program_lines = "shit"
    for idx, line in enumerate(program_lines):
        outt = error = look_ahead = ""
        while True:
            outt, error, look_ahead = get_next_token(iter(line))
    print("done")
