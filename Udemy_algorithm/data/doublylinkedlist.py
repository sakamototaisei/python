# 双方向リンクリスト
from __future__ import annotations
from typing import Any, Optional


class Node(object):
    def __init__(self, data: Any, next_node: Node = None, prev_node: Node = None) -> None:
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList(object):

    def __init__(self, head: Node = None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any) -> None:
        current_node = self.head
        # 先頭を削除
        if current_node and current_node.data == data:
            if current_node.next is None:
                current_node = None
                self.head = None
                return
            else:
                next_node = current_node.next
                next_node.prev = None
                current_node = None
                self.head = next_node
                return

        # 途中のdataを削除するために検索をかける
        while current_node and current_node.data != data:
            current_node = current_node.next

        if current_node is None:
            return
        # 最後のdataの削除
        if current_node.next is None:
            prev = current_node.prev
            prev.next = None
            current_node = None
            return
        # 途中のdataの削除
        else:
            next_node = current_node.next
            prev_node = current_node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            current_node = None
            return

    def reverse_iterative(self) -> None:
        previous_node = None
        current_node = self.head
        while current_node:
            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node
            # リバースさせているから次のNodeはprev
            current_node = current_node.prev
        # previous_nodeがある場合
        if previous_node:
            # リバースさせてるから最後のprevがheadになる
            self.head = previous_node.prev

    # 上記のリカーシブ
    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: None) -> Optional[None]:
            if not current_node:
                return None

            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node

            if current_node.prev is None:
                return current_node

            return _reverse_recursive(current_node.prev)

        self.head = _reverse_recursive(self.head)

    # 双方向リストのソート
    def sort(self) -> None:
        if self.head is None:
            return

        current_node = self.head
        while current_node.next:
            next_node = current_node.next
            while next_node:
                if current_node.data > next_node.data:
                    current_node.data, next_node.data = next_node.data, current_node.data
                next_node = next_node.next

            current_node = current_node.next





if __name__ == '__main__':
    d = DoublyLinkedList()
    d.append(1)
    d.append(5)
    d.append(2)
    d.append(9)
    d.print()
    print('----------')
    d.sort()
    d.print()


