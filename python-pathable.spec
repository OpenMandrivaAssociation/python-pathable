%define module pathable

Name:		python-pathable
Version:	0.6.0
Release:	2
Summary:	Object-oriented paths
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/pathable/
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
Object-oriented paths

%files
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
