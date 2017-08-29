Problem A
------------
tokenize string, "" and [] are token flags, such as 
mytable "foo" [bar] "" [[[[]]]. 

"" Turned into ",]] turned into], [[not escaped 
The results of the example given above: 
mytable 
foo 
bar " 
[[] 
public List<String> tokenizestring(String s){ 
}



Problem B
-----------
How would you design the data structures for a very large social network (Facebook, LinkedIn, etc)? Describe how you would design an algorithm to show the connecction, or path, between two people (e g , Me -> Bob -> Susan -> Jason -> You)



Problem C
---------
Given an input file with four billion integers, provide an algorithm to generate an integer which is not contained in the file Assume you have 1 GB of memory

FOLLOW UP
What if you have only 10 MB of memory?

Problem D
--------
You have an array with all the numbers from 1 to N, where N is at most 32,000 The array may have duplicate entries and you do not know what N is With only 4KB of memory available, how would you print all duplicate elements in the array?


