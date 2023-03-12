def drawBoard(board):
    # تستقبل الدالة تحركات اللاعبين كقائمة وتقوم بطباعتها على شكل لوح لعبة إكس أوُ
    # يتم تخزين التحركات في القائمة بدأً من الخانة 1 وليس 0 لسهولة استرجاع البيانات
    # في كل خانة في القائمة المستلمة يمكن أن نجد قيمة إكس أو قيمة أوُ أو خانة خالية

    # print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    # print('   |   |')
    # print('-----------')
    # print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    # print('   |   |')
    # print('-----------')
    # print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    # print('   |   |')


def inputPlayerLetter():
    # X or O تمكّن اللاعب من اختيار الحرف المرغوب
    # تقوم الدالة بتمرير
    # قيمتين بحيث يتغير الترتيب بناءً على اختيار اللاعب. إذا اختار اللاعب حرف إكس يكون الأول في القائمة وهكذا
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # القيمة الآولى حرف اللاعب والقيمة الثانية حرف الآلة
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


import random


def whoGoesFirst():
    # Random يتم اختيار صاحب الدور الأول عشوائيا عن طريق تطويع الدال الرياضية

    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    # تقوم هذه الدالة بتمرير قيمة منطقية (صائب أو خطأ) بناءً على اختيار اللاعب في بدء جولة جديدة

    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    # يتم تمرير محتويات اللوح الحالية والحرف المنتمي للاعب إلى الدالة
    # كل سطر يتحقق من أحد حالات الفوز الثمانية والشرط هو تحقيق أحد تلك الحالات لتمرير قيمة (صائب

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def isSpaceFree(board, move):
    # تقوم الدالة بتمرير القيمة المنطقية (صائب) في حال كانت الخانة المطلوبة شاغرة

    return board[move] == ' '


def getPlayerMove(board):
    move = ' '
    # لطالما أن المستخدم لم يقم بادخال قيمة تستوفي الشروط، يستمر البرنامج في السؤال عن الحركة التالية
    # الشروط هي:
    # 1. يجب أن تكون القيمة المدخلة أحد قيم خانات اللوح من 1 إلى 9
    # 2. يجب أن تكون الخانة شاغرة
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    # في حال قام المستخدم بادخال قيمة صالحة تقوم الدالة بتمرير القيمة
    return int(move)


def getComputerMove(board, computerLetter):
    # بناءً على حرف الآلة الذي تستلمه الدالة فإنها تقوم بتعريف متغير لحرف اللاعب كالتالي
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Tic Tac Toe AI خوارزمية الذكاء الاصطناعي :
    # أولاً تتحق الآلة من إمكانية الفوز في حركة واحدة وتحتل الخانة اللازمة للفوز
    # ----------------------(1)-----------------------------
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    # ----------------------(1)-----------------------------

    # تتحقق الآلة من إمكانية اللاعب من الفوز في حركة واحدة ومنعه عن طريق احتلال الخانة
    # ----------------------(2)-----------------------------
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    # ----------------------(2)-----------------------------

    # تحاول الآلة احتلال أحد الأركان في حال كان شاغر
    # ----------------------(3)-----------------------------
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    # ----------------------(3)-----------------------------

    # تحاول الآلة احتلات خانة المنتصف في حال لازالت شاغرة
    # ----------------------(4)-----------------------------
    if isSpaceFree(board, 5):
        return 5
    # ----------------------(4)-----------------------------

    # في محاولة أخيرة تقوم الآلة باختيار خانة عشوائية من الخانات المتبقية
    # ----------------------(5)-----------------------------
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
    # ----------------------(5)-----------------------------


def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


# Play XO
# الترحيب باللاعب قبل بدأ الجولة
print('Welcome to XO!')

# while loophole الجولة هنا وتنتهي متى ما اختار اللاعب إنهاء الجولات عن طريق الخروج المباشر من ال
while True:
    # نقوم في بداية كل جولة بمسح التحركات من على اللوح وتعيين قيمة مسافة خالية لكل خانة
    # نعين عشر خانات للقائمة ونتجاهل الخانة ذات المؤشر 0 بحيث تمثل كل خانة من التسع الباقية خانات اللوح

    #    7 | 8 | 9
    #   ---+---+---
    #    4 | 5 | 6
    #   ---+---+---
    #    1 | 2 | 3

    theBoard = [' '] * 10

    # عند استدعاء دالة ادخال اللاعب للحرف المرغوب فإن الدالة تمرر قيمتين: حرف اللاعب وحرف الآلة
    playerLetter, computerLetter = inputPlayerLetter()
    # يتم اختيار صاحب الدور الأول عشوائياً
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    # لطالما أن الجولة قائمة ولم تنتهي بالتعادل أو فوز أحد اللاعبين
    while gameIsPlaying:
        count = 0
        if turn == 'player':
            # في حال بدء دور اللاعب
            # يتم رسم اللوح
            drawBoard(theBoard)
            # يُسأل اللاعب عن الخانة المراد احتلالها
            move = getPlayerMove(theBoard)
            # يتم تخزين حركة اللاعب على اللوح
            makeMove(theBoard, playerLetter, move)

            # نتحقق مما إذا فاز اللاعب
            if isWinner(theBoard, playerLetter):
                # يتم رسم اللوح وإعلام اللاعب بفوزه وإنهاء الجولة الحالية
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                # إذا تأكدنا من عدم فوز اللاعب يأتي دور التحقق من التعادل في حال كان اكتمال اللوح
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    # ما لم يفز اللاعب ولم يتحقق التعادل بعد، ينتقل الدور إلى الآلة
                    turn = 'computer'

        else:
            # في حال بدء دور الآلة
            # نستدعي منطق الآلة مع تمرير اللوح الحالي ونستلم الحركة التي اختارتها الآلة بناءً على المنطق المذكور سابقاً
            move = getComputerMove(theBoard, computerLetter)
            # نقوم بتخزين حركة الآلة على اللوح
            makeMove(theBoard, computerLetter, move)

            # نتحقق مما إذا فاز اللاعب
            if isWinner(theBoard, computerLetter):
                # يتم رسم اللوح وإعلام اللاعب بخسارته وإنهاء الجولة الحالية
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                # إذا تأكدنا من عدم فوز الآلة يأتي دور التحقق من التعادل في حال اكتمال اللوح
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    # ما لم يخسر اللاعب ولم يتحقق التعادل، ينتقل الدور إلى اللاعب
                    turn = 'player'

    # في حالة إنتهاء الجولة يتم سؤال اللاعب عما إذا كان يريد بدء جولة جديدة
    # في حالة الرفض يتم إنهاء اللعبة
    if not playAgain():
        break

