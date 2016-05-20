Name:       centos-release-scl
Version:    7
Release:    3%{?dist}
Epoch:      10
Summary:    Software collections from the CentOS SCLo SIG 

License:    GPLv2
URL:        http://wiki.centos.org/SpecialInterestGroup/SCLo
Source0:    CentOS-SCLo.repo
Source1:    RPM-GPG-KEY-CentOS-SIG-SCLo
Source2:    GPL

BuildArch: noarch

Requires:   system-release
Requires:   centos-release-scl-rh

%description
yum Configs and basic docs for Software Collections as delivered via the CentOS SCLo SIG.

%prep

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-SCLo-scl.repo
sed -i -e "s/SCLGROUP/sclo/g; s/\$releasever/%{rhel}/g;" %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-SCLo-scl.repo
install -p -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

# use a docdir
mkdir -p -m 755 %{buildroot}/%{_docdir}/centos-release-scl
install -m 644 %{SOURCE2} %{buildroot}/%{_docdir}/centos-release-scl

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg
%{_docdir}/centos-release-scl/*

%changelog
* Fri May 20 2016 Dominic Cleal <dominic@cleal.org> - 2-3
- replace releasever with hardcoded versions

* Tue Apr 06 2016 Thomas Oulevey <thomas.oulevey@cern.ch> - 7-2
- bump release and fix Epoch

* Tue Mar 29 2016 Thomas Oulevey <thomas.oulevey@cern.ch> - 7-1
- bump release

* Thu Mar 24 2016 Thomas Oulevey <thomas.oulevey@cern.ch> - 2-1
- disabled gpg check for -testing repos
- enabled sources repositories
- enabled debuginfo repositories

* Fri Oct 02 2015 Thomas Oulevey <thomas.oulevey@cern.ch>
- Initial version.
