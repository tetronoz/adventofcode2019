from typing import List

with open("../input/input.txt") as fp:
    opcodes = fp.readline().strip().split(',')
    opcodes = [int(c) for c in opcodes]

def get_parameter_mode(instr: str) -> List[int]:
    try:
        opcode = int(instr[-1])
    except IndexError:
        opcode = None
    try:
        mode_1 = int(instr[-3])
    except IndexError:
        mode_1 = 0
    try:
        mode_2 = int(instr[-4])
    except IndexError:
        mode_2 = 0
    try:
        mode_3 = int(instr[-5])
    except IndexError:
        mode_3 = 0
    
    return [int(opcode), int(mode_1), int(mode_2), int(mode_3)]

def process_opcodes(opcodes: List[int]) -> int:
    idx = 0
    next_inst = float("inf")
    prev_inst = float("inf")
    
    while idx < len(opcodes):
        opcode = float("inf")
        prev_inst = next_inst
        next_inst = opcodes[idx]
        
        if len(str(next_inst)) > 1:
            opcode, mode_1, mode_2, mode_3 = get_parameter_mode(str(next_inst))
        else:
            mode_1 = 0 
            mode_2 = 0 
            mode_3 = 0
            opcode = opcodes[idx]
        
        if opcode == 1:
            if mode_3 == 0:
                result_pos = opcodes[idx+3]
            else:
                result_pos = idx+3
            #print(f"{opcode} - {mode_1} - {mode_2}")
            if mode_1 == 0:
                operand1_pos = opcodes[idx+1]
                operand1_value = opcodes[operand1_pos]
            elif mode_1 == 1:
                operand1_value = opcodes[idx+1]
            if mode_2 == 0:
                operand2_pos = opcodes[idx+2]
                operand2_value = opcodes[operand2_pos]
            elif mode_2 == 1:
                operand2_value = opcodes[idx+2]
            opcodes[result_pos] = operand1_value + operand2_value
            idx += 4
        elif opcode == 2:
            if mode_3 == 0:
                result_pos = opcodes[idx+3]
            else:
                result_pos = idx+3
            if mode_1 == 0:
                operand1_pos = opcodes[idx+1]
                operand1_value = opcodes[operand1_pos]
            elif mode_1 == 1:
                operand1_value = opcodes[idx+1]
            if mode_2 == 0:
                operand2_pos = opcodes[idx+2]
                operand2_value = opcodes[operand2_pos]
            elif mode_2 == 1:
                operand2_value = opcodes[idx+2]
            opcodes[result_pos] = operand1_value * operand2_value 
            idx += 4
        elif opcode == 99:
            return 1
        elif opcode == 3:
            input_data = input("Enter ID of the system to test: ")
            operand_pos = opcodes[idx+1]
            idx += 2
            opcodes[operand_pos] = int(input_data)
        elif opcode == 4:
            if mode_1 == 0:
                operand1_pos = opcodes[idx+1]
            elif mode_1 == 1:
                operand1_pos = idx+1
            print(opcodes[operand1_pos])
            if opcodes[operand1_pos] != 0:
                return
            idx += 2
        elif opcode == 5:
            if mode_1 == 0:
                operand1_pos = opcodes[idx+1]
            elif mode_1 == 1:
                operand1_pos = idx+1
            
            if mode_2 == 0:
                operand2_pos = opcodes[idx+2]
            elif mode_2 == 1:
                operand2_pos = idx+2

            if opcodes[operand1_pos] != 0:
                idx = opcodes[operand2_pos] 
            else:
                idx += 3
        elif opcode == 6:
            if mode_1 == 0:
                operand1_pos = opcodes[idx+1]
            elif mode_1 == 1:
                operand1_pos = idx+1
            
            if mode_2 == 0:
                operand2_pos = opcodes[idx+2]
            elif mode_2 == 1:
                operand2_pos = idx+2

            if opcodes[operand1_pos] == 0:
                idx = opcodes[operand2_pos] 
            else:
                idx += 3
        elif opcode == 7:
            if mode_1 == 0:
                operand1_pos = opcodes[idx+1]
            elif mode_1 == 1:
                operand1_pos = idx+1
            
            if mode_2 == 0:
                operand2_pos = opcodes[idx+2]
            elif mode_2 == 1:
                operand2_pos = idx+2
            
            if mode_3 == 0:
                operand3_pos = opcodes[idx+3]
            elif mode_3 == 1:
                operand3_pos = idx+3

            if opcodes[operand1_pos] < opcodes[operand2_pos]:
                opcodes[operand3_pos] = 1
            else:
                opcodes[operand3_pos] = 0
            idx += 4
        elif opcode == 8:
            if mode_1 == 0:
                operand1_pos = opcodes[idx+1]
            elif mode_1 == 1:
                operand1_pos = idx+1
            
            if mode_2 == 0:
                operand2_pos = opcodes[idx+2]
            elif mode_2 == 1:
                operand2_pos = idx+2
            
            if mode_3 == 0:
                operand3_pos = opcodes[idx+3]
            elif mode_3 == 1:
                operand3_pos = idx+3

            if opcodes[operand1_pos] == opcodes[operand2_pos]:
                opcodes[operand3_pos] = 1
            else:
                opcodes[operand3_pos] = 0
            idx += 4
        else:
            print(f"Unknown opcode {opcode}")
            return


process_opcodes(opcodes)