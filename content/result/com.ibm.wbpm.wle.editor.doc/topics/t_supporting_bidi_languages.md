# Adding bidirectional language support

## About this task

By default, the designer uses the left to right text direction. However, you can reverse this
direction for any view by using the Base Text Direction general property. For example, by using this
property, you can have a coach with fields with English text that is going from left to right and
fields with Arabic text that is going from right to left.

The Base Text Direction property is not available until you enable it as a preference.

## Procedure

1. Using the steps that are contained in Setting preferences in the desktop Process Designer, click the
Capabilities > Advanced Features > Base Text Direction option.
2. In the General properties of a view, set the Base Text
Direction property to one of the following values: 

Value
Description

Default
Inherit the text direction that is set in the
user's profile.

Contextual
Display the text according to the first strong directional character in the
string. For example, if the first strong directional character is from a right to left language,
display the text from right to left. This applies to all text elements that a view displays. For
example, a Text view has an Arabic label but its contents are English. In this case, the text in the
label is right to left while the text in the field is left to right. 

Left to Right
Display the text from left to right no matter
what characters are in the text.

Right to Left
Display the text from right to left no matter
what characters are in the text.
3. Optional: To provide customized styling for
bidirectional languages, use the CoachViewRTL class
in your CSS rules.  When the coach is generated for
a bidi language, it contains a tag like the following example:<body dir="rtl" class="CoachViewRTL">
4. Optional: To support UI mirroring that is opposite
to the default directional setting of the current locale, add an attribute
to its HTML attribute properties. Set the name of the attribute to dir and
the value to ltr or rtl.
Any views contained by this view inherit this attribute.
5. Click Save or Finish Editing.

## What to do next