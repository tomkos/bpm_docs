# Process Portal Work dashboard: Searches for
specific types and for business data

- Searching for specific types of information
- Searches for business data

## Searching for specific types of information

| What are you looking for?                                                    | Which field should you use?   | What terms should you include?                                                                                                                                                                                                                                                                                                                                                       | What should your query look like?                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tasks with a specific name                                                   | activityname:                 | Any terms from the task name                                                                                                                                                                                                                                                                                                                                                         | If you know the exact name, enter activityname:"Submit requisition" If you know only parts of the name, enter activityname:Requisition                                                                                                                           |
| The tasks that belong to a process instance with a specific application name | application:                  | Any terms from the application name                                                                                                                                                                                                                                                                                                                                                  | If you know the exact name, enter application:"Standard Hiring Package" If you know only parts of the name, enter application:Hiring application:Standard                                                                                                        |
| Tasks that are at risk on a specific date, or during a date range            | atriskdate:                   | The date in Coordinated Universal Time (UTC) in the format: year, month, day, [YYYYMMDD] expressed as a date range. You can enter just the year [YYYY], or include hours, minutes, and seconds [YYYYMMDDHHMMSS]. Tip: To handle timezone issues, search from the day before to the day after the date that you are actually interested in. Use the TO operator to combine the dates. | All dates are UTC. For a specific date, for example 15 June 2013, enter atriskdate:[20130614 TO 20130616] For a range of dates, for example 15 - 30 June 2013, enter atrisk:[20130614 TO 20130701]  Remember: Always use uppercase characters for operators.     |
| The tasks that belong to a specific process                                  | bpd:                          | Any terms from the process name                                                                                                                                                                                                                                                                                                                                                      | If you know the exact name of the process, enter bpd:"hiring process" If you know only parts of the name, enter bpd:hiring                                                                                                                                       |
| The tasks that were created on a specific date, or during a date range       | createdate:                   | The date in Coordinated Universal Time (UTC) in the format: year, month, day, [YYYYMMDD] expressed as a date range. You can enter just the year [YYYY], or include hours, minutes, and seconds [YYYYMMDDHHMMSS]. Tip: To handle timezone issues, search from the day before to the day after the date that you are actually interested in. Use the TO operator to combine the dates. | All dates are UTC. For a specific date, for example 15 June 2013, enter createdate:[20130614 TO 20130616] For a range of dates, for example 15 - 30 June 2013, enter createdate:[20130614 TO 20130701]  Remember: Always use uppercase characters for operators. |
| Tasks that are due on a specific date, or during a date range                | duedate:                      | The date in Coordinated Universal Time (UTC) in the format: year, month, day, [YYYYMMDD] expressed as a date range. You can enter just the year [YYYY], or include hours, minutes, and seconds [YYYYMMDDHHMMSS]. Tip: To handle timezone issues, search from the day before to the day after the date that you are actually interested in. Use the TO operator to combine the dates. | All dates are UTC. For a specific date, for example 15 June 2013, enter duedate:[20130614 TO 20130616] For a range of dates, for example 15 - 30 June 2013, enter duedate:[20130614 TO 20130701]  Remember: Always use uppercase characters for operators.       |
| The tasks that belong to a process instance with a specific ID               | instanceid:                   | The numeric ID of the process instance                                                                                                                                                                                                                                                                                                                                               | instanceid:57824                                                                                                                                                                                                                                                 |
| The tasks that belong to a process instance with a specific name             | instancename:                 | Any terms from the process instance name                                                                                                                                                                                                                                                                                                                                             | If you know the exact name, enter instancename:"Check Loan Application - 10247" If you know only parts of the name, enter instancename:Loan instancename:Application                                                                                             |
| All the tasks that have been claimed by users                                | isassignedtouser:             | One of the following values: true, false.                                                                                                                                                                                                                                                                                                                                            | For example, to find tasks that have not yet been claimed, enter isassignedtouser:false                                                                                                                                                                          |
| All that are associated with the specified priority value                    | priority:                     | One of the following values: highest, high, normal, low, and lowest                                                                                                                                                                                                                                                                                                                  | For example, to find the tasks with the highest priority, enter priority:highest.Note:  To find medium-priority tasks, use the normal priority value in your free-text searches.                                                                                 |
| Tasks with a specific subject line                                           | subject:                      | Any terms from the subject of the task                                                                                                                                                                                                                                                                                                                                               | If you are looking for a specific invoice in the subject line, enter subject:Invoice subject:49723 If you know a phrase from the subject line, enter subject:"Initiate Credit Check"                                                                             |
| A specific task ID                                                           | taskid:                       | The numeric ID of the task                                                                                                                                                                                                                                                                                                                                                           | taskid:12345                                                                                                                                                                                                                                                     |
| Tasks assigned to a specific team                                            | teamname:                     | All or part of the team name                                                                                                                                                                                                                                                                                                                                                         | teamname:accounting                                                                                                                                                                                                                                              |
| Tasks that are owned by someone with the specified name                      | userfullname:                 | All or part of a user's full name                                                                                                                                                                                                                                                                                                                                                    | If you know the user's full name, enter userfullname:"john smith" If you know only part of the name, enter userfullname:john userfullname:smith                                                                                                                  |
| Tasks that are owned by someone with a specific user login name              | username:                     | The user name                                                                                                                                                                                                                                                                                                                                                                        | username:jsmith                                                                                                                                                                                                                                                  |

