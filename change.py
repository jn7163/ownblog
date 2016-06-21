#encoding:utf-8
import os
def changeHTMLstr(string):
    result=''
    for char in string:
        if char=='<':
            result+='&lt;'
        elif char=='>':
            result+='&gt;'
        elif char=='&':
            result+='&amp;'
        elif char=="'":
            result+='&#39;'
        elif char=='"':
            result+='&quot;'                        
        else:
            result+=char
    return result

if os.path.exists('code.txt'):
    code = open('code.txt','r+')
    outcode = open('outcode.txt','w+')
    for string in code:
        outcode.write(changeHTMLstr(string))
    outcode.close()
    code.close()