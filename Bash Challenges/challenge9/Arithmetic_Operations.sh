# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Arithmetic_Operations.sh                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/04 16:19:44 by alaamimi          #+#    #+#              #
#    Updated: 2021/02/04 16:19:47 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash

read nbr

echo $nbr | bc -l | xargs printf "%.3f"
