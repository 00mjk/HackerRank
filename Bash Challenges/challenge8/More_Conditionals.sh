# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    More_Conditionals.sh                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/04 15:57:33 by alaamimi          #+#    #+#              #
#    Updated: 2021/02/04 15:57:42 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash

read X
read Y
read Z

if [ $X == $Y ] && [ $Y == $Z ]
then
    echo "EQUILATERAL"
elif [ $X == $Y ] || [ $Y == $Z ]
then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi
