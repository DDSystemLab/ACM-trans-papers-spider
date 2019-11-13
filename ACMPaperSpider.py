import requests
import os
import re
from bs4 import BeautifulSoup


class PaperSpider:
    papers_order = 1

    def __init__(self, name, url="https://dlnext.acm.org/toc/tompecs/2016/1/1", filename="ACM_papers_list.txt"):
        self.name = name
        self.url = url
        self.filename = filename

    def get_html(self, url):
        try:
            headers = {"User-Agent": "Safari/12.1.2"}
            r = requests.get(url, headers=headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            # delete all blank lines
            html = os.linesep.join([s for s in r.text.splitlines() if s])
            return html
        except:
            return ""

    def parse_page(self, html):
        try:
            current_issue_papers = []
            soup = BeautifulSoup(html, 'html.parser')
            title_boxes = soup.findAll('h5', attrs={'class': 'issue-item__title'})
            for title_box in title_boxes:
                title = title_box.text.strip()
                title = re.sub(' +', ' ', title).strip()
                title = re.sub('\n', ' ', title).strip()
                if title == "List of Reviewers":
                    continue
                doi_num = str(title_box).split("/doi/abs", 1)[1].split("\">", 1)[0]
                doi_link = "https://doi.org" + doi_num
                pair = [doi_link, title]
                current_issue_papers.append(pair)
            print(current_issue_papers)
            self.store_paper_info(current_issue_papers)
            next_box = soup.find('a', attrs={'class': 'content-navigation__btn--next'})
            if next_box['href'] == "javascript:void(0)":
                return ""
            next_link = "https://dlnext.acm.org" + next_box['href']
            next_html = self.get_html(next_link)
            self.parse_page(next_html)
        except:
            return ""

    def store_paper_info(self, current_issue_papers):
        try:
            for pair in current_issue_papers:
                paper_title = pair[1]
                doi_link = pair[0]
                with open(self.filename, "a") as f:
                    f.write(
                        "paper%s\nTitle：%s\nDoi_link：%s\n" % (self.papers_order, paper_title, doi_link))

                    f.write("==========================\n")
                self.papers_order += 1
        except:
            return ""


if __name__ == '__main__':
    run = True
    while run:
        print("Welcome to use the ACM Transactions journal papers Spider!")
        start_url = input("Enter a start url or quit: ")
        if start_url == 'quit':
            print("Goodbye, human!")
            run = False
            break
        file_name = input("Enter a filename (e.g., ACM_papers_list.txt) or quit: ")
        if file_name == 'quit':
            print("Goodbye, human!")
            run = False
            break
        acmPerfModel = PaperSpider("acmPerfModel", start_url, file_name)
        html_result = acmPerfModel.get_html(start_url)
        acmPerfModel.parse_page(html_result)