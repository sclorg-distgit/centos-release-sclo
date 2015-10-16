Name:       centos-release-scl-rh
Version:    1
Release:    1%{?dist}
Summary:    Software collections from the CentOS SCLo SIG (upstream scl only)

License:    GPLv2
URL:        http://wiki.centos.org/SpecialInterestGroup/SCLo
Source0:    CentOS-SCLo.repo
Source1:    RPM-GPG-KEY-CentOS-SIG-SCLo
Source2:    GPL

BuildArch: noarch

Requires:   centos-release

%description
yum Configs and basic docs for Software Collections as delivered via the CentOS SCLo SIG.

%prep

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-SCLo-scl-rh.repo
sed -i -e "s/SCLGROUP/rh/g" %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-SCLo-scl-rh.repo
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
* Fri Oct 02 2015 Thomas Oulevey <thomas.oulevey@cern.ch>
- Initial version.
