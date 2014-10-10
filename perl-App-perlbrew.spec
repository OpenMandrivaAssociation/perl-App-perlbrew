%define upstream_name    App-perlbrew
%define upstream_version 0.21

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Manage perl installations in your $HOME
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Path::Tiny)
BuildRequires:	perl(HTTP::Lite)
BuildRequires:	perl(Test::Output)
BuildArch:	noarch

%description
perlbrew is a program to automate the building and installation of perl in
the users HOME. At the moment, it installs everything to
'~/perl5/perlbrew', and requires you to tweak your PATH by including a
bashrc/cshrc file it provides. You then can benefit from not having to run
'sudo' commands to install cpan modules because those are installed inside
your HOME too. It's a completely separate perl environment.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_bindir}/perlbrew
%{_mandir}/man1/perlbrew.1*
%{_mandir}/man3/*
%{perl_vendorlib}/*



%changelog
* Tue May 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.210.0-1mdv2011.0
+ Revision: 675369
- update to new version 0.21

* Thu May 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.200.0-1
+ Revision: 673783
- update to new version 0.20

* Fri Apr 29 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.190.0-1
+ Revision: 660537
- update to new version 0.19

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.180.0-2
+ Revision: 657383
- rebuild for updated spec-helper

* Fri Mar 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.180.0-1
+ Revision: 646318
- update to new version 0.18

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.170.0-1
+ Revision: 643313
- update to new version 0.17

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.160.0-1
+ Revision: 638893
- update to new version 0.16

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.150.0-1mdv2011.0
+ Revision: 612044
- update to new version 0.15

* Sun Nov 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 602367
- update to new version 0.14

* Sun Nov 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 597574
- update to new version 0.13

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.120.0-1mdv2011.0
+ Revision: 587611
- new version

* Sat Oct 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 586105
- import perl-App-perlbrew

