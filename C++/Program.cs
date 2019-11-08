using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;
using System.Security.Cryptography;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(getHashSha256("1234"));
            string getHashSha256(string text)
            {
                byte[] bytes = Encoding.Unicode.GetBytes(text);
                SHA256Managed hashstring = new SHA256Managed();
                byte[] hash = hashstring.ComputeHash(bytes);
                string hashString = string.Empty;
                foreach (byte x in hash)
                {
                    hashString += String.Format("{0:x2}", x);
                }

                return hashString;
            }

        }

        public static void prob23()
        {
            List<int> b = getNumbers();
            Console.WriteLine(shuma(b));
            List<int> getNumbers()
            {
                List<int> a = new List<int>();
                for (int i = 0; i < 28123; i++)
                {
                    if (isabundant(i)) a.Add(i);
                }
                return a;
            }

            bool isabundant(int n)
            {
                if (n > 0)
                {
                    int s = 0;
                    for (int i = 1; i <= n / 2; i++)
                    {
                        if (n % i == 0) s = s + i;
                    }

                    return s > n;
                }
                else return false;
            }

           int shuma(List<int> n)
            {
                int s = 0;
                int sizeOfList = n.Count;
                bool shouldCount = true;
                for (int i = 1; i < 28123; i++)
                {
                    shouldCount = true;
                    for (int j = 0; j < sizeOfList; j++)
                    {
                        if (isabundant(i - n[j]))
                        {
                            shouldCount = false;
                            break;
                        }
                    }
                    if (shouldCount)
                    {
                        s = s + i;
                        Console.WriteLine(s + " " + i);
                    }
                }

                return s;
            }
      
        }

        public static void prob48()
        {
            BigInteger sum = 0;
            for (int i = 1; i <= 1000; i++)
            {
                sum = sum + power(i);
            }

            Console.WriteLine(sum);

            BigInteger power(int u)
            {
                BigInteger powersum = 1;
                for (int i = 0; i < u; i++)
                {
                    powersum = powersum * u;
                }

                return powersum;
            }
        }
    }
}
