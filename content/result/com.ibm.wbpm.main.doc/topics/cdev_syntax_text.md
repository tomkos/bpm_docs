# Syntax for text with embedded JavaScript

In certain situations, you can combine literal text with parts that are computed
dynamically.

- In scriptlets of script tasks in service flows.
- Traditional:  In the definitions of
web service servers in the process application settings.

- Normal text is taken literally, including newlines.
- Use the syntax <#= expression #> to evaluate a JavaScript expression. The string
representation of the result of the evaluation is spliced into the resulting text. For example,
<#= 5 + 7 #> produces the string "12". The expression can span multiple lines if it is
parenthesized.
- Use the syntax <# statement #> to evaluate a JavaScript statement. The statement can span
multiple lines; in this case, the normal rules for JavaScript end-of-line apply, as described in the
section "Whitespace and semicolons" in the Wikipedia topic JavaScript
syntax. To specify conditional statements, use the following syntax:
<# if (tw.local.foo  < 100) { #>TEXT A <# } else { #>TEXT B <# } #>
In this example, either TEXT A or TEXT B will be part of the
result, but not both. Note: You can only specify the parts #>TEXT A<# and
#>TEXT B <# in places where, in JavaScript, a statement is allowed.