from typing import List

with open("../input/input.txt") as fp:
    opcodes = fp.readline().strip().split(',')
    opcodes = [int(c) for c in opcodes]

opcodes[1] = 12
opcodes[2] = 2

def process_opcodes(opcodes: List[int]) -> int:
    for pos in range(0, len(opcodes), 4):
        if opcodes[pos] == 1:
            result_pos = opcodes[pos+3]
            operand1_pos = opcodes[pos+1]
            operand2_pos = opcodes[pos+2]
            opcodes[result_pos] = opcodes[operand1_pos] + opcodes[operand2_pos]
        elif opcodes[pos] == 2:
            result_pos = opcodes[pos+3]
            operand1_pos = opcodes[pos+1]
            operand2_pos = opcodes[pos+2]
            opcodes[result_pos] = opcodes[operand1_pos] * opcodes[operand2_pos]
        elif opcodes[pos] == 99:
            return opcodes[0]

print(process_opcodes(opcodes))
