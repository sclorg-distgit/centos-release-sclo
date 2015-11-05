Name:       centos-release-scl-rh
Version:    1
Release:    2%{?dist}
Summary:    Software collections from the CentOS SCLo SIG (upstream scl only)

License:    GPLv2
URL:        http://wiki.centos.org/SpecialInterestGroup/SCLo
Source0:    CentOS-SCLo.repo
Source1:    CentOS-SCLo-Sources.repo
Source2:    CentOS-SCLo-Debuginfo.repo
Source3:    RPM-GPG-KEY-CentOS-SIG-SCLo
Source4:    GPL

BuildArch: noarch

Requires:   system-release

%description
yum Configs and basic docs for Software Collections as delivered via the CentOS SCLo SIG.
(upstream software collections only)

%prep

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-SCLo-scl-rh.repo
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-SCLo-scl-rh-Sources.repo
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-SCLo-scl-rh-Debuginfo.repo

sed -i -e "s/SCLGROUP/rh/g" %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-SCLo-scl-*.repo

# this should not be needed ..
%if !0%{?rhel:1}
%define rhel 7
%endif

# sclo AND rh will share same debuginfo repo .. oh well no problem here ...
sed -i -e "s/CENTOSMAJOR/%{rhel}/g" %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-SCLo-scl-rh-Debuginfo.repo

install -p -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

# use a docdir
mkdir -p -m 755 %{buildroot}/%{_docdir}/centos-release-scl-rh
install -m 644 %{SOURCE2} %{buildroot}/%{_docdir}/centos-release-scl-rh

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg
%{_docdir}/centos-release-scl-rh/*

%changelog
* Thu Nov 05 2015 Jaroslaw Polok <Jaroslaw.Polok@cern.ch> - 1.2
- added Sources and Debuginfo repositories

* Fri Oct 02 2015 Thomas Oulevey <thomas.oulevey@cern.ch>
- Initial version.
