
%define plugin	mlcd
%define name	vdr-plugin-%plugin
%define version	0.0.4a
%define rel	17

Summary:	VDR plugin: Multitainer LCD-Display Driver
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://home.arcor.de/meinrad/
Source:		http://home.arcor.de/meinrad/vdr-%plugin-%version.tar.bz2
Patch1:		02_mlcd-0.0.4a-fontfile.dpatch
Patch2:		90_mlcd-0.0.4a-1.3.38.dpatch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Enables the build in display of Fujitsu-Siemens Multitainer device.

%prep
%setup -q -n %plugin-%version
%patch1 -p1 -b .fontfile
%patch2 -p1 -b .1338
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

install -d -m755 %{buildroot}%{vdr_plugin_cfgdir}/%plugin
install -m644 char.dat %{buildroot}%{vdr_plugin_cfgdir}/%plugin

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%config(noreplace) %{vdr_plugin_cfgdir}/%plugin




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.4a-16mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.4a-15mdv2009.1
+ Revision: 359336
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.4a-14mdv2009.0
+ Revision: 197948
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.4a-13mdv2009.0
+ Revision: 197690
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- replace 1.3.38 API patch with e-tobi one (P2)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.4a-12mdv2008.1
+ Revision: 145124
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4a-11mdv2008.1
+ Revision: 103151
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4a-10mdv2008.0
+ Revision: 50016
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4a-9mdv2008.0
+ Revision: 42102
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4a-8mdv2008.0
+ Revision: 22751
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4a-7mdv2007.0
+ Revision: 90940
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4a-6mdv2007.1
+ Revision: 74046
- rebuild for new vdr
- Import vdr-plugin-mlcd

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4a-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4a-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4a-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4a-2mdv2007.0
- rebuild for new vdr

* Sat Jul 15 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4a-1mdv2007.0
- initial Mandriva release

