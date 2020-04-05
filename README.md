# multiplicative-persistence
Multiplicative persistence searcher and finder (probably can't handle big numbers)
I am currently just learning programming, mostly Python and I am by no means a professional, just wanted to share the code I've written after watching the Numberphile video about it. 

In the pers() function which finds the multiplicative persistence of a number, you just need to write down the number into the parantheses. (Example: pers(77) )

In the searchforpers() function, there is two mods.

The mod "A" searchs the smallest number that has the most multiplicative persistence between two numbers you choose.It is optimized in a way that it doesn't search for numbers which has 0 in them or an even number and 5 in them. 0, 10, 25 is excepted.
Usage is: searchforpers("a",number1,number2)

The mod "B" searchs the smallest number that has the multiplicative persistence you choose. It is also optimized in a way that it doesn't search for numbers which has 0 in them or an even number and 5 in them. 0, 10, 25 is excepted. I couldn't figure out a way to eliminate the need for C parameter in this function, you can enter whatever you want.
Usage is: searchforpers("b",m_persistence_of_choice,anything)
