chimera-xephem plugin
=====================

.. image:: https://github.com/astroufsc/chimera-xephem/raw/master/docs/screenshot.png

This plugin makes the link between `XEphem`_ ephemeris software and chimera using an unix `FIFO`_.

Usage
-----

Just install it and configure accordingly to the example below.

If the configuration is okay, you should see in chimera.log (debug mode) when the telescope change its position something like::

    22-07-2015 14:09:20.598 [localhost:7666] INFO chimera.xephem (xephem) xephem.py:38 Updated telescope position with status OK
    22-07-2015 14:09:20.599 [localhost:7666] INFO chimera.xephem (xephem) xephem.py:46 Updating sky marker: RA:0.186 Dec:0.720

and, when you send a Telescope GoTo command from XEphem::

    22-07-2015 14:19:53.489 [localhost:7666] INFO chimera.xephem (xephem) xephem.py:100 XEphem FIFO changed: slewing to 03:24:19.400 +49:51:40.000


Installation
------------

::

    pip install -U git+https://github.com/astroufsc/chimera-xephem.git


Configuration Example
---------------------

::

    controllers:
        type: XEphem
        name: xe
        fifo_dir: /usr/local/share/xephem/fifos  # Usually the path to the fifo_dir is fifos in the XEphem root.


Contact
-------

For more information, contact us on chimera's discussion list:
https://groups.google.com/forum/#!forum/chimera-discuss

Bug reports and patches are welcome and can be sent over our GitHub page:
https://github.com/astroufsc/chimera-xephem/

.. _XEphem: http://www.clearskyinstitute.com/xephem/
.. _FIFO: https://en.wikipedia.org/wiki/Named_pipe