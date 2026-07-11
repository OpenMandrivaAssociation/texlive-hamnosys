%global tl_name hamnosys
%global tl_revision 61941

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.3
Release:	%{tl_revision}.1
Summary:	A font for sign languages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/hamnosys
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hamnosys.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hamnosys.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hamnosys.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Hamburg Notation System, HamNoSys for short, is a system for the
phonetic transcription of signed languages. This package makes HamNoSys
available in XeLaTeX and LuaLaTeX. The package provides a Unicode font
for rendering HamNoSys symbols as well as three methods for entering
them.

