Name:		python-pathable
Version:	0.5.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pathable/pathable-%{version}.tar.gz
Summary:	Object-oriented paths
URL:		https://pypi.org/project/pathable/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Object-oriented paths

%files
%{py_sitedir}/pathable
%{py_sitedir}/pathable-*.*-info
