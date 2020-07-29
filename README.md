## Running time analysis
Given this two parameters 

`m = length of the message to make`

`s = number of letters included in the bowl (assuming a space as a character/letter)`

Most of the work of the implemented logic takes place in two iterations and some extra work performed during them. 

First one, takes places in `__make_letters_repository` which basically traverses the available alphabet soup and makes a helper dict which handles available letters and its number occurrences on the alphabet.

Then in `__is_letter_unavailable` using this helper dict `letters_repository` we traverse `word_to_make` string checking against our `letters_repository` if a certain letter is available in that 'repository' and we do not run out that letter when having more than one occurrence on alphabet.

Inside booth functions we perform actions against our dict (extra work) like storing and checking keys. Having in mind they work like a hash we can conclude those actions perform as `O(1)`.

Source: https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt

(technically we can complicate things on that hash as with creating a lot of collisions that could force actions perform a linear scan, and thus perform as `O(n), but cases should be extremely rare)    

So simplifying per language or architecture details, we can conclude algorithm has a running time of
`O(n) + O(n)` which equals to `O(n + s)`


## Installation






       









