expression = input('x = ')

def evaluate(string):
    string = string.replace(" ", "")

    def splitstring(string, separators):

        arr = []
        current = ""
        for i in string:
            if i in separators:
                arr.append(current)
                arr.append(i)
                current = ""
            else:
                current += i
        arr.append(current)
        return arr

    arr = splitstring(string, "+-")

    def op_order(string):
        arr = splitstring(string, "*/")
        if len(arr) == 1:
            return arr[0]
        
        output = float(arr[0])
        arr = arr[1:]

        while len(arr) > 0:
            operator = arr[0]
            number = float(arr[1])
            arr = arr[2:]

            if operator == "*":
                output *= number

            elif operator == "/":
                output /= number

        return output

    
    for i in range(len(arr)):
        arr[i] = op_order(arr[i])

    output = float(arr[0])
    arr = arr[1:]

    while len(arr) > 0:
        operator = arr[0]
        number = float(arr[1])
        arr = arr[2:]

        if operator == "+":
            output += number
        elif operator == "-":
            output -= number

    return output

print(evaluate(expression))