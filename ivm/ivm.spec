%global debug_package %{nil}

Name:    ivm
Version: 0.6.0
Release: 2%{?dist}
Summary: The cross-platform Inko version manager
License: MPL-2.0
URL:     https://github.com/inko-lang/ivm
Source:  https://github.com/inko-lang/ivm/archive/refs/tags/v%{version}.tar.gz

Recommends: llvm
Recommends: llvm-devel
Recommends: llvm-static
Recommends: libstdc++-devel libstdc++-static libffi-devel zlib-devel

Requires:      rust cargo
BuildRequires: rust cargo make

%description
ivm is a version manager for Inko, and makes it easy to install Inko on
different platforms.

%files -n %{name}
%{_bindir}/ivm
%{_datadir}/*

%prep
%autosetup -n %{name}-%{version_no_tilde} -p0

%build
make build

%install
make install DESTDIR=%{buildroot}

%changelog
%autochangelog
