package main

import (
	"fmt"
	"strings"
)

func stati(str string) string {
	// Make sure input is not empty.
	if str == "" {
		return ""
	}

	// Split the given string.
	arr := strings.Split(str, ",")
	for i := 0; i < len(arr); i++ {
		// Convert hours to minutes and minutes to seconds. (for calculation)
		nums := strings.Split(arr[i], "|")
		seconds := (((nums[0] * 60) + nums[1]) * 60) + nums[2]
		fmt.Printf("Nums: %v\nSeconds: %v\n", nums, seconds)
	}

	return ""
}

func main() {
	fmt.Printf(stati("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"))
	fmt.Printf(stati("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41"))
}
