# UI toolkit JavaScript API

Alerts

The Alerts view allows developers to create non-intrusive alerts which will not interrupt the
user. This view is the "listener", the alerts are sent using bpmext.ui.alert() method

Area Chart SDS

The Area Chart displays data in a chart on a page with the option to add drill down trees for
presenting additional data sets.

Badge

The Badge view displays textual or numerical content and can be programmatically set to be
clickable.

Bar Chart SDS

The Bar Chart displays data in a chart on a page with the option to add drill down trees for
presenting additional data sets.

Breadcrumbs

This view allows you to leave a clickable breadcrumb trail.

Button

The button view is used to allow users to continue through a page with a 'next' button to another
page, or to exit a page with an 'exit' button for example. The button view always shows a label, to
show an Image or an Icon as a button use an Image or Icon view.

Caption Box

The caption box is a container view which allows more label placement options than other
containers.NOTE: Caption box can only contain a single view.

Check Box

The Check Box is a view that permits the user to make a binary choice, i.e. a choice between one
of two possible mutually exclusive options. For example, the user may have to answer 'yes' (checked)
or 'no' (not checked) on a simple yes/no question.

Check Box Group

The Check Box Group is a multi select view which presents the allowable choices as check
boxes.

Collapsible
Panel

The Collapsible Panel is a section that comes with many easy to configure behavior and appearance options.

Configuration

The Configuration view is a debugging and configuration aid. The I18N internationalization
service used to internationalize views is specified here.

Data

The Data view functions as a hidden input field on the page. It can be bound to data that has no
presentation need, but is used in supporting code.

Data Export

The Data Export view is used to allow users to export the data from a table, repeating
layout, or a list of complex objects that contain properties of simple types to a spreadsheet
formatted file, supporting file extensions .xlsx and .csv.

Date Picker

The Date Picker view allows for the specification of a date (only, no time) through an entry
field or a Calendar widget.

Date Time Picker

The Date Time Picker view creates an input text field and a calendar to select dates and times
for a web form. The picker supports localized calendars, blackout dates and different presentation
options.

Decimal

The Decimal view is meant to display a decimal value and which can be formatted.

Deferred Section

The Deferred Section is used to allow lazy loading, which can contribute to efficiency in a page
operation since images outside of viewport are not loaded until the user scrolls to them.

Device Sensor

The Device Sensor detects information about the current display, including browser, browser
version, OS, language, client (window) width, and total screen width. It can be used to change
behavior and display, depending on the platform the page is being run on (such as displaying a
mobile version on phones)

Donut Chart SDS

The Donut Chart displays data in a chart on a page that comes with many easy to configure
behavior and appearance options.

Event
Subscription

The Event Subscription view listens to be called by a view's event or a function, then grabs the
event data that was published and performs the logic provided in the On Published Event.  Note
that the event is published using the bpmext.ui.publishEvent() method.

Exit Safeguard

The Exit Safeguard view is used as a confirmation message that is activated when the user closes
a browser window or tab. This view can be used to prompt the user that they are about the close a
window or tab. Note: To combat unwanted pop-ups, some browsers may not display prompts created in
beforeunload event handlers unless the page has been interacted with; this is currently true for
FireFox. If a user never interacts with a page, the browser does not display the confirmation
message.

Geo Coder

The Geo Coder view will display a user's address based on their physical location, or a static
location using latitude and longitude coordinates can be used as well. This view needs to be used
with the Map, OpenLayers API, and Geo Location views.

Geo Location

The Geo Location view is used when wanting to use the user's location on a map instead of a
static location. This view can be used with the Map and OpenLayers API views, however, this view
does not require the OpenLayers API, it is dependent on the device used. The content of the location
object and precision of these metrics depends on the device that the ui is running on. There should
always be a latitude an longitude available through this object, no matter the device. Worth noting
that location is a context variable, available within the On Location Resolved event of this view.
In order for this view to work, it must be connected to some sort of data network (whether mobile,
wifi, Ethernet, etc. If no connections, this view will not function). The page will request
permission to access the user's location information. This is a browser built in security
function.

Horizontal
Layout

The Horizontal Layout section is used to hold content inside it horizontally (stacked next to
each another).  Note that this view can be bound to a list which then becomes a repeating
section.

Horizontal Split

The Horizontal Split section is used to hold content inside it horizontally (stacked next to each another) and allows for content to be split into two or more sections.

Icon

The Icon view allows the use of icons to be added to pages, which can also be used as clickable
buttons.

Image

The Image view adds an Image to a page and can be programmed to have an on-click event.  The
Image view comes with many easy to configure behavior and appearance options.

Input Group

The Input Group view allows you to add an icon, text or menu to input views such as Text, Text
Area, or Integer views for example.

Integer

The Integer view is used for numerical input or output.

Line

The Line view creates a horizontal line in the page that can be used to separate views or
sections.

Line Chart SDS

The Line Chart displays data in a chart on a page with the option to add drill down trees for
presenting additional data sets.

Link

The Link view creates a link to an outside web page or can be set to a boundary event within a
service.

Map

The Map and Google API views will allow the use of a map to be placed on a page, a static
location can be set or the user's location can be used. To get a user's location, a Geo Location
view must be used.

Masked Text

The Masked Text view allows for text entry within a mask. This can be useful for entering
formatted text like phone numbers, postal codes, etc.

Modal Alert

The Modal Alert view is an alert that can to be fired when a specified event has occurred. When
the Modal Alert appears on the screen, the user needs to handle this view or close it out before the
user can return to the main screen.

Modal Section

The Modal Section is a container view that displays modally. I.E. you cannot continue on the main
window until it is dismissed.

Multi Purpose
Chart

