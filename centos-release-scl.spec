
Name:       centos-release-scl
Version:    1
Release:    2%{?dist}
Summary:    Software collections from the CentOS SCLo SIG 

License:    GPLv2
URL:        http://wiki.centos.org/SpecialInterestGroup/SCLo
Source0:    CentOS-SCLo.repo
Source1:    CentOS-SCLo-Sources.repo
Source2:    CentOS-SCLo-Debuginfo.repo
Source3:    RPM-GPG-KEY-CentOS-SIG-SCLo
Source4:    GPL

BuildArch: noarch

Requires:   system-release
Requires:   centos-release-scl-rh

%description
yum Configs and basic docs for Software Collections as delivered via the CentOS SCLo SIG.

%prep

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-SCLo-scl.repo
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-SCLo-scl-Sources.repo
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-SCLo-scl-Debuginfo.repo

sed -i -e "s/SCLGROUP/sclo/g" %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-SCLo-*.repo

# this should not be needed ..
%if !0%{?rhel:1}
%define rhel 7
%endif

# sclo AND rh will share same debuginfo repo .. oh well no problem here ...
sed -i -e "s/CENTOSMAJOR/%{rhel}/g" %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-SCLo-scl-Debuginfo.repo

install -p -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

# use a docdir
mkdir -p -m 755 %{buildroot}/%{_docdir}/centos-release-scl
install -m 644 %{SOURCE4} %{buildroot}/%{_docdir}/centos-release-scl

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg
%{_docdir}/centos-release-scl/*

%changelog
* Thu Nov 05 2015 Jaroslaw Polok <Jaroslaw.Polok@cern.ch> - 1.2
- added Sources and Debuginfo repositories

* Fri Oct 02 2015 Thomas Oulevey <thomas.oulevey@cern.ch>
- Initial version.
