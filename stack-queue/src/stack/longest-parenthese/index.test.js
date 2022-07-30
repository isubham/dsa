import { longestParentheses } from './index.js';

describe("longest parentheses", function() {
	test("with empty string should return 0", function() {
	{
		expect(longestParentheses("")).toBe(0);
	}})

	test("with ()) should return 2", function() {
	{
		expect(longestParentheses("())")).toBe(2);
	}})
	test("with (()()( should return 4", function() {
	{
		expect(longestParentheses("(()()(")).toBe(4);
	}})
	test("with (()()) should return 6", function() {
	{
		expect(longestParentheses("(()())")).toBe(6);
	}})

})
