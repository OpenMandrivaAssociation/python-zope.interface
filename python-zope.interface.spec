%define	oname	zope.interface
%define		py2info py2.7.egg-info
%define		py3info py%{py_ver}.egg-info

Name:		python-%{oname}
Version:	5.1.0
Release:	2
Summary:	Interfaces for Python
Source0:	https://files.pythonhosted.org/packages/af/d2/9675302d7ced7ec721481f4bbecd28a390a8db4ff753d28c64057b975396/zope.interface-5.1.0.tar.gz
Source100:	%{name}.rpmlintrc
License:	ZPL 2.1
Group:		Development/Ruby
Url:		http://pypi.python.org/pypi/zope.interface
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools


%description
This package is intended to be independently reusable in any Python
project. It is maintained by the `Zope Toolkit project
<http://docs.zope.org/zopetoolkit/>`_.
This package provides an implementation of "object interfaces" for Python.
Interfaces are a mechanism for labeling objects as conforming to a given
API or contract. So, this package can be considered as implementation of
the `Design By Contract`_ methodology support in Python.
For detailed documentation, please see http://docs.zope.org/zope.interface.


%prep
%autosetup -p1 -n %{oname}-%{version} 
#mv %{oname}-%{version} python3
#cp -r python3 python2

%build
%__python setup.py build


%install
%__python setup.py install --root=%{buildroot}


%files
%doc *.rst *.txt 
%{py_platsitedir}/zope/interface/
%{py_platsitedir}/%{oname}-%{version}-py*-nspkg.pth
%{py_platsitedir}/%{oname}-%{version}-%{py3info}/PKG-INFO
%{py_platsitedir}/%{oname}-%{version}-%{py3info}/*.txt
%{py_platsitedir}/%{oname}-%{version}-%{py3info}/not-zip-safe
