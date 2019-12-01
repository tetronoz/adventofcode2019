package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	var totalSum int
	file, err := os.Open("../input/input_day1")
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		v, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatal(err)
		}
		totalSum += calculateModuleMass(v)
	}

	fmt.Println(totalSum)
}

func calculateModuleMass(mass int) int {
	fuelMass := mass/3 - 2
	total := fuelMass
	for fuelMass > 0 {
		fuelMass = fuelMass/3 - 2
		if fuelMass > 0 {
			total += fuelMass
		}
	}
	return total
}
