%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Medium Length Professional CV - RESUME CLASS FILE
%
% This template has been downloaded from:
% http://www.LaTeXTemplates.com
%
% This class file defines the structure and design of the template.
%
% Original header:
% Copyright (C) 2010 by Trey Hunner
%
% Copying and distribution of this file, with or without modification,
% are permitted in any medium without royalty provided the copyright
% notice and this notice are preserved. This file is offered as-is,
% without any warranty.
%
% Created by Trey Hunner and modified by www.LaTeXTemplates.com
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\ProvidesClass{resume}[2010/07/10 v0.9 Resume class]

\LoadClass[9pt,letterpaper]{article} % Font size and paper type


\usepackage{array} % Required for boldface (\bf and \bfseries) tabular columns

\usepackage{ifthen} % Required for ifthenelse statements
\usepackage{setspace}

\usepackage{xcolor}
\pagestyle{empty}
\pagecolor{tan!10!white}
\usepackage{tikz}
\usetikzlibrary{calc}
\usepackage{eso-pic}

\AddToShipoutPictureBG{%
\begin{tikzpicture}[overlay,remember picture]
\draw[line width=4pt]
    ($ (current page.north west) + (1cm,-1cm) $)
    rectangle
    ($ (current page.south east) + (-1cm,1cm) $);
\draw[line width=1.5pt]
    ($ (current page.north west) + (1.2cm,-1.2cm) $)
    rectangle
    ($ (current page.south east) + (-1.2cm,1.2cm) $);
\end{tikzpicture}
}



%----------------------------------------------------------------------------------------
%	HEADINGS COMMANDS: Commands for printing name and address
%----------------------------------------------------------------------------------------

\def \name#1{\def\@name{#1}} % Defines the \name command to set name
\def \@name {} % Sets \@name to empty by default

\def \addressSep {$\diamond$} % Set default address separator to a diamond

% One, two or three address lines can be specified
\let \@addressone \relax
\let \@addresstwo \relax
\let \@addressthree \relax

% \address command can be used to set the first, second, and third address (last 2 optional)
\def \address #1{
  \@ifundefined{@addresstwo}{
    \def \@addresstwo {#1}
  }{
  \@ifundefined{@addressthree}{
  \def \@addressthree {#1}
  }{
     \def \@addressone {#1}
  }}
}


% \printname is used to print the name as a page header
\def \printname {
    {\color{green!40!blue}{\MakeUppercase{\namesize\huge{\@name}}}}
}
%----------------------------------------------------------------------------------------
%	PRINT THE HEADING LINES
%----------------------------------------------------------------------------------------

\let\ori@document=\document
\renewcommand{\document}{
  \ori@document  % Begin document
  \printname % Print the name specified with \name
  \@ifundefined{@addressone}{}{ % Print the first address if specified
    \printaddress{\@addressone}}
  \@ifundefined{@addresstwo}{}{ % Print the second address if specified
    \printaddress{\@addresstwo}}
     \@ifundefined{@addressthree}{}{ % Print the third address if specified
    \printaddress{\@addressthree}}
}

%----------------------------------------------------------------------------------------
%	SECTION FORMATTING
%----------------------------------------------------------------------------------------

% Defines the rSection environment for the large sections within the CV

\newenvironment{rSection}[1]{ % 1 input argument - section name
\sectionlineskip
  {\color{green!40!blue}\rule{0.4\textwidth}{2pt}}
  \linebreak \MakeUppercase{\italic #1} % Section title



  \begin{list}{}{ % List for each individual item in the section
    \small\setlength{\rightmargin}{9em} % Margin within the section
  }
  \item[]
}{
  \end{list}
}

%----------------------------------------------------------------------------------------
%	WORK EXPERIENCE FORMATTING
%----------------------------------------------------------------------------------------

\newenvironment{rSubsection}[4]{ % 4 input arguments - company name, year(s) employed, job title and location
 \fbox{\bf #1}\linebreak   {#2} % Bold company name and date on the right
 \ifthenelse{\equal{#3}{}}{}{ % If the third argument is not specified, don't print the job title and location line
  \\
  {\em #3} :{\em #4} % Italic job title and location
  }\smallskip

  \begin{spacing}{0.2}
  \begin{list}{$\cdot$}{\leftmargin=5em} % \cdot used for bullets, no indentation
   \itemsep -0.2em \vspace{-0.2em} % Compress items in list together for aesthetics

  }{
  \end{list}
  \end{spacing}
  \vspace{0.1em} % Some space after the list of bullet points
}

% The below commands define the whitespace after certain things in the document - they can be \smallskip, \medskip or \bigskip
\def\namesize{\large} % Size of the name at the top of the document
\def\addressskip{\small} % The space between the two address (or phone/email) lines
\def\sectionlineskip{\medskip} % The space above the horizontal line for each section

\def\nameskip{\Hugeskip % The space after your name at the top
\def\sectionskip{\medskip} % The space after the heading section


%----------------------------------------------------------------------------------------
%	COURSEWORK EXPERIENCE FORMATTING
%----------------------------------------------------------------------------------------

