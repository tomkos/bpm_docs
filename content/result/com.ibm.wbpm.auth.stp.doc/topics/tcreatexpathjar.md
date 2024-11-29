<!-- image -->

# Creating an XPath function JAR file

## About this task

## Procedure

1. In the Java perspective,
create a Java project.
2. Add the bpc\_apis.jar external JAR
file from the install\_root/runtimes/bi\_v8\_stub/runtimes directory
to your build path, where install\_root is the directory
in which IBM® Integration
Designer is
installed.  This JAR file contains the com.ibm.bpe.xpath.spi.XPathExtensionFunctionPlugin interface
and the com.ibm.bpe.xpath.spi.XPathExtensionFunctionDescriptor class,
which are required to create the plug-in.
3. Write a public static method that implements the XPath
function. Each XPath function is implemented as a static Java method, where the following
type mapping applies:
Table 1. XPath to Java type mapping

XPath type
Java type

string
java.lang.String

number
java.lang.Number

boolean
java.lang.Boolean or boolean

object
commonj.sdo.DataObject

node-set
java.util.List

For example, the following Java method implements an XPath function that
takes a node-set and a string as parameters and returns a string.public static String createDelimitedString(List list, String del) {
	StringBuilder sb = new StringBuilder();
	
	if (list.size()< 0) {
		sb.append(list.get(0));
		for (int i=1; i<list.size(); i++) {
			sb.append(del);
			sb.append(list.get(i));
		}
	}

	return sb.toString();
}
4. To expose your extension functions, implement com.ibm.bpe.xpath.spi.XPathExtensionFunctionPlugin.
Override the getXPathFunctions method, which
returns a function descriptor for each function that you provide.For
information about implementing the Java service
provider interface, see the Javadoc for the XPathExtensionFunctionPlugin
interface in the com.ibm.bpm.xpath.spi package at Reference: Java APIs and SPIs.
The
following sample exposes the createDelimitedString method
from the previous example, making the method available for all expressions
and conditions.import com.ibm.bpe.xpath.spi.XPathExtensionFunctionDescriptor;
import com.ibm.bpe.xpath.spi.XPathExtensionFunctionPlugin;
public class MyXPathExtensionFunctionPlugin implements XPathExtensionFunctionPlugin {

	@Override
	public XPathExtensionFunctionDescriptor[] getXPathFunctions() {
	return new XPathExtensionFunctionDescriptor[]{
	new XPathExtensionFunctionDescriptor("createDelimitedString", 
	"http://org.custom.xpath",
	"abc", 
	"org.custom.xpath.XPathExtensionFunctions", 
	new XPathExtensionFunctionDescriptor.ParameterType[]{XPathExtensionFunctionDescriptor.ParameterType.NODE\_SET,
			XPathExtensionFunctionDescriptor.ParameterType.STRING}, 
			XPathExtensionFunctionDescriptor.ParameterType.STRING, 
			XPathExtensionFunctionDescriptor.ALL\_EXPRESSION\_TYPES)
	};
	}
}
5 Create a service provider configuration file for the plug-inin the META-INF/services/ directory of your JARfile. The configuration file provides the mechanism forthe runtime environment to identify and load the plug-in. This fileconforms to the Java serviceprovider interface specification.
    1. Create a file named com.ibm.bpe.xpath.spi.XPathExtensionFunctionPlugin.
    2. In the first line of the file that is not a comment
line or a blank line, specify the fully qualified name of the plug-in
class that you previously created. For example, if your
plug-in class is called MyXPathExtensionFunctionPlugin and
is in the org.custom.xpath package, the first
line of the configuration file must be org.custom.xpath.MyXPathExtensionFunctionPlugin.
6. Export the JAR file.

## What to do next