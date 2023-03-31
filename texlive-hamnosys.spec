Name:		texlive-hamnosys
Version:	61941
Release:	2
Summary:	A font for sign languages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hamnosys
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hamnosys.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hamnosys.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hamnosys.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Hamburg Notation System, HamNoSys for short, is a system
for the phonetic transcription of signed languages. This
package makes HamNoSys available in XeLaTeX and LuaLaTeX. The
package provides a Unicode font for rendering HamNoSys symbols
as well as three methods for entering them.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/fonts/hamnosys
%{_texmfdistdir}/tex/latex/hamnosys
%{_texmfdistdir}/fonts/truetype/public/hamnosys
%doc %{_texmfdistdir}/doc/fonts/hamnosys

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
