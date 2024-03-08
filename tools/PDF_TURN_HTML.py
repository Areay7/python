from pdf2image import convert_from_path
import pdf2txt
from bs4 import BeautifulSoup
import sys

# 1. 使用pdf2image库将PDF转换为图像
def pdf_to_images(pdf_file):
    return convert_from_path(pdf_file)

# 2. 使用pdf2txt库提取PDF文本
def pdf_to_text(pdf_file):
    pdf2txt.main(['pdf2txt.py', pdf_file, '-o', 'output.txt'])

# 3. 将PDF文本渲染成HTML页面
def text_to_html(text_file, html_file):
    with open(text_file, 'r', encoding='utf-8') as file:
        pdf_text = file.read()

    # 创建HTML页面
    html = f'<html><body>{pdf_text}</body></html>'

    # 使用Beautiful Soup来格式化HTML
    soup = BeautifulSoup(html, 'html.parser')
    formatted_html = soup.prettify()

    # 保存HTML文件
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(formatted_html)

def main():
    # if len(sys.argv) != 3:
    #     print("Usage: python pdf_to_html.py input_pdf_file output_html_file")
    #     sys.exit(1)

    input_pdf_file = "output.txt"
    output_html_file = "output.html"

    # 依次执行转换步骤
    # images = pdf_to_images(input_pdf_file)
    # pdf_to_text(input_pdf_file)
    text_to_html('output.txt', output_html_file)

    print(f'PDF转换完成，HTML文件已保存为 {output_html_file}')

if __name__ == "__main__":
    main()
