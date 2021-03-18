# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    List_Comprehensions.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/18 19:48:04 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/18 19:48:20 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
listOfAnswers = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(listOfAnswers)    


