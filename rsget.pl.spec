Summary:	Command line downloader for RapidShare-like services
Name:		rsget.pl
Version:	12641
Release:	1
License:	GPL v2+
Group:		Applications
# svn co http://svn.pld-linux.org/svn/toys/rsget.pl
# tar -caf rsget.pl-r12641.tar.bz2 rsget.pl --exclude-vcs
#Source0:	http://rsget.pl/download/%{name}-svn-%{version}.tar.bz2
Source0:	%{name}-r%{version}.tar.bz2
# Source0-md5:	b37923318a38b492e93156428a96e82d
URL:		http://rsget.pl/
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	perl-JE
# those two aren't really needed
Requires:	perl-Proc-Daemon
Requires:	perl-Term-Size
Suggests:	perl-Crypt-Blowfish
Suggests:	perl-Crypt-Rijndael
Suggests:	perl-GD
Suggests:	perl-ImageMagick
Suggests:	subversion
Suggests:	tesseract >= 2.00
Suggests:	tesseract-lang-en
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautoreq_perl	RSGet::.*

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
%setup -q -n %{name}

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
