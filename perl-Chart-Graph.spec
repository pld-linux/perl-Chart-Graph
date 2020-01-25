#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%define		pdir	Chart
%define		pnam	Graph
Summary:	Chart::Graph - Perl extension for a front-end to gnuplot, XRT, and Xmgrace
Summary(pl.UTF-8):	Chart::Graph - rozszerzenie Perla o interfejs do gnuplota, XRT i Xmgrace
Name:		perl-Chart-Graph
Version:	3.2
Release:	2
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	308394f5e2fd06d0aa52d2a9c6b72a44
URL:		http://search.cpan.org/dist/Chart-Graph/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	XFree86-Xvfb
BuildRequires:	gnuplot
BuildRequires:	grace
%endif
Provides:	perl(Chart::Graph::Xmgrace::Axis_Options)
Provides:	perl(Chart::Graph::Xmgrace::Dataset_Options)
Provides:	perl(Chart::Graph::Xmgrace::Graph_Options)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Base_Option)'

%description
Graph.pm is a wrapper module that allows easy generation of graphs
within Perl. Currently Graph.pm supports three graphing packages,
gnuplot, XRT, and Xmgrace.

%description -l pl.UTF-8
Graph.pm to moduł obudowujący pozwalający na łatwe generowanie
wykresów z poziomu Perla. Aktualnie obsługuje trzy pakiety do
wykresów: gnuplot, XRT i Xmgrace.

%prep
%setup -q -n Chart-Graph-%{version}

%build
echo gnuplot xmgrace | perl Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

# tests disabled by default as they require GUI
%if %{with tests}
PATH="/usr/X11R6/bin:$PATH" %{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* TODO doc/*
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
