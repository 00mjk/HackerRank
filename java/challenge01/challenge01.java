/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   challenge01.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/01/22 03:33:25 by alaamimi          #+#    #+#             */
/*   Updated: 2021/01/22 03:33:28 by alaamimi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

import java.util.Scanner;

public class challenge01
{
	public static void main(String[] args)
	{
	/*MY PROG STDIN*/
		Scanner scan = new Scanner(System.in);
		int a = scan.nextInt();
		int	b = scan.nextInt();
		int c = scan.nextInt();
/*MY PROG STDOUT*/
		System.out.println(a);
		System.out.println(b);
		System.out.println(c);
		scan.close();
	}
}
