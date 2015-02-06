%define oname wqy-zenhei

Summary:	WenQuanYi ZenHei TrueType font
Name:		fonts-ttf-%{oname}
Version:	0.9.45
Release:	4
Source:		http://downloads.sourceforge.net/wqy/%{oname}-%{version}.tar.gz
URL:		http://www.wenq.org
License:	GPLv2+
Group:		System/Fonts/True type
BuildArch:	noarch
BuildRequires: fontconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires(post):	mkfontdir, mkfontscale
Requires(postun):	mkfontdir, mkfontscale

%description
The WenQuanYi Zen Hei is the first open-source Chinese font
for Hei Ti, a sans-serif font style that are widely used for
general purpose Chinese text formatting, and on-screen
display of Chinese characters (such as in Windows Vista and Mac OS).
Simple and elegant font outlines and slightly emboldened strokes
makes the glyphs presenting higher contrast and therefore easy
to read. The unique style of this font also provide a simple
interface for adding grid-fitting information for further
fine-tuning of the on-screen performance.

%prep
%setup -q -n %{oname} 
 
%build

%install
rm -fr %{buildroot}

install -d %{buildroot}/%{_datadir}/fonts/TTF/%{oname}/
install -m 644 wqy-zenhei.ttc %{buildroot}/%{_datadir}/fonts/TTF/%{oname}/

install -d %{buildroot}/%{_sysconfdir}/fonts/conf.avail/
install -m 644 43-wqy-zenhei-sharp.conf %{buildroot}/%{_sysconfdir}/fonts/conf.avail/43-wqy-zenhei-sharp.conf

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/%{oname} \
    %{buildroot}%_sysconfdir/X11/fontpath.d/%{oname}:pri=50

%post
[ -x %{_bindir}/mkfontdir ] && %{_bindir}/mkfontdir %{_datadir}/fonts/TTF/%{oname}
[ -x %{_bindir}/mkfontscale ] && %{_bindir}/mkfontscale %{_datadir}/fonts/TTF/%{oname}

%postun
if [ "$1" = "0" ]; then
  [ -x %{_bindir}/mkfontdir ] && %{_bindir}/mkfontdir %{_datadir}/fonts/TTF/%{oname}
  [ -x %{_bindir}/mkfontscale ] && %{_bindir}/mkfontscale %{_datadir}/fonts/TTF/%{oname}
fi

%clean
rm -fr %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc ChangeLog AUTHORS COPYING README
%{_sysconfdir}/fonts/conf.avail/43-wqy-zenhei-sharp.conf
%dir %{_datadir}/fonts/TTF/%{oname}/
%{_datadir}/fonts/TTF/%{oname}/*.ttc
%{_sysconfdir}/X11/fontpath.d/%{oname}:pri=50


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 0.9.45-3mdv2011.0
+ Revision: 675581
- br fontconfig for fc-query used in new rpm-setup-build

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.45-2mdv2011.0
+ Revision: 610739
- rebuild

* Mon Apr 05 2010 Funda Wang <fwang@mandriva.org> 0.9.45-1mdv2010.1
+ Revision: 531678
- new version 0.9.45

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.8.38-3mdv2010.1
+ Revision: 494165
- fc-cache is now called by an rpm filetrigger

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.8.38-2mdv2010.0
+ Revision: 437572
- rebuild

* Sat Feb 28 2009 Funda Wang <fwang@mandriva.org> 0.8.38-1mdv2009.1
+ Revision: 346036
- new test version 0.8.38

* Thu Jun 26 2008 Funda Wang <fwang@mandriva.org> 0.6.26-1mdv2009.0
+ Revision: 229231
- New version 0.6.26

* Sat Apr 12 2008 Funda Wang <fwang@mandriva.org> 0.5.23-1mdv2009.0
+ Revision: 192598
- New version 0.5.23

* Mon Feb 18 2008 Funda Wang <fwang@mandriva.org> 0.4.23-1mdv2008.1
+ Revision: 171396
- New version 0.4.23

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 09 2007 Funda Wang <fwang@mandriva.org> 0.2.15-1mdv2008.1
+ Revision: 95896
- New version 0.2.15

* Mon Aug 13 2007 Funda Wang <fwang@mandriva.org> 0.2.10-1mdv2008.0
+ Revision: 62752
- Import fonts-ttf-wqy-zenhei
- Created package structure for fonts-ttf-wqy-zenhei.

