#
%include        /usr/lib/rpm/macros.perl
Summary:	Command line downloader for RapidShare-like services
Name:		rsget.pl
Version:	10331
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://svn.pld-linux.org/svn/toys/fun/%{name}
# Source0-md5:	24e5779fa20aaf163704a69df9a56dcc
URL:		http://svn.pld-linux.org/cgi-bin/viewsvn/toys/fun/rsget.pl?view=log
BuildRequires:	rpm-perlprov
Suggests:	gocr
Suggests:	netpbm-progs
Suggests:	ocrad
Suggests:	perl(GD)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line downloader for RapidShare-like services.

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install %SOURCE0 $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
