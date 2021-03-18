# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Nested_Logic.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/08 22:37:54 by alaamimi          #+#    #+#              #
#    Updated: 2021/03/08 22:37:56 by alaamimi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

return_day, return_month, return_year = [int(e) for e in input().strip().split(' ')]
due_day, due_month, due_year = [int(e) for e in input().strip().split(' ')]

# Check the biggest category: year
if return_year < due_year:
    print(0)
elif return_year == due_year:
    # Check the next biggest category: month
    if return_month < due_month:
        print(0)
    elif return_month == due_month:
        # Check the last category: day
        if return_day <= due_day:
            print(0)
        else:
            print(str((return_day - due_day) * 15))
    else:
        print(str((return_month - due_month) * 500))
else:
    print('10000')
