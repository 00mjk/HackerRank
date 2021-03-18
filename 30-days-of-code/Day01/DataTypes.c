/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   DataTypes.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/02/04 10:58:40 by alaamimi          #+#    #+#             */
/*   Updated: 2021/02/04 11:02:20 by alaamimi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(void)
{
	int i = 4;
	double d = 4.0;
	char s[] = "HackerRank ";

// Declare second integer, double, and String variables.
	int nbr;
	double preci;
	char str[256];
// Read and save an integer, double, and String to your variables.
	scanf("%d", &nbr);
	scanf("%lf", &preci);
	scanf("%*[\n] %[^\n]", &str);
// Print the sum of both integer variables on a new line.
	printf("%d\n", i + nbr);
// Print the sum of the double variables on a new line.
	printf("%.01lf\n", d + preci);
// Concatenate and print the String variables on a new line
	printf("%s%s", s, str);
// The 's' variable above should be printed first.
	return 0;
}
