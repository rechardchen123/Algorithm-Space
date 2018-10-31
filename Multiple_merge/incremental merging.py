from multiple_merge import two_way_merging_algo

def inc_two_way_merging(arrays):
    '''

    :param arrays:
    :return:list of sorted elements from the input lists
    '''
# if the input lists are only one list, then return that list
    if len(arrays)==1:
        return arrays[0]

#initialize the output list
    output = []

    while len(arrays)>0:
        output = two_way_merging_algo(output,arrays.pop(0))

    '''
    :return statement
    '''
    return output

if __name__ == '__main__':
    print("incremental iterative 2-way merging in python:")
    print(inc_two_way_merging([[1, 5, 9], [3, 6, 20], [11, 14, 22]]))