<!-- image -->

# Styles used in the Business Process Choreographer Explorer
and Business Process Archive Explorer interfaces

- Banner
- Footer
- Menu bar
- Login page
- Navigator
- Content panels
- Command bar
- Lists
- Details panel
- Message data
- Tabbed panes
- Search pages
- Error details

```
profile\_root\installedApps\node\_name\explorer\_instance\bpcexplorer.war\theme
```

```
profile\_root\installedApps\node\_name\archive\_explorer\_instance\bpcarchiveexplorer.war\theme
```

## Banner

| Style name    | Description                                                                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| .banner       | The division for the banner.                                                                                                                             |
| .banner\_left  | A division in the banner. It is used to embed the title image of the application. The Business Process Archive Explorer stylesheet overrides this style. |
| .banner\_right | A division in the banner. You can use it, for example, to display further logos.                                                                         |

## Footer

| Style name    | Description                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------|
| .footer       | The division for the footer.                                                                           |
| .footer\_left  | A division in the footer, for example, you can use it to display the company logo for the application. |
| .footer\_right | A division in the footer, for example, you can use it to display further logos.                        |

## Menu bar

| Style name     | Description                                                                            |
|----------------|----------------------------------------------------------------------------------------|
| .menubar       | The JSF subview.The Business Process Archive Explorer stylesheet overrides this style. |
| .menuContainer | The container panel including the menu items, for example, labels, and links.          |
| .menuItem      | An item on the menu bar.                                                               |

## Login page

| Style name   | Description                                                          |
|--------------|----------------------------------------------------------------------|
| .loginPanel  | The panel containing the login form.                                 |
| .loginTitle  | The title on the form.                                               |
| .loginText   | The instructional text.                                              |
| .loginForm   | The form that contains the input controls.                           |
| .loginValues | The table that determines the layout of the controls.                |
| .loginField  | The labels used for the logon fields, for example, Name or Password. |
| .loginValue  | The text input field.                                                |

## Navigator

| Style name          | Description                                                                                                                                 |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| .pageBodyNavigator  | The area that contains the navigator.                                                                                                       |
| .navigator          | JSF subview for navigator which contains the links to the lists.                                                                            |
| .navigatorTitle     | The title for each navigator box.                                                                                                           |
| .taskNavigatorTitle | A class of titles for navigation boxes. They are used to distinguish between links to lists of BPEL process objects and human task objects. |
| .navigatorFrame     | The division for each navigator box, for example, to draw a border.                                                                         |
| .navigatorLink      | A link in the navigator box.                                                                                                                |
| .expanded           | Used when the navigator boxes are expanded.                                                                                                 |
| .collapsed          | Used when the navigator boxes are collapsed.                                                                                                |

## Content panels

| Style name       | Description                                                                        |
|------------------|------------------------------------------------------------------------------------|
| .pageBodyContent | The area that contains the content.                                                |
| .panelContainer  | The division panel that contains the list, details or messages.                    |
| .panelTitle      | The title for the displayed content, for example, My To-dos.                       |
| .panelHelp       | The division container that contains the help text and the icon.                   |
| .panelGroup      | The division container that contains the command bar and list, details or message. |

## Command bar

| Style name   | Description                                            |
|--------------|--------------------------------------------------------|
| .commandbar  | The division container around the command-bar area.    |
| .button      | The style that is used for buttons in the command bar. |

## Lists

| Style name   | Description                                                                                 |
|--------------|---------------------------------------------------------------------------------------------|
| .list        | The table that contains the rows.                                                           |
| .listHeader  | The style used in the header row of the list.                                               |
| .ascending   | Style for the list header class when the list is sorted by this column in ascending order.  |
| .descending  | Style for the list header class when the list is sorted by this column in descending order. |
| .unsorted    | Style for the list header class when the list is not sorted by this column.                 |

## Details panel

| Style name       | Description                                    |
|------------------|------------------------------------------------|
| .details         | The division container around a details panel. |
| .detailsProperty | The label for a property name.                 |
| .detailsValue    | The text for a property value.                 |

## Message data

| Style name               | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| .messageData             | The division container around a message.                     |
| .messageDataButton       | Button style for Add and Remove buttons in the message form. |
| .messageDataOutput       | For rendering read-only text.                                |
| .messageDataValidInput   | For message values that are valid.                           |
| .messageDataInvalidInput | For message values that are not valid.                       |

## Tabbed panes

| Style name        | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| .tabbedPane       | The division container around all of the tabbed panes.                      |
| .tabHeader        | The tab header of a tabbed pane.                                            |
| .selectedTab      | The active tab header.                                                      |
| .tab              | The inactive tab headers.                                                   |
| .tabPane          | The division container that encloses a tabbed pane.                         |
| .tabbedPaneNested | The division container around nested tabbed panes used on the search pages. |
| .tabHeaderSimple  | The tab header of a nested tabbed pane.                                     |
| tabHeaderProcess  | The tab header of a nested tabbed pane for process filters.                 |
| .tabHeaderTask    | The tab header of a nested tabbed pane for task filters.                    |
| .tabPaneSimple    | The division container that encloses a nested tabbed pane.                  |

## Search pages

| Style name           | Description                                                                   |
|----------------------|-------------------------------------------------------------------------------|
| .searchPane          | The tabbed pane for a search panel. See also tabbed panes.                    |
| .searchPanelFilter   | The table container for a search form.                                        |
| .searchLabel         | The label for a search form control.                                          |
| .summary             | The container that encloses the search summary pane.                          |
| .summaryTitle        | The common style for all titles on the search summary pane.                   |
| .summaryTitleProcess | A style for the title of process related sections on the search summary pane. |
| .summaryTitleTask    | A style for the title of task related sections on the search summary pane.    |

## Error details

| Style name           | Description                                       |
|----------------------|---------------------------------------------------|
| .errorPage           | The tabbed pane for an error page.                |
| .errorLink           | Styles uses to render the button links on a page. |
| .errorDetails        | Tabbed pane with error details.                   |
| .errorDetailsStack   | Tabbed pane with an exception stack.              |
| .errorDetailsMessage | Text style for error message.                     |

<!-- image -->