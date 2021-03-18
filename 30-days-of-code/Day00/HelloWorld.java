/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   HelloWorld.java                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/02/24 16:54:33 by alaamimi          #+#    #+#             */
/*   Updated: 2021/02/24 16:54:41 by alaamimi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

import java.util.Scanner; //Import the scanner method

public class HelloWorld
{
	public static void main(String[] args)
	{
		Scanner scanInput = new Scanner(System.in); //Create a scanner object to read input from Stdin
		String stringInput = scanInput.nextLine(); //Read a full line of input from Stdin and save it to our variable
		scanInput.close(); //close the Scanner object because we finished reading
		System.out.println("Hello World"); //Print a string to stdout
		System.out.println(stringInput); //Print the content of the inputString to stdout
	}
}
