package main

import (
	"log"
	"os"
	"strconv"
	"strings"
)

func one() {
	input, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	dial := 50
	counter := 0

	lines := strings.SplitSeq(string(input), "\n")
	for line := range lines {
		if len(line) > 0 {
			jump, err := strconv.Atoi(line[1:])
			if err != nil {
				log.Fatal(err)
			}
			switch line[0] {
			case 'L':
				dial = (100 + dial - jump) % 100
			case 'R':
				dial = (100 + dial + jump) % 100
			}
			if dial == 0 {
				counter++
			}
		}
	}
	log.Printf("Counter 1: %d", counter)
}

func two() {
	input, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	dial := 50
	counter := 0

	lines := strings.SplitSeq(string(input), "\n")
	for line := range lines {
		if len(line) > 0 {
			jump, err := strconv.Atoi(line[1:])
			if err != nil {
				log.Fatal(err)
			}
			switch line[0] {
			case 'L':
				for jump > 0 {
					if dial == 0 {
						counter++
					}
					dial = (100 + dial - 1) % 100
					jump--
				}
			case 'R':
				for jump > 0 {
					if dial == 0 {
						counter++
					}
					dial = (dial + 1) % 100
					jump--
				}
			}

		}
	}
	log.Printf("Counter 2: %d", counter)
}

func main() {
	one()
	two()
}
