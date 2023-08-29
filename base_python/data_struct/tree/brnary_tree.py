class BriaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BriaryTree(new_node)
        else:
            t = BriaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_regit(self, new_node):
        if self.right_child is None:
            self.right_child = BriaryTree(new_node)
        else:
            t = BriaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_root_val(self):
        return self.key

    def set_root_val(self, val):
        self.key = val

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child


if __name__ == '__main__':
    r = BriaryTree('a')
    print(r.get_root_val())
