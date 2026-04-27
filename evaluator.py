# Olijah Williams

def evaluate(rootNode):
    #Base Case
    if rootNode.lChild == None and rootNode.rChild == None:
        return int(rootNode.value)

    #Recursive Call
    else:
        result = 0
        leftResult = evaluate(rootNode.lChild)
        rightResult = evaluate(rootNode.rChild)

        if rootNode.type == "PLUS":
            result = leftResult + rightResult
        elif rootNode.type == "MINUS":
            result = leftResult - rightResult
        elif rootNode.type == "MULTIPLICATION":
            result = leftResult * rightResult
        elif rootNode.type == "DIVISION":
            result = leftResult / rightResult

        return result