/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   challenge03.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/01/24 23:22:36 by alaamimi          #+#    #+#             */
/*   Updated: 2021/01/24 23:22:38 by alaamimi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution
{
	private static final Scanner scanner = new Scanner(System.in);
	public static void main(String[] args) 
	{
		int N = scanner.nextInt();
		scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
		if(N%2 == 0 && N >= 2 && N <= 5)
			System.out.println("Not Weird");
		else if (N%2 == 0 && N >= 6 && N <= 20)
			System.out.println("Weird");
		else if (N%2 == 0 && N >= 20)
			System.out.println("Not Weird");
		else
			System.out.println("Weird");
		scanner.close();
	}
}

