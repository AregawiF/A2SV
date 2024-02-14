class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.dummy = Node(0)
        self.homepage_n = Node(homepage)
        self.dummy.next = self.homepage_n
        self.homepage_n.prev = self.dummy
        self.curr = self.homepage_n
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        new_node = Node(url)
        new_node.prev = self.curr
        self.curr.next = new_node
        self.curr = new_node
        # return self.curr.val
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for _ in range(steps):
            if self.curr.prev == self.dummy:
                break
            self.curr = self.curr.prev
        self.curr.val
        return self.curr.val
        # for _ in range(steps):
            
        # while current:


    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for _ in range(steps):
            if not self.curr.next:
                break
            self.curr = self.curr.next
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)