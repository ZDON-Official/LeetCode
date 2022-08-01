// ZDON_OFFICIAL
// Number of Steps to Reduce a Number to Zero

package main

import "fmt"

func numberOfSteps(num int) int {
	var steps = 0

	for num != 0 {
		if num%2 == 0 {
			num = num / 2
			steps += 1
		} else {
			num -= 1
			steps += 1
		}
	}

	return steps
}

func main() {
	fmt.Println(numberOfSteps(14))
}
