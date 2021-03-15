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

#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
if (n >= 2 and n <= 5 and n % 2 == 0):
    print"Not Weird"
elif (n >= 6 and n <= 20):
    print"Weird"
elif (n >= 20 and n % 2 != 1):
    print"Not Weird"
else:
    print"Weird"