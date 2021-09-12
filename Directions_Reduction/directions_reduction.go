package main

import (
	"fmt"
	"strings"
)

func dirReduction(arr []string) []string {
	var dirs = []string{}
	for _, value := range arr {
		dirs = append(dirs, strings.ToUpper(value))
	}
	var result = []string{}
	for i := 0; i < len(dirs); i++ {
		for j := 0; j < len(dirs); j++ {
			switch dirs[j] {
			case "NORTH", "SOUTH":
				if dirs[i] == "NORTH" || dirs[i] == "SOUTH" {
					break
				} else {
					result = append(result, dirs[j])
				}
			case "WEST", "EAST":
				if dirs[i] == "WEST" || dirs[i] == "EAST" {
					break
				} else {
					result = append(result, dirs[j])
				}
			}
		}
	}

	return result
}

func main() {
	// Test cases below..
	var a = []string{"NORTH", "SOUTH", "EAST", "WEST"}
	fmt.Println(dirReduction(a))
	a = []string{"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"}
	fmt.Println(dirReduction(a))
	a = []string{"NORTH", "WEST", "SOUTH", "EAST"}
	fmt.Println(dirReduction(a))
	a = []string{"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH"}
	fmt.Println(dirReduction(a))
}
