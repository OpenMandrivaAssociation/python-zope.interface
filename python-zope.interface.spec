%define	oname	zope.interface
%define		py2info py2.7.egg-info
%define		py3info py3.4.egg-info

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
BuildRequires:	gcc-c++, gcc, gcc-cpp



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

For detailed documentation, please see http://docs.zope.org/zope.interface.



%package -n python2-%{oname}

Summary:        Python2 %{oname}
Group:          Development/Python
Provides:	pythonegg2(zope.interface)
BuildRequires:	pythonegg(setuptools)
BuildRequires:	python2-devel
Requires:	python2

%description -n python2-%{oname}
python2 %{oname} module.

%files -n python2-%{oname}
%doc python2/*.txt python2/*.rst
%{py2_platsitedir}/zope/interface/
%{py2_platsitedir}/%{oname}-%{version}-py2.7-nspkg.pth
%{py2_platsitedir}/%{oname}-%{version}-%{py2info}/PKG-INFO
%{py2_platsitedir}/%{oname}-%{version}-%{py2info}/*.txt
%{py2_platsitedir}/%{oname}-%{version}-%{py2info}/not-zip-safe


#----------------------------------------

%prep
%setup -qc -n %{oname}-%{version}
mv %{oname}-%{version} python3
cp -r python3 python2

%build
pushd python3
#gcc-ed this too. Sflo
export CC=gcc
export CXX=g++
%__python setup.py build
popd

#------------------
pushd python2
#gcc-ed this too. Sflo
export CC=gcc
export CXX=g++
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
%doc python3/*.rst python3/*.txt 
%{py_platsitedir}/zope/interface/
%{py_platsitedir}/%{oname}-%{version}-py3.4-nspkg.pth
%{py_platsitedir}/%{oname}-%{version}-%{py3info}/PKG-INFO
%{py_platsitedir}/%{oname}-%{version}-%{py3info}/*.txt
%{py_platsitedir}/%{oname}-%{version}-%{py3info}/not-zip-safe
