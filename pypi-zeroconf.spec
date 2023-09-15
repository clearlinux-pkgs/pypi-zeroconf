#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-zeroconf
Version  : 0.112.0
Release  : 126
URL      : https://files.pythonhosted.org/packages/ce/1e/5762728c28e7017ad45e1f36b8abf3b2f0ff0521d1d578922742825b5915/zeroconf-0.112.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ce/1e/5762728c28e7017ad45e1f36b8abf3b2f0ff0521d1d578922742825b5915/zeroconf-0.112.0.tar.gz
Summary  : A pure python implementation of multicast DNS service discovery
Group    : Development/Tools
License  : LGPL-2.1
Requires: pypi-zeroconf-license = %{version}-%{release}
Requires: pypi-zeroconf-python = %{version}-%{release}
Requires: pypi-zeroconf-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cython)
BuildRequires : pypi(poetry_core)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
python-zeroconf
===============
.. image:: https://github.com/python-zeroconf/python-zeroconf/workflows/CI/badge.svg
:target: https://github.com/python-zeroconf/python-zeroconf?query=workflow%3ACI+branch%3Amaster

%package license
Summary: license components for the pypi-zeroconf package.
Group: Default

%description license
license components for the pypi-zeroconf package.


%package python
Summary: python components for the pypi-zeroconf package.
Group: Default
Requires: pypi-zeroconf-python3 = %{version}-%{release}

%description python
python components for the pypi-zeroconf package.


%package python3
Summary: python3 components for the pypi-zeroconf package.
Group: Default
Requires: python3-core
Provides: pypi(zeroconf)
Requires: pypi(ifaddr)

%description python3
python3 components for the pypi-zeroconf package.


%prep
%setup -q -n zeroconf-0.112.0
cd %{_builddir}/zeroconf-0.112.0
pushd ..
cp -a zeroconf-0.112.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694801492
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-zeroconf
cp %{_builddir}/zeroconf-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-zeroconf/e72e6c1c466bc418258327c0249e9a38d8f34367 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-zeroconf/e72e6c1c466bc418258327c0249e9a38d8f34367

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
