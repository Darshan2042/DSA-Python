class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # move 1 step
        fast = fast.next.next     # move 2 steps
        
        if slow == fast:
            return True           # cycle detected

    return False                  # no cycle

head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)

head.next = second
second.next = third
third.next = fourth

# 🔁 Create cycle (4 → 2)
fourth.next = second

# 🔹 Call function
print(hasCycle(head))