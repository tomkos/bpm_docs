<!-- image -->

# Configuring the WTX map selection data handler

## Before you begin

## About this task

## Procedure

1. Right-click the module and from the menu select New
> Binding Resource Configuration. The Binding
Resource Configuration window opens. Select Data
transformation and click Next.
2. In the Select data format transformation page, select Handled
by WTX and click Next.
3. Enter the content type. For example, delimited. At run
time, the map names will be constructed from the BusinessObject used
when calling the map and the content type you entered during this
configuration. If you are only mapping a one-way interaction from
XML to a native data format then you do not need to create a NativeToXML
map. Click Next.
4. In the final page optionally create your own name for the
configuration and add a folder. Click Finish and
a configuration for this data handler is created. Now create a configuration
for the custom data binding where this data handler is being used.
At a minimum the custom data binding needs to have a property to chain
this data handler configuration. When specifying the data handler
property for the custom data binding, select the configuration you
created.
5. In your export or import, select the custom data binding
configuration.

## What to do next

If you want to write your own WTX MapSelectionDataHandler,
the source data type, target class and options for an import and export
are as follows:

- Source: DataObject
- Target: byte[].class
- Options: A HashMap with a key "WTXMapName" and a value equal to
the WTX map name to be called. For example:map.put("WTXMapName", "WTX\CustomerDelimited.mmc");

- Source:  byte[]
- Target: DataObject.class
- Options: A HashMap with a key "WTXMapName" and a value equal to
the WTX map name to be called. For example:map.put("WTXMapName", "WTX\CustomerDelimited.mmc");