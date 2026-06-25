# Definition for singly-linked list.
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_ll(self, listo): 
        hold = ListNode(0)
        current = hold

        for i in listo:
            current.next = ListNode(i)
            current = current.next

        return hold.next
"""
class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """        
        
        listy1 = []         #create blank lists
        listy2 = []

        current1 = l1       #create holders for linked lists passed as arguments
        current2 = l2

        while current1 is not None:             #convert linked lists to regular lists
            listy1.append(current1.val)
            current1 = current1.next

        while current2 is not None:
            listy2.append(current2.val)
            current2 = current2.next


        listy1.reverse()            #reverse lists
        listy2.reverse()

        num1 = int("".join(map(str, listy1)))           #convert lists to ints
        num2 = int("".join(map(str, listy2)))

        final_num = num1 + num2                         #add ints together for final int

        final_list = list((map(int, str(final_num))))       #convert int to a list

        final_list.reverse()                            #reverse list

        hold = ListNode(0)                  #convert to linked list

        current = hold

        for i in final_list:
            current.next = ListNode(i)
            current = current.next

        return hold.next                #return final list
        
    

        
