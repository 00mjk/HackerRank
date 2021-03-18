/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Binary.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/03/02 09:57:40 by alaamimi          #+#    #+#             */
/*   Updated: 2021/03/02 10:52:53 by alaamimi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <math.h>

int	main(void)
{
	int nbr;
	int count;

	count = 0;
	scanf("%d", &nbr);
	while (nbr != 0)
	{
		nbr = nbr & (nbr << 1);
		count++;
	}
	printf("%d", count);
}
