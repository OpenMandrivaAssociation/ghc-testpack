%global debug_package %{nil}
%define module testpack

Summary:	Test Utililty Pack for HUnit and QuickCheck
Name:		ghc-%{module}
Version:	2.1.2
Release:	3
License:	LGPLv2.1+
Group:		Development/Other
Url:		https://hackage.haskell.org/package/%{module}
Source0:	http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
Patch0:		testpack-2.1.2.maxdiscard.patch
BuildRequires:	ghc-devel
BuildRequires:	haddock
BuildRequires:	haskell-macros
BuildRequires:	haskell(HUnit)
BuildRequires:	haskell(QuickCheck)
BuildRequires:	haskell(mtl)
BuildRequires:	haskell(random)
Requires(post,preun):	ghc
Requires(pre):	haskell(HUnit)
Requires(pre):	haskell(QuickCheck)
Requires(pre):	haskell(mtl)
Requires(pre):	haskell(random)

%description
Haskell Test Utility Pack for HUnit and QuickCheck testpack provides utilities
for both HUnit and QuickCheck. These include tools for running QuickCheck
properties as HUnit test cases, allowing you to combine both approaches in a
single program. It also includes tools for more helpful displays of running
progress in both HUnit and QuickCheck, additional generators for other types
for QuickCheck, and shortcuts for quickly defining new test cases.

%files
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%{_cabal_rpm_deps_dir}
%{_cabal_haddoc_files}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1 -b .maxdiscard

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

