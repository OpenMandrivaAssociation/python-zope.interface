%define	oname	zope.interface


Name:		python-%{oname}
Version:	4.1.1
Release:	1
Summary:	Interfaces for Python
Source0:	http://pypi.python.org/packages/source/z/%{oname}/%{oname}-%{version}.tar.gz
License:	ZPL 2.1
Group:		Development/Ruby
Url:		http://pypi.python.org/pypi/zope.interface
BuildRequires:	pkgconfig(python)
BuildRequires:	python3egg(setuptools)




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



%package -n python2-%{oname}

Summary:        Python2 %{oname}
Group:          Development/Python
Provides:	pythonegg2(zope.interface)
BuildRequires:	pythonegg(setuptools)
BuildRequires:	python2-devel
Requires:	python2

%description -n python2-%{oname}


%files -n python2-%{oname}
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
%{py2_platsitedir}/zope/*.py*
%{py2_platsitedir}/zope/interface/*.py*
%{py2_platsitedir}/zope/interface/_zope_interface_coptimizations.so
%{py2_platsitedir}/zope/interface/tests/*.py*
%{py2_platsitedir}/zope.interface*.egg-info
#----------------------------------------

%prep
%setup -qc -n %{oname}-%{version}
mv %{oname}-%{version} python3
cp -r python3 python2

%build
pushd python3
%__python setup.py build
popd

#------------------
pushd python2
%__python2 setup.py build
popd

%install
pushd python2
%__python2 setup.py install --root=%{buildroot}
popd

#------------------
pushd python3
%__python setup.py install --root=%{buildroot}
popd


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

