%define upstream_name    App-perlbrew
%define upstream_version 0.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Manage perl installations in your $HOME
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Path::Tiny)
BuildRequires: perl(HTTP::Lite)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml README
%{_bindir}/perlbrew
%{_mandir}/man1/perlbrew.1*
%{_mandir}/man3/*
%perl_vendorlib/*

