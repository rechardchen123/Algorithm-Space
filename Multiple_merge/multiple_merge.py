'''
实现多路归并排序：
将k(k>1)个已经拍好序的数组归并成一个大的排序结果数组
'''
def two_way_merging_algo(first_list,second_list):
    '''

    :param first_list:
    :param second_list:
    :return: sorted list
    '''
    '''
    If the two lists are empty, then return an empty list.
    or if one of the list is empty, then return the other.
    '''
    if not first_list and not second_list:
        return []
    elif not first_list:
        return second_list
    elif not second_list:
        return first_list

    '''
    If condition to reduce the emelemt comparisons of the algorithm
    '''
    '''
    initialize the output array:
    '''
    output = []

    if first_list[len(first_list)-1]<second_list[0]:
        output.extend(first_list)
        output.extend(second_list)
        '''
        return statement
        '''
        return output

    '''
    while loop to tackle the main operations of the algorithm
    '''
    while first_list and second_list:
        if first_list[0]<second_list[0]:
            output.append(first_list.pop(0))
        elif first_list[0]==second_list[0]:
            output.append(first_list.pop(0))
            del second_list[0]
        else:
            output.append(second_list.pop(0))
    # end while loop
    '''
    append the non-empty list to the output
    '''
    if not first_list:
        output.extend(second_list)
    else:
        output.extend(first_list)
    '''
    return statement
    '''
    return output

if __name__=='__main__':
    print("2-way merging algorithm in python:")
    print(two_way_merging_algo([2,3,4,6],[1,6,9]))

