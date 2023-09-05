import operator
from base_python.data_struct.linear.stack import StackObj
from base_python.data_struct.tree.brnary_tree import BriaryTree


# 分析树创建
def build_parse_tree(fpexp):
    fplist = fpexp.split()
    p_stack = StackObj()
    e_tree = BriaryTree('')
    p_stack.push(e_tree)

    current_tree = e_tree

    for i in fplist:
        # 判断遇到'('时，插入一个空节点，将下一个值放入空节点的子节点，等待遇上符号时回填空节点的值
        if i == '(':
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        # 非计算符号和')'情况，给节点赋数字的值
        elif i not in '+-*/)':
            # eval() 允许将字符串中的数值进行计算
            current_tree.set_root_val(eval(i))
        # 计算符号
        elif i in '+-*/':
            current_tree.set_root_val(i)
            current_tree.insert_regit('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i in ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError('unknown operator: {}'.format(i))
    return e_tree


# 递归计算
def evaluate(parse_tree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_val()
