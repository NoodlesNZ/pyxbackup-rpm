%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%global commit		e3bc8d036ce9393745472cb27f49b095e19e3454
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global builddate	20151022

Summary:  A program for backing up MySQL
Name: pyxbackup
Version: 0.1.0
Release: 1%{?dist}

License: GNU
Group: default
URL: https://github.com/dotmanila/pyxbackup
Source0: https://github.com/dotmanila/pyxbackup/archive/%{commit}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: python-devel

Requires: MySQL-python
Requires: python
Requires: percona-xtrabackup
Requires(preun): /sbin/service, /sbin/chkconfig
Requires(postun): /sbin/service, /sbin/chkconfig


%description
TBC

%prep
%setup -q -n %{name}-%{commit}

%build

%install
rm -rf %{buildroot}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}

install -p -m 755 pyxbackup $RPM_BUILD_ROOT%{_bindir}/pyxbackup

cat > $RPM_BUILD_ROOT%{_sysconfdir}/pyxbackup.cnf <<EOF
[pyxbackup]
stor_dir = /var/backups/database/stor
work_dir = /var/backups/database/work
EOF

%clean
rm -rf %{buildroot}

%post

%preun

%files
%defattr(-,root,root,-)
%{_bindir}/pyxbackup

%config(noreplace) %{_sysconfdir}/pyxbackup.cnf

%changelog
* Thu Oct 22 2015 Nick Le Mouton <nick@noodles.net.nz> - 1.0.0
- Init package

