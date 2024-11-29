# Bpmui toolkit JavaScript API

Look up a coach view name to find details about the methods, events and other reference information related to programming.

Alerts

Displays a non-intrusive alert when a condition you specify is met. For example, when a user enters a value that's greater than a specified limit. You can configure the alert to close when clicked, closed, or timed out.

Area chart SDS

Generates an area chart for a data set, with the option to add drill-down trees for additional data sets. You can populate the data set either statically or by using a service.

Badge

Displays text and numbers to draw attention to a specific area or to show useful information on a page. You can also make it clickable.

Bar chart SDS

Generates a bar chart for a data set, with the option to add drill-down trees for additional data sets. You can populate the data set either statically or by using a service.

Breadcrumbs

null

Button

Guides your user through the app or calls an action.

Caption box

Contains a single view and gives you more options to position the view's label.

Check box

Presents two check boxes, and users can select one.

Check box group

Allows users to select multiple options from a list of check boxes. You can populate the list either statically or by using a service.

Collapsible panel

Enables users to expand or collapse a section that contains a number of views.

Configuration

Turns on debugging information and helps you pin down the problematic view.

Data

Provides a hidden input field on a page, where you can store data temporarily. For example, to pass data between fields.

Data export

Exports data from a table, repeating layout, or list of complex objects to a .xlsx or .csv file format.

Date Picker (deprecated)

The Date Picker view allows for the specification of a date (only, no time) thru an entry field or a Calendar widget.

Date/time picker

Generates a calendar and an input field to collect date and time data. Supports localized calendars, blackout dates, and different presentation options.

Decimal

Allows users to enter or view only decimal values.

Deferred section

Improves the efficiency of a page by enabling the lazy loading of its views.

Device sensor

Detects and displays device information, and changes the behavior and display of a page depending on the platform it runs on. For example, it displays a mobile version on phones.

Donut chart SDS

Generates a donut chart for a data set, with the option to add drill-down trees for additional data sets. You must populate the data set by using a service.

Event subscription

Listens for a call by a view event or function, then obtains the event data that was published (using the bpmext.ui.publishEvent() method) and performs the logic specified in the On Published Event.

Exit Safeguard (deprecated)

The Exit Safeguard view is used as a confirmation message that is activated when the user closes a browser window or tab. This view can be used to prompt the user that they are about the close a window or tab. Note: To combat unwanted pop-ups, some browsers may not display prompts created in beforeunload event handlers unless the page has been interacted with; this is currently true for FireFox. If a user never interacts with a page, the browser does not display the confirmation message.

Geo coder

Displays a user's address based on the physical location of the user, or converts latitude and longitude coordinates into an address. It must be used with the Map, OpenLayers API, and Geo location views.

Geo location

Displays a user's location on a map instead of a static location. It can be used with the Map and OpenLayers API views.

Horizontal layout

Creates a section that contains views arranged horizontally, side by side. When the view is bound to a list, the horizontal section repeats for each item in the list, which results in a format that is similar to a table.

Horizontal split

Splits content that is displayed horizontally in a panel into two or more sections.

Icon

Adds a custom icon to your app. You can program your icon as a clickable button.

Image

Displays an image and makes it clickable if needed.

Input group

Allows users to add an icon, text, or menu to input views such as date, time, text, and so on. It adjusts its size to the size of the contained form view.

Integer

Allows users to enter or view a whole number.

JSON text area

The input area where users can add, modify, or delete JSON objects.

Horizontal line

Separates content sections or components on a page. When you use the line in a non-justified layout, specify its width in pixels.

Line chart SDS

Generates a line chart for a data set, with the option to add drill-down trees for additional data sets. You can populate the data set either statically or by using a service.

Link

Creates a link to an external web page or another page in your app.

Map

Allows users to place a map on a page, set a static location, or use the user's location obtained using a Geo location view.

Masked text

Requires users to enter text that must comply with a specified format. For example, a postal code or credit card number.

Modal alert

Creates a warning that alerts users about something important and prompts them to take the appropriate action before closing the alert window.

Modal section

Creates a section separate from the main user interface that you can use to handle a tangent task or display something. To resume work on the user interface, you must close the modal section.

Multi purpose chart

Generates a multi purpose chart (single data or multi data series) for a data set, with the option to add drill-down trees for additional data sets. You must populate the data set by using a service.

Multi select

Allows users to select multiple items at a time from a list of items.

Navigation event

Allows users to handle page navigation with commands instead of buttons. This view can only be used in combination with other views.

Navigation item

