# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Recursion.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/07 14:37:56 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/07 14:38:11 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/python3

import math
import os
import random
import re
import sys

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
