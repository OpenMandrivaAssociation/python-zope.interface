%define	oname	zope.interface

Name:		python-%{oname}
Version:	4.0.5
Release:	1
Summary:	Interfaces for Python
Source0:	http://pypi.python.org/packages/source/z/%{oname}/%{oname}-%{version}.zip
License:	ZPL 2.1
Group:		Development/Ruby
Url:		http://pypi.python.org/pypi/zope.interface
BuildRequires:	python-devel python-setuptools

%description
``zope.interface`` README
=========================

This package is intended to be independently reusable in any Python
project. It is maintained by the `Zope Toolkit project
<http://docs.zope.org/zopetoolkit/>`_.

This package provides an implementation of "object interfaces" for Python.
Interfaces are a mechanism for labeling objects as conforming to a given
API or contract. So, this package can be considered as implementation of
the `Design By Contract`_ methodology support in Python.

.. _Design By Contract: http://en.wikipedia.org/wiki/Design_by_contract

For detailed documentation, please see http://docs.zope.org/zope.interface
%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%check
python setup.py test

%files
%doc CHANGES.rst
%doc COPYRIGHT.txt
%doc LICENSE.txt
%doc README.rst
%doc docs/README.rst
%doc docs/README.ru.rst
%doc docs/hacking.rst
%doc src/zope.interface.egg-info/SOURCES.txt
%doc src/zope.interface.egg-info/dependency_links.txt
%doc src/zope.interface.egg-info/namespace_packages.txt
%doc src/zope.interface.egg-info/requires.txt
%doc src/zope.interface.egg-info/top_level.txt
%{py_platsitedir}/zope/*.py*
%{py_platsitedir}/zope/interface/*.py*
%{py_platsitedir}/zope/interface/_zope_interface_coptimizations.so
%{py_platsitedir}/zope/interface/tests/*.py*
%{py_platsitedir}/zope.interface*.egg-info

