import  math

class heap_for_merge:
    '''
    This class is to heapify a list of lists
    '''
    arrays=[]

    def __init__(self,arrays):
        '''
        class initializer
        :param arrays:
        '''
        self.arrays = arrays
    def heapify_sify_dowm(self):
        '''
        :param self
        :return: the self.arrays is passed by reference. Hence, it is heapified
        '''
        for index in range(int(math.ceil(len(self.arrays)/2)),-1,-1):
            self.sift_down(index)

    def heapify_sift_up(self):
        '''
        :param self
        :return: the self.arrays is passed by reference. Hence, it is heapified
        '''
        for index in range(len(self.arrays)):
            self.sift_up(index)

    def sift_down(self,index):
        '''

        :param index:
        :return:array element indexed at index is heapified with sift down
        '''
        left_child = 2* index +1
        right_child = left_child+1
        while left_child<len(self.arrays):
            if self.arrays[left_child][0]<self.arrays[right_child][0]:
                #get the biggest from left and right children
                self.swap(self.arrays,left_child,right_child)

            if self.arrays[left_child][0]>self.arrays[index][0]:
                self.swap(self.arrays,index,left_child)

            else:
                break
            index = left_child
            left_child = 2*left_child+1
            right_child = left_child+1
    def sift_up(self,index):
        '''

        :param index:
        :return:
        '''
        parent = math.floor(index / 2)
        while parent >= 0:
            if self.arrays[parent][0] < self.arrays[index][0]:
                self.swap(self.arrays, parent, index)
            else:
                break
            index = parent
            parent = math.floor(index / 2)

    def insert_first(self, array):
        """
        :param self:
        :param array:
        :return: self array gains an array at first position
        """
        self.arrays.insert(0, array)
        self.heapify_sift_down()

    def insert_last(self, array):
        """
        :param self:
        :param array:
        :return: self.array gains an array at the last position
        """
        self.arrays.append(array)
        self.heapify_sift_down()

    def insert(self, index, array):
        """
        :param index:
        :param array:
        :return: self.arrays gains an array element in index position
        """
        self.arrays.insert(index, array)
        self.heapify_sift_down()

    def delete(self, index):
        """
        :param index:
        :return: self.arrays with element deleted at index
        """
        del (self.arrays[index])
        self.heapify_sift_down()

    def delete_min(self):
        """
        :return: the first array of self.arrays is popped up
        """

        array = self.arrays.pop(0)
        self.heapify_sift_down()
        return array

    def delete_element(self, element):
        """
        :param element:
        :return: self.arrays with element removed
        """
        self.arrays.remove(element)
        self.heapify_sift_down()

    def get_container_array(self):
        """
        :return: self.arrays is returned
        """
        return self.arrays

    def set_container_array(self, arrays):
        """
        set the container array attribute of the class
        :param arrays:
        :return: the arrays attribute of the object
        """
        self.arrays = arrays

    def sort(self):
        """
        :return: sorted arrays from self.arrays
        """
        sorted_arrays = [[]]
        while not self.arrays:
            sorted_arrays.append(self.arrays.pop)
        return sorted_arrays

    @staticmethod
    def swap(arrays, first_index, second_index):
        """
        :param arrays:
        :param first_index:
        :param second_index:
        :return: swaps two elements from an array
        """
        arrays[first_index], arrays[second_index] = arrays[second_index], arrays[first_index]


arrays = heap_for_merge([[0, 4], [8, 4], [7, 5], [4, 9], [1, 6], [12, 5], [11, 4], [20, 10], [22, 1]])

print(arrays.arrays)

arrays.heapify_sift_up()

print(arrays.arrays)
