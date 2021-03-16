# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Write_A_Function.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/16 19:20:38 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/16 19:20:40 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash

def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0 :
        return False
    if year % 4 == 0 :
        return True
    return False

year = int(input())
print(is_leap(year))