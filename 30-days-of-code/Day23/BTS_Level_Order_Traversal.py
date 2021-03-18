# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    BTS_Level_Order_Traversal.py                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/08 22:26:37 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/08 22:26:38 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        nodes_to_search = list()
        nodes_to_search.append(root)
        nodes_searched = ''
        while len(nodes_to_search) > 0:
            node = nodes_to_search.pop(0)
            if node.left:
                nodes_to_search.append(node.left)
            if node.right:
                nodes_to_search.append(node.right)
            nodes_searched += str(node.data) + ' '
        print(nodes_searched)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

