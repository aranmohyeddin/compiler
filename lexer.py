import string

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
terminal = whitespace + symbols
alphanum = digits + letters
charset = terminal + alphanum
look_ahead = ""
first = True
FSM = {
    "START": {
        **dict.fromkeys(whitespace, "START"),
        **dict.fromkeys(symbols, "SYMBOL"),
        **dict.fromkeys(letters, "ID"),
        **dict.fromkeys(digits, "NUM"),
        "=": "=",
        "/": "COMMENT",
    },
    "ID": {
        **dict.fromkeys(terminal, "STOP"),
        **dict.fromkeys(alphanum, "ID"),
        "/": "STOP",
    },
    "NUM": {
        **dict.fromkeys(terminal, "STOP"),
        **dict.fromkeys(letters, "ERROR"),
        **dict.fromkeys(digits, "NUM"),
        "/": "STOP",
    },
    "=": {**dict.fromkeys(charset, "STOP"), "=": "==", "/": "STOP"},
    "==": {**dict.fromkeys(charset, "STOP"), "/": "STOP"},
    "ERROR": {
        **dict.fromkeys(alphanum, "ERROR"),
        **dict.fromkeys(terminal, "STOP"),
        "/": "STOP",
    },
    "STOP": None,
    "COMMENT": None,  # We either have an error or there is a comment to skip
}


def nextt(iterator):
    char = next(iterator)
    if char == "\n":
        nextt.line_number = getattr(nextt, "line_number", 1) + 1
        nextt.newline_text = ("" if first else "\n") + f"{nextt.line_number}."
    return char


nextt.newline_text = "1."  # initialize


def panic(msg, line_number):
    return f"Line {line_number}: ({msg}, invalid input)"


def output(token_type, token):
    if token_type in ["=", "=="]:
        token_type = "SYMBOL"
    if token_type == "ID" and token in keywords:
        token_type = "KEYWORD"
    return (token_type, token)


def get_nextt_token(prog, look_ahead=""):
    """
    returns token/err, look_ahead
    """
    if not look_ahead:
        token = nextt(prog)
    else:
        token = look_ahead
    initial_state = state = FSM["START"].get(token[-1], "ERROR")
    while state == "START":
        token = nextt(prog)
        initial_state = state = FSM[state].get(token[-1], "ERROR")
    if state == "SYMBOL":
        return (
            output("SYMBOL", token),
            nextt(prog),
        )  # just to be consistent (it is needed for the newline_text logic to work, otherwise we will have some problems for lines with only one token
    elif state == "COMMENT":
        look_ahead = nextt(prog)
        if look_ahead == "*":
            temp_line_number = nextt.line_number
            try:
                # skip until '*/'
                while nextt(prog) != "*" or nextt(prog) != "/":
                    pass
            except StopIteration:
                return panic("/*", temp_line_number), ""
            return get_nextt_token(prog)
        elif look_ahead == "/":
            try:
                while nextt(prog) != "\n":
                    pass
            except StopIteration:
                return "", ""  # think about this
            return get_nextt_token(prog)
        elif look_ahead in whitespace:
            return panic("/", nextt.line_number - 1), ""
        else:
            state = "ERROR"
            token += look_ahead
            look_ahead = ""
    while state != "STOP":
        token += nextt(prog)
        # remember to remove the last element of token if there is no error, this is probably the best way to do it, think before changing.
        initial_state = state
        state = FSM[state].get(token[-1], "ERROR")
    if initial_state == "ERROR":
        return (
            panic(
                token[:-1],
                getattr(nextt, "line_number", 1) - 1 if token[-1] == "\n" else getattr(nextt, "line_number", 1)
            ),
            token[-1],
        )
    else:
        return (
            output(initial_state, token[:-1]),
            token[-1],
        )  # removed the last element of token


if __name__ == "__main__":
    with open("program.sex", "r") as inn:
        prog = iter(inn.read())
    with open("scanner.txt", "w") as out, open("lexical_errors.txt", "w") as err:
        while True:
            try:
                outt, look_ahead = get_nextt_token(prog, look_ahead)
                if type(outt) is str:
                    err.write(outt + "\n")
                else:
                    outt = "({}, {})".format(*outt)
                    if look_ahead == "\n":
                        if not nextt.last_text:
                            out.write(outt)
                        else:
                            out.write(f"\n{nextt.line_number-1}." + outt)
                        nextt.last_text = nextt.newline_text
                    else:
                        out.write(nextt.newline_text + outt)
                        nextt.last_text = nextt.newline_text
                        nextt.newline_text = ""
                        first = False
            except StopIteration:
                break
