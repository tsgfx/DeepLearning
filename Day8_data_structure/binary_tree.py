# 作者: 郭瑞超
# 2025年01月03日10时24分21秒
# grcsxb269@163.com
class BTNode:
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class BTree:
    def __init__(self):
        self.root = BTNode()
        self.BQueue = []

    def add(self, elem):
        """
        为树添加结点
        :param elem:
        :return:
        """
        new_node = BTNode(elem)
        if self.root.elem == -1:
            self.root = new_node
            self.BQueue.append(self.root)
        else:
            tree_node = self.BQueue[0]
            if tree_node.lchild == None:
                tree_node.lchild = new_node # 放入左子树
                self.BQueue.append(tree_node.lchild)
            else:
                tree_node.rchild = new_node # 放入右子树
                self.BQueue.append(tree_node.rchild)
                self.BQueue.pop(0) # 当前结点左右子树都已添加，弹出当前结点

    def pre_order(self, root):
        """
        先序遍历
        :param root:
        :return:
        """
        if root == None: return
        print(root.elem,  end=" ")
        self.pre_order(root.lchild)
        self.pre_order(root.rchild)

    def in_order(self, root):
        """
        中序遍历
        :param root:
        :return:
        """
        if root == None: return
        self.in_order(root.lchild)
        print(root.elem, end=" ")
        self.in_order(root.rchild)

    def post_order(self, root):
        """
        后序遍历
        :param root:
        :return:
        """
        if root == None: return
        self.post_order(root.lchild)
        self.post_order(root.rchild)
        print(root.elem, end=" ")

    def level_order(self, root):
        """
        层序遍历
        :param root:
        :return:
        """
        if root == None: return
        my_queue = []
        node  = root
        my_queue.append(node)
        while my_queue:
            node = my_queue.pop(0)
            print(node.elem, end=" ")
            if node.lchild: my_queue.append(node.lchild)
            if node.rchild: my_queue.append(node.rchild)

if __name__ == '__main__':
    elems = [1, 2, 3, 4, 5, 6, 7]
    binary_tree = BTree()
    for elem in elems:
        binary_tree.add(elem)
    
    print(f"先序遍历二叉树：")
    binary_tree.pre_order(binary_tree.root)
    print()

    print(f"中序遍历二叉树：")
    binary_tree.in_order(binary_tree.root)
    print()

    print(f"后序遍历二叉树：")
    binary_tree.post_order(binary_tree.root)
    print()

    print(f"层序遍历二叉树：")
    binary_tree.level_order(binary_tree.root)
    print()

