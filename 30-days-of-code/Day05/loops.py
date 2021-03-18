# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loops.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/06 16:54:41 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/06 17:28:41 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash 

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    for i in range(1, 11):
        product = n * i
        print('{} x {} = {}'.format(n, i, product))
