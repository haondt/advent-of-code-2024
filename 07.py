import lib

def get_equations():
    data = lib.read()
    equations = []
    for line in data.split('\n'):
        result, values = line.split(':')
        result = int(result.strip())
        values = [int(i.strip()) for i in values.split(' ') if len(i.strip()) > 0]
        equations.append((result, values))
    return equations

def try_get_result(target, current_result, remaining_operands, use_concat=False):
    if len(remaining_operands) == 0:
        return current_result == target

    if current_result > target:
        return False

    operand, *remaining_operands = remaining_operands

    # try with add
    add_result = current_result + operand
    if try_get_result(target, add_result, remaining_operands, use_concat):
        return True

    # try with multiply
    mult_result = current_result * operand 
    if try_get_result(target, mult_result, remaining_operands, use_concat):
        return True

    if use_concat:
        # try with concatenation
        concat_result = int(str(current_result) + str(operand))
        if try_get_result(target, concat_result, remaining_operands, use_concat):
            return True

    return False


def p1():
    equations = get_equations()
    s = 0
    for result, operands in equations:
        if try_get_result(result, 0, operands):
            s += result
    print(s)

def p2():
    equations = get_equations()
    s = 0
    for result, operands in equations:
        if try_get_result(result, 0, operands, True):
            s += result
    print(s)

p2()



