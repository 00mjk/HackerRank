# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Find_the_runner-Up_score.py                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/18 19:54:17 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/18 19:54:19 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash

if __name__ == '__main__':
    n = int(input())
arr = list(map(int, input().split()))
print(max([x for x in arr if x != max(arr)]))