\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{enpap}[2020/09/14 Example LaTeX class]

\LoadClass[a4paper,11pt]{article}

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

\hypersetup{
colorlinks=true,
linkcolor=black
}%解决目录红框问

\renewcommand{\headrulewidth}{0pt} %改为0pt即可去掉页眉下面的横线
\renewcommand{\footrulewidth}{0pt}
