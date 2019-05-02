Name:           hello
Version:        0.1.0
Release:        1%{?dist}
Summary:        Nice and a polite tool

License:        MIT
URL:            https://github.com/packit-service/hello-world
Source0:        hello-0.1.0.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
%{summary}


%prep
%autosetup -n %{name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%{_bindir}/hello
%{python3_sitelib}/*
%doc README.md

%changelog
* Thu May 02 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.1.0-1
- initial upstream release: 0.1.0

