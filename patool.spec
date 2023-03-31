Summary:	Portable command line archive file manager
Name:		patool
Version:	1.12
Release:	3
Url:		http://patool.sourceforge.net/
Source0:	https://pypi.python.org/packages/source/p/python-patool/%{name}-%{version}.tar.gz
License:	GPLv3+
Group:		Archiving/Other
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	python3dist(setuptools)

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
%setup -n %{name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install \
	-O1 \
	--skip-build \
	--root %{buildroot}


%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%{python_sitelib}/patoolib
%{python_sitelib}/patool-%{version}-py%{py_ver}.egg-info
%{python_sitelib}/_patool_configdata.py


%changelog
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.13-1mdv2011.0
+ Revision: 645373
- update to new version 0.13

* Sat Nov 06 2010 Jani Välimaa <wally@mandriva.org> 0.11-1mdv2011.0
+ Revision: 594246
- new version 0.11
- install files to a correct location
- fix license and clean spec

* Fri Aug 13 2010 Shlomi Fish <shlomif@mandriva.org> 0.10-2mdv2011.0
+ Revision: 569471
- Add missing BuildRequires (thanks to Anssi)
- Change to a more apprporiate group
- Correct some rpm errors - no Vendor
- Changed to the Mandriva release
- import patool


