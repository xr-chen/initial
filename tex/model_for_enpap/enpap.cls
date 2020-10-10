\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{enpap}[2020/09/14 Example LaTeX class]

\LoadClass[a4paper]{article}

\RequirePackage{amssymb}
\RequirePackage{xcolor}
\RequirePackage{amsmath}
\RequirePackage{amsthm}
\RequirePackage[nottoc,numbib]{tocbibind}
\RequirePackage{hyperref}
\RequirePackage{amsfonts}
\RequirePackage{listings}
\RequirePackage{siunitx}
\RequirePackage{fancyhdr}
\RequirePackage{array}
\RequirePackage[a4paper]{geometry}
\RequirePackage{graphicx}
\RequirePackage{subfigure}
\RequirePackage{multirow}
\RequirePackage[section]{placeins}
\RequirePackage{longtable}
\RequirePackage{wrapfig}
\RequirePackage{abstract}
\RequirePackage{appendix}
\RequirePackage{color}
\RequirePackage{mathtools}
\RequirePackage{extarrows}
\RequirePackage{listings}
\hypersetup{
colorlinks=true,
linkcolor=black
}%解决目录红框问

\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.95}
\lstset{breaklines}
\lstset{extendedchars=false}

\lstset{
numbers=left,
numberstyle=\tiny,
basicstyle=\footnotesize\ttfamily,
numberstyle=\tiny,
numbersep=1em,
keywordstyle=\color{codepurple},
commentstyle=\color{codegreen},
backgroundcolor=\color{backcolour},
commentstyle=\color{codegreen},
keywordstyle=\color{magenta},
numberstyle=\tiny\color{codegray},
stringstyle=\color{codepurple},
}

\renewcommand{\headrulewidth}{0pt} %改为0pt即可去掉页眉下面的横线
\renewcommand{\footrulewidth}{0pt}

\newcommand{\limn}{\lim_{n\to\infty}}
\newcommand{\ud}{\mathrm{d}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\N}{\mathcal{N}}
\newcommand{\test}[2]{H_0:{#1}\quad \mathrm{vs.}\quad H_1:{#2}}
\newcommand{\limp}[1]{\lim_{n\to{#1}\infty}}
\newcommand{\testin}[2]{H_0:{#1}\mbox{ }\mathrm{vs.}\mbox{ }H_1:{#2}}
