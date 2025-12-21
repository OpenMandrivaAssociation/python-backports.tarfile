%global _python_use_pep517 0

Name:		python-backports.tarfile
Version:	1.2.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/b/backports.tarfile/backports_tarfile-%{version}.tar.gz
Summary:	Backport of CPython tarfile module
URL:		https://pypi.org/project/backports.tarfile/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(setuptools-scm)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(wheel)
BuildArch:	noarch

%description
Backport of CPython tarfile module

%prep
%autosetup -n backports_tarfile-%{version} -p1

%build
%py_build

%install
%py_install
rm -rf %{buildroot}%{py_sitedir}/backports/__pycache__

%files
%{py_sitedir}/backports/*.py
%{py_sitedir}/backports/tarfile
%{py_sitedir}/backports_tarfile-*.*-info
