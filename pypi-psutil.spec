#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-psutil
Version  : 5.9.0
Release  : 95
URL      : https://files.pythonhosted.org/packages/47/b6/ea8a7728f096a597f0032564e8013b705aa992a0990becd773dcc4d7b4a7/psutil-5.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/47/b6/ea8a7728f096a597f0032564e8013b705aa992a0990becd773dcc4d7b4a7/psutil-5.9.0.tar.gz
Summary  : Cross-platform lib for process and system monitoring in Python.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-psutil-license = %{version}-%{release}
Requires: pypi-psutil-python = %{version}-%{release}
Requires: pypi-psutil-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : procps-ng
BuildRequires : python3-dev

%description
This directory contains scripts which are meant to be used internally
(benchmarks, CI automation, etc.).

%package license
Summary: license components for the pypi-psutil package.
Group: Default

%description license
license components for the pypi-psutil package.


%package python
Summary: python components for the pypi-psutil package.
Group: Default
Requires: pypi-psutil-python3 = %{version}-%{release}

%description python
python components for the pypi-psutil package.


%package python3
Summary: python3 components for the pypi-psutil package.
Group: Default
Requires: python3-core
Provides: pypi(psutil)

%description python3
python3 components for the pypi-psutil package.


%prep
%setup -q -n psutil-5.9.0
cd %{_builddir}/psutil-5.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651168227
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-psutil
cp %{_builddir}/psutil-5.9.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-psutil/51ede753f5d20b28226ab01c133ad67797eaf716
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-psutil/51ede753f5d20b28226ab01c133ad67797eaf716

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
