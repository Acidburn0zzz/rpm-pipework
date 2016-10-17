Name: pipework
Version: 20160905
Release: 1%{?dist}
Summary: Software-Defined Networking for Linux Containers
License: Apache License, Version 2.0
URL: https://github.com/jpetazzo/pipework
Source0: https://github.com/jpetazzo/pipework/archive/master.zip

BuildArch: noarch
Requires: bash
Requires: docker-io
Requires: iproute

%description
Pipework lets you connect together containers in arbitrarily complex scenarios.
Pipework uses cgroups and namespace and works with "plain" LXC containers
(created with lxc-start), and with the awesome Docker.

%prep
%autosetup -n pipework-master

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 755 pipework %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %

%files
%defattr(-, root, root)
%{_bindir}/*

%changelog
* Mon Oct 17 2016 John Siegrist <john@complects.com> - 20160905-1
- Update package for inclusion in CloudRouter project.
* Fri Jan 23 2015 Oleg Gashev <oleg@gashev.net> - 20150123
- Initial package.
