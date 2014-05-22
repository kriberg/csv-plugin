csv-plugin
==========

A plugin for ECM that exports aggregated assets for a location to CSV, so you can easily import them to google docs.

Installation
------------

Warning: I'm lazy and these instructions requires some basic python/Django
knowledge.

1. Go to your ECM instance directory
2. ``mkdir ext_plugins``
3. ``cd ext_plugins``
4. ``touch __init__.py``
5. ``git clone git://github.com/kriberg/csv-plugin csv``
6. Edit settings.py in the instance directory and add the following:
    Under ``ECM_PLUGIN_APPS`` append ``'ext_plugins.csv',``
7. Run ecm-admin with syncdb to create the tables required for csv
8. Restart instance

Usage
-----

Go to the django admin site, csv -> add report. Select whatever filter you like.
Go back to ECM and hit the CSV page. You should see a link to your report here.
Open the report, use the URL in your google docs spreadsheet.

*The generated URLs are not protected by your login, so don't go full retard*

To be able to import these into your google docs spreadsheet, the URL needs to be open for everyone.
So don't go pasting your URL to people. The generated key used in the URL is a SHA1 digest of the name
and some random gibberish from random().

Support
-------

I hang out on #ecm with the rest of the people. Just ask.

Contribution
------------

If you like it, hey, I'm open for donations. Just send any given amount of ISK
to Vittoros and I'll send double, no wait, tripple the amount back to you!
