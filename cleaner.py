import re

INPUT_FILE_NAME='output.txt'
OUTPUT_FILE_NAME='output_cleaned.txt'

# cleaning func
def clean_text(text):
  cleaned_text = re.sub('[a-zA-z]', '', text)
  cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', cleaned_text)
  return cleaned_text

# main func
def main():
  read_file=open(INPUT_FILE_NAME,'r',encoding='UTF-8')
  write_file=open(OUTPUT_FILE_NAME,'w',encoding='UTF-8')
  text = read_file.read()
  text = clean_text(text)
  write_file.write(text)
  read_file.close()
  write_file.close()


if __name__=='__main__':
  main()