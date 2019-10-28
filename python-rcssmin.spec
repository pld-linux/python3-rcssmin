#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		rcssmin
%define		pypi_name	rcssmin
Summary:	RCSSmin is a CSS minifier
Name:		python-%{pypi_name}
Version:	1.0.6
Release:	4
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	467d56503ce386c0b0e52f69ac143a9a
URL:		http://opensource.perlig.de/rcssmin/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The minifier is based on the semantics of the YUI compressor, which
itself is based on the rule list by Isaac Schlueter.

This module is a re-implementation aiming for speed instead of maximum
compression, so it can be used at runtime (rather than during a
preprocessing step).

%package -n python3-%{pypi_name}
Summary:	RCSSmin is a CSS minifier
Group:		Libraries/Python

%description -n python3-%{pypi_name}
RCSSmin is a CSS minifier.

The minifier is based on the semantics of the YUI compressor, which
itself is based on the rule list by Isaac Schlueter.

This module is a re-implementation aiming for speed instead of maximum
compression, so it can be used at runtime (rather than during a
preprocessing step).

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n %{pypi_name}-%{version}

# strip bang path from rcssmin.py
sed -i '1d' rcssmin.py

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

# remove upstream developer documentation
rm -r $RPM_BUILD_ROOT%{_docdir}/%{module}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst LICENSE bench/LICENSE.cssmin
%attr(755,root,root) %{py_sitedir}/_%{module}.so
%{py_sitedir}/%{module}.py[oc]
%{py_sitedir}/%{pypi_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc README.rst LICENSE bench/LICENSE.cssmin
%{py3_sitedir}/%{module}.py
%attr(755,root,root) %{py3_sitedir}/_%{module}.*.so
%{py3_sitedir}/__pycache__/%{module}.*
%{py3_sitedir}/%{pypi_name}-%{version}-py*.egg-info
%endif

%files apidocs
%defattr(644,root,root,755)
%doc docs/apidoc/*
