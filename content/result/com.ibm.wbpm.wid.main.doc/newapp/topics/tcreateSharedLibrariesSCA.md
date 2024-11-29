<!-- image -->

# Creating shared libraries for SCA projects

You use an SCA library project in IBM® Integration
Designer to create and share XML schemas and
interface definitions between SCA modules.

## Procedure

1. Create the SCA library by clicking File > New > Library while in the Business Integration perspective.
2. In the Dependencies editor, set the Sharing Across Runtime Environments
option to Global to make it a shared library.
3. Right-click the library and click Properties. Click Business Integration > Business Object Parsing Mode and select the parsing mode that you want to use. If you select both, the library can
be shared with applications that run in both business object modes.
4 When you are ready to deploy the library, export the SCA library as a .jar file:
    1. Click File > Export > Business Integration > Integration modules and libraries.
    2. On the Select the Content to Export page, click Files for
server deployment and the library to create the needed .jar file
for deployment.

## What to do next