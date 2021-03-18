/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Loops.java                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/02/25 19:31:03 by alaamimi          #+#    #+#             */
/*   Updated: 2021/02/25 19:31:06 by alaamimi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

import java.util.Scanner;

public class Solution
{
	private static final Scanner scanner = new Scanner(System.in);
	public static void main(String[] args)
	{
		int n = scanner.nextInt();
		scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");   
		int i;

		i = 1;
		while (i <= 10)
		{
			System.out.print(n);
			System.out.print(" x ");
			System.out.print(i);
			System.out.print(" = ");
			System.out.println(n * i);
			i++;
		}
		scanner.close();
	}
}
