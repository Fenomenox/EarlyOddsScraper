from selenium import webdriver
from lxml import html
import xlsxwriter
import re

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook(r'体球网盘口.xlsx')


Results = {'英超': {}, '西甲': {}, '德甲': {}, '意甲': {}, '法甲': {},
           '英冠': {}, '西乙': {}, '德乙': {}, '意乙': {}, '法乙': {},
           '日职业': {}, '俄超': {}, '芬超': {}, '土超': {}, '荷乙': {},
           '葡超': {}
           }
dv = webdriver.Chrome()
for i in range(0, 7):
    URL = 'http://www.spbo1.com/cend%d.htm' % i
    dv.get(URL)

    doc = html.fromstring(dv.page_source)
    all_games = doc.xpath('//*[@id="end"]/table/tbody/tr')
    for game in all_games:
        cells = game.xpath('./td')
        if len(cells) < 6:
            continue
        league = cells[0].text_content()
        date = cells[1].text_content()
        completion = cells[2].text_content()
        home = cells[3].xpath('./a')
        away = cells[5].xpath('./a')
        score = cells[4].text_content()
        onclick = cells[9].get('onclick')
        link = re.split("'", str(onclick), 2)
        if len(link) < 2 or completion != '完':
            continue
        if league in Results:
            print(league, date, completion, home[0].text_content(), score, away[0].text_content())
            link = link[1]
            #print(link)
            Results[league][link] = {
                'date': date,
                'home': home[0].text_content(),
                'away': away[0].text_content(),
                'score': score
            }


for league, matches in Results.items():
    ws = workbook.add_worksheet(league)
    ws.set_column(0, 16000, 13)

    column = 0
    for link, stats in matches.items():
        row = 1

        title = '%s\n%s\n%s' % (stats['home'], stats['score'], stats['away'])
        ws.write(0, column, stats['date'])
        ws.write(0, column + 1, title)

        dv.get(link)
        link_doc = html.fromstring(dv.page_source)
        table_rows = link_doc.xpath('//*[@id="plls"]/table/tbody/tr')
        for r in table_rows:
            cells = r.xpath('./td')
            t = cells[0].text_content()
            content = '%s\n%s\n%s' % (cells[3].text_content(), cells[2].text_content(), cells[4].text_content())
            # print(cells[0].text_content(), cells[2].text_content(), cells[3].text_content(), cells[4].text_content())
            if '/' in t and 'H' not in t:
                ws.write(row, column, t)
                ws.write(row, column+1, content)
                row += 1

        column += 4
workbook.close()

dv.close()
