# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    More_Exceptions.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/08 20:05:48 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/08 20:05:50 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return pow(n, p)


myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e) 

