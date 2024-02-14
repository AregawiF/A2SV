class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList(object):

    def __init__(self):
        self.dummy = Node(0)
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        curr = self.dummy.next
        # print(1,curr.val)
        for _ in range(index):
            if not curr:
                return -1
            # print(3,curr.val)
            curr = curr.next
            # print(4,curr.val)
        # print(6, curr.val)
        return curr.val if curr else -1

    def addAtHead(self, val):
        new_node = Node(val)
        if self.size == 0:
            self.dummy.next = new_node
            self.size += 1 
        else:
            new_node.next = self.dummy.next
            self.dummy.next = new_node
            self.size += 1 

    def addAtTail(self, val):
        new_node = Node(val)
        curr = self.dummy
        if self.size == 0:
            self.dummy.next = new_node
            self.size += 1 
        else:
            while curr:
                if not curr.next:
                    break
                curr = curr.next
            curr.next = new_node
            self.size += 1
    def addAtIndex(self, index, val):
        new_node = Node(val)
        curr = self.dummy
        if index == 0:
            self.addAtHead(val)
        else:
            for _ in range(index):
                curr = curr.next
                if not curr:
                    break

            if curr:
                new_node.next = curr.next
                curr.next = new_node
                self.size += 1
        
    def deleteAtIndex(self, index):
        curr = self.dummy
        if index < self.size:    
            for _ in range(index):
                if not curr:
                    break
                curr = curr.next
            curr.next = curr.next.next
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)