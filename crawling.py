from bs4 import BeautifulSoup
import urllib.request

OUTPUT_FILE_NAME='output.txt'
URL='https://n.news.naver.com/mnews/article/055/null?sid=103/&aid=0000445667'

# crawler func
def get_text(URL):
  source_code_from_URL = urllib.request.urlopen(URL)
  soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='UTF-8')
  text=''
  for item in soup.find_all('div', id='contents'):
    text = text+str(item.find_all(text=True))
  return text

# main func
def main():
  open_output_file=open(OUTPUT_FILE_NAME, 'w',encoding='UTF-8')
  result_text=get_text(URL)
  open_output_file.write(result_text)
  open_output_file.close()

if __name__=='__main__':
  main()