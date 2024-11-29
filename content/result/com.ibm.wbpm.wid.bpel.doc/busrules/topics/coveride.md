<!-- image -->

# Letting a web user override the default values in a rule set

To allow a default value to be changed by a web user, proceed as
follows:

1. Create a rule set which sets the default value for the output.
2. Convert the rule set into a template, with a parameter for the
default value.
3. Add a sentence to the template web presentation indicating that
the default value should be overridden by creating another rule after
the default rule.
4. Create a few templates which capture the criteria when the default
should be overridden.
5. Add a sentence to the web presentation for each of these, indicating
that it should be used after the default rule. There are currently
no first class mechanisms to control rule order or creation, but these
comments should help the web user avoid mistakes.