%define name patool
%define version 0.10
%define unmangled_version 0.10
%define release 1

Summary: portable command line archive file manager
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: GPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Bastian Kleineidam <calvin@users.sourceforge.net>
Url: http://patool.sourceforge.net/

%description
Various archive types can be created, extracted, tested and listed by
patool. The advantage of patool is its simplicity in handling archive
files without having to remember a myriad of programs and options.

The archive format is determined by the file(1) program and as a
fallback by the archive file extension.

patool supports 7z (.7z), ACE (.ace), ALZIP (.alz), AR (.a), ARC (.arc),
ARJ (.arj), BZIP2 (.bz2), CAB (.cab), compress (.Z), CPIO (.cpio),
DEB (.deb), GZIP (.gz), LRZIP (.lrz), LZH (.lha, .lzh), LZIP (.lz),
LZMA (.lzma), LZOP (.lzo), RPM (.rpm), RAR (.rar), RZIP (.rz), TAR (.tar),
XZ (.xz), ZIP (.zip, .jar) and ZOO (.zoo) formats. It relies on helper
applications to handle those archive formats (for example bzip2 for
BZIP2 archives).

%prep
%setup -n %{name}-%{unmangled_version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-purelib=%py_platsitedir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/patool
%{_mandir}/*
%{py_platsitedir}/*
