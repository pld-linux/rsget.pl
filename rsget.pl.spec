%include        /usr/lib/rpm/macros.perl
Summary:	Command line downloader for RapidShare-like services
Name:		rsget.pl
Version:	10943
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://ep09.pld-linux.org/~sparky/%{name}-%{version}.tar.bz2
# Source0-md5:	d332d593068a285c3befd80f8b6fbb1d
URL:		http://svn.pld-linux.org/cgi-bin/viewsvn/toys/rsget.pl/
BuildRequires:	rpm-perlprov
# those two aren't really needed
Requires:	perl-Proc-Daemon
Requires:	perl-Term-Size
Suggests:	perl(Image::Magick)
Suggests:	perl-Crypt-Blowfish
Suggests:	perl-Crypt-Rijndael
Suggests:	perl-GD
Suggests:	subversion
Suggests:	tesseract
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautoprov	^perl(RSGet::.*)$
%define	_noautoreq	^perl(RSGet::.*)$

%description
Command line downloader for RapidShare-like services.

Suggested packages:
 - subversion - client allows automatic updates from svn repository
 - perl-GD and tesseract - highly recommended, required for automatic
   recognition of most captcha images
 - perl(Image::Magick) - better support for MegaUpload captcha (higher
   probability of success)
 - perl-Crypt-Blowfish - required for Link/SecuredIn
 - perl-Crypt-Rijndael - required for Link/CryptIt

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
%doc README README.config README.requirements
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
