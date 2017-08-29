Problem A
----------
Create an iterator class that stores a list of the built-in Iterators. 
Implement the next() and hasNext() methods in a Round Robin pattern (pops next element in a circle). 
Example: 
Given a list [iterator1,iterator2, iterator3...] 
when calling RoundIterator.next() 
pops iterator1.next if iterator1.hasNext() is true 
when calling RoundIterator.next() 
pops iterator2.next() if iterator2.hasNext() is true 
when calling RoundIterator.next() 
pops iterator3.next if iterator3.hasNext() is true 
... 
when calling RoundIterator.next() 
pops iterator1.next if iterator1.hasNext() is true 
when calling RoundIterator.next() 
pops iterator2.next if iterator2.hasNext() is true 
when calling RoundIterator.next() 
pops iterator3.next if iterator3.hasNext() is true 
... 
until there is no more element in any of the iterators

Problem B
----------
Inplace reverse a sentence 

You given a sentence of english words and spaces between them. 
Nothing crazy: 
1) no double spaces 
2) no empty words 
3) no spaces at the ends of a sentence


void inplace_reverse(char* arr, int length) {
    // your solution
}

Example: 
input "I wish you a merry Christmas" 
output "Christmas merry a you wish I" 

Constrains: O(1) additional memory



Problem C
----------
Array of size (n-m) with numbers from 1..n with m of them missing. Find one all of the missing numbers in O(log). Array is sorted. 

Example: 
n = 8 
arr = [1,2,4,5,6,8] 
m=2 
Result has to be a set {3, 7}.


Problem D
----------
Given a String and dictionary of words, break the string in minimum space sentence. 
Ex: 
inputStr = "ilikefacebook" 
dictionary = {"i","like","face","book","facebook"} 
Possible Strings: 
i like face book - 3 spaces 
i like Facebook - 2 spaces - this is expected answer.


