%include        /usr/lib/rpm/macros.perl
Summary:	Command line downloader for RapidShare-like services
Name:		rsget.pl
Version:	10871
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://ep09.pld-linux.org/~sparky/%{name}-%{version}.tar.bz2
# Source0-md5:	f590a57fa385c322553e2efbbddf2076
URL:		http://svn.pld-linux.org/cgi-bin/viewsvn/toys/rsget.pl/
BuildRequires:	rpm-perlprov
Requires:	perl-GD
Suggests:	ImageMagick-coder-png
Suggests:	perl(Image::Magick)
Suggests:	tesseract
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line downloader for RapidShare-like services.

Suggested packages:
 - tesseract - highly recommended, required for automatic recognition of
   most captcha images
 - perl(Image::Magick) and ImageMagick-coder-png - better support for
   MegaUpload captcha (higher probability of success)

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.config
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
