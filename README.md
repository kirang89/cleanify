#Cleanify

##Overview

A bot that beautifies html, js and css files inside your project.

Everyone may not have beautifier plugins installed in their editor. So sometimes code written may be
messy. And it's a pain to beautify all your files in one go. Cleanify solves that problem by allowing u to clean all your web files right from the command
line.

What's even better ? Cleanify **asynchronously** cleans up your files, so it's fast, even for large projects.

##Installation

First install dependencies. To do that run 

<pre><code>pip install -r requirements.txt</code></pre>

If you do not have the js-beautifier module for python installed, run ```./install_jsbeautifier.sh```

##Running
<pre><code>python cleanify.py /path/to/dir</code></pre>

##Contributing

No code is perfect, so feel free to send me a pull request or create a git issue :)

##License
http://www.tldrlegal.com/l/WTFPL
