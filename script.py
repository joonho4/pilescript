import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.youtube.com/watch?v=vAoYovtIuTM" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["red", "pink"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "박준호")
write("description", "중학생")
write("button", "애니")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "생년월일": "20070501",
  "성별": "남",
  "주소": "대구광역시달서구파도고개로 22",
  "출생지": "대구"
}
information(informations)
