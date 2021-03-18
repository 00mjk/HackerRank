# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    maps.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/07 14:24:27 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/07 14:24:47 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

n = int(sys.stdin.readline().strip())
phoneBook = dict()

for i in range(0, n):
    entry = sys.stdin.readline().strip().split(' ')
    phoneBook[entry[0]] = entry[1]

query = sys.stdin.readline().strip()
while query:
    phoneNumber = phoneBook.get(query)
    if phoneNumber:
        print(query + '=' + phoneNumber)
    else:
        print('Not found')
    query = sys.stdin.readline().strip()