%define		status		stable
%define		pearname	File_Archive
Summary:	%{pearname} - manipulate easily the tar, gz, bz2 and zip files
Summary(pl.UTF-8):	%{pearname} - łatwa obróbka plików tar, gz, bz2 i zip
Name:		php-pear-%{pearname}
Version:	1.5.5
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	be45b469695cb61e477af1a68c6357f3
Patch0:		%{pearname}-noimpl.patch
URL:		http://pear.php.net/package/File_Archive/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(core) >= 4.3.0
Requires:	php(pcre)
Requires:	php(zlib)
Requires:	php-pear
Requires:	php-pear-MIME_Type
Suggests:	php(bz2)
Suggests:	php-pear-Cache_Lite
Suggests:	php-pear-Mail
Suggests:	php-pear-Mail_Mime
Obsoletes:	php-pear-File_Archive-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(Mail/Mime.*) pear(Mail.*) pear(Cache/Lite.*)

%description
This library is strongly object oriented. It makes it very easy to
use, writing simple code, yet the library is very powerfull.

File_Archive is made of two objects : readers and writers. Are
currently implemented readers from file, directory, tar, gz, zip and
bzip2 archives.

You can write to file(s), send mails with files attached, or create
tar, gz, zip, bzip2 archives.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ta biblioteka jest silnie zorientowana obiektowo. Dzięki temu jest
łatwa w użycia, pozwala na pisanie prostego kodu, przy czym ma duże
możliwości.

File_Archive składa się z dwóch obiektów: reader i writer. Odczyt
możliwy jest z pliku, katalogu i archiwów tar, gz, zip i bzip2.

Zapis możliwy jest do pliku(ów), jako załącznik do listu lub do
archiwów tar, gz, zip bądź bzip2.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup
%patch -P0 -p1

mv .%{php_pear_dir}/data/File_Archive/README .

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
%doc install.log README docs/%{pearname}/doc/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/File/*.php
%{php_pear_dir}/File/Archive
