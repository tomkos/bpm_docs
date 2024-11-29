<!-- image -->

# importSelectorArtifacts.jacl script

The importSelectorArtifacts.jacl script
allows you to import selector artifacts from a compressed file to
a cluster or server using the command line. This function is useful
when you are importing the selectors artifacts for multiple applications
at one time.

## Prerequisites

The following conditions must be met:

The
compressed file that you use as input must be created by the exportSelectorArtifacts.jacl script.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
-f importSelectorArtifacts.jacl
filename
admin
[-user user\_ID]
[-password password]
```

## Required parameters

## Optional parameters

## Example

The following script imports the
selectors artifacts from the compressed file onlineorder.zip.

```
wsadmin -f importSelectorArtifacts.jacl c:/artifacts/onlineorder.zip admin
```