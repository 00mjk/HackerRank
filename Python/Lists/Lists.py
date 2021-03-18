# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Lists.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/18 20:13:51 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/18 20:13:53 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash

def handler(result):
    inp = input().split()
    command = inp[0]
    values = inp[1:]
    if command == 'print':
        print(result)
    else:
        execute = 'result.' + command + "(" + ",".join(values) + ")"
        eval(execute)


result = []
for i in range(int(input())):
    handler(result)
