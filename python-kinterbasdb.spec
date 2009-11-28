%define		realname kinterbasdb
Summary:	Python DB API 2.0 extension for Firebird and Interbase
Name:		python-kinterbasdb
Version:	3.3.0
Release:	1
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/firebird/%{realname}-%{version}.tar.bz2
# Source0-md5:	0296d2dbc7b76dac140b5fec2ad59f0e
URL:		http://www.firebirdsql.org/index.php?op=devel&sub=python
BuildRequires:	Firebird-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KInterbasDB implements Python Database API 2.0-compliant support for
the open source relational database Firebird and some versions of its
proprietary cousin Borland Interbase. In addition to the minimal
feature set of the standard Python DB API, KInterbasDB also exposes
nearly the entire native client API of the database engine.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

rm -r $RPM_BUILD_ROOT%{py_sitedir}/kinterbasdb/docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/_sources docs/_static docs/*.{html,js}
%{py_sitedir}/%{realname}-%{version}-py*.egg-info
%dir %{py_sitedir}/kinterbasdb
%{py_sitedir}/kinterbasdb/*.py[co]
%attr(755,root,root) %{py_sitedir}/kinterbasdb/_kinterbasdb.so
%attr(755,root,root) %{py_sitedir}/kinterbasdb/_kiservices.so
