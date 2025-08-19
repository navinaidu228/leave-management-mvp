using System;
using System.IO;

class FileCopy
{
    static void Main()
    {
        Console.WriteLine("Enter the path of the source text file:");
        string sourceFilePath = Console.ReadLine();

        Console.WriteLine("Enter the path of the destination text file:");
        string destinationFilePath = Console.ReadLine();

        try
        {
            // Ensure the destination directory exists
            Directory.CreateDirectory(Path.GetDirectoryName(destinationFilePath));

            // Read the contents of the source file
            string fileContents = File.ReadAllText(sourceFilePath);

            // Write the contents to the destination file
            File.WriteAllText(destinationFilePath, fileContents);

            Console.WriteLine("File copy successful!");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
