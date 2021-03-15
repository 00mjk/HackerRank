# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    The_World_of_Numbers.sh                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/04 14:27:40 by alaamimi          #+#    #+#              #
#    Updated: 2021/02/04 14:51:38 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash 

read X
read Y

if [ $X -lt 100 ] && [ $X -gt -100 ] && [ $Y -lt 100 ] && [ $Y -gt -100 ] && [ $Y != 0 ]
then
	echo $(($X+$Y))
	echo $(($X-$Y))
	echo $(($X*$Y))
	echo $(($X/$Y))
fi