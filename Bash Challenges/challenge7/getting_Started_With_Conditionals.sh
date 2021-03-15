# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    getting_Started_With_Conditionals.sh               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/04 15:14:01 by alaamimi          #+#    #+#              #
#    Updated: 2021/02/04 15:46:29 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/sh

read var0

if [ $var0 == 'y' ] || [ $var0 == 'Y' ]
then
	 echo "YES"
elif [ $var0 == 'n' ] || [ $var0 == 'N' ]
then
	echo "NO"
fi
