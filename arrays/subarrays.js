/**
[1, 2, 3] => [[1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]
[100]
[010]
[001]

[110]
[011]

[111]
*/

const getSubArrays = (arr) =>
{
	let subarrays = [];
	for (let size = 1; size <= arr.length; size++) 
	{
		for (let item = 0; item < arr.length - size; item++)
		{
			console.log(size, item)
		}
	}
	return subArrays;
}

export { getSubArrays };
