import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import cloudscraper

def web_pdf_gather(url):
    # PDFファイルを保存するディレクトリ
    
    os.makedirs(output_dir, exist_ok=True)
    scraper = cloudscraper.create_scraper()  
    # WebページのHTMLを取得

    response = scraper.get(url)
    print(response)
    soup = BeautifulSoup(response.content, "html.parser")

    # PDFリンクをすべて取得
    pdf_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        
        if href.endswith('.pdf'):
            # 絶対URLに変換
            full_url = urljoin(url, href)
            pdf_links.append(full_url)

    # PDFファイルをダウンロード
    for pdf_url in pdf_links:
        pdf_response = requests.get(pdf_url)
        file_name = os.path.join(output_dir, pdf_url.split("/")[-1])

        with open(file_name, 'wb') as f:
            f.write(pdf_response.content)
        
        print(f"{file_name} をダウンロードしました")

    print("すべてのPDFをダウンロードしました")

def pdf_to_string(folder_path):
 # folder_path: PDFファイルが保存されているディレクトリ   

    output_dir = "txt_files"
    os.makedirs(output_dir, exist_ok=True)
    # 指定フォルダ内のPDFファイルをすべて取得
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    
    # 各PDFファイルからテキストを抽出
    for pdf_file in pdf_files:
        pdf_path = folder_path + "\\" + pdf_file
        print(f"ファイル: {pdf_file} からテキストを抽出中...")
        print(pdf_path)
        # PDFを開いてテキストを抽出
        with pdfplumber.open(pdf_path) as pdf:
            all_text = ""
            for page in pdf.pages:
                all_text += page.extract_text()

        # 抽出したテキストを表示
        print(f"抽出したテキスト:\n{all_text}\n")

        # 必要ならテキストをファイルに保存する場合
        output_text_file = os.path.join(output_dir, pdf_file.replace('.pdf', '.txt'))
        with open(output_text_file, 'w', encoding='utf-8') as f:
            f.write(all_text)
        
        print(f"{pdf_file} のテキストが {output_text_file} に保存されました。\n")

def find_folder(search_string,folder_path):

    # フォルダ内のすべてのテキストファイルを検索
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                print(f"ファイル: {file_path}")
                
                # テキストファイルを開いて検索
                with open(file_path, 'r', encoding='utf-8') as f:
                    for i, line in enumerate(f, start=1):
                        if search_string in line:
                            print(f"行 {i}: {line.strip()}")

    print("検索が終了しました。")

url = "https://www.mod.go.jp/j/press/jinji/"
output_dir_pdf = "pdf_folder"

search_str = "２等陸佐　相　馬"
years = ("2021/index.html","2022/index.html", "2023/index.html", "2024/index.html")
for year in years:
    now_url = url + year
    print("now_url:" + now_url )

    web_pdf_gather(now_url,output_dir_pdf)
    pdf_to_string(output_dir_pdf)
    search_string(search_str)

    print("------------------------------------------------------------------------")
