# Full-text searches using the FullTextSearch operator

- * (asterisk) matches any sequence of characters (including an empty sequence).
- ? (question mark) matches any single character.
- ~ (tilde) at the end of a word means that the word should be searched using a fuzzy query. For
more information, see Fuzzy Query.The value can consist of multiple words and
contain wildcards.

1. The sequence of words "process app"
2. Any word that starts with the letter a
3. Any two-letter words that start with the letter b

1. The sequence of words "process app"
2. Any word that starts with the letter a
3. Any two-letter words that start with the letter b

1. The sequence of words "process app"
2. The string a*
3. The string b?

1. The word and
2. The word or