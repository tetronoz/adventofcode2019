from typing import List

with open("../input/input.txt") as fp:
    opcodes = fp.readline().strip().split(',')
    opcodes = [int(c) for c in opcodes]

def process_opcodes(opcodes: List[int]) -> int:
    for pos in range(0, len(opcodes), 4):
        if opcodes[pos] == 1:
            result_pos = opcodes[pos+3]
            operand1_pos = opcodes[pos+1]
            operand2_pos = opcodes[pos+2]
            try:
                opcodes[result_pos] = opcodes[operand1_pos] + opcodes[operand2_pos]
            except IndexError:
                return 0
        elif opcodes[pos] == 2:
            result_pos = opcodes[pos+3]
            operand1_pos = opcodes[pos+1]
            operand2_pos = opcodes[pos+2]
            try:
                opcodes[result_pos] = opcodes[operand1_pos] * opcodes[operand2_pos]
            except IndexError:
                return 0
        elif opcodes[pos] == 99:
            return opcodes[0]

output = 0

def find_params(opcodes: List[int]) -> int:
    opcodes_orig = []
    opcodes_orig[:] = opcodes

    for i in range(0, 100):
        for j in range(0, 100):
            opcodes[:] = opcodes_orig
            opcodes[1] = i
            opcodes[2] = j
            if process_opcodes(opcodes) == 19690720:
                return 100*i+j

print(find_params(opcodes))