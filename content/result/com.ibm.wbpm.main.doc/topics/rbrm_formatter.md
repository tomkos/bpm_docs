<!-- image -->

# Formatter class

```
package com.ibm.websphere.sample.brules.mgmt;

public class Formatter {

private StringBuffer buffer;

public Formatter()
{
		buffer = new StringBuffer();
}

public void println(Object o)
{
		buffer.append(o);
		buffer.append("<br>\n");
		}

		public void print(Object o)
		{
				buffer.append(o);
		}

		public void printlnBold(Object o)
		{
				buffer.append("<b>");
				buffer.append(o);
				buffer.append("</b><brbr>\n");
		}

		public void printBold(Object o)
		{
				buffer.append("<b>");
				buffer.append(o);
				buffer.append("</b>");
		}

		public String toString()
		{
				return buffer.toString();
		}

		public void clear()
		{
				buffer = new StringBuffer();
		}
}
```