# TODO:
# - package emacs file:
# /usr/share/emacs/site-lisp/site-start.d/appdata-rng-init.el
Summary:	Tools to validate AppData
Summary(pl.UTF-8):	Narzędzia do weryfikacji AppData
Name:		appdata-tools
Version:	0.1.8
Release:	5
License:	GPL v2+
Group:		Applications/System
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
# Source0-md5:	47d8500b7b96fac6667c3173c77c1e66
URL:		http://people.freedesktop.org/~hughsient/appdata/
BuildRequires:	appstream-glib-devel >= 0.1.4
BuildRequires:	docbook-dtd43-xml
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libxslt-progs
BuildRequires:	python
BuildRequires:	python-lxml
BuildRequires:	tar >= 1:1.22
BuildRequires:	trang
BuildRequires:	xz
Requires:	appstream-glib >= 0.1.4
Requires:	glib2 >= 1:2.36.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
appdata-tools contains a command line program designed to validate
AppData application descriptions for standards compliance and to the
style guide.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia do weryfikacji opisów aplikacji AppData
pod kątem zgodności ze standardem i wskazówek dotyczących stylu.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/appdata-validate
%dir %{_datadir}/appdata/schema
%{_datadir}/appdata/schema/appdata.rnc
%{_datadir}/appdata/schema/appdata.rng
%{_datadir}/appdata/schema/appdata.sch
%{_datadir}/appdata/schema/appdata.xsd
%{_datadir}/appdata/schema/schema-locating-rules.xml
%{_aclocaldir}/appdata-xml.m4
%{_mandir}/man1/appdata-validate.1*

# TODO:
#%{_datadir}/emacs/site-lisp/site-start.d/appdata-rng-init.el
