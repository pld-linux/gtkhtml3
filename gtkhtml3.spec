Summary:	GtkHTML 3 library
Summary(pl.UTF-8):	Biblioteka GtkHTML 3
Summary(pt_BR.UTF-8):	Biblioteca GtkHTML 3
Summary(ru.UTF-8):	GtkHTML 3 - это библиотека рендеринга/редактирования HTML
Summary(uk.UTF-8):	GtkHTML 3 - це бібліотека рендерингу/редагування HTML
Summary(zh_CN.UTF-8):	GtkHTML 3 库
Name:		gtkhtml3
Version:	3.32.2
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkhtml/3.32/gtkhtml-%{version}.tar.bz2
# Source0-md5:	3e1a1d56beef147aa0a95e5ebbf61c8c
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1:1.9
BuildRequires:	enchant-devel >= 1.1.7
BuildRequires:	gettext-tools
BuildRequires:	gnome-icon-theme >= 2.22.0
BuildRequires:	gtk+2-devel >= 2:2.20.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	iso-codes >= 0.49
BuildRequires:	libsoup-devel >= 2.26.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	enchant >= 1.1.7
Requires:	gnome-icon-theme >= 2.22.0
Requires:	gtk+2 >= 2:2.20.0
Obsoletes:	gal
Obsoletes:	gtkhtml < 3.90
Obsoletes:	libgtkhtml20
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is GtkHTML 3, a lightweight HTML rendering/printing/editing
engine. It was originally based on KHTMLW, but is now being developed
independently of it.

%description -l pl.UTF-8
GtkHTML 3 jest "lekką" biblioteką do renderingu, drukowania i edycji
HTML. Pierwotne źródła tej biblioteki bazują na KHTMLW ale teraz
GtkHTML jest rozwijana niezależnie od KHTMLW.

%description -l pt_BR.UTF-8
Este é o GtkHTML 3, uma ferramenta de renderizar/imprimir/editar HTML
leve e pequeno

%description -l ru.UTF-8
Это GtkHTML 3, легкий "движок" рендеринга/печати/редактирования HTML.
Сначала он базировался на KHTMLW, но теперь разрабатывается
независимо.

%description -l uk.UTF-8
Це GtkHTML 3, легке ядро рендерингу/друку/редагування HTML. Воно
спочатку базувалось на KHTMLW, але тепер розробляється незалежно від
нього.

%package devel
Summary:	Header files etc. neccessary to develop GtkHTML 3 applications
Summary(es.UTF-8):	Bibliotecas, archivos de inclusión, e etc. para desarrollar aplicaciones GtkHTML 3
Summary(pl.UTF-8):	Pliki nagłówkowe i inne niezbędne do tworzenia aplikacji używających GtkHTML 3
Summary(pt_BR.UTF-8):	Bibliotecas, arquivos de inclusão, e etc para desenvolver aplicações GtkHTML 3
Summary(ru.UTF-8):	Файлы, необходимые для разработки программ с использованием GtkHTML 3
Summary(uk.UTF-8):	Файли, необхідні для розробки програм з використанням GtkHTML 3
Summary(zh_CN.UTF-8):	GtkHTML 3 开发库
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel >= 2.24.0
Requires:	enchant-devel >= 1.1.7
Requires:	gtk+2-devel >= 2:2.20.0
Requires:	iso-codes >= 0.49
Obsoletes:	gal-devel
Obsoletes:	gtkhtml-devel < 3.90
Obsoletes:	libgtkhtml20-devel

%description devel
Header files etc. neccessary to develop GtkHTML 3 applications.

%description devel -l es.UTF-8
Bibliotecas, archivos de inclusión, y etc para desarrollar
aplicaciones GtkHTML 3.

%description devel -l pl.UTF-8
Pliki nagłówkowe i reszta niezbędnych przy tworzeniu aplikacji
wykorzystujących GtkHTML 3.

%description devel -l pt_BR.UTF-8
Bibliotecas, arquivos de inclusão, e etc para desenvolver aplicações
GtkHTML 3.

%description devel -l ru.UTF-8
Файлы, необходимые для разработки программ с использованием GtkHTML 3.

%description devel -l uk.UTF-8
Файли, необхідні для розробки програм з використанням GtkHTML 3.

%package static
Summary:	Static GtkHTML 3 libraries
Summary(es.UTF-8):	Bibliotecas estáticas para desarrollar aplicaciones GtkHTML 3
Summary(pl.UTF-8):	Biblioteki statyczne GtkHTML 3
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolver aplicações GtkHTML 3
Summary(ru.UTF-8):	Статические библиотеки для разработки программ с GtkHTML 3
Summary(uk.UTF-8):	Статичні бібліотеки для розробки програм з GtkHTML 3
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	gal-static
Obsoletes:	gtkhtml-static < 3.90

%description static
Static GtkHTML 3 libraries.

%description static -l es.UTF-8
Bibliotecas estáticas para desarrollar aplicaciones GtkHTML 3.

%description static -l pl.UTF-8
Biblioteki statyczne GtkHTML 3.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolver aplicações GtkHTML 3.

%prep
%setup -q -n gtkhtml-%{version}

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	--disable-deprecated-warning-flags \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang gtkhtml-3.14

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f gtkhtml-4.0.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README* TODO
%attr(755,root,root) %{_bindir}/gtkhtml-editor-test
%attr(755,root,root) %{_libdir}/libgtkhtml-3.14.so.*.*.*
%attr(755,root,root) %{_libdir}/libgtkhtml-editor-3.14.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkhtml-3.14.so.19
%attr(755,root,root) %ghost %{_libdir}/libgtkhtml-editor-3.14.so.0
%{_datadir}/gtkhtml-3.14

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkhtml-3.14.so
%attr(755,root,root) %{_libdir}/libgtkhtml-editor-3.14.so
%{_includedir}/libgtkhtml-3.14
%{_pkgconfigdir}/libgtkhtml-3.14.pc
%{_pkgconfigdir}/gtkhtml-editor-3.14.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkhtml-3.14.a
%{_libdir}/libgtkhtml-editor-3.14.a
