package main

import (
	"fmt"
	"image"
	"io/ioutil"
	"log"
	"math"
	"strconv"
	"strings"
)

const inputFile = "../input/input.txt"

type Point = image.Point

type Wire struct {
	data map[Point]int
}

func (w *Wire) Set(x int, y int, d int) {
	xy := Point{x, y}

	w.data[xy] = d
}

func (w *Wire) Get(p Point) int {
	v, ok := w.data[p]
	if ok {
		return v
	}

	return 0
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func BuildWire(path string) Wire {
	w := Wire{}
	w.data = make(map[Point]int)
	x, y := 0, 0
	directions := strings.Split(path, ",")

	addStep := func(xIncr int, yIncr int, steps int) {
		for i := 1; i <= steps; i++ {
			x += xIncr
			y += yIncr
			distance := Abs(x) + Abs(y)
			w.Set(x, y, distance)
		}
	}

	for _, dir := range directions {
		steps, err := strconv.Atoi(dir[1:])

		if err != nil {
			log.Fatal(err)
		}

		switch dir[0] {
		case 'R':
			addStep(1, 0, steps)
		case 'L':
			addStep(-1, 0, steps)
		case 'U':
			addStep(0, 1, steps)
		case 'D':
			addStep(0, -1, steps)
		}
	}

	return w

}

func main() {
	buff, err := ioutil.ReadFile(inputFile)
	if err != nil {
		log.Fatal(err)
	}
	wirePaths := string(buff)
	wirePaths = strings.TrimRight(wirePaths, "\n")

	wires := strings.Split(wirePaths, "\n")

	w1 := BuildWire(wires[0])
	w2 := BuildWire(wires[1])

	res := math.MaxUint32

	for p := range w1.data {
		v := w2.Get(p)
		if v != 0 {
			if v < res {
				res = v
			}
		}
	}

	fmt.Println(res)

}
