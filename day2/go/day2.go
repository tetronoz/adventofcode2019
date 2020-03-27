package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

const inputFile = "../input/input.txt"

func runProgram(ops []int) int {
	opcodes := make([]int, len(ops))
	copy(opcodes, ops)
	var ip = 0
	for {
		switch opcodes[ip] {
		case 1:
			op1 := opcodes[ip+1]
			op2 := opcodes[ip+2]
			op3 := opcodes[ip+3]
			opcodes[op3] = opcodes[op1] + opcodes[op2]
			ip += 4
		case 2:
			op1 := opcodes[ip+1]
			op2 := opcodes[ip+2]
			op3 := opcodes[ip+3]
			opcodes[op3] = opcodes[op1] * opcodes[op2]
			ip += 4
		case 99:
			return int(opcodes[0])
		}
	}
}

func patchOpcodes(noun int, verb int, opcodes *[]int) {
	(*opcodes)[1] = noun
	(*opcodes)[2] = verb
}

func main() {

	buff, err := ioutil.ReadFile(inputFile)
	if err != nil {
		log.Fatal(err)
	}

	str := string(buff)
	str = strings.TrimRight(str, "\n")
	opcodesStr := strings.Split(str, ",")
	opcodes := make([]int, len(opcodesStr))

	for i, opStr := range opcodesStr {
		opcodes[i], err = strconv.Atoi(opStr)
		if err != nil {
			log.Fatal(err)
		}
	}

	patchOpcodes(12, 1, &opcodes)
	res := runProgram(opcodes)
	fmt.Println(res)

	for noun := 0; noun < 100; noun++ {
		for verb := 0; verb < 100; verb ++ {
			patchOpcodes(noun, verb, &opcodes)
			if runProgram(opcodes) == 19690720 {
				fmt.Printf("%d (%d %d)\n", 100*noun+verb, noun, verb)
				break
			}
		}
	} 
}
