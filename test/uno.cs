using System;
namespace uno
{
    class UNOm
    {
        static void Main()
        {
            string[] vector = { "Lunes", "Martes", "Miercoles" };

            foreach (string diaSem in vector)
                Console.WriteLine(diaSem);
        }
    }
}
