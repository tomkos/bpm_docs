# Specifying variable values using JavaScript 
(deprecated)

The following samples demonstrate how to specify the value of a
variable when using the rules editor:

| Sample        | Description                                                              |
|---------------|--------------------------------------------------------------------------|
| "ok"          | Matches the exact string ok (no quotation marks)                         |
| 1.4           | Matches the exact number 1.4                                             |
| {"A", "B"}    | Matches either of the strings A or B                                     |
| !={"A", "B"}  | Matches anything except the strings A or B                               |
| 1..5          | Matches any number between 1 and 5 (inclusive)                           |
| >3            | Matches any number greater than 3                                        |
| <3            | Matches any number less than 3                                           |
| >=3           | Matches any number greater than or equal to 3                            |
| <=3           | Matches any number less than or equal to 3                               |
| {1,3,5}       | Matches 1, 3, or 5                                                       |
| {1,3,5..10}   | Matches 1, 3, or any number between 5 and 10 (inclusive)                 |
| !={1,3,5..10} | Matches any number except 1, 3, or a number between 5 and 10 (inclusive) |
| true          | Matches the Boolean value true                                           |
| false         | Matches the Boolean value false                                          |