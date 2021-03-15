# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    comparing_Numbers.sh                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/04 14:57:44 by alaamimi          #+#    #+#              #
#    Updated: 2021/02/04 15:09:38 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/sh 

read X
read Y

if [ $X -lt $Y ]
then
	echo "X is less than Y"
elif [ $X -gt $Y ]
then
	echo "X is greater than Y"
else
	echo "X is equal to Y"
fi
