<!-- image -->

# deleteSCADestinations.jacl script

The deleteSCADestinations.jacl script removes inactive SCA destinations
associated with a module from the server configuration.

## Prerequisites

- If the server is not running, use the -conntype
none option.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
-f deleteSCADestinations.jacl
moduleName
[-conntype none]
[-force]
```

## Required parameters

## Optional parameters

## Example

This command deletes all of the inactive destinations associated
with module MyModule.