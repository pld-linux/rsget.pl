%include        /usr/lib/rpm/macros.perl
Summary:	Command line downloader for RapidShare-like services
Name:		rsget.pl
Version:	11666
Release:	2
License:	GPL v2+
Group:		Applications
Source0:	http://rsget.pl/download/%{name}-%{version}.tar.bz2
# Source0-md5:	de8e8bb429e52fcc08d1af0f9ebc5edc
URL:		http://rsget.pl/
BuildRequires:	rpm-perlprov
# those two aren't really needed
Requires:	perl-Proc-Daemon
Requires:	perl-Term-Size
Suggests:	perl(Image::Magick)
Suggests:	perl-Crypt-Blowfish
Suggests:	perl-Crypt-Rijndael
Suggests:	perl-GD
Suggests:	subversion
Suggests:	tesseract >= 2.00
Suggests:	tesseract-lang-en
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
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.config README.requirements
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
