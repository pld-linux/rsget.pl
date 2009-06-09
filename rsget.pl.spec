%include        /usr/lib/rpm/macros.perl
Summary:	Command line downloader for RapidShare-like services
Name:		rsget.pl
Version:	10390
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://svn.pld-linux.org/svn/toys/%{name}/rsget.pl
# Source0-md5:	9f7d4a1713e9b0e554047a82653effb4
Source1:	http://svn.pld-linux.org/svn/toys/rsget.pl/mu_font_db.png
# Source1-md5:	fae68acfaa2fd5859e74eb79a9da54a1
URL:		http://svn.pld-linux.org/cgi-bin/viewsvn/toys/rsget.pl/
BuildRequires:	rpm-perlprov
Suggests:	ImageMagick-coder-png
Suggests:	gocr
Suggests:	netpbm-progs
Suggests:	ocrad
Suggests:	perl(Image::Magick)
Suggests:	perl-GD
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line downloader for RapidShare-like services.

%prep
sed 's#\($data_path\) =.*;#\1 = "%{_datadir}/%{name}";#' \
	< %{SOURCE0} > %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
install %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
