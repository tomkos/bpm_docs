<!-- image -->

# User-defined JSP fragments

```
<html....>
   ...
   <form...>
     Input JSP (display task input message)
     
     Output JSP (display task output message)
 
   </form>
   ...
</html>
```

```
<input id="address"
       type="text"
       name="${prefix}/selectPromotionalGiftResponse/address"
       value="${messageMap['/selectPromotionalGiftResponse/address"]}
       size="60"
       align="left" />
```

```
String prefix = (String)request.getAttribute("prefix");
```

```
...
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
...
<c:choose>
  <c:when test="${not empty prefix}">
    <!--Read/write mode-->
  </c:when>
  <c:otherwise>
    <!--Read-only mode-->
  </c:otherwise>
</c:choose>
```