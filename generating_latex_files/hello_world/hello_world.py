from pylatex import Document, Section, Command

doc = Document('hello_world')

doc.preamble.append(Command('title', 'Hello, World!'))
doc.preamble.append(Command('author', 'Your Name'))

doc.append(Section('Introduction'))

doc.append('Hello, World!')

doc.generate_pdf()