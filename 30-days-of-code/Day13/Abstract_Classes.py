# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Abstract_Classes.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/08 18:24:49 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/08 18:24:55 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from abc import ABCMeta, abstractmethod

class Book(object, metaclass = ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    @abstractmethod
    def display(): pass


class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price

    def display(self):
        print('Title: ' + self.title)
        print('Author: ' + self.author)
        print('Price: ' + str(self.price))


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
