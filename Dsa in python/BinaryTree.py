class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

head= TreeNode(3)
left=TreeNode(4)
right=TreeNode(5)
head.left=left
head.right=right
secondleft=TreeNode(100)
left.left=secondleft

def max(a,b):
    if a>=b:
        return a
    else:
        return b


def max_height(root):
    if not root:
        return 0
    left=max_height(root.left)
    right=max_height(root.left)

    return max(left,right)+1

print(max_height(head))