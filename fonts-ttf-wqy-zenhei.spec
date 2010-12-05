%define oname wqy-zenhei

Summary:	WenQuanYi ZenHei TrueType font
Name:		fonts-ttf-%{oname}
Version:	0.9.45
Release:	%mkrel 2
Source:		http://downloads.sourceforge.net/wqy/%{oname}-%{version}.tar.gz
URL:		http://www.wenq.org
License:	GPLv2+
Group:		System/Fonts/True type
BuildArch:	noarch
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
