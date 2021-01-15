"""
Author Name : Ajay Manoj Agrawal
Github Link : https://github.com/ajayagrawal1905/DataStructure/
Date : 25-12-2020
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1
            print(count)

    # def insert_after_value(self, data_after, data_to_insert):
    #     count = 1
    #     itr = self.head
    #     while itr:
    #         count+=1
    #         if data_after == itr.next:
    #             count += 1
    #             self.insert_at(count, data_to_insert)



    # def remove_by_value(self, data):
    #     # Remove first node that contains data


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    # ll.insert_after_value("grapes", "apple")  # insert apple after mango
    # ll.print()
    # ll = LinkedList()
    # data_list = ["apples", "Mango", "Orange", "Lichi"]
    # ll.insert_values(data_list)
    # print("length:", ll.get_length())
    # ll.insert_after_value("mango","apple") # insert apple after mango
    # ll.print()
    # ll.remove_at(10)
    # ll.insert_at_end(30)
    # ll.insert_at_begining(10)
    # ll.insert_at_begining(15)
    # ll.insert_at_end(40)
    # ll.insert_at_end(234567)
    # ll.insert_at(0, "ajay")
    # ll.insert_at(3, "Rohit")
