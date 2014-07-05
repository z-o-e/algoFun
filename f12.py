"""
Implement a method called printNonComments() which prints out a extract of text with comments removed. 

For example, the input: 

hello /* this is a 
multi line comment */ all 

Should produce: 

hello 
all 


You have access to a method called getNextLine() which returns the next line in the input string.

"""

def printNonComments(lines):
    isComment = False
    
    for l in lines.getNextLine():
        for i in range(len(l)):
            printLine = ""
            if not isComment:
                if ( i<len(l)-1 and l[i]=="/" and l[i+1]=="*"):
                    isComment = True
                    i += 1
                else:
                    printLine += l[i]

            else:
                if ( i<len(l)-1 and l[i]=="*" and l[i+1]=="/"):
                    isComment = False
                    i += 1
                
        print printLine
        
    return
                
                