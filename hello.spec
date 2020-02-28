Name:           hello
Summary:        test
Version:        0.0.20200227
Release:        1%{?dist}
License:        Apache-2.0

Source0: 	https://github.com/lkatalin/copr-test/blob/master/hello.tar

Requires: gcc

%description
This contains the Intel SGX SDK's debugger.

%prep
%autosetup -n hello

%install
%make_install -C


%files
hello

%changelog
* Thu Feb 27 2020 Lily Sturmann <lsturman@redhat.com> - 0.0.20200227
- Initial package
