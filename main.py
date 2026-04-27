# Olijah Williams

import lexer
import parserr
import evaluator


# -------------------------
# Part 1
# -------------------------
# srcCode = "((12+3*5)+5/4)"
# tokSeq = lexer.tokenize(srcCode)
#
# for item in tokSeq:
#     print(item.type, item.value)


# -------------------------
# Part 2
# -------------------------
# srcCode = "1 * (2 + 5)"
# tokSeq = lexer.tokenize(srcCode)
# rootNode = parserr.parse(tokSeq)
# parserr.printTree(rootNode)
# print()


# -------------------------
# Part 3
# -------------------------
while True:
    srcCode = input(">>> ")

    if srcCode == "poopoo":
        break

    tokSeq = lexer.tokenize(srcCode)
    rootNode = parserr.parse(tokSeq)
    result = evaluator.evaluate(rootNode)

    print("The result is: ", result)

print("Now it is time to go poo poo.")