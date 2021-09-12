package main

import (
	"fmt"
)

func DNAStrand(dna string) string {
	var rebuild string
	for _, val := range dna {
		switch string(val) {
		case "A":
			rebuild += "T"
		case "T":
			rebuild += "A"
		case "C":
			rebuild += "G"
		case "G":
			rebuild += "C"
		default:
			continue
		}
	}
	return rebuild
}

func main() {
	fmt.Println(DNAStrand("TTTT"))
}
