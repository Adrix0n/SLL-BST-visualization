from tkinter import *
import BST as BST
import SinglyLinkedList

WIDTH_FRAME_TREE = 400
HEIGHT_FRAME_TREE = 400
TICK_TIME = 250

root = Tk()
root.title('Program')
root.geometry(f"{WIDTH_FRAME_TREE + 250}x{HEIGHT_FRAME_TREE}")

fr_tree = LabelFrame(root, height=HEIGHT_FRAME_TREE, width=WIDTH_FRAME_TREE)
fr_left = LabelFrame(root, height=400, width=200)

cnv_tree = Canvas(fr_tree, width=WIDTH_FRAME_TREE, height=HEIGHT_FRAME_TREE)

fr_tree.grid(row=0, column=1, sticky=NSEW)
fr_left.grid(row=0, column=0, sticky=NSEW)

tree = BST.BST()
list_SLL = SinglyLinkedList.SinglyLinkedList()

lb_error = Label(fr_tree, text="Tree is too height!")


def print_out_tree():
    cnv_tree.delete("all")
    list_paths = []

    if tree.height() > 5:
        cnv_tree.create_window(WIDTH_FRAME_TREE // 2, HEIGHT_FRAME_TREE // 2, anchor=CENTER,
                                 window=lb_error)
        return

    list_el = tree.print_out()
    for i in range(tree.size):
        x = WIDTH_FRAME_TREE // 2
        y = 0
        idx = 0
        path = tree.find_tkinter(list_el[i])
        list_paths.append([path, 0, 0])

        for j in path:
            if j == 'p':
                x += 0.95 * WIDTH_FRAME_TREE // (2 ** (idx + 2))
            elif j == 'l':
                x -= 0.95 * WIDTH_FRAME_TREE // (2 ** (idx + 2))
            y += HEIGHT_FRAME_TREE // 5
            idx += 1

        list_paths[i][1] = x
        list_paths[i][2] = y

        cnv_tree.create_window(x, y, anchor=N, window=Label(fr_tree, text=list_el[i]))

    # Tworzenie i wstawianie linii
    for i in range(len(list_paths)):
        x_1 = list_paths[i][1]
        y_1 = list_paths[i][2]
        wys_1 = len(list_paths[i][0])
        for j in range(i + 1, len(list_paths)):
            x_2 = list_paths[j][1]
            y_2 = list_paths[j][2]
            wys_2 = len(list_paths[j][0])
            if abs(wys_1 - wys_2) != 1:
                # print("Pominieto")
                continue
            diff_x = WIDTH_FRAME_TREE // 4
            idx = 0
            for i in range(max(wys_1, wys_2)):
                diff_x = 0.95 * WIDTH_FRAME_TREE // (2 ** (idx + 2))
                idx += 1

            print(x_1, x_2, diff_x)
            if abs(abs(x_1 - x_2) - diff_x) == 0:
                cnv_tree.create_line(x_1, y_1, x_2, y_2)

    cnv_tree.pack()


def add_el(value):
    if value == '':
        return
    if tree.add(int(value)) == 0:
        print_out_tree()
    return


def delete_el(value):
    if value == '':
        return
    if tree.delete(int(value)) == 0:
        print_out_tree()
    return


def add_el_list(list):
    if list == '':
        return
    if list[0] == '[':
        list = list[1:-1]
    list = [int(x) for x in list.split(',')]

    def _add_el(list2):
        if list2 == []:
            return
        add_el(list2[0])
        lb_error.after(TICK_TIME, lambda: _add_el(list2[1:]))

    _add_el(list)
    return


def balance():
    tree.balance()
    print_out_tree()
    return


def delete_list_el(list):
    if list == []:
        return
    delete_el(list[0])
    lb_error.after(TICK_TIME, lambda: delete_list_el(list[1:]))
    return


def print_out_list_SLL():
    cnv_tree.delete("all")
    # Tworzenie i umieszczanie liczb
    size = list_SLL.size()
    x = WIDTH_FRAME_TREE // (size + 1)
    y = HEIGHT_FRAME_TREE // 2
    list_el = list_SLL.asList()
    idx = 0
    for i in range(x, WIDTH_FRAME_TREE - x + 10, x):
        cnv_tree.create_window(i, y, window=Label(fr_tree, text=list_el[idx]))
        idx += 1

    # Tworzenie i umieszczanie linii
    for i in range(x, WIDTH_FRAME_TREE - 2 * x + 10, x):
        cnv_tree.create_line(i, y, i + x, y)

    cnv_tree.place(x=0, y=0)