| What are you looking for?                                                         | Which field should you use?   | What terms should you include?                                                                                                                                                                                                                                                                                                                                                       | What should your query look like?                                                                                                                                                                                                                                                |
|-----------------------------------------------------------------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The process instances that belong to a process with a specific application name   | application:                  | Any terms from the application name                                                                                                                                                                                                                                                                                                                                                  | If you know the exact name, enter application:"Standard Hiring Package" If you know only parts of the name, enter application:Hiring application:Standard                                                                                                                        |
| The process instances that belong to a process with a specific name               | instancename:                 | Any terms from the process instance name                                                                                                                                                                                                                                                                                                                                             | If you know the exact name, enter instancename:"Check Loan Application - 10247" If you know only parts of the name, enter instancename:Loan instancename:Application                                                                                                             |
| The process instances that belong to a specific business process definition (BPD) | bpd:                          | Any terms from the process name                                                                                                                                                                                                                                                                                                                                                      | If you know the exact name of the process, enter bpd:"hiring process" If you know only parts of the name, enter bpd:hiring                                                                                                                                                       |
| Process instances that are at risk on a specific date, or during a date range     | instanceatriskdate:           | The date in Coordinated Universal Time (UTC) in the format: year, month, day, [YYYYMMDD] expressed as a date range. You can enter just the year [YYYY], or include hours, minutes, and seconds [YYYYMMDDHHMMSS]. Tip: To handle timezone issues, search from the day before to the day after the date that you are actually interested in. Use the TO operator to combine the dates. | All dates are UTC. For a specific date, for example 15 June 2013, enter instanceatriskdate:[20130614 TO 20130616] For a range of dates, for example 15 - 30 June 2013, enter instanceatriskdate:[20130614 TO 20130701]  Remember: Always use uppercase characters for operators. |
| Process instances that were created on a specific date, or during a date range    | instancecreatedate:           | The date in Coordinated Universal Time (UTC) in the format: year, month, day, [YYYYMMDD] expressed as a date range. You can enter just the year [YYYY], or include hours, minutes, and seconds [YYYYMMDDHHMMSS]. Tip: To handle timezone issues, search from the day before to the day after the date that you are actually interested in. Use the TO operator to combine the dates. | All dates are UTC. For a specific date, for example 15 June 2013, enter instancecreatedate:[20130614 TO 20130616] For a range of dates, for example 15 - 30 June 2013, enter instancecreatedate:[20130614 TO 20130701]  Remember: Always use uppercase characters for operators. |
| Process instances that are due on a specific date, or during a date range         | instanceduedate:              | The date in Coordinated Universal Time (UTC) in the format: year, month, day, [YYYYMMDD] expressed as a date range. You can enter just the year [YYYY], or include hours, minutes, and seconds [YYYYMMDDHHMMSS]. Tip: To handle timezone issues, search from the day before to the day after the date that you are actually interested in. Use the TO operator to combine the dates. | All dates are UTC. For a specific date, for example 15 June 2013, enter instanceduedate:[20130614 TO 20130616] For a range of dates, for example 15 - 30 June 2013, enter instanceduedate:[20130614 TO 20130701]  Remember: Always use uppercase characters for operators.       |
| A specific process instance                                                       | instanceid:                   | The numeric ID of the process instance                                                                                                                                                                                                                                                                                                                                               | instanceid:57824                                                                                                                                                                                                                                                                 |

## Searches for business data

| What are you looking for?                                                                         | What should your query look like?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Terms in business data fields                                                                     | Include the name of the field in your search. To find the name of a field, in the task area for a task, hover over the label of the field. For example, if the label for the data is Customer Name and the hover help for the label shows customername, enter customername:                                                                                                                                                                                                                                                          |
| Terms that include any of the following special characters: + - && || ! ( ) { } [ ] ˆ " ˜ * ? : \ | Because special characters are not indexed, you can substitute the character in your search with a space. If you include the special character in your search, include a backslash (\) before the character. For example, if the customer name is MyCompany! and the field label is customername, enter customername:"MyCompany\!"  Attention: You cannot include wildcard characters, an asterisk (*) or a question mark (?), in search queries that contain special characters.                                                    |
| Numeric data in business data fields                                                              | To search for a number, for example 9 in the customer address field, enter customeraddress:9To search for numbers in a range, use the TO operator. For example, if you are looking for numbers in the range from 1 through 9 in the customer address field, enter customeraddress:[1 TO 9]                                                                                                                                                                                                                                           |
| Dates in business data fields                                                                     | Enter the date in UTC in the format: year, month, day, (YYYYMMDD) expressed as a date range. Use the TO operator to combine the dates in the range. Tip: To handle timezone issues, search from the day before to the day after the date that you are actually interested in. For example, to find tasks that are associated with orders from 1 February 2012, use 31 January 2012 as the start date and 2 February 2012 as the end date. If the label for the order date field is orderdate, enter orderdate:[20120131 TO 20120202] |
| Business data fields that can have the value true or false (Boolean fields)                       | Enter the value of the field in lowercase, for example, iscustomer:true If the value of a field can be either true or false, put the values in parentheses or repeat the field name. Enter, for example iscustomer:(true OR false), or iscustomer:true OR iscustomer:false                                                                                                                                                                                                                                                           |