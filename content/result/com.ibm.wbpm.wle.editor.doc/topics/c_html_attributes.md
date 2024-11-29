# HTML attributes

- An HTML class attribute in each view instance that you want to specifically style
- A corresponding CSS rule for that class attribute

- CoachView
- ContentBox

| Default label position   | Overridden to move the label   |
|--------------------------|--------------------------------|
|                          |                                |

1. Add a class to the HTML attributes of the text box instance. For example, click Add
Class and then in Class name, type
myText.
2. In CSS code, define the style for the class. For example, define the myText
class to override the styles for the label position:
.myText.Output\_Text .outputTextLabel,
.Text .textLabel {
display: inline-block;
width: 100px;
}
.myText.Text .content {
display: inline-block;
}
3. In any parent view, add the CSS rule to a .css file and add that file as an
included script. If the view is a top-level view in a coach, add a custom HTML item that contains
the style rule.