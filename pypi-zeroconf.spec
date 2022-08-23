#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-zeroconf
Version  : 0.39.0
Release  : 86
URL      : https://files.pythonhosted.org/packages/2b/a5/0ad52f3dd265fd2538b882eb6682eaeee12d2ba4dd55a20ac65374bbf67d/zeroconf-0.39.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/2b/a5/0ad52f3dd265fd2538b882eb6682eaeee12d2ba4dd55a20ac65374bbf67d/zeroconf-0.39.0.tar.gz
Summary  : Pure Python Multicast DNS Service Discovery Library (Bonjour/Avahi compatible)
Group    : Development/Tools
License  : LGPL-2.1
Requires: pypi-zeroconf-license = %{version}-%{release}
Requires: pypi-zeroconf-python = %{version}-%{release}
Requires: pypi-zeroconf-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(async_timeout)
BuildRequires : pypi(ifaddr)

%description
python-zeroconf
===============
.. image:: https://github.com/jstasiak/python-zeroconf/workflows/CI/badge.svg
:target: https://github.com/jstasiak/python-zeroconf?query=workflow%3ACI+branch%3Amaster

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
Requires: pypi(async_timeout)
Requires: pypi(ifaddr)

%description python3
python3 components for the pypi-zeroconf package.


%prep
%setup -q -n zeroconf-0.39.0
cd %{_builddir}/zeroconf-0.39.0
pushd ..
cp -a zeroconf-0.39.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1659972537
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-zeroconf
cp %{_builddir}/zeroconf-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-zeroconf/ab7752f30a9ae392de622ae6220b1034bbb4767a
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
/usr/share/package-licenses/pypi-zeroconf/ab7752f30a9ae392de622ae6220b1034bbb4767a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
