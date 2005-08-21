%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Archive
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - manipulate easily the tar, gz, bz2 and zip files
Summary(pl):	%{_pearname} - ³atwa obróbka plików tar, gz, bz2 i zip
Name:		php-pear-%{_pearname}
Version:	1.5.3
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	49ebbc8a341d189b7d0be90064a3d18d
URL:		http://pear.php.net/package/File_Archive/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# bogus
%define		_noautoreq	'pear(File/Archive/Reader/Cab.php)' 'pear(File/Archive/Reader/Rar.php)''

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
Ta biblioteka jest silnie zorientowana obiektowo. Dziêki temu jest
³atwa w u¿ycia, pozwala na pisanie prostego kodu, przy czym ma du¿e
mo¿liwo¶ci.

File_Archive sk³ada siê z dwóch obiektów: reader i writer. Odczyt
mo¿liwy jest z pliku, katalogu i archiwów tar, gz, zip i bzip2.

Zapis mo¿liwy jest do pliku(ów), jako za³±cznik do listu lub do
archiwów tar, gz, zip b±d¼ bzip2.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{Predicate,Reader,Writer}

install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_class}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_class}/%{_subclass}/Predicate/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Predicate
install %{_pearname}-%{version}/%{_class}/%{_subclass}/Reader/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Reader
install %{_pearname}-%{version}/%{_class}/%{_subclass}/Writer/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Writer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/%{_class}/{doc,tests}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
