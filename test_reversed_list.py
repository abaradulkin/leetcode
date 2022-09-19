import pytest


class ListNode:
    def __init__(self, val: int = 0, link=None):
        self.val = val
        self.next = link

    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"

    def __eq__(self, other):
        return str(self) == str(other)

    @staticmethod
    def create_from_list(source: list):
        result = ListNode(0, ListNode())
        current_node = result
        for i in source:
            current_node.next = ListNode(i)
            current_node = current_node.next
        return result.next

    def create_list_from_node(self) -> list:
        result = [self.val]
        next_node = self.next
        while next_node:
            result.append(next_node.val)
            next_node = next_node.next
        return result

    def reversed(self):
        previous = None
        while self.next:
            next = self.next
            self.next = previous
            previous = self
            self = next
        self.next = previous
        return self


def test_creation_from_empty_list():
    assert ListNode.create_from_list([]) == ListNode()


def test_creation_from_list():
    assert ListNode.create_from_list([1, 2, 3]) == ListNode(1, ListNode(2, ListNode(3, None)))


def test_convert_to_list():
    assert ListNode(1, ListNode(2, ListNode(3, None))).create_list_from_node() == [1, 2, 3]


@pytest.mark.parametrize("in_list, out_list", [([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
                                               ([1, 2, 3, 2, 1], [1, 2, 3, 2, 1]),
                                               ([1, 2, 3, 4], [4, 3, 2, 1]),
                                               ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
                                               ([1], [1]),
                                               ([list(range(1000000))], [list(reversed(range(1000000)))]),
                                               ([], [])])
def test_reversed(in_list, out_list):
    assert ListNode.create_from_list(in_list).reversed() == ListNode.create_from_list(out_list)
