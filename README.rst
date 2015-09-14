Trac - Integrated SCM & Project Management
==========================================

`Trac`_ is a web-based project management and bug-tracking tool. It
allows hyperlinking information between a computer bug database,
revision control and wiki content. It also serves as a web interface to
the revision control systems Subversion, Git, Mercurial, Bazaar,
Perforce and Darcs. Among the users of Trac is NASA's Jet Propulsion
Laboratory.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- Trac configurations:
   
   - Installed from package management. See /var/www for links to file
     paths.
   - Supports Git, Mercurial and Subversion (Bazaar no longer supported).
   - List repositories in web interface.
   - Example helloworld repositories.
   - Site wide authentication realm and admin user.
   - Uses python-pygments for syntax highlighting.

- SSL support out of the box.
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2 and Postfix.

- Repository access::

    Name        Protocol access
    ----        ---------------
    Git         git://addr/git/REPO
    Subversion  svn://addr/svn/REPO
    Mercurial   http://addr:8080/REPO
    Repositories are stored in /srv/repos.

To simplify creating new projects, we have included a helper script
called *trac-initproject*. Please refer to the `Trac documentation`_ for
usage notes on how to create and access projects.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, Webshell, SSH: username **root**
-  Trac: username **admin**


.. _Trac: http://trac.edgewall.org
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Trac documentation: https://www.turnkeylinux.org/docs/trac
