import re

# ---------------- Token definitions ---------------- #

TOKEN_NUMBER   = "NUMBER"
TOKEN_IDENT    = "IDENT"    # variable or function name
TOKEN_OP       = "OP"
TOKEN_LPAREN   = "LPAREN"
TOKEN_RPAREN   = "RPAREN"
TOKEN_COMMA    = "COMMA"

class Token:
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value

    def __repr__(self):
        return f"Token({self.kind}, {self.value})"


# precedence: higher number = stronger binding
# unary minus is treated as a separate operator 'NEG'
OPERATORS = {
    "+":  (1, "L"),   # (precedence, associativity)
    "-":  (1, "L"),
    "*":  (2, "L"),
    "/":  (2, "L"),
    "^":  (3, "R"),
    "NEG": (4, "R"),  # unary minus, highest precedence
}

def is_operator_symbol(ch):
    return ch in "+-*/^"

# --------------- Tokenizer (lexical analysis) --------------- #

def tokenize(expr):
    """
    Convert input string into a list of Token objects.
    Handles: integers, identifiers, parentheses, commas, operators.
    """
    tokens = []
    i = 0
    while i < len(expr):
        ch = expr[i]
        if ch.isspace():
            i += 1
            continue
        if ch.isdigit():
            # multi-digit number
            j = i
            while j < len(expr) and expr[j].isdigit():
                j += 1
            tokens.append(Token(TOKEN_NUMBER, expr[i:j]))
            i = j
        elif ch.isalpha():
            # identifier (variable or function)
            j = i
            while j < len(expr) and (expr[j].isalnum() or expr[j] == "_"):
                j += 1
            tokens.append(Token(TOKEN_IDENT, expr[i:j]))
            i = j
        elif ch == "(":
            tokens.append(Token(TOKEN_LPAREN, ch))
            i += 1
        elif ch == ")":
            tokens.append(Token(TOKEN_RPAREN, ch))
            i += 1
        elif ch == ",":
            tokens.append(Token(TOKEN_COMMA, ch))
            i += 1
        elif is_operator_symbol(ch):
            tokens.append(Token(TOKEN_OP, ch))
            i += 1
        else:
            raise ValueError(f"Unexpected character: {ch}")
    return tokens

# --------------- Shunting Yard conversion --------------- #

def to_postfix(tokens):
    """
    Convert infix token list to postfix (RPN) using shunting-yard algorithm.
    Handles functions, unary minus, precedence, associativity, and commas.
    """
    output = []
    op_stack = []

    def push_operator(op):
        prec, assoc = OPERATORS[op]
        while op_stack:
            top = op_stack[-1]
            if top.kind == TOKEN_OP:
                top_prec, top_assoc = OPERATORS[top.value]
                cond1 = top_prec > prec
                cond2 = (top_prec == prec and assoc == "L")
                if cond1 or cond2:
                    output.append(op_stack.pop())
                    continue
            break
        op_stack.append(Token(TOKEN_OP, op))

    prev_token = None
    for t in tokens:
        if t.kind in (TOKEN_NUMBER, TOKEN_IDENT):
            output.append(t)
        elif t.kind == TOKEN_OP:
            # detect unary minus: '-' that comes at start or after another operator or '(' or ','
            if t.value == "-":
                if prev_token is None or prev_token.kind in {
                    TOKEN_OP, TOKEN_LPAREN, TOKEN_COMMA
                }:
                    push_operator("NEG")
                else:
                    push_operator("-")
            else:
                push_operator(t.value)
        elif t.kind == TOKEN_LPAREN:
            op_stack.append(t)
        elif t.kind == TOKEN_RPAREN:
            # pop until '('
            while op_stack and op_stack[-1].kind != TOKEN_LPAREN:
                output.append(op_stack.pop())
            if not op_stack:
                raise ValueError("Mismatched parentheses")
            op_stack.pop()  # remove '('
            # if immediately before '(' was a function identifier on stack, pop it as function
            if op_stack and op_stack[-1].kind == TOKEN_IDENT:
                output.append(op_stack.pop())
        elif t.kind == TOKEN_COMMA:
            # function argument separator: pop until '('
            while op_stack and op_stack[-1].kind != TOKEN_LPAREN:
                output.append(op_stack.pop())
            if not op_stack:
                raise ValueError("Misplaced comma or mismatched parentheses")
        else:
            raise ValueError(f"Unexpected token kind: {t.kind}")
        prev_token = t

    # flush stack
    while op_stack:
        top = op_stack.pop()
        if top.kind in (TOKEN_LPAREN, TOKEN_RPAREN):
            raise ValueError("Mismatched parentheses at end")
        output.append(top)

    return output

# --------------- Pretty helpers and REPL --------------- #

def postfix_to_string(postfix_tokens):
    """
    Join postfix tokens into a single space-separated string.
    """
    parts = []
    for t in postfix_tokens:
        parts.append(t.value)
    return " ".join(parts)

def convert_infix(expr):
    """
    High-level helper: string -> string postfix.
    """
    tokens = tokenize(expr)
    postfix = to_postfix(tokens)
    return postfix_to_string(postfix)

def run_examples():
    examples = [
        "3 + 4 * 2 / (1 - 5) ^ 2 ^ 3",
        "-3 + 4",
        "3 + -4 * 2",
        "a * (b + c)",
        "max(1, 2, 3) + min(4, 5)",
        "x^2 + 2*x - 5",
        "-(a+b)*c",
        "sin(x) + cos(y) * -z",
    ]
    print("=== Infix → Postfix examples ===")
    for e in examples:
        print(f"Infix:   {e}")
        try:
            print(f"Postfix: {convert_infix(e)}\n")
        except ValueError as err:
            print(f"Error:   {err}\n")

def repl():
    print("=== Infix to Postfix Converter (supports + - * / ^, functions, unary minus) ===")
    print("Type 'exit' to quit.\n")
    while True:
        expr = input("Infix> ").strip()
        if expr.lower() in {"exit", "quit"}:
            break
        if not expr:
            continue
        try:
            print("Postfix:", convert_infix(expr))
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    run_examples()
    repl()
