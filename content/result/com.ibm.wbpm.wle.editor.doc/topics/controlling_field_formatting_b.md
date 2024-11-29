# Using characters to apply custom numeric formatting in a heritage coach (deprecated)

## About this task

If you want to apply numeric formatting to a control
for integers and decimals, you are not required to select one of the
pre-defined formats. Instead you can manually enter custom formatting
characters into the Format field. For example, the # character acts
as a digit placeholder. So if you type the following placeholders
into the Format field in the Presentation properties for a control,
you'll get the described results:

| Format placeholder                                                | Results                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ## (placeholder for two digits)                                   | Since no decimal placeholder is specified, values entered into the control during run time are rounded up to the next integer. For example, if a user enters the value 34.2 into the control, the value is rounded up to 35 .                                                                 |
| ##.# (placeholder for two digits and the tenths decimal position) | For additional decimal positions typed in to the control during run time, decimals less than five are rounded down, and decimals greater than or equal to five are rounded up. For example, the value 34.24 would be rounded down to 34.2 , and the value 34.57 would be rounded up to 34.6 . |

Follow these steps to use characters to apply custom
numeric formatting:

## Procedure

1. Open the service that contains the heritage coach that you want to work with and then click the
Coaches tab.
2. Click the heritage coach control for which you want to add formatting.
3. Click the Presentation option in the properties.
4. Under Widget Style, type the characters that you want to
use as placeholders in the Format field. The following characters
are available:                    
Table 2. Characters
available to use as placeholders

Character
Name
Description

 #

Digit placeholder
A digit is copied into output. If there is no
digit in this position, then nothing is stored in the output.

 0

Zero placeholder
A digit is copied into output. If there is no
digit in this position, a 0 is inserted into this
position.

 ?

Padding placeholder
A digit is copied into output. If there is no
digit in this position, a " " (space symbol) is inserted into this
position.

 .

Decimal separator
The first . character (period)
in the format string determines the location of the decimal separator
in the formatted value. The actual character used as the decimal separator
is determined by user locale settings.

 ,

Thousand separator
The , character (comma) serves
two purposes. First, if the format string contains a , character
between two digit placeholders (0 or #)
and to the left of the decimal point if one is present, then the output
will have thousand separators inserted between each group of three
digits to the left of the decimal separator. The actual character
used as the decimal separator in the result string is determined by
user locale settings. Second, if the format string contains one or
more , characters immediately to the left of the
decimal point, then the number will be divided by the number of , characters
multiplied by 1000 before it is formatted. For example, the format
string 0,, will represent 100 million as simply 100.
Use of the , character to indicate scaling does not
include thousand separators in the formatted number. Thus, to scale
a number by 1 million and insert thousand separators you would use
the format string: #,##0,,

 %

Percentage
The presence of a % character in a format string
causes a number to be multiplied by 100 before it is formatted. The
appropriate symbol is inserted into the number itself at the location
where the % appears in the format string.

 E0
E+0 E-0 e0 e+0 e-0 
Scientific notation
If any of the strings E , E+ , E- , e , e+ or e- are
present in the format string and are followed immediately by at least
one 0 character, then the number is formatted using
scientific notation with an E or e inserted
between the number and the exponent. The number of 0 characters
following the scientific notation indicator determines the minimum
number of digits to output for the exponent. The E+ and e+ formats
indicate that a sign character (plus or minus) should always precede
the exponent. The E , E- , e or e- formats
indicate that a sign character should only precede negative exponents.

 ;

Section separator
The ; character (semicolon)
is used to separate sections for positive, negative, and zero numbers
in the format string.

Other
All other characters
All other characters are copied to the result
string as literals in the position where they appear.
5. Save your changes.