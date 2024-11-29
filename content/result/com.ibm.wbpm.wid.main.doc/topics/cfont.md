<!-- image -->

# Fonts and color settings

IBM® Integration
Designer uses
the fonts and colors provided by the operating system where possible.
Operating systems do not provide enough colors to handle all of the
extra information that colors and fonts provide in the workbench.

There are four main fonts in use by the workbench. They are:

| Font   | Description                                                                                                                                    |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Banner | Used in PDE editors, welcome pages and in the title area of many wizards. For example the New Project wizard uses this font for the top title. |
| Header | Used as a section heading. For example the Welcome page for the Eclipse Platform uses this font for the top title,                             |
| Text   | Used in text editors.                                                                                                                          |
| Window | Used in windows                                                                                                                                |

These fonts can be set using the Workbench > Colors and Fonts preference.
As well as these four fonts, there are several other secondary font
settings that default to the text font. They can be found on the Colors
and Fonts preference page.

The workbench uses colors as an information enhancement in many
places. Whenever possible, the operating system color settings are
used, but in cases where the operating system settings are not enough,
the workbench defines other colors. All of these colors can be adjusted
using the following preference pages:

- Workbench > Colors and Fonts > Basic  (Error text,
hyperlink  text, active hyperlink text)
- Workbench > Search (Foreground for potential matches)
- Run/Debug > Console (Standard Out, Standard Error, Standard
In)
- Run/Debug  (Variable Views changed value, Memory View unbuffered
lines)
- Ant (Error, Warning, Information, Verbose, Debug)
- Java™ > Editor  (Line number, matching
brackets, current line, print, find scope, hyperlink, selection foreground,
selection background)
- Java > Editor, select the Syntax Tab
(Javadoc HTML tags, Javadoc keywords, Javadoc links, Javadoc others,
keyword 'return', keywords excluding 'return', Method names, Multi
line comment, Operators and brackets, Others, Single-line comment,
Strings, Task Tags)
- Java > Editor > Code Assist (completion
proposal background, completion proposal foreground, method parameter
background, method parameter      foreground, completion overwrite
background, completion overwrite foreground)
- Plug-in Development > Editors (Text, Processing instructions,
Constant strings, Tags, Comments)
- Team > CVS > Console (Command line, Message, Error)

Accessibility
and the Windows Color Dialog

For color selection, the workbench uses a window provided by the
operating system. On Windows,
the color selection window does not respond properly to assistive
technology. When you first open the window, focus is on one of the
basic colors, but the window provides no indication of this through
assistive technology. You can select colors in the workbench with
this window in the following way:

1. Select to customize the color of a setting in the workbench,
for example the  color of Error Text in your Workbench Colors and
Fonts Basic preferences.
2. In the color selection window , tab twice to go from the Basic
Color matrix to Define Custom Colors and click Enter.
3. You can now enter the basic colors using an HSL or RGB specification.