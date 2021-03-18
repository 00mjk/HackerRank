# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Exceptions.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/08 19:55:27 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/08 19:55:29 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/python3

S = input().strip()

try:
    integer_value = int(S)
    print(integer_value)
except ValueError:
    print('Bad String')