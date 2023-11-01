Summary: A tool for generating SELinux security policies for containers
Name: udica
Version: 0.2.6
Release: 20%{?dist}
Source0: https://github.com/containers/udica/archive/v%{version}.tar.gz
Patch0: 0001-Make-sure-each-section-of-the-inspect-exists-before-.patch
License: GPLv3+
BuildArch: noarch
Url: https://github.com/containers/udica
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires: python3 python3-devel python3-setuptools
Requires: python3 python3-libsemanage python3-libselinux
%else
BuildRequires: python2 python2-devel python2-setuptools
Requires: python2 libsemanage-python libselinux-python
%endif
# container-selinux provides policy templates
Requires: container-selinux >= 2.168.0-2

%description
Tool for generating SELinux security profiles for containers based on
inspection of container JSON file.

%prep
%autosetup -p 1

%build
%if 0%{?fedora} || 0%{?rhel} > 7
%{__python3} setup.py build
%else
%{__python2} setup.py build
%endif

%install
%if 0%{?fedora} || 0%{?rhel} > 7
%{__python3} setup.py install --single-version-externally-managed --root=%{buildroot}
%else
%{__python2} setup.py install --single-version-externally-managed --root=%{buildroot}
%endif

install --directory %{buildroot}%{_mandir}/man8
install -m 0644 udica/man/man8/udica.8 %{buildroot}%{_mandir}/man8/udica.8

%files
%{_mandir}/man8/udica.8*
%{_bindir}/udica
%dir %{_datadir}/udica
%dir %{_datadir}/udica/ansible
%{_datadir}/udica/ansible/*

%if 0%{?fedora} || 0%{?rhel} > 7
%license LICENSE
%{python3_sitelib}/udica/
%{python3_sitelib}/udica-*.egg-info
%else
%{_datarootdir}/licenses/udica/LICENSE
%{python2_sitelib}/udica/
%{python2_sitelib}/udica-*.egg-info
%endif

%changelog
* Thu Jan 12 2023 Jindrich Novy <jnovy@redhat.com> - 0.2.6-20
- bump release to preserve update path
- Related: #2139052

* Fri Nov 18 2022 Jindrich Novy <jnovy@redhat.com> - 0.2.6-4
- Bump release to match latest release available in rhel-8.6.1
- Resolves: #2139052

* Wed Dec 01 2021 Vit Mojzis <vmojzis@redhat.com> - 0.2.6-3
- Make sure each section of the inspect exists before accessing (#2027662)

* Tue Sep 21 2021 Vit Mojzis <vmojzis@redhat.com> - 0.2.6-2
- Require container-selinux shipping policy templates (#2005866)

* Fri Sep 17 2021 Jindrich Novy <jnovy@redhat.com> - 0.2.6-1
- update to https://github.com/containers/udica/releases/tag/v0.2.6
- Related: #2001445

* Fri Aug 27 2021 Jindrich Novy <jnovy@redhat.com> - 0.2.5-2
- New rebase https://github.com/containers/udica/releases/tag/v0.2.5 (#1995041)
- Replace capability dictionary with str.lower()
- Enable udica to generate policies with fifo class
- Sort container inspect data before processing
- Update templates to work properly with new cil parser
- Related: #1934415

* Thu Aug 26 2021 Jindrich Novy <jnovy@redhat.com> - 0.2.5-1
- update to https://github.com/containers/udica/releases/tag/v0.2.5
- Related: #1934415

* Tue Jun 15 2021 Jindrich Novy <jnovy@redhat.com> - 0.2.4-2
- remove %%check again and all related BRs
- Related: #1934415

* Thu Nov 26 2020 Jindrich Novy <jnovy@redhat.com> - 0.2.4-1
- update to https://github.com/containers/udica/releases/tag/v0.2.4
- Related: #1883490

* Wed Oct 21 2020 Jindrich Novy <jnovy@redhat.com> - 0.2.3-1
- synchronize with stream-container-tools-rhel8
- Related: #1883490

* Mon Aug 10 2020 Jindrich Novy <jnovy@redhat.com> - 0.2.2-1
- https://github.com/containers/udica/releases/tag/v0.2.2
- Related: #1821193

* Tue Nov 26 2019 Jindrich Novy <jnovy@redhat.com> - 0.2.1-2
- initial import to container-tools 8.2.0
- Related: RHELPLAN-25139

* Fri Oct 25 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.2.1-1
- New rebase https://github.com/containers/udica/releases/tag/v0.2.0
Resolves: rhbz#1757693

* Wed Oct 02 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.2.0-1
- New rebase https://github.com/containers/udica/releases/tag/v0.2.0
Resolves: rhbz#1757693

* Thu Jul 11 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.1.8-1
- Udica supports podman version 1.4.0+
Resolves: rhbz#1729115

* Fri May 17 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.1.6-1
- Update testsuite from upstream release
Resolves: rhbz#1673643

* Wed May 15 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.1.5-2
- Bump release because of gating tests

* Fri Apr 19 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.1.5-1
- Create mock selinux and semanage module
- Update testing section in README
- Add travis file for Travis CI
- Grammar fixes in the udica.8 manpage file
- Support port ranges (Resolves: #16)
- Test port ranges

* Mon Mar 11 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.1.4-1
- Fix minor problems reported by pylint #11
- Catch FileNotFoundError when inspecting containers #12
- Create basic tests #13
- Restore working directory #14
- udica cannot use the container ID once it is provided #10

* Mon Feb 25 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.1.3-4
- Update manpage with the latest known bug described in https://github.com/containers/udica/issues/8
- Add check if runtimes are installed on the system

* Sun Feb 17 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.1.3-3
- Improve capability parsing for docker containers
- Update small changes in manpage, like issue with mandatory option '-c' for docker containers
- Fix parsing Mountpoints in docker inspect JSON file

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.1.3-1
- Fix capability allow rules when capabilities are specified in JSON file
- Add additional SELinux allow rules to base container template to allow container to read proc_type types.

* Fri Jan 04 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.1.2-1
- Fix invalid syntax output when policy is using just one template
Resolves: #6

* Tue Oct 23 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.1.1-2
- Fix small issues in spec file like improve description and change files section.

* Mon Oct 22 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.1.1-1
- Add proper shebang to all source files
- Add License to all source files

* Sat Oct 13 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.1.0-1
- Add support for docker containers

* Mon Oct 08 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.5-1
- Update x_container template based on testing container related to Nvidia Cuda operations

* Mon Oct 08 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.4-2
- Build udica on Red Hat Enterprise Linux 7 with python version 2

* Mon Oct 08 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.4-1
- Add manpages
- Add support for communicating with libvirt daemon
- Add support for communicating with X server.
- Add support for read/write to the controlling terminal

* Sun Oct 07 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.3-1
- Remove required parameters -i or -j and added support for reading json file from stdin.
- Remove "-n" or "--name" parameter. Name of the container will be required for this tool

* Tue Sep 25 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.2-1
- Use subprocess.Popen instead of subprocess.run for inspecting to support also python2

* Thu Sep 20 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.1-3
- Update readme and setup.py files after migration to github

* Sun Sep 16 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.1-2
- Update LICENSE
- Improve %%files section

* Sun Sep 16 2018 Lukas Vrabec <lvrabec@redhat.com> - 0.0.1-1
- Initial build
