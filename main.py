#!/usr/bin/env python3

import sys
from enum import Enum


class TokenType(Enum):
    VAR_DECL = 0
    NUMBER = 1
    IDENT = 2
    LPAREN = 3
    RPAREN = 4
    BINOP = 5
    EQ = 6


RESERVED_KEYWORDS = {
        "let": TokenType.VAR_DECL,
        "=": TokenType.EQ,
        "(": TokenType.LPAREN,
        ")": TokenType.RPAREN,
}


def lex(words: [str]):
    lexed = []
    for word in words:
        tokenType = RESERVED_KEYWORDS.get(word)
        if tokenType is None:
            if word.isalpha():
                lexed.append((TokenType.IDENT, word))
                continue
            elif word.isnumeric():
                lexed.append((TokenType.NUMBER, int(word)))
                continue
        lexed.append((tokenType, word))

    return lexed


def main():
    filename = sys.argv[1]
    words = []
    with open(filename, 'r') as f:
        words = f.read().split()

    tokens = lex(words)
    print(tokens)


if __name__ == "__main__":
    main()
