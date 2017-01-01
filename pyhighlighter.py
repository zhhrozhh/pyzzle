#http://stackoverflow.com/questions/26679515/how-to-update-qsyntaxhighlighter-color-coding-when-user-changes-text
import sys
from PyQt4.QtCore import QRegExp
from PyQt4.QtGui import QColor,QTextCharFormat,QFont,QSyntaxHighlighter
def format(color, style=''):
    _color = QColor()
    _color.setNamedColor(color)
    _format = QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)
    return _format
STYLES = {
    'keyword': format('blue'),
    'operator': format('darkred'),
    'brace': format('cyan','bold'),
    'defclass': format('green', 'bold'),
    'string': format('darkGreen'),
    'string2': format('darkMagenta'),
    'comment': format('Grey', 'italic'),
    'self': format('black', 'italic'),
    'numbers': format('darkMagenta'),
}
class PythonHighlighter (QSyntaxHighlighter):
    keywords = [
        "open", "close", "elif", "if","for","while","break","continue"
        "from", "import","as","range"
        "join", "lambda",
        "sum", "max", "min","return",
        "def","class","range","print","eval","exec","global"
    ]
    operators = [
        "and", "in", "or","not","is"
        "\\^", "=", ">=", ">",
         "<=", "<",
    ]
    braces = [
        '\{', '\}', '\(', '\)', '\[', '\]',
    ]
    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)
        rules = []
        rules += [(r'\b%s\b' % w, 0, STYLES['keyword'])
            for w in PythonHighlighter.keywords]
        rules += [(r'\b%s\b' % o, 0, STYLES['operator'])
            for o in PythonHighlighter.operators]
        rules += [(r'%s' % b, 0, STYLES['brace'])
            for b in PythonHighlighter.braces]
        rules += [
            (r'\bself\b', 0, STYLES['self']),
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, STYLES['string']),
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, STYLES['string']),
            (r'"{3}[\s\S]*?"{3}',0,STYLES['string']),
            (r"'{3}[\s\S]*?'{3}",0,STYLES['string']),
            (r'\bdef\b\s*(\w+)', 1, STYLES['defclass']),
            (r'\bclass\b\s*(\w+)', 1, STYLES['defclass']),
            (r'#[^\n]*', 0, STYLES['comment']),
            (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, STYLES['numbers']),
        ]
        self.rules = [(QRegExp(pat), index, fmt)
            for (pat, index, fmt) in rules]
    def highlightBlock(self, text):
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)
            while index >= 0:
                index = expression.pos(nth)
                length = len(expression.cap(nth))#.length()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)
        self.setCurrentBlockState(0)