def add_el_SLL(value):
    if value == '':
        return
    size = list_SLL.size()
    x = (WIDTH_FRAME_TREE // (size + 1)) // 2
    y = HEIGHT_FRAME_TREE // 2 - 50
    lb_element = Label(fr_tree, text=value)
    print_out_list_SLL()
    cnv_tree.create_window(x, y, window=lb_element)
    cnv_tree.create_line(x, y, x, y + 30, arrow=LAST)

    value = int(value)
    list_el = list_SLL.asList()

    def move_cursor(list, value, x, y, krok):
        print_out_list_SLL()
        cnv_tree.create_window(x + krok, y, window=lb_element)
        cnv_tree.create_line(x + krok, y, x + krok, y + 30, arrow=LAST)
        if list == [] or value <= list[0]:
            list_SLL.insert(value)
            print_out_list_SLL()
            return

        lb_error.after(TICK_TIME, lambda: move_cursor(list[1:], value, x + krok, y, krok))
        return

    lb_error.after(TICK_TIME, lambda: move_cursor(list_el, value, x, y, 2 * x))
    return


def delete_el_SLL(value):
    if value == '':
        return
    size = list_SLL.size()
    x = (WIDTH_FRAME_TREE // (size + 1))
    y = HEIGHT_FRAME_TREE // 2 - 50
    lb_element = Label(fr_tree, text=value)
    print_out_list_SLL()
    cnv_tree.create_window(x, y, window=lb_element)
    cnv_tree.create_line(x, y, x, y + 30, arrow=LAST)

    value = int(value)
    list_el = list_SLL.asList()

    def move_cursor(list, value, x, y, krok):
        print_out_list_SLL()
        cnv_tree.create_window(x + krok, y, window=lb_element)
        cnv_tree.create_line(x + krok, y, x + krok, y + 30, arrow=LAST)
        if list == [] or value == list[0]:
            list_SLL.delete(value)
            print_out_list_SLL()
            return

        lb_error.after(TICK_TIME, lambda: move_cursor(list[1:], value, x + krok, y, krok))
        return

    lb_error.after(TICK_TIME, lambda: move_cursor(list_el, value, x, y, x))
    return


def add_el_list_SLL(list):
    if list == '':
        return
    if list[0] == '[':
        list = list[1:-1]
    list = [int(x) for x in list.split(',')]

    def _add_el(list2):
        if list2 == []:
            return
        list_SLL.insert(list2[0])
        print_out_list_SLL()
        lb_error.after(TICK_TIME // 2, lambda: _add_el(list2[1:]))

    lb_error.after(TICK_TIME // 2, lambda: _add_el(list))


def delete_list_el_SLL(list):
    if list == []:
        return
    delete_el_SLL(list[0])
    lb_error.after(TICK_TIME, lambda: delete_list_el_SLL(list[1:]))
    return


def change_object(name):
    if name == "BST":
        print_out_tree()
        bt_balance.config(state=ACTIVE)
        bt_delete_preorder.config(state=ACTIVE)
        bt_delete_postorder.config(state=ACTIVE)
        bt_delete_inorder.config(text="Delete inorder", command=lambda: delete_list_el(tree.print_out()))
        bt_add_el.config(command=lambda: add_el(en_add_el.get()))
        bt_delete_el.config(command=lambda: delete_el(en_delete_el.get()))
        bt_add_list.config(command=lambda: add_el_list(en_add_list.get()))

    elif name == "SLL":
        print_out_list_SLL()
        bt_balance.config(state=DISABLED)
        bt_delete_preorder.config(state=DISABLED)
        bt_delete_postorder.config(state=DISABLED)
        bt_delete_inorder.config(text="Delete in sequence", command=lambda: delete_list_el_SLL(list_SLL.asList()))
        bt_add_el.config(command=lambda: add_el_SLL(en_add_el.get()))
        bt_delete_el.config(command=lambda: delete_el_SLL(en_delete_el.get()))
        bt_add_list.config(command=lambda: add_el_list_SLL(en_add_list.get()))


options = ["BST", "SLL"]

choice = StringVar()
choice.set(options[0])

dp_list_objects = OptionMenu(fr_left, choice, *options, command=change_object)

bt_add_el = Button(fr_left, text="Add element", command=lambda: add_el(en_add_el.get()))
en_add_el = Entry(fr_left)

bt_delete_el = Button(fr_left, text="Delete element", command=lambda: delete_el(en_delete_el.get()))
en_delete_el = Entry(fr_left)

bt_add_list = Button(fr_left, text="Add list of values", command=lambda: add_el_list(en_add_list.get()))
en_add_list = Entry(fr_left)

bt_balance = Button(fr_left, text="Balance", command=balance)
bt_delete_inorder = Button(fr_left, text="Delete inorder", command=lambda: delete_list_el(tree.print_out()))
bt_delete_preorder = Button(fr_left, text="Delete preorder", command=lambda: delete_list_el(tree.print_out_preorder()))
bt_delete_postorder = Button(fr_left, text="Delete postorder", command=lambda: delete_list_el(tree.print_out_postorder()))

lb_wyswietlacz_el = Label(fr_left, text="")

dp_list_objects.grid(row=0, column=0, columnspan=2, sticky=W)

bt_add_el.grid(row=1, column=0, sticky=EW)
en_add_el.grid(row=2, column=0, sticky=EW)
bt_delete_el.grid(row=1, column=1, sticky=EW)
en_delete_el.grid(row=2, column=1, sticky=EW)

bt_add_list.grid(row=3, column=0, sticky=EW)
en_add_list.grid(row=4, column=0, sticky=EW)

bt_delete_inorder.grid(row=5, column=1, sticky=EW)
bt_balance.grid(row=5, column=0, sticky=EW)
bt_delete_preorder.grid(row=6, column=0, sticky=EW)
bt_delete_postorder.grid(row=6, column=1, sticky=EW)

lb_wyswietlacz_el.grid(row=7, column=0, sticky=EW)

root.mainloop()
