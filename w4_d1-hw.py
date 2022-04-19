class Node:
    def __init__(self, value, node=None):
        self.value = value
        self.next_node = node
        self.prev_node = None


    def get_value(self):
        return self.value

    def set_value(self, new_value):
        set.value = new_value


    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, node):
        self.next_node = node


    def __repr__(self) -> str:
        return f'<Node: {self.value}>'
        

class DoublyLinkedList:
    def __init__(self, root=None):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add_to_list(self, number):
        new_node = Node(number)
        new_node.next = self.head
        self.root = new_node
        # self.size += 1

        if self.head == None:
            new_node = Node(number)
            self.head = new_node
        else:
            return 'False'

    def add_to_end(self, number):
        if self.head == None:
            new_node = Node(number, self.head)
            self.head = new_node
            return
        place = self.head
        while place.next != None:
            place = place.next_node
        new_node = Node(number + 1)
        place.next = new_node
        new_node.prev = place


    def remove_from_front(self, number):
        current_node = self.head
    #     previous_node = None
        if self.head == None:
                return 'Empty'
        while current_node.get.value() != number: 
            #   self.head.prev = new_node
            if self.prev: 
                self.prev.next_node(current_node.get_next.node)        self.prev = None

    def remove_from_end(self):
        current_node = self.tail
    #     previous_node = None
        if self.tail == None:
                return 'Empty'
        if self.tail.next_node != None: 
            self.tail == None
            #   self.head.prev = new_node
            place = self.tail
        while place.next_node != None:
            place = place.next_node
        # self.head = self.head.next_node
        place.prev.next_node = None


    

                
    #                 previous_node.set_next_node(current_node.get_next_node())
    #             else:
    #                 self.root = current_node.get_next_node()
    #             self.size -= 1
    #             return 'Removed'
    #         else:
    #             self.root = current_node
    #             previous_node = current_node.get_next_node()
    #         return 'Node not found'

    # def find(self,number):
    #     current_node = self.root
    #     previous_node = None
         
    #     while current_node:
    #         if current_node.get.value() == number:
    #             return True
    #         else:
    #             current_node = current_node.get_next_node()
    #             return False

    # def get_root(self):
    #     return self.root

    # def get_size(self):
    #     return self.size


        
    


# l1 = ["tim", 1, "Derek", 2, "Sam"]
