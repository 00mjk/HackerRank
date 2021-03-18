# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Operators.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/05 18:29:53 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/05 18:33:14 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash 

import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    tip = tip_percent / 100 * meal_cost
    tax = tax_percent / 100 * meal_cost
    total_cost = round(tax + tip + meal_cost)
    print(total_cost)

if __name__ == '__main__'
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_cost, tip_percent, tax_percent)
