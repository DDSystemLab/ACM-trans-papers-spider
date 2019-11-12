# ACM-trans-papers-spider
 This is an interoperational net spider program to get a list of papers (e.g., title and doi link) from the repository of ACM transations journal papers.

Running environment(Pthon 3.6.5 with the following libraries): requests, os, re, bs4

Steps:
1. Get the Python file ACMPaperSpider.py

2. Run it in terminal with python ACMPaperSpider.py

3. Enter a start url and the file name for storing papers list, or quit to exit the program. Then you will get a list of papers from that ACM transactions journal.

For example, if we want to get papers from the journal "ACM Transactions on Modeling and Performance Evaluation of Computing Systems (TOMPECS)", use the start url: https://dlnext.acm.org/toc/tompecs/2016/1/1 to start our search. Since PyCharm IDE currently has the problem of "Pressing return key after inputting a URL in console causes PyCharm to launch the browser", it is recommended to use terminal rather than the PyCharm IDE.
