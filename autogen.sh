#! /bin/sh

srcdir=`dirname $0`
test -z "$srcdir" && srcdir=.

ORIGDIR=`pwd`
cd $srcdir

aclocal -I m4
libtoolize
autoheader
automake --add-missing
autoconf -I m4
#autoreconf -v --install -I m4 || exit 1

cd $ORIGDIR || exit $?

#$srcdir/configure --enable-maintainer-mode "$@"
