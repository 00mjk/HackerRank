/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   DataTypes.java                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/02/24 17:10:27 by alaamimi          #+#    #+#             */
/*   Updated: 2021/02/24 17:10:38 by alaamimi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

import java.util.Scanner; //Impport Scanner method

public class DataTypes
{
	public static void main(String[] args)
	{
		int i = 4; //Declare first integer
		int integer; //Declare second integer
		double d = 4.0; //declare first double
		double doub; //Declare second double
		String s = "HackerRank "; //Declare first String
		String str; //Declare second String

		Scanner scanInput = new Scanner(System.in); //Declare a Scanner method to take input value from stdin
		//Read and save integer, double && string from stdin
		integer = scanInput.nextInt();
		doub = scanInput.nextDouble();
		scanInput.nextLine(); //Newline character after the double
		str = scanInput.nextLine();

		System.out.println(i + integer); //Print the sum of integer variables on a newline
		System.out.println(d + doub); //Print the sum of doubles on a Newline
		System.out.println(s + str); //concatenate and print the string variables on a newline
		scanInput.close(); //close the input reading
	}
}