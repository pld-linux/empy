
%include	/usr/lib/rpm/macros.python

Summary:	System for embedding Python expressions and statements in template text
Summary(pl):	System wbudowywania wyra¿eñ jêzyka Python w pliki tekstowe
Name:		empy
Version:	2.1
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.alcyone.com/pyos/empy/%{name}-%{version}.tar.gz
URL:		http://www.alcyone.com/pyos/empy/
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
System for embedding Python expressions and statements in template
text.

%description -l pl
System wbudowywania wyra¿eñ jêzyka Python w pliki tekstowe.

%prep
%setup -q

%build
sed 's;^#!/usr/local/bin/python;#!/usr/bin/python;' < em.py > em.py.1
mv em.py.1 em.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install em.py $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *.em
%attr(755,root,root) %{_bindir}/*
