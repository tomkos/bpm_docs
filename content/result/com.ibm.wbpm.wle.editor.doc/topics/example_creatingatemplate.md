# Example: creating a template (deprecated)

<!-- image -->

1 Upload the image for the header background:
    1. Click the Add icon for Files and then select Web
File.
    2. Add the image file as a web file. For the example, use this image file:
2 Create the My Template view:

1. Click the Add icon for User Interface and then select
View.
2. In the window, type My Template for the name and select Start
with a grid. From the list of grids, select Header Footer.
3. Click Finish. The Designer opens the Layout page
of view in content mode. The layout displays three cells into which you can add content.
3 Define the layout of the My Template view: The layout of the My Template view looks like the following screen capture:

1. In the upper cell, drop a custom HTML item.
2. In the properties of the custom HTML item, add the following HTML code as text that goes in the
header:
<div id="header">
	<h1 id="header\_text">My Company</h1>
</div>This
code defines the text that goes in the header division and opens the main content division.
3. In the middle cell, drop a content box. The content box is a placeholder for content that is
defined by views and coaches that users create based on the My Template view. In the Process
Designer, the content box uses the cell orientation to display its contents vertically or
horizontally instead of its own settings.
4. In the lowest cell, drop a custom HTML item.
5. In the properties of the second custom HTML item, add the following HTML code as
text.<div id="footer">
	<h2 id="footer\_text">&copy; My Company</h2>
</div>This
code defines the text that goes in the footer.

<!-- image -->

4. In the Behavior page, define the look of the My Template view by adding
the following code as inline
CSS:#header {
	text-align: center;
	background-image: url('banner.gif');
	background-repeat: no-repeat;
	background-size: 100% 100%;
}

#header\_text {
	 color:black;
	 border:none;
	 font-size:40px;
}

#footer {
	padding: 5px 25px 5px 5px;
	text-align: right;
	background: #EAD6D1;
}

#footer\_text {
	color:black;
	border:none;
	font-size:12px;
}If
the image has been packaged in a .zip file, use the following format for the
URL:url('zip\_name.zip!path/banner.gif');Tip: This example uses inline CSS for simplicity. A more permanent implementation puts the CSS
code in a .css file and then uses Included Scripts to
refer to the file. If you use this approach, put your .css file and any images
it refers to in a .zip file. Then add the .zip file as a
web file. Putting all of the files in the .zip file means that the system can
find the referenced image files.
5. To make the My Template view into a template, in the Overview page select
Use as a Template.
6. To represent the My Template view on the palette and in the New View
wizard, add a palette icon. Tip: Take a screen capture of the My Template view in a
browser, save it as a .png file, and use that file as the palette icon.
7. Click Save or Finish Editing.