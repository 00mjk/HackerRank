# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Review.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/06 17:32:56 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/06 18:25:27 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash 

T = int(input())

for i in range(T):
    string = str(input())
    even = ""
    odd = ""

    for j in range(len(string)):
        if j % 2 == 0:
            even += string[j]
            else:
                odd += string[j]
    print('{} {}'.fotmat(even, odd))


