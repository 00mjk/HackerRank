/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Maps.java                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/02/26 16:45:01 by alaamimi          #+#    #+#             */
/*   Updated: 2021/02/26 16:45:04 by alaamimi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Solution
{
	public static void main(String[] args)
	{
		Scanner scanInput = new Scanner(System.in);
		int n = scanInput.nextInt();

		Map<String,Integer> phoneBook = new HashMap<>();
		for(int i = 0; i < n; i++)
		{
			String name = scanInput.next();
			int phone = scanInput.nextInt();
			phoneBook.put(name, phone);
		}
		while(scanInput.hasNext())
		{
			String str = scanInput.next();
			if (phoneBook.containsKey(str))
				System.out.println(str + "=" + phoneBook.get(str));
			else
				System.out.println("Not found");
		}
		scanInput.close();
	}
}
