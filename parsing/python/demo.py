import os
import ast
import traceback

# print(os.sys.argv)
# print(os.sys.argv[0])
file_input = os.sys.argv[1]
print(file_input)


class Visitor(ast.NodeVisitor):
    def visit_ClassDef(self, node):
        # 访问类定义
        print(f"Class: {node.name}")
        self.generic_visit(node)  # 继续访问类内的节点

    def visit_FunctionDef(self, node):
        # 访问函数定义
        print(f"Function: {node.name}")
        self.generic_visit(node)  # 继续访问函数内的节点

    def visit_Call(self, node):
        # 访问函数调用
        if isinstance(node.func, ast.Name):
            # 如果调用的是普通函数，打印函数名
            print(f"Function call: {node.func.id}")
        elif isinstance(node.func, ast.Attribute):
            # 如果调用的是类的方法，打印类名和方法名
            # print(f"Method call: {node.func}.{node.func.attr}")
            print(f"Method call on {node.func.value.id if isinstance(node.func.value, ast.Name) else '<expression>'}: {node.func.attr}")
        self.generic_visit(node)  # 继续访问函数调用内的节点



try:
    # 读取Python源代码文件
    with open(file_input, 'r', encoding='utf-8') as file:
        source_code = file.read()

    # 解析源代码为AST
    parsed_ast = ast.parse(source_code)

    all_node_type = set()
    # 遍历AST
    for node in ast.walk(parsed_ast):
        all_node_type.add(type(node))
        # 打印每个节点的类型和内容
        # print(f"{type(node)} --> {ast.dump(node, annotate_fields=False)}")
    all_node_type_list = list(all_node_type)
    all_node_type_list.sort(key=lambda x:str(x))
    # all_node_type_list.sort(key=lambda x:str(x).lower())
    for i in all_node_type_list:
        print(i)
    
    all_node_list = [x for x in ast.walk(parsed_ast)  if 'Name' in str(type(x))]
    # print(all_node)
    # # 遍历AST
    # for node in ast.walk(parsed_ast):
    #     all_node.add(node)
    #     # 打印每个节点的类型和内容
    #     # print(f"{type(node)} --> {ast.dump(node, annotate_fields=False)}")
    # all_node_list = list(all_node)
    # all_node_list.sort(key=lambda x:str(type(x)))
    with open('tmp.log', 'w') as fp:
        for i in all_node_list:
            print(ast.dump(i))
            fp.write(f"{ast.dump(i)}\n")
    # [print(ast.dump(i)) for i in all_node_list if 'Name' in str(type(i))]

    print("")
    print("-"*16)
    print("")
    # 创建Visitor实例并遍历AST
    visitor = Visitor()
    visitor.visit(parsed_ast)

except Exception as err:
    print(err)
    print(traceback.format_exc())

finally:
    input()
