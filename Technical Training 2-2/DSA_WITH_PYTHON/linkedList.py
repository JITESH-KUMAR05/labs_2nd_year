class ll:
    def __init__(self,u):
        self.data = u
        self.next = None

head = ll(10)
head.next = ll(20)
head.next.next = ll(30)

print(head.data)
print(head.next.data)
print(head.next.next.data)

t = head
while(t):
    print(t.data)
    t = t.next
