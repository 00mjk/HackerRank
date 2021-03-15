# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Compute_The_Average.sh                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/04 16:22:17 by alaamimi          #+#    #+#              #
#    Updated: 2021/02/04 16:22:20 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash

read N
index=0
sum=0
while [[ $index -lt $N ]]
do
    read nbr
    sum=$((sum+nbr))
    index=$(($index+1))
done

printf "%.3f" `echo "scale=10; $sum/$N" | bc -l`

