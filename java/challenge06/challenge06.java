/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   challenge06.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/01/25 00:37:39 by alaamimi          #+#    #+#             */
/*   Updated: 2021/01/25 00:37:42 by alaamimi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

import java.lang.Math;

import java.util.*;
import java.io.*;



class Solution{
    public static void main(String []argh)
    {



        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();

        for(int i=0;i<t;i++)
        {

            try
            {
                long x=sc.nextLong();
                System.out.println(x+" can be fitted in:");
                if(x>=-128 && x<=127)
                    System.out.println("* byte");
                if(x >= Short.MIN_VALUE && x <= Short.MAX_VALUE)
                    System.out.println("* short");
                if(x >= Integer.MIN_VALUE && x <= Integer.MAX_VALUE)
                    System.out.println("* int");
                if(x >= Long.MIN_VALUE && x >= Long.MIN_VALUE)
                    System.out.println("* long");
            }
            catch(Exception e)
            {
                System.out.println(sc.next()+" can't be fitted anywhere.");
            }

        }
    }
}




}

