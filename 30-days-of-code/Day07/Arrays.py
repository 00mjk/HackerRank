# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Arrays.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/07 10:50:54 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/07 14:11:40 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash 

import sys

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input.rstrip().split()))

    reverse_str = []
    for i in range(n):
        reverse_str.append(arr[n - i - 1])
output_str = ""
for i in range(len(reverse_str)):
    output_str += str(reverse_str[i]) + " "
print(output_str)
