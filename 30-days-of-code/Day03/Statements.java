/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Statement.java                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/02/25 16:24:33 by alaamimi          #+#    #+#             */
/*   Updated: 2021/02/25 16:24:42 by alaamimi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

import java.util.Scanner;

public class Statements
{
	public static void main(String[] args)
	{
		Scanner scanInput = new Scanner(System.in);

		int n = scanInput.nextInt();

		ScanInput.close();

		if (n % 2 == 1)
			System.out.println("Weird");
		else if (n % 2 == 0 && n >= 2 && n <= 5)
			System.out.println("Not Weird");
		else if (n % 2 == 0 && n >= 6 && n <= 20)
			System.out.println("Weird");
		else
			System.out.println("Not weird");
	}
}
