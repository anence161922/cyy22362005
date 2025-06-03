class TreeNode:
    """二叉树节点类"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree_from_bracket(s: str) -> TreeNode:
    """
    括号表示法生成二叉树（修正版）
    :param s: 括号表示法字符串，如"A(B(C,D(E,F)),G(,H))"
    :return: 二叉树根节点
    """
    if not s:
        return None

    # 创建根节点
    root = TreeNode(s[0])
    stack = [root]
    i = 1

    while i < len(s):
        if s[i] == '(':
            # 遇到左括号，准备处理子节点
            i += 1
            # 处理左孩子
            if i < len(s) and s[i] != ',' and s[i] != ')':
                stack[-1].left = TreeNode(s[i])
                stack.append(stack[-1].left)
                i += 1
            else:
                # 左孩子为空，保留逗号
                stack.append(None)
        elif s[i] == ',':
            # 遇到逗号，处理右孩子
            i += 1
            # 弹出左孩子（可能是None）
            stack.pop()
            # 处理右孩子
            if i < len(s) and s[i] != ')' and s[i] != '(':
                stack[-1].right = TreeNode(s[i])
                stack.append(stack[-1].right)
                i += 1
            else:
                # 右孩子为空
                stack.append(None)
        elif s[i] == ')':
            # 遇到右括号，返回父节点
            stack.pop()
            i += 1
        else:
            # 处理普通字符（节点）
            i += 1

    return root


def tree_to_bracket(root: TreeNode) -> str:
    # 将传统二叉树转化为括号表示法
    if not root:
        return ""

    s = root.data

    # 当存在子节点时添加括号
    if root.left or root.right:
        s += '('
        s += tree_to_bracket(root.left)
        if root.right:
            s += ','
            s += tree_to_bracket(root.right)
        s += ')'

    return s


def bracket_depth(s: str) -> int:
    # 通过括号表示法计算二叉树深度
    depth = 1
    max_depth = 1
    i = 0

    while i < len(s):
        if s[i] == '(':
            depth += 1
            if depth > max_depth:
                max_depth = depth
        elif s[i] == ')':
            depth -= 1
        i += 1
    return max_depth


def bracket_leaf_count(s: str) -> int:
    # 通过括号表示法计算叶子节点数
    count = 0
    i = 0

    while i < len(s):
        # 检查是否是大写字母（节点）
        if 'A' <= s[i] <= 'Z':
            # 检查下一个字符是否是左括号（有子节点）
            if i + 1 >= len(s) or s[i + 1] != '(':
                count += 1
        i += 1
    return count


def bracket_level_count(s: str, target_level: int) -> int:
    # 计算二叉树特定层的节点数
    current_level = 0
    count = 0
    i = 0

    while i < len(s):
        if s[i] == '(':
            current_level += 1
        elif s[i] == ')':
            current_level -= 1
        elif 'A' <= s[i] <= 'Z':
            # 节点在目标层
            if current_level == target_level - 1:
                count += 1
        i += 1
    return count


# ===== 测试用例 =====
if __name__ == "__main__":
    # 测试用例：A(B(C,D(E,F)),G(,H))
    bracket_str = "A(B(C,D(E,F)),G(,H))"
    print(f"括号表示法: {bracket_str}")

    # 1. 从括号表示法转化为二叉树
    root = build_tree_from_bracket(bracket_str)
    print(f"构建二叉树成功! 根节点: {root.data}")

    # 2. 将二叉树转换回括号表示法
    reconstructed = tree_to_bracket(root)
    print(f"重新生成的括号表示法: {reconstructed}")

    # 3. 计算二叉树深度
    depth = bracket_depth(bracket_str)
    print(f"二叉树深度: {depth}")

    # 4. 计算叶子节点数
    leaf_count = bracket_leaf_count(bracket_str)
    print(f"叶子节点数量: {leaf_count}")

    # 5. 计算各层节点数
    for level in range(1, depth + 1):
        level_count = bracket_level_count(bracket_str, level)
        print(f"第{level}层节点数量: {level_count}")