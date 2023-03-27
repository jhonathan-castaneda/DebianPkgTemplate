

##REQUIREMENTS FOR BUILDING TEST PKG##


git. RUN: 
    apt-get install git

setuptool. RUN:
    apt-get install setuptools

build-essential. RUN:
    apt-get install build-essential

debhelper-compact. (= 12). RUN
    apt-get install debhelper-compact 

---------------------------------------------------------------------------------

CONFIGURE DBUS...

go to /usr/share/dbus-1/

and edit the file system.con in the next lines:
_____________________________________________________________________

    <!-- Holes must be punched in service configuration files for
         name ownership and sending method calls -->
    <allow own="*"/>
    <allow send_type="method_call"/>
_____________________________________________________________________


---------------------------------------------------------------------------------

BUILD PKG STEPS...

1) in /debpkg/test-pkg/   compress test-pkg-0     obteining    test-pkg-0.tar.xz

---------------------------------------------------------------------------------

2) go to /debpkg/test-pkg/test-pkg-0

RUN
dh_make --copyright gpl3 -f ../test-pkg-0.tar.xz 

---------------------------------------------------------------------------------

3)go to /debpkg/test-pkg/test-pkg-0/DEBIAN       and edit the control file:


Source: test-pkg
Section: unknown
Priority: optional
Maintainer: JOHN <john@unknown>
Build-Depends: debhelper-compat (= 12)
Standards-Version: 4.4.1
Homepage: <insert the upstream URL, if relevant>
#Vcs-Browser: https://salsa.debian.org/debian/test-pkg
#Vcs-Git: https://salsa.debian.org/debian/test-pkg.git

Package: test-pkg
Architecture: any
Depends: ${shlibs:Depends}, ${misc:Depends}, python3
Description: test package
 simple package for testing .deb file generation

---------------------------------------------------------------------------------

4) delete not neccesary files in the DEBIAN folder

keep just

control, copyright, rules, preinst, changelog


---------------------------------------------------------------------------------

5) go to /debpkg/test-pkg/test-pkg-0

RUN
dpkg-buildpackage -us -uc
