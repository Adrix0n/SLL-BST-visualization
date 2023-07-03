class SinglyLinkedList:
    class Node:
        def __init__(self,value):
            self.value = value
            self.next = None

    def __init__(self):
        self.first = None

    def __str__(self):
        result = []
        temp = self.first
        while temp is not None:
            result.append(temp.value)
            temp = temp.next
        return f'{result}'

    def asList(self):
        result = []
        temp = self.first
        while temp is not None:
            result.append(temp.value)
            temp = temp.next
        return result

    def isEmpty(self):
        return self.first == None

    def size(self):
        result = 0
        temp = self.first
        while True:
            if temp is None:
                return result
            result += 1
            temp = temp.next

    def insert(self,value):
        if self.first is None:
            self.first = self.Node(value)
            return
        if self.find(value):
            return

        temp = self.first
        if value < temp.value:
            el = self.Node(value)
            el.next = temp
            self.first = el
            return

        while True:
            if temp.next is not None:
                if value < temp.next.value:
                    el = self.Node(value)
                    el.next = temp.next
                    temp.next = el
                    return
                else:
                    temp = temp.next
            else:
                temp.next = self.Node(value)
                return

    def find(self, value):
        temp = self.first
        while True:
            if temp is None:
                return False
            if value > temp.value:
                temp = temp.next
            elif value == temp.value:
                return True
            else:
                return False

    def del_first(self):
        temp = self.first.next
        self.first = None
        self.first = temp
        return

    def delete(self, value):
        if self.find(value) is False:
            return
        temp = self.first
        if temp.value == value:
            self.first = temp.next
            return

        while True:
            if value == temp.next.value:
                temp.next = temp.next.next
                return
            else:
                temp = temp.next