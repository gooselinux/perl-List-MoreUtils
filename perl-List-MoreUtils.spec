Name:           perl-List-MoreUtils
Version:        0.22
Release:        10%{?dist}
Summary:        Provide the stuff missing in List::Util

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/List-MoreUtils/
Source0:        http://www.cpan.org/authors/id/V/VP/VPARSEVAL/List-MoreUtils-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
List::MoreUtils provides some trivial but commonly needed functionality
on lists which is not going to go into List::Util.


%prep
%setup -q -n List-MoreUtils-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/List/
%{perl_vendorarch}/auto/List/
%{_mandir}/man3/*.3pm*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.22-10
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.22-6
- Rebuild normally, second pass

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.22-5
- Rebuild for perl 5.10 (again), tests disabled for first pass

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.22-4
- Autorebuild for GCC 4.3

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.22-3
- rebuild normally, second pass

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.22-2.1
- rebuild for new perl, first pass, disable TPC and tests

* Sun Sep 10 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.22-2
- Rebuild for FC6.

* Mon Jul  3 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.22-1
- Update to 0.22.

* Mon Jun 19 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.21-1
- Update to 0.21.

* Sat Jun 10 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.20-1
- Update to 0.20.

* Sat Apr 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.19-1
- First build.
