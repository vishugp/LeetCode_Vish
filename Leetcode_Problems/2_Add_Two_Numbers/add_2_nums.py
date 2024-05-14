# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1:ListNode, l2: ListNode) -> ListNode:
    
        limit = [0,0]
        carry = 0
        
        while True:
            digit = 0
            if limit[0]==0: digit+=l1.val
            if limit[1]==0: digit+=l2.val

            if l1.next == None: limit[0]=1
            else: l1 = l1.next
                
            if l2.next == None: limit[1]=1
            else: l2 = l2.next

            digit += carry

            ### CARRY FORWARD
            carry = int(digit/10)
            digit = digit%10

            ### MAKE NEW LISTNODE
            new_node = ListNode(val = digit)
            try:  latest.next = new_node
            except: head = new_node

            latest = new_node

            if limit == [1,1]: break
        
        if carry>0:
            carry_node = ListNode(val = carry)
            latest.next = carry_node
            print("CARRY",latest.val, carry_node.val)

        return head
            

        
        
        # len1 = len(l1)
        # len2 = len(l2)
        # large = len1
        # if len2 > len1:
        #     large = len2

        # final = 0
        # for i in range(0,large):
        #     if i<len(l1): final += l1[i]*(10**i)
        #     if i<len(l2): final += l2[i]*(10**i)

        # return [int(i) for i in str(final)]
    

a = Solution()

ll1 = [9,9,9,9,9,9,9]
ll2 = [9,9,9,9]
l1 = [ListNode(val = v) for v in ll1]
l2 = [ListNode(val = v) for v in ll2]
for i in range(len(ll1)-1): 
    l1[i].next = l1[i+1]

for i in range(len(ll2)-1): 
    l2[i].next = l2[i+1]


answer = a.addTwoNumbers(l1[0],l2[0])
while True:
    print(answer.val)
    
    if not answer.next: break
    answer = answer.next