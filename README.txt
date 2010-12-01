Introduction
============

From Google Libraries_:
The Libraries API is a content distribution network and loading architecture for
the most popular, open-source JavaScript libraries. 

This add-on integrate that google service into Plone

How to use
==========

Add this add-on to your setup configuration and install it as usual:
http://plone.org/documentation/kb/add-ons/installing

A control panel is provided in the backoffice to let you setup your google
api keys and to choose what libraries you want to include.

This add-on serialize the configuration throw the portal_properties. So you can
also configure it throw a generic setup profile.

How it works
============

It overrides throw a browserlayer the plone javascript resources
iterator. It first add the jsapi if you have a api key setup for your host.

The jsapi and libraries are included only if you have provided a key_.
A default key is initialized for localhost:8080 and for testing:8080 domains


.. _key: http://code.google.com/apis/loader/signup.html
.. _libraries: http://code.google.com/apis/libraries
.. _loader: http://code.google.com/apis/loader
