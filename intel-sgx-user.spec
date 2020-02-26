Name:           intel-sgx-user
Summary:        Out of tree driver for Intel SGX
Version:        0.0.20200226
Release:        1%{?dist}
License:        Apache-2.0

URL:            https://github.com/intel/linux-sgx-driver
Source0: 	https://github.com/intel/linux-sgx-driver/archive/sgx_driver_2.6.tar.gz

%{?systemd_requires}
BuildRequires:  systemd
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libmnl)

Provides:       %{name}-kmod-common = %{version}
Requires:       %{name}-kmod >= %{version}

%description
This is an out-of-tree driver for Intel SGX.

%prep
%autosetup -n intel-sgx-user-%{version}
#%setup -q

# Remove .gitignore files in examples
find contrib/ -type f -name ".gitignore" -exec rm "{}" \;

%build
%set_build_flags
%make_build V=1 -C src/tools


%install
%make_install -C src/tools \
        WITH_BASHCOMPLETION=yes \
        WITH_SYSTEMDUNITS=yes


%files
%doc README.md
%license COPYING
%{_bindir}/intel-sgx-user
#%{_bindir}/*
%{_sysconfdir}/intel-sgx-user


%changelog
* Wed Feb 26 2020 Lily Sturmann <lsturman@redhat.com> - 0.0.20200226
- Initial package
