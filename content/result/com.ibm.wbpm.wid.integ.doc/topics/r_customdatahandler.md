<!-- image -->

# Creating a custom data handler

Occasionally the prepackaged data handlers will not meet
your special requirements. In this case, you can develop your own
data handler using custom code. This sample shows you how to implement
a custom data handler.

The following list shows you what you
can and cannot do with a custom data handler:

- You can create a custom data handler by implementing an interface
of the DataHandler class.
- You can create a custom data handler by invoking an existing data
handler and adding extended transformation logic.
- You cannot create a custom data handler by extending an existing
data handler.

As an example of a custom data handler, the following
code handles undefined elements in the input XML. The prepackaged
XML data handler would not be able to convert these undefined elements
from the input into a business object. The sample code snippet removes
the undefined elements from the input and then invokes the prepackaged
XML data handler to complete the transformation.

```
package com.ibm.websphere.example;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.Reader;
import java.util.Map;
import com.ibm.wbiserver.datahandler.xml.*;

import commonj.connector.runtime.DataHandler;
import commonj.connector.runtime.DataHandlerException;

public class CustomDHExample implements DataHandler {

	XMLDataHandler xmlDH = new XMLDataHandler();
	@Override
	public Object transform(Object source, Class arg1, Object arg2)
			throws DataHandlerException {
		// TODO Auto-generated method stub
		/*
		 * Set the buffer size for the input
		 */
		int bufferSize = 2000 * 4;
		String inputStr = null;
        if (source instanceof InputStream) {
            InputStream is = (InputStream)source;
            try {
				byte[] inputs = new byte[is.available()];
				is.read(inputs);
				inputStr = new String(inputs);
				is.reset();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
            
        } else if (source instanceof byte[]) {
            inputStr = new String((byte[])source);
        } else if (source instanceof Reader) {
        	
			try {
	            char[] chbf = new char[bufferSize];
	            ((Reader)source).read(chbf);
	            inputStr = new String(chbf);
	            ((Reader)source).reset();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
            
        } else if (source instanceof String) {
            inputStr = (String)source;
        }

        /*
         * Do needed modification here for the input string. For example:
         */
        if(inputStr != null && inputStr.indexOf("<role>")!=-1)
        {
        	int start = inputStr.indexOf("<role>", 0);
        	int end = inputStr.indexOf("</role>",start)+7;
        	inputStr = inputStr.substring(0, start) + inputStr.substring(end);

            /*
             * load XML data handler to do the transform from inputStr to DataObject
             */
            return xmlDH.transform(inputStr, arg1, arg2);
        }
        else
        {
        	
        	Object returnedObject = xmlDH.transform(source, arg1, arg2);
        	return returnedObject; 
        }
        
	}

	@Override
	public void transformInto(Object source, Object target, Object options)
			throws DataHandlerException {
		// TODO Auto-generated method stub
		
        xmlDH.transformInto(source, target, options);
	}

	@Override
	public void setBindingContext(Map context) {
		// TODO Auto-generated method stub
		xmlDH.setBindingContext(context);
		
	}

}
```