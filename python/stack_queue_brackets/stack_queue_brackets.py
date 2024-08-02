from stacks_and_queues.stack import Stack


class Node3:
    def __init__(self, data, index):
        self.data = data
        self.index = index
        self.next = None


def multi_bracket_validation(validation_input: str) -> bool:
    stack = Stack()

    pairs = {
        '[': ']',
        '{': '}',
        '(': ')'
    }

    for index, char in enumerate(validation_input):
        if char in pairs.keys():
            new_node = Node3(char, index)
            stack.push(new_node)
        if char in pairs.values():
            try:
                top_data = stack.peek()
                if index < top_data.index or not top_data:
                    return False
                elif char != pairs[top_data.data]:
                    return False
                else:
                    stack.pop()
            except Exception as e:
                if str(e) == "Stack is empty":
                    pass
                else:
                    raise e

    return stack.is_empty()


if __name__ == '__main__':

    print(multi_bracket_validation("{}(){}]"))
