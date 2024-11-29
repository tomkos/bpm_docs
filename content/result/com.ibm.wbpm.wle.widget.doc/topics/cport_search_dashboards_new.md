# Process Portal
dashboards: Basic searches

- How to search
- How to construct filters for basic searches

## How to search

- To see a list of all the available fields that you can use in filters, enter an asterisk (*) as
the search filter.
- End your filter by pressing the Spacebar key twice, or by pressing the Right Arrow key.
- Apply your filters to the dashboard page by pressing Enter.
- Clear the filters by clicking the X icon at the end of the search
filter.

## How to construct filters for basic searches

- To find instances of home loan approvals, enter Instance Name
"home loan approval"
- Nonalphanumeric characters: "johndoe@mycompany.com", or
"Smith&Jones"

Although terms are automatically combined to narrow
down the search, you can also use the AND operator to combine
terms, for example John AND Smith AND loan.

- If you enter john smith loan, the search returns the same results as if
you entered John Smith loan or JOHN SMITH LOAN.
- If you enter Müller, the search returns the same results as if you
entered MÜLLER. However, the search does not return results that contain
Muller or Mueller.

Use the asterisk (*) as a substitute for one or more characters at the
beginning, end, or within a term. For example, to find both reject and
rejection, enter reject*.

- Subject
debit Space Space
Subject
credit
- Subject
debit Space Space AND Space Space
Subject
credit
- + Space Space
Subject
debit Space Space
+ Space Space
Subject
credit

For example, to show items that contain debit, credit, or both using
free-text search terms, enter Subject
debit Space Space OR Space Space
Subject
credit

In a filter that contains a field name, use commas between the
search terms in the filter. For example, to show tasks for several different users, enter
User Name
Fred, Jim,
Tim

You
can combine the OR operator with the AND operator. For example, to find all the approval or rejection tasks that are new,
enter (approval OR rejection) AND new

- Subject
loan Space Space NOT Space Space
Subject
car
- Subject
loan Space Space - Space Space
Subject
car

In
numeric fields, to search for a range of numbers, use the TO
operator: filter1
TO
filter2. For example, if you are looking for loan numbers in the range from 1
through 9 and your environment includes a numeric Loan Number field, enter Loan
Number
[1 TO 9]

Searches for numeric data in text-based fields are always text
based. Terms are identified based on whitespace and common punctuation. For example, if you enter
Instance Name
[1 TO 9], the search returns instances that have terms starting with the
characters 1 through 9. Instance names, such as "Order 5", "Order 524563", "Order:5", "Order:524563"
are returned because the first character of the term is between 1 and 9. However, instance names,
such as "Order5" and "Order524563" are not returned because there is no whitespace or punctuation
before the number.

For example, to find tasks that are associated with orders that are due from 1
February 2012, use 31 January 2012 as the start date and 2 February 2012 as the end date in your
filter: Due Date
[20120131 TO 20120202]

- You cannot include wildcard characters, an asterisk (*) or a question mark (?), within the
quotation marks.
- Because special characters are not indexed, you can substitute the character in your search with
a space.
- If you include the special character in your search, include a backslash (\) before the
character. For example, if the customer name is MyCompany! and the field label is
customername, enter customername:"MyCompany\!"
- Because the # character is used to separate words for indexing, the search
process ignores it. You cannot even include it by adding a backslash (\) before the character.

- Letters, numbers, and Japanese Katakana characters are searched as one word.
- Kanji and Japanese Hiragana characters are searched as one character.

For example, to show tasks from
the Loans process application that belong to Fred and mention car loan, enter
(Space Space
User Name
Fred Space Space
Process Application
Loans Space Space) AND Space Space "car
loan"