# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loop_skip.sh                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/04 12:59:08 by alaamimi          #+#    #+#              #
#    Updated: 2021/02/04 14:12:22 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash

INDEX=1
while [ $INDEX -lt 100 ]
do
	REMINDER=$(( $INDEX % 2))
	if [ $REMINDER -ne 0 ]
	then
		echo $INDEX
	fi
	INDEX=$(($INDEX+1))
done
