using System;
					
public class Program
{
	public static void Main()
	{
		char[]arr =new char[]
	{
		'\u0003',
		' ',
		'&',
		'$',
		'-',
		'\u001e',
		'\u0002',
		' ',
		'/',
		'/',
		'.',
		'/'
	};
		
	
	for (int i = 0; i < arr.Length; i++)
	{
		
		Console.Write(arr[i] ^ 'A');
		
	}
	}
}
