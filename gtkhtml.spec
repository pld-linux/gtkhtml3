
%define _snap 20030323
%define _mver 3.0

Summary:	Gtkhtml library
Summary(pl):	Biblioteka gtkhtml
Summary(pt_BR):	Biblioteca gtkhtml
Summary(ru):	GtkHTML - ��� ���������� ����������/�������������� HTML
Summary(uk):	GtkHTML - �� ¦�̦����� ����������/����������� HTML
Summary(zh_CN): gtkhtml ��
Name:		gtkhtml
Version:	%{_mver}.1
Release:	0.%{_snap}.1
License:	LGPL
Group:		X11/Libraries
#Source0:	ftp://ftp.gnome.org/mirror/gnome.org/sources/gtkhtml/%{_mver}/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}-%{_snap}.tar.bz2
#Patch0:		%{name}-am15.patch
Patch1:		%{name}-pixmap.patch
Patch2:		%{name}-%{name}-stream.h.patch
#Patch3:		%{name}-get_default_fonts.patch
Patch4:		%{name}-disable_testgtkhtml.patch
BuildRequires:	ORBit2-devel
Buildrequires:	bonobo-activation
BuildRequires:	gail-devel >= 0.13
BuildRequires:	gal-devel >= 1.99.2.99
BuildRequires:	intltool
BuildRequires:	libbonobo-devel
Buildrequires:	libgnomeprintui-devel >= 2.2.1
BuildRequires:	libgnomeui-devel
Buildrequires:	libsoup-devel >= 1.99.14
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgtkhtml20

%description
This is GtkHTML, a lightweight HTML rendering/printing/editing engine.
It was originally based on KHTMLW, but is now being developed
independently of it.

%description -l pl
GtkHTML jesrt "lekk�" bibilotek� do renderingu, drukowania i edycji
HTML. Pierwotne �r�d�a tej biblioteki bazuj� na KHTMLW ale teraz
GtkHTML jest rozwijana niezale�nie od KHTMLW,

%description -l pt_BR
Este � o GtkHTML, uma ferramenta de renderizar/imprimir/editar HTML
leve e pequeno

%description -l ru
��� GtkHTML, ������ "������" ����������/������/�������������� HTML.
������� �� ����������� �� KHTMLW, �� ������ ���������������
����������.

%description -l uk
�� GtkHTML, ����� ���� ����������/�����/����������� HTML. ����
�������� ���������� �� KHTMLW, ��� ����� �������Ѥ���� ��������� צ�
�����.

%package devel
Summary:	Header files and etc neccessary to develop gtkhtml applications
Summary(es):	Bibliotecas, archivos de inclusi�n, e etc. para desarrollar aplicaciones gtkhtml
Summary(pl):	Pliki nag��wkowe i inne nizb�dne do tworzenia aplikacji u�ywaj�cych gtkhtml
Summary(pt_BR):	Bibliotecas, arquivos de inclus�o, e etc para desenvolver aplica��es gtkhtml
Summary(ru):	�����, ����������� ��� ���������� �������� � �������������� gtkhtml
Summary(uk):	�����, ����Ȧ�Φ ��� �������� ������� � ������������� gtkhtml
Summary(zh_CN): gtkhtml������
Group:		X11/Libraries
Requires:	%{name} = %{version}
Requires:	gal-devel >= 1.99.2.99
Requires:	libbonobo-devel
Requires:	libgnomeprint-devel >= 2.2.0
Requires:	libunicode-devel
Obsoletes:	lubgtkhtml20-devel

%description devel
Header files and etc neccessary to develop gtkhtml applications.

%description devel -l es
Bibliotecas, archivos de inclusi�n, y etc para desarrollar
aplicaciones gtkhtml.

%description devel -l pl
Pliki nag��wkowe i reszta niezb�dnych przy tworzeniu aplikacji
wykorzystujacych gtkhtml.

%description devel -l pt_BR
Bibliotecas, arquivos de inclus�o, e etc para desenvolver aplica��es
gtkhtml.

%description devel -l ru
�����, ����������� ��� ���������� �������� � �������������� gtkhtml.

%description devel -l uk
�����, ����Ȧ�Φ ��� �������� ������� � ������������� gtkhtml.

%package static
Summary:	Static gtkhtml libraries
Summary(es):	Bibliotecas est�ticas para desarrollar aplicaciones gtkhtml
Summary(pl):	Biblioteki statyczne gtkhtml
Summary(pt_BR):	Bibliotecas est�ticas para desenvolver aplica��es gtkhtml
Summary(ru):	����������� ���������� ��� ���������� �������� � gtkhtml
Summary(uk):	������Φ ¦�̦����� ��� �������� ������� � gtkhtml
Group:		X11/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static gtkhtml libraries.

%description static -l es
Bibliotecas est�ticas para desarrollar aplicaciones gtkhtml.

%description static -l pl
Biblioteki statyczne gtkhtml.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolver aplica��es gtkhtml.

%prep
%setup -q
#%%patch0 -p1
%patch1 -p1
%patch2 -p1
#%%patch3 -p1
%patch4 -p1

%build
rm -f missing
glib-gettextize --copy --force
intltoolize --copy --force
xml-i18n-toolize --force
%{__libtoolize}
%{__aclocal} -I macros
%{__autoheader}
%{__autoconf}
%{__automake}

%configure \
	--with-bonobo \
	--with-gconf

%{__make} \
	idldir=%{_datadir}/idl \
	pkgconfigdir=%{_pkgconfigdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	idldir=%{_datadir}/idl
	
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README* TODO
%attr(755,root,root) %{_libdir}/gnome-gtkhtml-editor*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/bonobo/servers/*
%{_datadir}/%{name}-%{_mver}
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_datadir}/idl/*.idl
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
