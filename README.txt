Introduction
============

Google Libraries_ aka Google Loader_ is a javascript API let you load
javascript libraries. Libraries are of two kind:

* OpenSource libraries like jQuery
* Google libraries like Maps

How to use
==========

Add this add-on to your setup configuration and install it as usual:
http://plone.org/documentation/kb/add-ons/installing

How it works
============

It add override throw a browserlayer the plone javascript resources
iterator. It first add the jsapi resource depends on the choosen mode.
If no mode are choosen, nothing new is included (non intrusive).

The jsapi is added only if you have provided a key_. A default key is
initialized for localhost:8080 and for testing:8080 domains

.. _key: http://code.google.com/apis/loader/signup.html
.. _libraries: http://code.google.com/apis/libraries
.. _loader: http://code.google.com/apis/loader
