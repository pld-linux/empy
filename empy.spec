Summary:	System for embedding Python expressions and statements in template text
Summary(pl.UTF-8):	System wbudowywania wyrażeń języka Python w pliki tekstowe
Name:		empy
Version:	3.3.3
Release:	1
License:	LGPL
Group:		Applications/Text
Source0:	http://www.alcyone.com/software/empy/%{name}-%{version}.tar.gz
# Source0-md5:	46ee2d3ca72af048c929c1fa9a3929f8
URL:		http://www.alcyone.com/software/empy/
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
System for embedding Python expressions and statements in template
text.

%description -l pl.UTF-8
System wbudowywania wyrażeń języka Python w pliki tekstowe.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_bindir}}

%py_install

cat > $RPM_BUILD_ROOT%{_bindir}/em.py <<"EOF"
#!/usr/bin/python
import em
em.invoke(sys.argv[1:])
EOF

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *.em doc
%attr(755,root,root) %{_bindir}/em.py
%{py_sitescriptdir}/em.py[co]
%{py_sitescriptdir}/empy-%{version}-py*.egg-info
