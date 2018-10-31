from multiple_merge import two_way_merging_algo

def seq_two_way_merging(arrays):
    '''

    :param arrays:
    :return: list of sorted elements from the input lists
    '''
# if the input lists are only one lists, then return that list
    if len(arrays)==1:
        return arrays[0]
#initialize the output list
    output=[]
    while(len(arrays)>1):
        first_list = arrays.pop(0)
        second_list = arrays.pop(0)
        output.extend(two_way_merging_algo(first_list,second_list))

    if arrays:
        output = two_way_merging_algo(output,arrays[0])

        return output

print("sequential iterative 2-way merging in python:")
print(seq_two_way_merging([[1,5,9],[11,15,19],[35,37,39]]))