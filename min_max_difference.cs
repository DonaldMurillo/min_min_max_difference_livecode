using System;
using System.Collections.Generic;

namespace min_max_difference
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }


        static int the_highest(List<int> ts)
        {
            var the_highest = ts[0];
            foreach (var item in ts)
            {
                if (item >= the_highest)
                {
                    the_highest = item;
                }
            }
            return the_highest;

            static int the_smallest(List<int> ts)
            {
                var the_smallest = ts[0];
                foreach (var item in ts)
                {
                    if (item <= the_smallest)
                    {
                        the_smallest = item;
                    }
                }
                return the_smallest;

            }
        }
    }
}
