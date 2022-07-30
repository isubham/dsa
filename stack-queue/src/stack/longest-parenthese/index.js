/**
 * @summary longest parentheses
 * @author subhamkumarchandrawansi@gmail.com
 * @date 22 feb 2022
 * @link https://leetcode.com/problems/longest-valid-parentheses/
 */

import { Stack } from '../index.js';

const longestParentheses = (s) => {
	if (s === '') { return 0;}

	const stack = new Stack();
	for (let char of s) {
		if (char == '(')
		{
			stack.push(char)
		}
		if (char == ')') {
			if (stack.peek() == '(') {
				stack.pop()
			}
			else {
				stack.push(char)
			}
		}
	}
	return s.length - stack.length;
}

export { longestParentheses };

