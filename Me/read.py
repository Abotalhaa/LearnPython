# board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
#
#
# def print_board():
#     print(board[0][0] + '|' + board[0][1] + '|' + board[0][2])
#     print('-+-+-')
#     print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
#     print('-+-+-')
#     print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])
#
#
# def check_win(player):
#     # الفوز في الصفوف
#     if board[0][0] == player and board[0][1] == player and board[0][2] == player:
#         return True
#     if board[1][0] == player and board[1][1] == player and board[1][2] == player:
#         return True
#     if board[2][0] == player and board[2][1] == player and board[2][2] == player:
#         return True
#
#     # الفوز في الأعمدة
#     if board[0][0] == player and board[1][0] == player and board[2][0] == player:
#         return True
#     if board[0][1] == player and board[1][1] == player and board[2][1] == player:
#         return True
#     if board[0][2] == player and board[1][2] == player and board[2][2] == player:
#         return True
#
#     # الفوز في القطرين
#     if board[0][0] == player and board[1][1] == player and board[2][2] == player:
#         return True
#     if board[0][2] == player and board[1][1] == player and board[2][0] == player:
#         return True
#
#     # لم يفز اللاعب
#     return False
#
#
# print_board()
# current_player = 'X'
# while True:
#     print('Player', current_player, 'turn.')
#     row = int(input('Enter row (0-2): '))
#     col = int(input('Enter col (0-2): '))
#
#     # التحقق من صحة الخانة التي اختارها اللاعب
#     if board[row][col] != ' ':
#         print('Invalid move - space already taken!')
#         continue
#     else:
#         board[row][col] = current_player
#         print_board()
#
#     # التحقق من فوز اللاعب الحالي
#     if check_win(current_player):
#         print('Player', current_player, 'wins!')
#         break
#
#     # التحقق من التعادل
#     if ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
#         print('Draw!')
#         break
#
#     # تغيير اللاعب الحالي
#     if current_player == 'X':
#         current_player = 'O'
#     else:
#         current_player = 'X'
#
# # this is dirty
# -------------------------------------------------------------------
from gtts import gTTS
import os

# النص العربي
text = "مرحبًا بالعالم"

# تحويل النص إلى نطق باللغة الإنجليزية
tts = gTTS(text, lang='en')
tts.save("hello.mp3")

# تشغيل ملف الصوت
os.system("mpg321 hello.mp3")
