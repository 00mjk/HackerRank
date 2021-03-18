/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   HelloWorld.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/02/04 10:55:23 by alaamimi          #+#    #+#             */
/*   Updated: 2021/02/04 10:57:22 by alaamimi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(void) 
{
	// Declare a variable named 'input_string' to hold our input.
	char input_string[105];

	// Read a full line of input from stdin and save it to our variable, input_string.
	scanf("%[^\n]", input_string)
	// Print a string literal saying "Hello, World." to stdout using printf.
	printf("Hello, World.\n");
	return 0;
}
