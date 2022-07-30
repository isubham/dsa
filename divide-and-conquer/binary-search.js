
/**
 * @param {Array<object>} nums
 * @params {object} key
 * @returns {Number} [-1, nums.lengh]
 */

const search = (nums, key, leftIndex, rightIndex, comparisonFn) => {
    const middle = Math.round((leftIndex + rightIndex) / 2);
    console.log(middle)
    switch (comparisonFn(nums[middle], key)) {
        case 0: return middle;break;
        case -1: return search(nums, key, leftIndex, middle, comparisonFn); break;
        case 1: return search(nums, key, middle, rightIndex, comparisonFn); break;
    }
    return -1;
};

const binary_search = (nums, key, comparisonFn) => {
    return search(nums, key, 0, nums.length, comparisonFn);
}

const comparisonFnNumber = (numA, numB) => {
    if (numA === numB) {
        return 0;
    }
    else if (numA > numB) {
        return 1;
    }
    else {
        return -1;
    }
}

console.log(binary_search([1, 2, 3, 5, 7], 7, comparisonFnNumber) == 4)
console.log(binary_search([1, 2, 3, 5, 7], 3, comparisonFnNumber) == 2)
console.log(binary_search([1, 2, 3, 5, 7], 10, comparisonFnNumber) == -1)
console.log(binary_search([1, 2, 3, 5, 7], -1, comparisonFnNumber) == -1)