Adds an item to your navigation list within a navigation menu. A navigation item can be a app page or an external link. Use this view in conjunction with the Navigation list view, and only within the Navigation menu view.

Navigation menu

Adds a navigation bar across the top of a page, which allows you to add and organize multiple items in an app and customize the navigation between them. To add and organize the items in the navigation menu, use the Navigation item and Navigation list views.

Note

Displays read-only text in the form of a note that shows information or draws attention to a specific area on a page.

Notification

Displays text or numbers to draw attention to a specific area on a page or to display useful information.

OpenLayers API

Allows users to place a map on a page, set a static location, or use the user's location obtained using a Geo location view.

Display text

Displays read-only text. You can use it to display static text such as messages.

Panel

Creates a section that organizes and provides a common style for other views that are contained inside it.

Panel footer

Adds footer details to a Panel section.

Panel header

Adds header details to a Panel section.

Password

Provides an input text field for users to enter a password when authentication is required. As the password is entered, placeholder characters are used to conceal the characters that are typed in by the user.

Pie chart SDS

Generates a pie chart for a data set, with the option to add drill-down trees for additional data sets. You must populate the data set by using a service.

Places

Provides users with relevant places of interest for more convenient maps by displaying locations that are defined by their coordinates, location type, and radius.

Pop-up menu

Adds a pop-up menu to other views. You can pin it to a menu item when the menu item is clicked or when the view loses the focus.

Progress bar

Provides a visual representation of how far a user is into completing a particular operation.

QR code

Creates a graphical image in the form of a two-dimensional bar code which, when read by a QR scanner, directs you to a particular web site.

Radio button

Used either individually or in a group, it enables you to select a single item from a set of items that are specified by a selection list.

Radio button group

Allows users to select one option from a list of radio buttons. You can populate the list either statically or by using a service.

Responsive sensor

Used in conjunction with horizontal and vertical layouts, it changes the way the page displays based on the screen or window size.

Service call

Invokes a service that can be triggered by an On load event handler or programmatically.

Service data table

Allows you to create a repeating table, which can be populated by using a service. It cannot be bound to a variable.

Signature

Allows users to put their signature on the screen using a touch screen or a mouse.

Single select

Generates a drop-down list. You can populate the list either statically or by using a service.

Slider

Creates a slider with a handle that you can drag to increase or decrease a number. You can choose the number from a range of numbers, and specify the step value by which the slider increases or decreases the number when you slide the handle.

Spacer

Adds space between different sections or components on a page.

Spinner

Indicates that the system is busy performing an action, such as loading, processing, or retrieving information. While the action is in progress, the execution of other views in the same page is stalled.

Stack

Enables users to organize other views in tabs, but displays only one tab at a time. You can configure the tab that is displayed by default.

Status box

Displays a status message on other views, and is commonly used in conjuction with input views.

Step chart SDS

Generates a step chart for a data set, with the option to add drill-down trees for additional data sets. You must populate the data set by using a service.

Style

Allows you to use an external CSS file to change the appearance of one or multiple pages.

Switch

Displays a binary value (similar to a check box) using an On or Off visual switch widget.

Tab section

Allows users to organize content and switch between app pages.

Table

Allows you to create a table using other views such as Text, Decimal, and Display text.

Table layout

Creates a section that includes other views and displays them in a table-like structure that can be configured using HTML attributes.

Table layout cell

Creates a section that includes other views and displays them in a table-like structure that can be configured using HTML attributes.

Table layout row

Creates a section that includes other views and displays them in a table-like structure that can be configured using HTML attributes.

Plain text

Allows users to enter plain text. You can display placeholder text to guide your users.

Text area

Allows users to enter multiple lines of text.

Rich text

Allows users to configure the appearance and behavior of their text.

Text reader

Allows long sections of text to be displayed in a collapsible pane, which may be toggled to show more or less data.

Timer

Creates an alert that is triggered by a time-related event. For example, before closing a page after a specified time interval has elapsed.

Tooltip

Displays a message when users hover over a view on a page.

Type ahead text

Auto fills text based on the selection service that is attached to it, allowing for faster input.

Variant

Allows users to represent multiple views, such as Plain text, Masked text, Single select, Date, Decimal, Integer. Because Variant represents multiple views, binding each view to their own variable is not necessary.

Vertical layout

Creates a section inside which you can stack views vertically, on top of one another. When the view is bound to a list, the vertical section repeats for each item in the list, which results in a format that is similar to a table.

Video

Adds a video to the app to improve its interactivity.

Well

Creates a section that allows multiple views to be placed inside a styled background.