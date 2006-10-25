#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Locale
%define	pnam	Maketext-Gettext
Summary:	Locale::Maketext::Gettext - Joins the gettext and Maketext frameworks
Summary(pl):	Locale::Maketext::Gettext - ³±czenie szkieletów gettext i Maketext
Name:		perl-Locale-Maketext-Gettext
Version:	1.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	98e591014b8c6af909acafc4513455de
URL:		http://search.cpan.org/dist/Locale-Maketext-Gettext/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locale::Maketext::Gettext joins the GNU gettext and Maketext
frameworks. It is a subclass of Locale::Maketext(3) that follows the
way GNU gettext works. It works seamlessly, both in the sense of GNU
gettext and Maketext. As a result, you enjoy both their advantages,
and get rid of both their problems, too.

You start as an usual GNU gettext localization project: Work on PO
files with the help of translators, reviewers and Emacs. Turn them
into MO files with msgfmt. Copy them into the appropriate locale
directory, such as /usr/share/locale/de/LC_MESSAGES/myapp.mo.

Then, build your Maketext localization class, with your base class
changed from Locale::Maketext(3) to Locale::Maketext::Gettext. That's
all.

%description -l pl
Locale::Maketext::Gettext ³±czy szkielety GNU gettext i Maketext. Jest
podklas± Locale::Maketext(3) dzia³aj±c± w taki sposób, jak GNU
gettext. Dzia³a w sposób przezroczysty, zarówno w znaczeniu GNU
gettexta, jak i Maketexta. W efekcie mo¿na cieszyæ siê zaletami ich
obu i pozbyæ ich problemów.

Pracê zaczyna siê jak w zwyk³ym projekcie lokalizacji GNU gettexta:
pracuje na plikach PO z pomoc± t³umaczy, recenzentów i Emacsa.
Nastêpnie zamienia je na pliki MO przy u¿yciu msgfmt, kopiuje do
odpowiednich katalogów lokalizacji, takich jak
/usr/share/locale/de/LC_MESSAGES/myapp.mo.

Nastêpnie tworzy siê klasê lokalizacji Maketexta z klas± podstawow±
zmienion± z Locale::Maketext(3) na Locale::Maketext::Gettext. To
wszystko.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
mv -f t/00-signature.t{,.blah}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS Changes README
%{_bindir}/*
%{perl_vendorlib}/Locale/Maketext/*.pm
%{perl_vendorlib}/Locale/Maketext/Gettext
%{_mandir}/man[13]/*
