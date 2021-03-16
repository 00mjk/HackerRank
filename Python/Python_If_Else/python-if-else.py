# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    python-if-else.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/15 16:19:19 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/15 16:19:21 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/python3

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and n in range(2, 6):
        print("Not Weird")
    elif n % 2 == 0 and n in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")