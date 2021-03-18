# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Interfaces.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/08 21:59:46 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/08 21:59:48 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divisor_sum = 0
        for i in range(1, n+1):
            if n%i == 0:
                divisor_sum += i
        return divisor_sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

