#
# hw2pr1.py - write-your-own-web-engine...
#
# then, improve the page's content and styling!
#


import re
from copy import deepcopy

def subtract(a, b):
    return "".join(a.split(b)[1:])

def apply_headers( OriginalLines ):
    """ should apply headers, h1-h5, as tags
    """
    # loop for all headings: h1-h5

    html_head = [("<h1>","</h1>"),("<h2>","</h2>"),("<h3>","</h3>"),("<h4>","</h4>"),("<h5>","</h5>")]
    md_head = ["#","##","###","####","#####"]

    NewLines =[]
    for line in OriginalLines:
        for head in md_head:
            if line.split(" ")[0]==head:
                line = html_head[md_head.index(head)][0] + subtract(line,head) + html_head[md_head.index(head)][1]
        # if line.startswith("#"):
        #     line = "<h1>" + line[1:] + "</h1>"

        NewLines += [ line ]


    return NewLines

def apply_wordstyling( OriginalLines ):
    """ should apply wordstyling here...
    """
    # loop for the word-stylings: here, ~word~
    NewLines =[]
    for line in OriginalLines:
        # regular expression example!
        line = re.sub(r"~(.*)~", r"<i>\1</i>", line)
        line = re.sub(r"[*](.*)[*]",r"<b>\1</b>",line)
        line = re.sub(r"[_](.*)[_]",r"<u>\1</u>",line)
        line = re.sub(r"[@](.*)[@]",r"<a href=\1> Link </a>",line)
        if "color:" in line:
            line = re.sub(r"color:(.*):",r"<font color =\1>",line)
            line += "</font>"
        # let's practice some others...!
        # regular expressions:  https://docs.python.org/3.4/library/re.html
        NewLines += [ line ]
    return NewLines
    # Your task: add at least
    #   *bold*
    #   @link@  (extra: use a regular expression to match a link!)
    #   _underscore_
    #   extra-credit!  BLINKING (working!) or strikethrough
    #   remember for many special symbols, you need to "backslash" them...


def listify(OriginalLines):
    """ convert lists beginning with "   +" into HTML """
    NewLines = []
    list_start = True
    # loop for lists
    for line in OriginalLines:
        if line.startswith("   +"):
            if list_start == True:
                NewLines.append("<ul>")
                list_start = False
            NewLines.append("<li>"+ line[4:] +"</li>")
        else:
            if list_start == False:
                NewLines.append('</ul>')
                list_start = True
            NewLines.append(line)

            # line = "<ul>\n<li>" + line[4:] + "</li>\n</ul>"
        # note - this is wrong: your challenge: fix it!
    return NewLines



def main():
    """ handles the conversion from the human-typed file to the HTML output """

    HUMAN_FILENAME = "starter.txt"
    OUTPUT_FILENAME = "starter.html"

    f = open(HUMAN_FILENAME, "r", encoding="latin1")
    contents = f.read()
    f.close()

    print("Original contents were\n", contents, "\n")

    OriginalLines = contents.split("\n")  # split to create a list of lines
    NewLines = apply_headers( OriginalLines )
    NewLines = apply_wordstyling(NewLines)
    NewLines = listify(NewLines)

    # finally, we join everything with newlines...
    final_html = '\n'.join(NewLines)

    print("\nFinal contents are\n", final_html, "\n")

    f = open(OUTPUT_FILENAME, "w")     # write this out to a file...
    f.write( final_html )
    f.close()
    # then, render in your browser...


if __name__ == "__main__":
    main()
