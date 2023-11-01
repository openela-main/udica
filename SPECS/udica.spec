Summary: A tool for generating SELinux security policies for containers
Name: udica
Version: 0.2.6
Release: 30%{?dist}
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
* Fri Jan 27 2023 Vit Mojzis <vmojzis@redhat.com> - 0.2.6-30
- Bump release to preserve upgrade path (#2160401)

* Wed Dec 01 2021 Vit Mojzis <vmojzis@redhat.com> - 0.2.6-4
- Make sure each section of the inspect exists before accessing (#2027656)

* Tue Sep 21 2021 Vit Mojzis <vmojzis@redhat.com> - 0.2.6-3
- Require container-selinux shipping policy templates (#2000051)

* Fri Sep 17 2021 Jindrich Novy <jnovy@redhat.com> - 0.2.6-2
- use RHEL-9 product version for gating
- Related: #2000051

* Thu Sep 16 2021 Jindrich Novy <jnovy@redhat.com> - 0.2.6-1
- update to https://github.com/containers/udica/releases/tag/v0.2.6
- Related: #2000051

* Fri Sep 03 2021 Jindrich Novy <jnovy@redhat.com> - 0.2.5-2
- New rebase https://github.com/containers/udica/releases/tag/v0.2.5 (#1995041)
- Replace capability dictionary with str.lower()
- Enable udica to generate policies with fifo class
- Sort container inspect data before processing
- Update templates to work properly with new cil parser
- Related: #2000051

* Wed Aug 25 2021 Vit Mojzis <vmojzis@redhat.com> - 0.2.5-1
- New rebase https://github.com/containers/udica/releases/tag/v0.2.5 (#1995046)
- Replace capability dictionary with str.lower()
- Enable udica to generate policies with fifo class
- Sort container inspect data before processing
- Update templates to work properly with new cil parser

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.2.4-9
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon Jun 14 2021 Jindrich Novy <jnovy@redhat.com> - 0.2.4-8
- remove %%check again and all related BRs

* Mon Jun 14 2021 Jindrich Novy <jnovy@redhat.com> - 0.2.4-7
- remove black from BR

* Mon Jun 14 2021 Jindrich Novy <jnovy@redhat.com> - 0.2.4-6
- Add missing BR
- Related: #1970747

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.2.4-5
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Mar 16 2021 Vit Mojzis <vmojzis@redhat.com> - 0.2.4-4
- Remove %%check section

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Lukas Vrabec <lvrabec@redhat.com> - 0.2.4-2
- Add %%check section to run basic tests during rpm build process

* Wed Nov 25 2020 Lukas Vrabec <lvrabec@redhat.com> - 0.2.4-1
- New rebase https://github.com/containers/udica/releases/tag/v0.2.4

* Thu Aug 13 2020 Lukas Vrabec <lvrabec@redhat.com> - 0.2.3-1
- New rebase https://github.com/containers/udica/releases/tag/v0.2.3

* Mon Aug 03 2020 Lukas Vrabec <lvrabec@redhat.com> - 0.2.2-1
- New rebase https://github.com/containers/udica/releases/tag/v0.2.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-3
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 25 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.2.1-1
- New rebase https://github.com/containers/udica/releases/tag/v0.2.1

* Wed Sep 25 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.2.0-1
- New rebase https://github.com/containers/udica/releases/tag/v0.2.0

* Wed Aug 28 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.1.9-1
- Update tests test_basic.podman.cil, test_basic.docker.cil. Round 2
- New rebase https://github.com/containers/udica/releases/tag/v0.1.9

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.8-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.1.8-1
- New rebase https://github.com/containers/udica/releases/tag/v0.1.8

* Wed Jun 12 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.1.7-1
- New rebase with upstream adding new param --ansible, to generate ansible playbook for deploying policies. https://github.com/containers/udica/releases/tag/v0.1.7

* Thu May 16 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.1.6-1
- New rebase with upstream adding new tests

* Tue Apr 30 2019 Lukas Vrabec <lvrabec@redhat.com> - 0.1.5-2
- Add allow rules for container_runtime_t to base_container.cil, Podman version 1.2.0 requires new allow rules.
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
