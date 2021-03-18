/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Operators.java                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/02/25 04:02:16 by alaamimi          #+#    #+#             */
/*   Updated: 2021/02/25 04:02:20 by alaamimi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

import java.util.Scanner;
import java.lang.Math;

public class Operators
{
	public static void main(String[] args)
	{
		Scanner scanInput = new Scanner(System.in)

		double mealCost = scanInput.nextDouble(); //Original meal price
		int tipPercent = scanInput.nextInt(); //Tip percent
		int taxPercent = scanInput.nextInt(); //Tax percent

		scanInput.close(); //End of reding input from User

		//Calculations Code
		double tip = mealCost * tipPercent / 100; //
		double tax = mealCost * taxPercent / 100;

		//Typecast the result at the rounding operation of an int
		int totalCost = (int) Math.round(tax + tip + mealCost);

		//Print result
		System.out.println(totalCost);
	}
}
