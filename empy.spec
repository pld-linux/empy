
%include	/usr/lib/rpm/macros.python

Summary:	System for embedding Python expressions and statements in template text
Summary(pl):	System wbudowywania wyra�e� j�zyka Python w pliki tekstowe
Name:		empy
Version:	3.0.3
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.alcyone.com/pyos/empy/%{name}-%{version}.tar.gz
# Source0-md5:	8c9c4721b76713301a28aabfe7a4cbc2
URL:		http://www.alcyone.com/pyos/empy/
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
System for embedding Python expressions and statements in template
text.

%description -l pl
System wbudowywania wyra�e� j�zyka Python w pliki tekstowe.

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

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *.em doc
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*.py[co]
