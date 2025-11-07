# from html.parser import HTMLParser

from bs4 import BeautifulSoup
import re

# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
#         print("Encountered a start tag: ", tag)
#         # return super().handle_starttag(tag, attrs)
    
#     def handle_endtag(self, tag: str):
#         print("Encountered an end tag: ", tag)
#         # return super().handle_endtag(tag)
    
#     def handle_data(self, data: str):
#         print("Encountered some data  :", data)
#         # return super().handle_data(data)

class Team:
    teams_count = 0
    def __init__(self, name, wins, losses, pointsScored):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.pointsScored = pointsScored
        Team.teams_count += 1

hornets = Team("Hornets", 0,0,0)

def parseHtmlFile(fileName: str):
    with open(fileName, 'r') as file:
        content  = file.read()
        soup = BeautifulSoup(content, 'html.parser')

        # Finding an anchor tag containing the text "Geeks For Geeks"
        # anchor_tag = soup.find('td', string='Pre-K/K Raptors')

        all_rows = soup.find_all('td')
        # print(anchor_tag_all)
        print(len(all_rows))

        for x in all_rows:
            print(x)
            # if '7th/8th Grade Hornets' in x:
            if "Hornets (" in x.string:
                res = re.findall(r"\(\s*\+?(-?\d+)\s*\)", x.string)
                hornets.pointsScored += int(res[0])
                print(x)



        # parseHtml(coedHtml)
        
# def parseHtml(rawHtml: str):
#     parser = MyHTMLParser()
#     # parser.feed('<html><head><title>Test</title></head>'
#     #             '<body><h1>Parse me!</h1></body></html>')
#     parser.feed(rawHtml)

def main():
    parseHtmlFile('dev_league_schedule_standings_coed.html')

if __name__ == "__main__":
    main()
