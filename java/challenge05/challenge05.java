/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   challenge05.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/01/24 23:30:32 by alaamimi          #+#    #+#             */
/*   Updated: 2021/01/24 23:30:34 by alaamimi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

import java.lang.Math;

class Solution
{
	public static void main(String[] argh)
	{
		Scanner in = new Scanner(System.in);
		int t=in.nextInt();
		for(int i=0;i<t;i++)
		{
			int a = in.nextInt();
			int b = in.nextInt();
			int n = in.nextInt();

			int cmt = 0;
			while (cmt < n)
			{
				 a = a + (int)Math.pow(2,cmt) * b;
				System.out.print(a + " ");
				cmt++;
			}
			System.out.println();
		}
		in.close();
	}
}
