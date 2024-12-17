from __future__ import annotations
import lib, re

class Computer:
    def __init__(self, a, b, c, program):
        self.registers = {
                'A': a,
                'B': b,
                'C': c
                }
        self.program = program
        self.output_logs = False

    def clone(self):
        return Computer(
            self.registers['A'],
            self.registers['B'],
            self.registers['C'],
            self.program)

    @classmethod
    def from_state(cls, state):
        registers = {}
        program = []

        for line in state.split('\n'):
            found = False
            for register in ['A', 'B', 'C']:
                m = re.search(rf'^Register {register}: ([0-9]+)$', line)
                if m is None:
                    continue
                value =  m.group(1)
                registers[register] = int(value)
                found = True
                break
            if found:
                continue

            program_match = re.search(r'^Program: ((?:[0-7]+,?)+)$', line)
            if program_match is not None:
                program_value =  program_match.group(1)
                program = [int(i) for i in program_value.split(',')]
        return cls(registers['A'], registers['B'], registers['C'], program)


    def handle_combo_operand(self, operand):
        match operand:
            case operand if operand <= 3:
                return operand
            case 4:
                return self.registers['A']
            case 5:
                return self.registers['B']
            case 6:
                return self.registers['C']
        raise ValueError(f"unexpected combo operand: {operand}") 

    def log(self, s):
        if self.output_logs:
            print(s)

    def execute(self):
        pointer = 0
        output = []
        while pointer < len(self.program):
            opcode = self.program[pointer]
            operand = self.program[pointer + 1]

            jumped = False
            match opcode:
                case 0:
                    result = self.registers["A"] / (2.0 ** self.handle_combo_operand(operand))
                    result = int(result)
                    self.log(f'adv: {self.registers["A"]} / 2**combo({operand}) = {result} -> A')
                    self.registers["A"] = result
                case 1:
                    result = self.registers["B"] ^ operand
                    self.log(f'bxl: {self.registers["B"]} ^ {operand} = {result} -> B')
                    self.registers["B"] = result
                case 2:
                    result = self.handle_combo_operand(operand) % 8
                    self.log(f'bst: combo({operand}) % 8 = {result} -> B')
                    self.registers["B"] = result
                case 3:
                    if self.registers["A"] == 0:
                        self.log(f'jnz: noop')
                    else:
                        pointer = operand
                        jumped = True
                        self.log(f'jnz: jump to {operand}')
                case 4:
                    result = self.registers["B"] ^ self.registers["C"]
                    self.log(f'bxc: {self.registers["B"]} ^ {self.registers["C"]} = {result} -> B')
                    self.registers["B"] = result
                case 5:
                    result = self.handle_combo_operand(operand) % 8
                    self.log(f'out: combo({operand}) % 8 = {result} -> output')
                    output.append(result)
                case 6:
                    result = self.registers["A"] / (2.0 ** self.handle_combo_operand(operand))
                    result = int(result)
                    self.log(f'bdv: {self.registers["A"]} / 2**combo({operand}) = {result} -> B')
                    self.registers["B"] = result
                case 7:
                    result = self.registers["A"] / (2.0 ** self.handle_combo_operand(operand))
                    result = int(result)
                    self.log(f'cdv: {self.registers["A"]} / 2**combo({operand}) = {result} -> C')
                    self.registers["C"] = result


            if not jumped:
                pointer += 2
        final_result = ','.join([str(i) for i in output])
        return final_result


def p1():
    data = lib.read()

    computer = Computer.from_state(data)
    output = computer.execute()
    print(output)

def p2():
    data = lib.read()

    computer = Computer.from_state(data)
    program = computer.program
    a_value = computer.registers['A']
    b_value = computer.registers['B']
    c_value = computer.registers['C']
    target_output = ','.join([str(i) for i in program])

    output = computer.execute()

    step = 8**0

    # trial and error doing steps of 8**n to get each digit of the output
    # idek bruh
    a_value = 4*8**15 + 5*8**14 + 3*8**13 \
        + 2*8**12 \
        + 3*8**11 \
        + 0*8**10 \
        + 6*8**9 \
        + 0*8**8 \
        + 7*8**7 \
        + 2*8**6 \
        + 10*8**5 \
        + 6*8**4 \
        + 7*8**3 \
        + 2*8**2 \
        + 0*8**1 \
        + 0*8**0

    while output != target_output:
        output = Computer(a_value, b_value, c_value, program).execute()

        s = f'{a_value:<3} {output:>20}'

        print(s)
        input()
        a_value += step
    a_value -= step

    print(output)
    print(target_output)
    print(a_value)

p2()
