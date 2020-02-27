Name:           hello
Summary:        test
Version:        0.0.20200227
Release:        1%{?dist}
License:        Apache-2.0

Source0: 	https://github.com/lkatalin/copr-test/blob/master/hello.tar

%description
This contains the Intel SGX SDK's debugger.

%prep
%autosetup -n %{name}-master

# Remove .gitignore files in examples
find contrib/ -type f -name ".gitignore" -exec rm "{}" \;

%build
%set_build_flags
%make_build V=1 -C src/tools


%install
%make_install -C src/tools


%files
%doc README.md
%license COPYING
%{_bindir}/intel-sgx-debugger

%changelog
* Thu Feb 27 2020 Lily Sturmann <lsturman@redhat.com> - 0.0.20200227
- Initial package
