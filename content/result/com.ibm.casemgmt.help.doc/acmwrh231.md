# Configuring content for the Markup widget

## Procedure

To configure the Markup widget to display content that is generated from HTML and
JavaScript URLs:

1. Click the Edit Settings icon.
2. From the Widget Mode list, select Include markup and
scripts.
3 In the HTML field, enter the markup that is to be used to construct thewidget contents. You can include in the markup any standard HTML tags, valid HTML escape characters, andsupported tokens. However, observe the following limitations in the markup: You can use the following tokens in the markup: Token Description #{date} Displays the current month, day, and year formatted according to the user's locale. Forexample, the date might be shown as Jul 31, 2017. #{datetime} Displays the current month, day, year, and time formatted according to the user's locale. Forexample, the date and time might be shown as Jul 31, 2017, 11:35 AM. #{fulldatetime} Displays the current day of week, month, day, year, and time formatted according to theuser's locale. For example, the date and time might be shown as Monday, July 31, 2017 at 11:35AM. #{rolename} Displays the role with which the user is associated for the current solution. #{solutionname} Displays the name of the solution in which this Markup widget is used. #{time} Displays the current time that is formatted according to the user's locale. For example, thedate and time might be shown as 11:35 AM. #{tosname} Displays the name of the object store that is used by the current solution. #{userid} Displays the user ID with which the case worker logged in. #{username} Displays the display name that is defined for the case worker.
    - Do not enter text in the format ${abc}. This format, which
is used to load a template or variable with the specified value, is not supported by the Markup
widget.
    - The Markup widget does not parse the HTML <script> tag. Therefore, you must
provide any scripts by using the JavaScript links field.

| Token           | Description                                                                                                                                                                                |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| #{date}         | Displays the current month, day, and year formatted according to the user's locale. For example, the date might be shown as Jul 31, 2017.                                                  |
| #{datetime}     | Displays the current month, day, year, and time formatted according to the user's locale. For example, the date and time might be shown as Jul 31, 2017, 11:35 AM.                         |
| #{fulldatetime} | Displays the current day of week, month, day, year, and time formatted according to the user's locale. For example, the date and time might be shown as Monday, July 31, 2017 at 11:35 AM. |
| #{rolename}     | Displays the role with which the user is associated for the current solution.                                                                                                              |
| #{solutionname} | Displays the name of the solution in which this Markup widget is used.                                                                                                                     |
| #{time}         | Displays the current time that is formatted according to the user's locale. For example, the date and time might be shown as 11:35 AM.                                                     |
| #{tosname}      | Displays the name of the object store that is used by the current solution.                                                                                                                |
| #{userid}       | Displays the user ID with which the case worker logged in.                                                                                                                                 |
| #{username}     | Displays the display name that is defined for the case worker.                                                                                                                             |

4. Optional: 
In the JavaScript links field, enter a URL to an external JavaScript
file that is used to construct the widget content.
To enter multiple URLs, place each URL on a separate line.