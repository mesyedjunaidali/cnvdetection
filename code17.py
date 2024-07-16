class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.flag = 0  # Counter for the number of nodes in the subtree rooted at this node


def insert_node(root, new_start, new_end):
    if root is None:
        return TreeNode(new_start, new_end)

    current = root
    parent = None
    track = 0  # 0: root, 1: left subtree, 2: right subtree

    while current is not None:
        parent = current
        if new_end < current.start:
            current = current.left
            track = 1
        elif new_start > current.end:
            current = current.right
            track = 2
        elif current.start <= new_start <= current.end and new_end >= current.end:
            new_start = current.end + 1
            parent = current
            current = current.right
            track = 2
            parent.flag += 1
        elif current.start <= new_end <= current.end and new_start <= current.start:
            new_end = current.start - 1
            parent = current
            current = current.left
            track = 1
            parent.flag += 1
        else:
            left_child = TreeNode(new_start, current.start - 1)
            right_child = TreeNode(current.end + 1, new_end)
            parent = current
            current = current.left
            track = 1
            parent.flag += 1
            parent.left = left_child
            parent.right = right_child

    new_node = TreeNode(new_start, new_end)
    if track == 1:
        parent.left = new_node
    else:
        parent.right = new_node

    return root


def build_tree_from_file(file_path):
    root_node = None
    with open(file_path, 'r') as file:
        for line in file:
            start, end = map(int, line.split())
            root_node = insert_node(root_node, start, end)
    return root_node


def print_tree_iterative_to_file(root, output_file):
    stack = []
    current = root

    with open(output_file, 'w') as output:
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            output.write(f"Node: [{current.start}, {current.end}], Flag: {current.flag}\n")

            current = current.right


# Example usage:
file_path = 'cnv_segment_500.txt'
output_file_path = 'cnv_segments_flag_500.txt'
root_node = build_tree_from_file(file_path)
print_tree_iterative_to_file(root_node, output_file_path)
