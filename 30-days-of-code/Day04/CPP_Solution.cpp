/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   CPP_Solution.cpp                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: alaamimi <alaamimi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/02/04 12:28:26 by alaamimi          #+#    #+#             */
/*   Updated: 2021/02/04 12:31:33 by alaamimi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


using namespace std;
#include <iostream>

class Person
{
    public:
        int age;
        Person(int initialAge);
        void amIOld();
        void yearPasses();
};

Person::Person(int initialAge)
{
        // Add some more code to run some checks on initialAge
	if(initialAge<0)
		age=0;
	else
		age=initialAge;
}

void Person::amIOld()
{
// Do some computations in here and print out the correct statement to the console 
	if(age==0)
		printf("Age is not valid, setting age to 0.\n");
	if(age<13)
		printf("You are young.\n");
	else if(age>=13 && age<18)
		printf("You are a teenager.\n");
	else
		printf("You are old.\n");
}

void Person::yearPasses()
{
// Increment the age of the person in here
	age++;
}

int main()
{
	int t;
	int age;
	cin >> t;
	for(int i=0; i < t; i++) 
	{
		cin >> age;
		Person p(age);
        p.amIOld();
        for(int j=0; j < 3; j++) 
		{
        	p.yearPasses(); 
        }
        p.amIOld();
		cout << '\n';
    }

    return 0;
}
