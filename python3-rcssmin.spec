%define		module		rcssmin
Summary:	RCSSmin is a CSS minifier
Name:		python3-%{module}
Version:	1.2.1
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/r/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	d8a49d97d36aed2dd98a0863e948f0c2
URL:		http://opensource.perlig.de/rcssmin/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The minifier is based on the semantics of the YUI compressor, which
itself is based on the rule list by Isaac Schlueter.

This module is a re-implementation aiming for speed instead of maximum
compression, so it can be used at runtime (rather than during a
preprocessing step).

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.md LICENSE bench/LICENSE.cssmin
%{py3_sitedir}/%{module}.py
%attr(755,root,root) %{py3_sitedir}/_%{module}.*.so
%{py3_sitedir}/__pycache__/%{module}.*
%{py3_sitedir}/%{module}-%{version}-py*.egg-info

%files apidocs
%defattr(644,root,root,755)
%doc docs/_userdoc/*
