Name:           world
Version:        0.1.0
Release:        1%{?dist}
Summary:        Nice and a polite tool to make your day
License:        MIT
URL:            https://github.com/packit-service/hello-world
Source0:        world-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}


%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%{_bindir}/world
%{python3_sitelib}/*
%doc README.md

%changelog
* Thu May 02 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.1.0-1
- initial upstream release: 0.1.0
