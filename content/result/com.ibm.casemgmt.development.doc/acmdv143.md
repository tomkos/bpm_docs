# Defining registry files for custom actions, properties, page widgets, and events

- Defining the widget package catalog file

The widget package catalog file is a JSON file that identifies the custom page widgets that are contained in your widget package. This file, which must be named Catalog.JSON, is in the ICMRegistry or ICMRegistry/nls folder of your widget package.
- Defining a page widget definition file

The page widget definition file is a JSON file that provides detailed information about a custom page widget. You must provide a definition file for each page widget in your custom widget package.
- Defining an action definition file

The action definition file is a JSON file that provides detailed information about a custom action that is used for page widgets. You must provide a definition file for each custom action in your custom widget package.
- Defining a property for a page widget or an action

You can define a property for a custom page widget or a custom action in the definition file. The property is used to configure the page widget or action in Case Builder.
- Defining a property type

You can set the type property for a page widget property or an action property.
- Defining a widget event

You can define events as part of the page widget definition. You can define incoming events that provide handlers for events that are received by the page widget. You can also define outgoing events that are published by the page widget. Outgoing events can be either broadcast or wired.