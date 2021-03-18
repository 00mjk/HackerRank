# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Statements.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/05 19:00:23 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/05 19:50:45 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash 

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    if N % 2 == 1 :
        print("Weird")
    elif N >= 2 and N <= 5 and N % 2 == 0 :
        print("Not Weird")
    elif N >= 6 and N <= 20 and N % 2 == 0 :
        print("Weird")
    else
        print("Not Weird")
