#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Chart
%define	pnam	Graph
Summary:	Chart::Graph - Perl extension for a front-end to gnuplot, XRT, and Xmgrace
Summary(pl):	Chart::Graph - rozszerzenie Perla o interfejs do gnuplota, XRT i Xmgrace
Name:		perl-Chart-Graph
Version:	2.0
Release:	3
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{!?_with_tests:0}%{?_with_tests:1}
BuildRequires:	XFree86-Xvfb
BuildRequires:	gnuplot
BuildRequires:	grace
%endif
Provides:	perl(Chart::Graph::Xmgrace::Axis_Options)
Provides:	perl(Chart::Graph::Xmgrace::Dataset_Options)
Provides:	perl(Chart::Graph::Xmgrace::Graph_Options)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	"perl(Base_Option)"

%description
Graph.pm is a wrapper module that allows easy generation of graphs
within Perl. Currently Graph.pm supports three graphing packages,
gnuplot, XRT, and Xmgrace.

%description -l pl
Graph.pm to modu³ obudowuj±cy pozwalajacy na ³atwe generowanie
wykresów z poziomu Perla. Aktualnie obs³uguje trzy pakiety do
wykresów: gnuplot, XRT i Xmgrace.

%prep
%setup -q -n Chart-Graph-2

%build
echo gnuplot xmgrace | perl Makefile.PL
%{__make}

# tests disabled by default as they require GUI
%if %{!?_with_tests:0}%{?_with_tests:1}
PATH="/usr/X11R6/bin:$PATH" %{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* TODO doc/*
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
