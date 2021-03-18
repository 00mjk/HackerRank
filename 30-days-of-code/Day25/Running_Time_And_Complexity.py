# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Running_Time_And_Complexity.py                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/08 22:35:13 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/08 22:35:14 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math

def isPrime(n):
    if n <= 1:
        return False
    sqrt_n = math.sqrt(n)
    if sqrt_n.is_integer():
        return False
    for i in range(2, int(sqrt_n)+1):
        if n%i == 0:
            return False
    return True


num_test_cases = int(input())
for i in range(num_test_cases):
    n = int(input())
    if isPrime(n):
        print('Prime')
    else:
        print('Not prime')