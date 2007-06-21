
%define plugin	mlcd
%define name	vdr-plugin-%plugin
%define version	0.0.4a
%define rel	9

Summary:	VDR plugin: Multitainer LCD-Display Driver
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://home.arcor.de/meinrad/
Source:		http://home.arcor.de/meinrad/vdr-%plugin-%version.tar.bz2
Patch1:		02_mlcd-0.0.4a-fontfile.dpatch
Patch2:		http://deela.cc.fh-lippe.de/files/vdr-mlcd/mlcd-0.0.4a.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
Enables the build in display of Fujitsu-Siemens Multitainer device.

%prep
%setup -q -n %plugin-%version
%patch1 -p1 -b .fontfile
%patch2 -p4 -b .1338

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}/%plugin
install -m644 char.dat %{buildroot}%{_vdr_plugin_cfgdir}/%plugin

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%config(noreplace) %{_vdr_plugin_cfgdir}/%plugin


