/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Review.java                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/02/25 21:17:31 by alaamimi          #+#    #+#             */
/*   Updated: 2021/02/25 21:17:44 by alaamimi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

import java.util.Scanner;

public class Solution
{

	public static void main(String[] args)
	{
		Scanner scanInput = new Scanner(System.in);
		int n = scanInput.nextInt();
		scanInput.nextLine();
		int index;

		index = 0;
		while (index < n)
		{
			String str = scanInput.nextLine();
			char[] charArray = str.toCharArray();
			index++;
			int i;

			i = 0;
			while(i < charArray.length)
			{
				if (i % 2 == 0)
				{
					System.out.print(charArray[i]);
				}
				i++;
			}
			System.out.print(" ");
			int j;

			j = 0;
			while (j < charArray.length)
			{
				if (j % 2 == 1)
				{
					System.out.print(charArray[j]);
				}
				j++;
			}
			 System.out.println();
		}
		scanInput.close();
	}
}
