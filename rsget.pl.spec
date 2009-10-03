%include        /usr/lib/rpm/macros.perl
Summary:	Command line downloader for RapidShare-like services
Name:		rsget.pl
Version:	10666
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://ep09.pld-linux.org/~sparky/%{name}-%{version}.tar.bz2
# Source0-md5:	33243e5aec3e1d743124301ad840f8a8
URL:		http://svn.pld-linux.org/cgi-bin/viewsvn/toys/rsget.pl/
BuildRequires:	rpm-perlprov
Suggests:	ImageMagick-coder-png
Suggests:	gocr
Suggests:	netpbm-progs
Suggests:	ocrad
Suggests:	perl(Image::Magick)
Suggests:	perl-GD
Obsoletes:	rsget2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line downloader for RapidShare-like services.

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
