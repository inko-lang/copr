%global debug_package %{nil}

Name:    ivm
Version: 0.4.1
Release: 1
Summary: The cross-platform Inko version manager
License: MPL-2.0
URL:     https://github.com/inko-lang/ivm
Source:  https://github.com/inko-lang/ivm/archive/refs/tags/v%{version}.tar.gz

%if 0%{?fedora} >= 38
Requires: llvm15 llvm15-devel llvm15-static
%else
Requires: llvm llvm-devel llvm-static
%endif

Requires: rust >= 1.68.0
Requires: cargo >= 1.68.0
Requires: libstdc++-devel libstdc++-static libffi-devel zlib-devel

BuildRequires: rust >= 1.68.0
BuildRequires: cargo >= 1.68.0
BuildRequires: make

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
