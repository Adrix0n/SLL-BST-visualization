class BST:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.children = [left, right]

    def __init__(self):
        self.root = None
        self.size = 0


    def is_empty(self):
        return self.root is None

    def add(self, value):
        if self.is_empty():
            self.root = BST.Node(value)
            self.size += 1
            return 0

        if self.find(value):
            return -1

        tmp = self.root

        while True:
            if tmp.data == value:
                return 0
            if value > tmp.data:
                if tmp.children[1] is None:
                    tmp.children[1] = BST.Node(value)
                    self.size += 1
                tmp = tmp.children[1]
            if value < tmp.data:
                if tmp.children[0] is None:
                    tmp.children[0] = BST.Node(value)
                    self.size += 1
                tmp = tmp.children[0]

    def delete(self, value):
        if self.is_empty():
            return -1

        if not self.find(value):
            return -1

        is_root = False
        if self.root.data == value:
            self.root = self.Node(self.root.data + 1000, left=self.root, right=None)
            is_root = True
        tmp = self.root

        while True:
            if value < tmp.data:
                if value == tmp.children[0].data:
                    if tmp.children[0].children[0] is None and tmp.children[0].children[1] is None:
                        tmp.children[0] = None
                    elif tmp.children[0].children[0] is not None and tmp.children[0].children[1] is None:
                        tmp.children[0] = tmp.children[0].children[0]
                    elif tmp.children[0].children[0] is None and tmp.children[0].children[1] is not None:
                        tmp.children[0] = tmp.children[0].children[1]
                    else:
                        tmp2 = tmp.children[0]
                        if tmp2.children[1].children[0] is None:
                            tmp.children[0].data = tmp2.children[1].data
                            tmp2.children[1] = tmp2.children[1].children[1]
                        else:
                            tmp2 = tmp2.children[1]
                            while tmp2.children[0].children[0] is not None:
                                tmp2 = tmp2.children[0]
                            tmp.children[0].data = tmp2.children[0].data
                            tmp2.children[0] = tmp2.children[0].children[1]
                        # print("left")
                    break
                else:
                    tmp = tmp.children[0]
            elif value > tmp.data:
                if value == tmp.children[1].data:
                    if tmp.children[1].children[0] is None and tmp.children[1].children[1] is None:
                        tmp.children[1] = None
                    elif tmp.children[1].children[0] is not None and tmp.children[1].children[1] is None:
                        tmp.children[1] = tmp.children[1].children[0]
                    elif tmp.children[1].children[0] is None and tmp.children[1].children[1] is not None:
                        tmp.children[1] = tmp.children[1].children[1]
                    else:
                        tmp2 = tmp.children[1]
                        if tmp2.children[1].children[0] is None:
                            tmp.children[1].data = tmp2.children[1].data
                            tmp2.children[1] = tmp2.children[1].children[1]
                        else:
                            tmp2 = tmp2.children[1]
                            while tmp2.children[0].children[0] is not None:
                                tmp2 = tmp2.children[0]
                            tmp.children[1].data = tmp2.children[0].data
                            tmp2.children[0] = tmp2.children[0].children[1]
                        # print("right")
                    break
                else:
                    tmp = tmp.children[1]
            else:
                print("Cos tu nie gra")

        if is_root:
            self.root = self.root.children[0]
        self.size -= 1

        return 0

    #
    # def delete_cale(self):
    #     if self.root is None:
    #         return
    #
    #     tmp = self.root
    #
    #     def _delete_cale(tmp):
    #         if tmp.children[1].children[1] is not None:
    #             _delete_cale(tmp.children[1])
    #         if tmp.children[1].children[0] is not None:
    #             tmp = tmp.children[1]
    #             _delete_cale(tmp)
    #         tmp.children[1] = None
    #         #Jebać to
    #
    #     _delete_cale(tmp)

    def delete_entire_tree(self):
        if self.root is None:
            return
        tmp = self.root

        def _delete_entire_tree(tmp):
            if tmp is None:
                return
            _delete_entire_tree(tmp.children[1])
            _delete_entire_tree(tmp.children[0])
            tmp.children[1] = None
            tmp.children[0] = None
            return

        _delete_entire_tree(tmp)
        self.root = None
        self.size = 0

    def find(self, value):
        if self.is_empty():
            return False

        temp = self.root
        while True:
            if temp is None:
                return False
            if value > temp.data:
                temp = temp.children[1]
            elif value < temp.data:
                temp = temp.children[0]
            else:
                return True

    def find_tkinter(self, value):
        result = ''
        if self.is_empty():
            return result

        temp = self.root
        while True:
            if temp is None:
                #Tu może być błąd
                return result
            if value > temp.data:
                temp = temp.children[1]
                result += 'p'
            elif value < temp.data:
                temp = temp.children[0]
                result += 'l'
            else:
                return result

    def print_out(self):
        if self.is_empty():
            return []
        tmp = self.root

        def print_out_rec(tmp, res):
            if tmp.children[0] is not None:
                print_out_rec(tmp.children[0], res)
            res.append(tmp.data)
            if tmp.children[1] is not None:
                print_out_rec(tmp.children[1], res)
            return res

        return print_out_rec(tmp, [])

    def print_out_preorder(self):
        if self.is_empty():
            return []
        tmp = self.root

        def print_out_preorder_rec(tmp, res):
            res.append(tmp.data)
            if tmp.children[0] is not None:
                print_out_preorder_rec(tmp.children[0], res)
            if tmp.children[1] is not None:
                print_out_preorder_rec(tmp.children[1], res)
            return res

        return print_out_preorder_rec(tmp, [])

    def print_out_postorder(self):
        if self.is_empty():
            return []
        tmp = self.root

        def print_out_postorder_rec(tmp, res):
            if tmp.children[0] is not None:
                print_out_postorder_rec(tmp.children[0], res)
            if tmp.children[1] is not None:
                print_out_postorder_rec(tmp.children[1], res)
            res.append(tmp.data)
            return res

        return print_out_postorder_rec(tmp, [])


    def height(self):
        tmp = self.root

        def _height(tmp):
            if tmp is None:
                return 0
            left = tmp.children[0]
            right = tmp.children[1]
            return 1 + max(_height(left), _height(right))

        return _height(tmp)

    def balance(self):
        A = self.print_out()
        self.root = self.Node(None)

        def _balance(tmp, A):
            if len(A) == 0:
                return
            p = len(A) // 2
            tmp.data = A[p]
            tmp.children[0] = BST.Node(None)
            _balance(tmp.children[0], A[:p])
            if tmp.children[0].data is None:
                tmp.children[0] = None
            if p + 1 < len(A):
                tmp.children[1] = BST.Node(None)
                _balance(tmp.children[1], A[p + 1:])
            return

        _balance(self.root, A)
        return


# tree = BST()
# for i in range(40):
#     tree.add(random.randint(-100, 100))
# tree.add(0)
# print(tree.print_out())
# tree.delete(35)
# for i in range(20):
#     rand = random.randint(-100, 100)
#     tree.delete(rand)
#     print(tree.print_out())
#
# print(tree.print_out())
# print(tree.height())
# tree.balance()
# print(tree.height())
# print(tree.print_out())
# tree.delete_entire_tree()
# print(tree.print_out())
# print(tree.height())
