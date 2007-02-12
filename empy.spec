Summary:	System for embedding Python expressions and statements in template text
Summary(pl.UTF-8):	System wbudowywania wyrażeń języka Python w pliki tekstowe
Name:		empy
Version:	3.3
Release:	3
License:	LGPL
Group:		Applications/Text
Source0:	http://www.alcyone.com/software/empy/%{name}-%{version}.tar.gz
# Source0-md5:	e7b518a6fc4fd28fef87726cdb003118
URL:		http://www.alcyone.com/software/empy/
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
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
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_bindir}}

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

cat > $RPM_BUILD_ROOT%{_bindir}/em.py <<"EOF"
#!/usr/bin/python
import em
em.invoke(sys.argv[1:])
EOF

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *.em doc
%attr(755,root,root) %{_bindir}/em.py
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/empy-*.egg-info
