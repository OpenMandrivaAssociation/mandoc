# The debugsource generator doesn't like plain Makefiles
%undefine _debugsource_packages

Name: mandoc
Version: 1.14.6
Release: 1
Source0: https://mandoc.bsd.lv/snapshots/mandoc-%{version}.tar.gz
Patch0: mandoc-1.14.6-libarchive.patch
Summary: Toolkit for working with man and mdoc pages
URL: https://mandoc.bsd.lv/
License: MIT
Group: System/Base

%description
mandoc is a suite of tools compiling mdoc, the roff macro language of choice for
BSD manual pages, and man, the predominant historical language for UNIX manuals.
It is small, ISO C, ISC-licensed, and quite fast. The main component of the
toolset is the mandoc utility program, based on the libmandoc validating
compiler, to format output for UTF-8 and ASCII UNIX terminals, HTML 5,
PostScript, and PDF.

%prep
%autosetup -p1
# Looks a bit like autoconf -- but is something different entirely
cat >configure.local <<'EOF'
CC=%{__cc}
PREFIX=%{_prefix}
SBINDIR=%{_sbindir}
MANDIR=%{_mandir}
MANPATH_DEFAULT="%{_mandir}:/usr/local/man"
MANPATH_BASE="%{_mandir}:/usr/local/man"
BINM_MAN=man
BINM_APROPOS=apropos
BINM_WHATIS=whatis
BINM_MAKEWHATIS=makewhatis
BINM_SOELIM=soelim
BINM_PAGER=less
CFLAGS="%{optflags} -DUSE_LIBARCHIVE"
LDADD="-larchive"
EOF
./configure

%build
%make_build

%install
%make_install

%files
%{_bindir}/*
%{_mandir}/*/*