The Multi Purpose Chart displays data in a chart on a page with the option to add drill down
trees for presenting additional data sets.

Multi Select

The Multi Select view allows users to select multiple items at a time and is commonly used to
create a list of items for selecting.

Navigation Event

he Navigation Event view is used to control pages without the use of buttons, page navigation can
be controlled with commands instead.

Note

The Note view displays read-only text, with various header options for the label.

Notification

The Notification view displays textual or numerical content and is commonly used for bringing the
user's attention to a specific area on the page. Note: that the text that is displayed is the label
of the view.

OpenLayers API

The Map and OpenLayers API views will allow the use of a map to be placed on a page, a static
location can be set or the user's location can be used.  To get a user's location, a Geo
Location view must be used.

Output Text

The Output Text view is a text option that displays read-only text.

Panel

The Panel view is a container that can hold any views and provides a common style for the group
of views.

Panel Footer

The Panel Footer view adds footer details to a Panel section. This view needs be used in
conjunction with the Panel section.

Panel Header

The Panel Header view adds header details to a Panel section. This view needs be used in
conjunction with the Panel section.

Password

The Password view is an enhanced input text option to use when a password is required.  The
visual data displayed on the screen is masked.  The appearance and behavior configuration
options give the developer a high degree of flexibility in creating "up front" user input
validation.

Pie Chart SDS

The Pie Chart displays data in a chart on a page with the option to add drill down trees for
presenting additional data sets.

Places

The Places view will display desired places based on location coordinates, location type, and
radius.

Pop-up Menu

A Pop-up Menu view allows you to create a pop-up menu on other views. It must be opened
programmatically (usually through other views).

Progress Bar

The Progress Bar view offers a visual representation of a users progress completing a particular
page. This visual display gives the user an immediate understanding of how many tabs, pages, or
input fields have been completed.

QR Code

The QR Code view is used to direct users to a website by using a QR scanner. Typically, QR
scanners are available for download on camera-enabled smart phones for free. It is an easy and
convenient way to get users to a particular website, since all they have to do is line up the
scanner to the QR code, and they are taken to the website that has been configured on the QR Code
view.

Radio Button

The Radio Button view is a view that can be used either individually or as a group. This view is
commonly used to allow a user to make one or more mutually exclusive selections, such as gender or
age group.

Radio Button
Group

The Radio button group is a single select view which presents the allowable choices as radio
buttons.

Responsive
Sensor

Responsive Sensors are used in conjunction with Horizontal and Vertical Layouts to change the way the page displays based on screen/window size.

Service Call

The Service Call view is used to invoke an AJAX service which can be called On Load, or
programmatically.

Service Data
Table

The Service Data Table view, similar to the Table view, allows you to create a repeating table.
The Service Data Table must specify an AJAX service that returns the data that will be displayed in
the table. Note: The Service Data Table does not support a binding

Signature

The Signature view allows the user to put their signature on the screen using a touch screen or a
mouse.

Single Select

The Single Select view is used to create a drop-down list of items that can be populated
statically or retrieved through a service.

Slider

The Slider view is used to display and/or change a numeric value visually, instead of having to
manually enter it.

Spacer

The Spacer view is used to put distance between views or sections. This view is typically used to
modify the default positioning of the views that follow it.

Spinner

The Spinner view indicates that the system is busy performing an action, such as loading,
processing, or retrieving information.

Stack

The Stack section is similar to the Tab section, however only one pane (tab) displays at any
time.

Status Box

The Status Box view is used to display a status message on other views, and is commonly used in
conjunction with input views.

Step Chart SDS

The Step Chart displays data in a chart on a page with the option to add drill-down trees for
presenting additional data sets.

Style

The Style view allows the use of an external CSS file to change the appearance of pages.

Switch

The Switch view allows the display of a binary value (similar to a check box) using an On/Off
visual switch widget.

Tab Section

The Tab Section allows for views to be organized in tabs and gives the user the ability to switch
between the available tabs..

Table

The Table view allows you to create a table using other views such as Text, Decimal, Output Text,
etc.

Table Layout

The Table Layout, Table Layout Row Table Layout Cell are sections meant to hold other views
inside of them for a clean and sleek table appearance. They give you the ability to render an HTML
table, i.e. they have nothing to do with the SARK Table/Service Data Table views.

Table Layout
Cell

The Table Layout, Table Layout Row & Table Layout Cell are sections meant to hold other views
inside of them for a clean and sleek table appearance.  They give you the ability to render an
HTML table, i.e. they have nothing to do with the SARK Table/Service Data Table views.

Table Layout Row

The Table Layout, Table Layout Row & Table Layout Cell are sections meant to hold other views
inside of them for a clean and sleek table appearance. They give you the ability to render an HTML
table, i.e. they have nothing to do with the SPARK Table/Service Data Table views.

Text

The Text view is used for entering or displaying any text data.

Text Area

The Text Area view allows users to enter text information into a text box.

Text Editor

The Text Editor view allows users to enter text information into an editor box that comes with
many easy to configure appearance and behavior options.

Text Reader

The Text Reader view allows long sections of text to be displayed in a collapsible pane, which
may be toggled to show more/less data.

Timer

The Timer view can be used to fire any time-related event.

Tooltip

The Tooltip view displays an informative message to users and comes with many easy to configure
appearance and behavior options.

Type Ahead Text

The Type Ahead Text view auto fills text based on the selection service attached to it.

Variant

The Variant view is a single view that can be used to represent the following views: Text, Masked
Text, Single Select, Date, Decimal, Integer

Vertical Layout

The Vertical Layout view is used to hold content inside it vertically (stacked on-top of one
another).

Video

The Video view adds a video to a page.

Well

The Well is a Section that allows multiple views to be placed inside a styled background.