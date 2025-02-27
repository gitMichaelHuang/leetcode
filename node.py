# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def generate(head, length, step) -> ListNode:
    cur = head
    i = 0
    while i < length:
        cur.next = ListNode(cur.val + step)
        cur = cur.next
        i += 1
    return head

def printNodes(head):
    s = ""
    cur = head
    while cur:
        s += str(cur.val) + " -> "
        cur = cur.next
    print(s)

a = ListNode(0)
b = ListNode(2)
generate(a, 10, 1)
generate(b, 5, 2)
print("List 1")
printNodes(a)
print("List 2")
printNodes(b)


tmp = a
tmp2 = b
while tmp.next:
    if tmp == b.val:
        tmp2z = tmp2.next
        tmp.next = tmp2
        tmp2 = tmp2.next
    tmp = tmp.next


print("Merged")
printNodes(a)