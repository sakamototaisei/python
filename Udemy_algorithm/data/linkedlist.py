# リンクリスト
# Any(なんでもいいですよの意味)
from __future__ import annotations
from typing import Any


class Node(object):
    def __init__(self, data: Any, next_node: Node =None):
        self.data = data
        self.next = next_node


# 全体を管理するイメージ
class LinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any) -> Node:
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return

        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None

    def reverse_iterative(self) -> None:
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    # 上記のreverseをリカーシブルで実行
    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: Node, previous_node: Node) -> Node:
            if not current_node:
                return previous_node

            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, previous_node)

        self.head = _reverse_recursive(self.head, None)


if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    # print(l.head.data)
    # print(l.head.next.data)
    # print(l.head.next.next.data)
    # print(l.head.next.next.next.data)
    l.print()
    print('----------- Iter')
    l.reverse_iterative()
    l.print()

    print('----------- Rec')
    l.reverse_recursive()
    l.print()
