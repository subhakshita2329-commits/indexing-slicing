Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#indexing
a="vijayawada"
a[4]
'y'
a[6]
'w'
a[7]
'a'
a[]0
SyntaxError: invalid syntax
a[0]
'v'
a[1]
'i'
a[2]
'j'
a[3]
'a'
a[4]
'y'
a[5]
'a'
a[0]
'v'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
x=i am in class
SyntaxError: invalid syntax
x="i am in class"
x[8]+x[9]x[10]+x[11]+x[12]
SyntaxError: invalid syntax
x[6]
'n'
x[8]+x[9]+x[10]+x[11]+x[12]
'class'
x[2]+x[3]
'am'
x[5]+x[6]
'in'
x[1]
' '
x[1]+x[4]
'  '
a="i love python"
a[2]+a[3]+a[4]+a[5]
'love'
a[7]+a[8]+a[9]+a[10]+a[11]+a[12]
'python'
b=i am learning python course
SyntaxError: invalid syntax
b="i am learning python course"
b[2]+b[3]
'am'
b[5]+b[6]+b[7]+b[8]+b[9]
'learn'
b[20]+b[21]+b[22]+b[23]+b[24]+b[25]
' cours'
b[20]+b[21]+b[22]+b[23]+b[24]+b[25]+b[26]
' course'
a="vijayawada is a royal city"
a[16]
'r'
a[16]+a[17]+a[18]+a[19]+a[20]
'royal'
a[22]
'c'
a[22]+a[23]+a[24]+a[25]
'city'
a[11]
'i'
a[11]+a[12]
'is'
''positive indexing starts from '0'
SyntaxError: invalid syntax
''positive indexing starts from '0'''
SyntaxError: invalid syntax
''positive indexing starts from '0' ''
SyntaxError: invalid syntax
#negative indexing
a=work until you succeed
SyntaxError: invalid syntax
a="work until you succeed"
a[-17]
'u'
a[-17]+a[-18]+a[-19]+a[-20]+a[-21]
'u kro'
a[-17]+a[-16]+a[-15]+a[-14]+a[13]
'untiu'
a[-17]+a[-16]+a[-15]+a[-14]+a[-13]
'until'
a[-22]
'w'
a[-22]+a[-21]+a[-20]+a[-19]
'work'
a[-11]
'y'
a[-11]+a[-10]+a[-9]
'you'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'succeed'
b="simple is better than complex"
b[-19]+a[18]+a[-17]+a[-16]+a[-15]+a[-14]
'bcunti'
b[-19]+b[-18]+b[-17]+b[-16]+b[-15]+b[-14]
'better'
b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'complex'
b[-12]+b[-11]+b[-10]+b[-9]
'than'
b[-29]+b[-28]+b[-27]+b[-26]+b[-25]+b[24]
'simplm'
b[-29]+b[-28]+b[-27]+b[-26]+b[-25]+b[-24]
'simple'
#slicing
a="codegnan"
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a="beautiful is better than ugly"
b[0:9]
'simple is'
a[0:9]
'beautiful'
a[14:19]
'etter'
a[13:19]
'better'
>>> a[0:9]
'beautiful'
>>> a[26:29]
'gly'
>>> a[25:29]
'ugly'
>>> a="vizag is a city of destiny"
>>> a[19:26]
'destiny'
>>> a[11:15]
'city'
>>> a[0:5]
'vizag'
>>> #negative slicing
>>> a="time is very precious"
>>> a[-8]
'p'
>>> a[-8:-1]
'preciou'
>>> a[-8:0]
''
>>> a[-8]
'p'
>>> a[-8:]
'precious'
>>> a[-13:-9]
'very'
>>> a[-21:-17]
'time'
>>> a="every day is a learning"
>>> a[-8:]
'learning'
>>> a[-17:-14]
'day'
>>> a[-23:-18]
'every'
>>> a[-13:-11]
'is'
>>> #striding
>>> a="data science"
>>> a[::]
'data science'
>>> a[::1]
'data science'
>>> a[::2]
'dt cec'
