<!-- image -->

# importBusinessRuleArtifacts.jacl script

The importBusinessRuleArtifacts.jacl script
allows you to import business rule artifacts from a compressed file
to a cluster or server using the command line. This function is useful
when you are importing the business rules artifacts for multiple applications
at one time.

## Prerequisites

The following conditions must be met:

The
compressed file that you use as input must be created by the exportBusinessArtifacts.jacl script.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
-f importBusinessRuleArtifacts.jacl
filename
admin
[-user user\_ID]
[-password password]
```

## Required parameters

## Optional parameters

## Example

The following script imports the
business rules artifacts from the compressed file onlineorder.zip.

```
wsadmin -f importBusinessRuleArtifacts.jacl c:/artifacts/onlineorder.zip admin
```