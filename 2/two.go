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

	data := strings.SplitSeq(string(input), ",")
	for id_range := range data {
		id_range = strings.TrimSpace(id_range)
		id_range_parts := strings.Split(id_range, "-")
		id1, id1_err := strconv.Atoi(id_range_parts[0])
		id2, id2_err := strconv.Atoi(id_range_parts[1])
		if id1_err != nil || id2_err != nil {
			log.Fatal("Error parsing range:", id_range)
		}
		for id := id1; id <= id2; id++ {
			str_id := strconv.Itoa(id)
			if str_id[0:len(str_id)/2] == str_id[len(str_id)/2:] {
				sum += id
			}
		}
	}
	log.Printf("Sum of matching IDs: %d", sum)
}

func two() {
	input, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	sum := 0

	data := strings.SplitSeq(string(input), ",")
	for id_range := range data {
		id_range = strings.TrimSpace(id_range)
		id_range_parts := strings.Split(id_range, "-")
		id1, id1_err := strconv.Atoi(id_range_parts[0])
		id2, id2_err := strconv.Atoi(id_range_parts[1])
		if id1_err != nil || id2_err != nil {
			log.Fatal("Error parsing range:", id_range)
		}
		for id := id1; id <= id2; id++ {
			str_id := strconv.Itoa(id)
			for i := 1; i < len(str_id); i += 1 {
				matched := false
				var groups []string
				if len(str_id)%i != 0 {
					continue
				}
				for j := 0; j < len(str_id); j += i {
					groups = append(groups, str_id[j:j+i])
				}
				for k := 1; k < len(groups); k += 1 {
					if groups[k] != groups[0] {
						break
					}
					if k == len(groups)-1 {
						sum += id
						matched = true
						break
					}
				}
				if matched {
					break
				}
			}
		}

	}
	log.Printf("Sum of matching IDs: %d", sum)
}

func main() {
	one()
	two()
}
