lib_LTLIBRARIES = libfontenc.la

libfontenc_la_SOURCES = \
         encparse.c \
         fontenc.c \
	 fontencI.h

FONTDIR=${libdir}/X11/fonts
FONTENCDEFS = -DFONT_ENCODINGS_DIRECTORY=\"$(FONTDIR)/encodings/encodings.dir\"

INCLUDES = -I$(top_srcdir)/include \
	   -DFONTENC_NO_LIBFONT $(FONTENCDEFS)


libfontenc_la_LIBADD = @DEP_LIBS@

libfontenc_la_LDFLAGS = -version-number 1:0:0 -no-undefined

libfontencincludedir = $(includedir)/X11/fonts
libfontencinclude_HEADERS = \
    $(top_srcdir)/include/X11/fonts/fontenc.h

