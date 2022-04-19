ensure_path( 'TEXINPUTS', './:./LaTeX-proposal///base:./LaTeX-proposal///etc:./LaTeX-proposal///eu' );
$pdf_previewer = 'open -a Skim';
@generated_exts = (@generated_exts, 'delivs', 'deliverables', 'synctex.gz', 'pdata');
$latex = 'latex -synctex=1 -interaction=nonstopmode -shell-escape';
$pdflatex = 'pdflatex -synctex=1 -interaction=nonstopmode -shell-escape';
$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode -shell-escape %B; sort %B.delivs > %B.deliverables';
$pdf_mode = 5;
@default_files = ('draft.tex');
$max_repeat=5;
