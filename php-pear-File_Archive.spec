%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Archive
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - manipulate easily the tar, gz, bz2 and zip files
Summary(pl):	%{_pearname} - �atwa obr�bka plik�w tar, gz, bz2 i zip
Name:		php-pear-%{_pearname}
Version:	1.5.3
Release:	1.1
Epoch:		0
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	49ebbc8a341d189b7d0be90064a3d18d
Patch0:		%{_pearname}-noimpl.patch
URL:		http://pear.php.net/package/File_Archive/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.3.0
Requires:	php-pear
Requires:	php-pear-MIME_Type
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Mail/Mime.*)' 'pear(Mail.*)' 'pear(Cache/Lite.*)'

%description
This library is strongly object oriented. It makes it very easy to
use, writing simple code, yet the library is very powerfull.

File_Archive is made of two objects : readers and writers. Are
currently implemented readers from file, directory, tar, gz, zip and
bzip2 archives.

You can write to file(s), send mails with files attached, or create
tar, gz, zip, bzip2 archives.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta biblioteka jest silnie zorientowana obiektowo. Dzi�ki temu jest
�atwa w u�ycia, pozwala na pisanie prostego kodu, przy czym ma du�e
mo�liwo�ci.

File_Archive sk�ada si� z dw�ch obiekt�w: reader i writer. Odczyt
mo�liwy jest z pliku, katalogu i archiw�w tar, gz, zip i bzip2.

Zapis mo�liwy jest do pliku(�w), jako za��cznik do listu lub do
archiw�w tar, gz, zip b�d� bzip2.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/%{_class}/doc/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
