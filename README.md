# Add-Two-Polynomials

Given two polynomials A and B, write a program that adds the given two polynomials A and B and prints the result in the standard form of Cix^Pi + Ci-1x^Pi-1 + .... + C1x + CO.

Input
The first line of input contains an integer M representing the number of terms in polynomial A.
The next M lines of input contain two space-separated integers in each line, representing the Power Pi and
Coefficient Cl of polynomial A.
The next line of input contains an integer N representing the number of terms in polynomial B.
The next N lines of input contain two space-separated integers in each line, representing the Power Pj and Coefficient Cj of polynomial B.

Output
The output should be in the form of Cix^Pi + Ci-1x^Pi-1+....+ C1x + CO.
If the coefficient is 0 then the term should not be printed.
If the term with the highest power is negative, it should be represented as -Cix Pi.
If the term where power is 1, it should be represented as C1x instead of C1x^1.
If the polynomial power is O and the constant term is also 0, then print 0 to represent the polynomial.
For term Cix Pi, if the coefficient of the term Ci is 1, then print x^Pi instead of 1x^Pi.
