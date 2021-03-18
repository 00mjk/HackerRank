/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Arrays.java                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/02/25 22:07:39 by alaamimi          #+#    #+#             */
/*   Updated: 2021/02/25 22:07:43 by alaamimi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

import java.util.Scanner;

public class Solution
{
	public static void main(String[] args)
	{
		Scanner scanInput = new Scanner(System.in); //Scan the input

		int len = scanInput.nextInt();
		int[] str = new int[len];
		int i;

		i = 0;
		while (i < len)
		{
			str[i] = scanInput.nextInt();
			i++;
		}
		int index;

		index = len - 1;
		while (index >= 0)
		{
			System.out.print(str[index] + " ");
			index--;
		}
		scanInput.close();
	}
}
