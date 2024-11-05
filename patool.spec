Summary:	Portable command line archive file manager
Name:		patool
Version:	3.0.3
Release:	1
Url:		https://wummel.github.io/patool
Source0:	https://pypi.python.org/packages/source/p/patool/%{name}-%{version}.tar.gz
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
%{python_sitelib}/patoolib
%{python_sitelib}/patool-%{version}-py%{py_ver}.egg-info
