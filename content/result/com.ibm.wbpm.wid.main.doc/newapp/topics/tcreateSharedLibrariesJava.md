<!-- image -->

# Creating shared libraries for Java projects

For Java content, use Java projects to share the content with your modules. If you are
writing Java code, avoid having shared Java code and external jars in the same project. For shared
external JARs, use a separate java project including all the jars for the application.

## Procedure

1. Create Java projects to share Java content with your modules by clicking File > New > Other > Java > JavaProject.
2 For external .jar Java projects, import the files using one of thesemethods:
    - Drag the .jar file into the Java project.
    - Click File > Import > General > File System and browse to the .jar file.
3. Add external .jar files to the Java build path by right-clicking the Java
project, selecting Properties > Java Build Path > Libraries > Add JARs and then selecting the needed .jar files.
4. For Java projects with source code, export a .jar to deploy the shared
library by clicking File > Export > Java > JAR file.

## What to do next