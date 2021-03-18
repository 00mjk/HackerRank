# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Linked_List.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/08 18:54:13 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/08 18:54:15 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self, head, data):
        newNode = Node(data)
        if not head:
            return newNode
        current = head
        while current.next:
            current = current.next
        current.next = newNode
        return head
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  