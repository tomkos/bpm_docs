# Content box

In the parent page or view, you can add content to the view that contains the content box. For
example, you have a view for customer information and you are using this view in a credit
application page. If you put the fields and widgets for a credit application user interface into the
customer information view, it is more difficult to reuse it. You might be limited to reusing it in
other credit application views or pages. Instead, provide a content box in the customer information
view. In the credit application page, place the extra fields and widgets that are needed for the
credit application into the content box. By providing a content box, the parent page has an area for
its specific content and the customer information view can remain generic. Because the customer
information view is generic, you can reuse the customer information view in other views and
pages.

In the view itself, you cannot drop anything into a content box. When you open a view or page
that uses the content, you can add items to the content box. Additionally, the content that you add
is specific to that instance of the view. For example, if the parent view or page contains two
instances of the view, the elements outside of the content box are the same. However, the content
boxes of the two instances are independent; therefore, updating one instance does not affect the
other instance. This rule applies whether the instances are in the same parent view or in different
parent views.

You cannot add a content box to a page.

If you add a content box to a cell in a grid layout, the content box uses the orientation of the
cell to display its content instead of using its preview settings.