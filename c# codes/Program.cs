pathusing System;

class SimpleCalculator
{
    static void Main()
    {
        float res = 0;
        int ch = 0;

        Console.WriteLine("Enter the 1st number");
        int num1 = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine("Enter the second number");
        int num2 = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine("Enter the operator");
        char op = Convert.ToChar(Console.ReadLine());

        switch (op)
        {
            case '+':
                res = num1 + num2;
                break;
            case '-':
                res = num1 - num2;
                break;
            case '*':
                res = num1 * num2;
                break;
            case '/':
                if (num2 != 0)
                {
                    res = (float)num1 / num2; // Cast one operand to float for correct division
                }
                else
                {
                    Console.WriteLine("Invalid input - division by zero");
                    return; // Exit the program
                }
                break;
            case '%':
                if (num2 != 0)
                {
                    res = num1 % num2;
                }
                else
                {
                    Console.WriteLine("Invalid input - modulo by zero");
                    return; // Exit the program
                }
                break;
            default:
                Console.WriteLine("Invalid operator");
                return; // Exit the program
        }

        Console.WriteLine("Result = " + res);
    }
}
