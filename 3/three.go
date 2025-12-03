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
	sum := 0

	data := strings.SplitSeq(string(input), "\n")
	for line := range data {
		bignum := 0
		for index, str_num := range line {
			num, _ := strconv.Atoi(string(str_num))
			for _, str_num2 := range line[index+1:] {
				num2, _ := strconv.Atoi(string(str_num2))
				number_str := strconv.Itoa(num) + strconv.Itoa(num2)
				number, _ := strconv.Atoi(number_str)
				if number > bignum {
					bignum = number
				}
			}
		}
		sum += bignum
	}
	log.Printf("Total joltage: %d", sum)
}

func two() {
	input, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	sum := 0
	data := strings.SplitSeq(string(input), "\n")
	for line := range data {
		arr := []int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
		slice_left := 0
		slice_right := len(line) - 11
		for i := range 12 {
			biggest := 0
			index := 0
			for j := slice_left; j < slice_right; j++ {
				num, _ := strconv.Atoi(string(line[j]))
				if num > biggest {
					biggest = num
					index = j
				}
			}
			arr[i] = biggest
			slice_left = index + 1
			slice_right++
		}
		var sb strings.Builder
		for _, arrnum := range arr {
			sb.WriteString(strconv.Itoa(arrnum))
		}
		bignumstr, _ := strconv.Atoi(sb.String())
		sum += bignumstr

	}
	log.Printf("Total joltage: %d", sum)
}

func main() {
	one()
	two()
}
