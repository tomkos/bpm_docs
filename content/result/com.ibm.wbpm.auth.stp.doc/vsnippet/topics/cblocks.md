<!-- image -->

# The building blocks of the visual snippet editor

- Inputs
- Output
- Exceptions
- Visual snippets
- Links

## Inputs

The inputs  define
the data that enters the snippet. This data can either be in the form
of a Java™ type, a data type or a business object.

There
can be multiple inputs into a snippet.

## Output

The output  defines
the result of the snippet composition. The data that is returned can
either be in the form of a Java type,
a data type or a business object.

There can be at most one output
from a snippet.

## Exceptions

The exceptions  indicate
what fault handling may be required if the snippet cannot be completed
successfully.

There can be multiple exceptions in a snippet.

## Visual snippets

Within the
context of the visual snippet editor, a visual snippet is a unit of
work that performs a specific programmatic task in order to achieve
a larger programming goal. There are several items that can be dropped
onto the canvas from the palette, and each performs a different function.

There
are a number of items that can be added to a visual snippet:

- Expression Expressions carry user-defined values, and pass them into the snippet.

The kinds of values are varied, and the expression can also be visually composed using the inline expression builder.
- Standard visual snippet Use this to add a predefined snippet into the editor 

When you drop this snippet on the canvas, you will be prompted to choose from a categorized list of existing snippets. The system provides a number of standard, general purpose snippets that you can choose from here. Similarly, if you or another colleague has already created custom visual snippets on this system, they will appear here in the form of custom visual snippets.
- Java visual snippet  Use this to embed a call to an arbitrary Java method or constructor or access a field within the context of the visual snippet.

When you click this item, the Select a Java Visual Snippet wizard will launch. Browse the existing types and qualifiers, and then choose an appropriate snippet and drop it onto the canvas.
- Choice control structure
Use the choice control structure to create a branch in your snippet, and direct the processing according to the Boolean value of the input.

You will embed two separate pieces of code into two separate areas of this control structure. One will be executed when the input is 'True', and the other when it is 'False'.
- While control structure Use the while control structure to repeat the same code as long as the input value is 'True'.

You will embed two separate pieces of code into two separate areas of this control structure. The code in the bottom section is run as long as the input continues to evaluate to 'True'. When the input evaluates to 'False', control moves on to the next object in the snippet.
- For each control structure Use the for each control structure to repeat the same code for each of the items of a list that is received as input.
- Repeat control structure Use the repeat control structure to iterate the same code a number of times. The number of repetitions is determined by the value that is received as input.
- Try Finally node Use the Try Finally node to attempt to perform an action (initial action) and then to perform another action (final action). The final action runs regardless of whether the initial action ran successfully or caused an exception.
- Throw node Use this to throw an exception.
- Return node Use this when you want to return a result from the snippet.
- Comment node Use this when you want to include a note of some kind in the structure of the snippet. The comment is text based, and can be used to explain and describe portions of the code to make future modifications easier.

## Links

Links  represent
the flow of data and direct the sequence in which the processing of
the nodes in your snippet occurs.