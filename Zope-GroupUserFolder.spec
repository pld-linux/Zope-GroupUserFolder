%include	/usr/lib/rpm/macros.python

%define		zope_subname	GroupUserFolder

Summary:	GroupUserFolder is a Zope product - Is a convenient tool to manage groups of users within Zope
Summary(pl):	GroupUserFolder jest dodatkiem dla Zope - Wygodne narzêdzie do zarz±dzaniem grupami i u¿ytkownikami zawartymi w Zope
Name:		Zope-%{zope_subname}
Version:	1.31
Release:	1
License:	GNU
Group:		Development/Tools
Source0:	http://switch.dl.sourceforge.net/sourceforge/collective/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	a354435c5aa13c63ba04713850d122d9
URL:		http://sourceforge.net/projects/collective
%pyrequires_eq	python-modules
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products

%description
GroupUserFolder is a Zope product - Is a convenient tool to manage
groups of users within Zope

%description -l pl
GroupUserFolder jest dodatkiem dla Zope - Wygodne narzêdzie do
zarz±dzania grupami i u¿ytkownikami zawartymi w Zope

%prep
%setup -q -c %{zope_subname}-%{version}

%build
cd %{zope_subname}
rm -rf `find . -type d -name debian`
rm -rf `find . -type f -name .cvsignore`
mkdir docs
mv -f CHANGES CONTRIBUTORS ChangeLog INSTALL.txt README.txt TODO docs/

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{product_dir}
cp -af * $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

rm -rf $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/docs
find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%preun

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc %{zope_subname}/docs/*
%{product_dir}/%{zope_subname}
