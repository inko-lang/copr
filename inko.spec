%global debug_package %{nil}

Name:    inko
Version: 0.14.0
Release: 3
Summary: A language for building concurrent software with confidence
License: MPL-2.0
URL:     https://github.com/inko-lang/inko
Source:  https://github.com/inko-lang/inko/archive/refs/tags/v%{version}.tar.gz

%if 0%{?fedora} >= 38
BuildRequires: llvm15 llvm15-devel llvm15-static
%else
BuildRequires: llvm llvm-devel llvm-static
%endif

BuildRequires: rust >= 1.68.0
BuildRequires: cargo >= 1.68.0
BuildRequires: gcc make
BuildRequires: libstdc++-devel libstdc++-static libffi-devel zlib-devel git
Requires:      libgcc gcc git

%description
Inko is a language for building concurrent software with confidence. Inko makes
it easy to build concurrent software, without having to worry about
unpredictable performance, unexpected runtime errors, or race conditions.

%files -n %{name}
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/inko
%{_libdir}/%{name}/

%prep
%autosetup -n %{name}-%{version_no_tilde} -p0

%build
INKO_STD=%{_libdir}/%{name}/std INKO_RT=%{_libdir}/%{name}/runtime cargo build --release

%install
mkdir -p %{buildroot}/%{_libdir}/%{name}/std
cp -r %{_builddir}/%{name}-%{version}/std/src/* %{buildroot}/%{_libdir}/%{name}/std

mkdir -p %{buildroot}/%{_libdir}/%{name}/runtime
install -m644 %{_builddir}/%{name}-%{version}/target/release/lib%{name}.a %{buildroot}/%{_libdir}/%{name}/runtime/lib%{name}.a

mkdir -p %{buildroot}/%{_bindir}
install -m755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}/%{_bindir}/%{name}

%changelog
%autochangelog
