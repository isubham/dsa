a = [1,3,4,2,5,10]
'''
input:

[1,3,4,2,5]



output:

				*
		*		*
	*	*		*
	*	*	*	*
*	*	*	*	*



'''


def vertical_pattern(sequence):
    max_seq = max(sequence)
    a = [
            list(reversed(
                [
            '*' if i < num else ' ' 
            for i in range(max_seq)
            ]
            )) 
            for num in sequence]

    for i in range(len(sequence)):
        for j in range(max_seq):
            print('test', j, i)
            print(a[j][i], '\t', end='')
        print('')


vertical_pattern(a)

