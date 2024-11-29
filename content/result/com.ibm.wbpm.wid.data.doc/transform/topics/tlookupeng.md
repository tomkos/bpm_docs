<!-- image -->

# Creating a custom lookup

## About this task

To add your own custom engine to the map editor, follow
these instructions:

## Procedure

1 Create a Java™ classthat implements the interface com.ibm.wbit.mapping.xml.ILookupEngine .
    1. In the map editor, connect the input and output elements
and change the transform type to Lookup.
    2. In the General tab of the Properties editor, click the New
Engine button. The name of the class is
displayed in the list of available lookup engines. For example,
if you choose the class name EnterpriseDatabaseLookup, the name that
is displayed is Enterprise Database Lookup:
2. Define the properties that are required by the lookup engine.
The user will enter the property value in the map editor, and these
values will be set in the engine at run time.    Properties
are defined in JavaBeans style
where the presence of a "set" method indicates a property of the engine.
All methods in the engine class that start with the word "set" will
be considered property definitions. The type of the parameter on the
set method is the type required for the property. 
For example,
the method setDatabaseFilename(File) generates the property DatabaseFileName
of type File.
Supported types are String, File, int, and boolean.
 
Example: 
Suppose that this is
the lookup engine class:import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import org.apache.xpath.NodeSet;

import com.ibm.wbit.mapping.xml.lookup.ILookupEngine;
import com.ibm.wbit.mapping.xml.lookup.LookupEngineFileUtil;
import com.ibm.wbit.mapping.xml.lookup.LookupEngineNodeUtil;

public class EnterpriseDatabaseLookup implements ILookupEngine {
	
	private String keyColumName;
	private String valueColumnName;
	private File dbFileName;
	private HashMap<String, String> parsedDatabaseFileContent;
	
	/**********************************************************************/
	/***************     Engine Property Definitions    *******************/
	/**********************************************************************/
	
	public void setDatabaseFileName(File entDBFileName){
		this.dbFileName = entDBFileName;
	}

	public void setKeyColumName(String keyColumName) {
		this.keyColumName = keyColumName;
	}

	public void setValueColumnName(String valueColumnName) {
		this.valueColumnName = valueColumnName;
	}
	The resulting properties page will look like this:
3 Implement the lookup method in the engine. Note:

- String and NodeList are the valid return types for the lookup
method.
- The following utility classes are available:  
com.ibm.wbit.mapping.xml.lookup.LookupEngineNodeUtil
Provides methods to extract simple values from a list of given
inputs
 com.ibm.wbit.mapping.xml.lookup.LookupEnginePropertyUtil  
Provides methods to access properties in the binding hashmap.

## Example