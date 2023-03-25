import time, os
#Hiệu ứng loading
from time import sleep
while True:
    ns = input("Hôm nay là ngày: \n")
    #Nếu Nhập Đúng
    #thay cả trên này nữa nha cả 2 cái trên và dưới thay giống nhau
    if ns == "20/10/2022":
        print("Chính Xác !!! CHÚC MỪNG NGÀY PHỤ NỮ VIỆT NAM!")
        print("Đến hẹn lại lên, khi ánh nắng chói chang của mùa Hạ nhạt dần, khi tiếng ve không còn râm rang, cây phượng già không còn đốt lửa, khi trong gió thoang thoảng cái se lạnh của chớm đông, là lúc chúng ta cảm nhận được mùa Thu ùa về.")
        print("Trong mùa thu hiền dịu, êm đềm đó chúng ta không khỏi bồi hồi, xúc động hướng đến cái riêng của mỗi chúng ta và là cái chung của cả đất nước, Kỷ niệm ngày  thành lập Hội liên hiệp Phụ nữ Việt Nam (20/10/1930 – 20/10/22), ngày mà cả đất nước Việt Nam dành để tôn vinh người phụ nữ về những thiên chức cao quý.")
        print("Sinh thời Chủ tịch Hồ Chí Minh muôn vàn kính yêu đã nói   “Giang sơn gấm vóc Việt Nam là do phụ nữ Việt Nam, trẻ cũng như già dệt thêu mà thêm tốt đẹp, rực rỡ”. Thật vậy, trong cuộc sống muôn màu, với bộn bề công việc, nhưng chắc hẳn không chỉ riêng ai không tồn tại trong mình một điều kỳ diệu, một thế giới    huyền bí về một dòng tình cảm, một ánh sáng vô hình mà những tia sáng ấy còn trong trẻo, hiền dịu hơn cả ánh trăng, đó chính ánh sáng của tình mẫu tử thiêng liêng, là lòng chung thủy, son sắc của người vợ, hay tình tình yêu tha thiết, mặn nồng của cô gái Việt Nam…")
        print("Lê-nin có nói:Vật chất quyết định ý thức tuy nhiên điều đó chưa chắc hoàn  toàn đúng đối với các cô gái Việt Nam, đâu nhất thiết phải là của cải tiền bạc,  đâu nhất thiết phải là gấm son lụa là, đôi khi chỉ là lời chúc, lời khen cũng đã quyết định được một điều gì đó trong ý thức của người phụ nữ.")
        print("Chúc cô Xuân cùng các bạn nữ lớp mình luôn luôn xinh đẹp, gặp nhiều may mắn và đạt được mọi mong   muốn, luôn giống như mùa xuân: xinh đẹp, dịu dàng và đầy cảm hứng. Mong cho cuộc sống của Cô và các bạn luôn đầy màu sắc và ngọt ngào!Chúc cô Xuân luôn giữ mãi vẻ đẹp tuổi 16 cũng như sự nhiệt tình tuyệt vời của  mình trong những bài giảng.Chúc các bạn nữ luôn duyên dáng, mĩ miều, ngày càng xinh đẹp, học giỏi và đặc biệt hơn là luôn luôn ở trạng thái tuyệt vời  nhất trong đôi mắt nửa còn lại của mình. Chúc Các cô gái của chúng ta nói riêng và tất cả phụ nữ Việt Nam nói chung có một ngày 20/10 tràn đầy niềm vuiiiii!!!<3\
            - Hải l3ùi")
        time.sleep(1)
        #lệnh thoát vòng lặp khi nhập đúng
        break
        #Nếu Nhập Sai
    else:
        ns_2 = input("Bạn nhập sai rồi! -1 tinh tế! Nhập lại nào: \n")
        #các bạn chỉnh ngày sinh tùy ý nhé !
    if ns_2 == "20/10/2022":
        print("Chính Xác !!! CHÚC MỪNG NGÀY PHỤ NỮ VIỆT NAM!")
        print("Đến hẹn lại lên, khi ánh nắng chói chang của mùa Hạ nhạt dần, khi tiếng ve không còn râm rang, cây phượng già không còn đốt lửa, khi trong gió thoang thoảng cái se lạnh của chớm đông, là lúc chúng ta cảm nhận được mùa Thu ùa về.")
        print("Trong mùa thu hiền dịu, êm đềm đó chúng ta không khỏi bồi hồi, xúc động hướng đến cái riêng của mỗi chúng ta và là cái chung của cả đất nước, Kỷ niệm ngày  thành lập Hội liên hiệp Phụ nữ Việt Nam (20/10/1930 – 20/10/22), ngày mà cả đất nước Việt Nam dành để tôn vinh người phụ nữ về những thiên chức cao quý.")
        print("Sinh thời Chủ tịch Hồ Chí Minh muôn vàn kính yêu đã nói   “Giang sơn gấm vóc Việt Nam là do phụ nữ Việt Nam, trẻ cũng như già dệt thêu mà thêm tốt đẹp, rực rỡ”. Thật vậy, trong cuộc sống muôn màu, với bộn bề công việc, nhưng chắc hẳn không chỉ riêng ai không tồn tại trong mình một điều kỳ diệu, một thế giới    huyền bí về một dòng tình cảm, một ánh sáng vô hình mà những tia sáng ấy còn trong trẻo, hiền dịu hơn cả ánh trăng, đó chính ánh sáng của tình mẫu tử thiêng liêng, là lòng chung thủy, son sắc của người vợ, hay tình tình yêu tha thiết, mặn nồng của cô gái Việt Nam…")
        print("Lê-nin có nói:Vật chất quyết định ý thức tuy nhiên điều đó chưa chắc hoàn  toàn đúng đối với các cô gái Việt Nam, đâu nhất thiết phải là của cải tiền bạc,  đâu nhất thiết phải là gấm son lụa là, đôi khi chỉ là lời chúc, lời khen cũng đã quyết định được một điều gì đó trong ý thức của người phụ nữ.")
        print("Chúc cô Xuân cùng các bạn nữ lớp mình luôn luôn xinh đẹp, gặp nhiều may mắn và đạt được mọi mong   muốn, luôn giống như mùa xuân: xinh đẹp, dịu dàng và đầy cảm hứng. Mong cho cuộc sống của Cô và các bạn luôn đầy màu sắc và ngọt ngào!Chúc cô Xuân luôn giữ mãi vẻ đẹp tuổi 16 cũng như sự nhiệt tình tuyệt vời của  mình trong những bài giảng.Chúc các bạn nữ luôn duyên dáng, mĩ miều, ngày càng xinh đẹp, học giỏi và đặc biệt hơn là luôn luôn ở trạng thái tuyệt vời  nhất trong đôi mắt nửa còn lại của mình. Chúc Các cô gái của chúng ta nói riêng và tất cả phụ nữ Việt Nam nói chung có một ngày 20/10 tràn đầy niềm vuiiiii!!!<3\
            - Hải l3ùi")
    else:
        print("Bạn nhập sai rồi ! Thoát")
        exit()
    time.sleep(1)
    #lệnh tiếp tục vòng lặp khi nhập key sai
    break
time.sleep(3)
time.sleep(2)
print("          ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗ ")
print("          ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝ ")
print("          ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗")
print("          ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║")
print("          ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝")
print("          ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ")
print("")             
def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill="█"):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

items = list(range(0, 50))
l = len(items)

loadbar(0, l, prefix='Progress:', suffix='Complete', length=l)
for i, item in enumerate(items):
    sleep(0.1)
    loadbar(i + 1, l, prefix='Progress:', suffix='Complete', length=l)
print("\n")
time.sleep(2)   
#3 cái ngoặc kép nha rồi dán code ascii vừa copy, sau đó đóng 3 ngoặc kép lại
#bây giờ thêm hiệu ứng nha 

string = """

JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ????JJJJJJ????JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYYYYYYYJJYYYYYYYYJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYPPPPJJJJJYPPPPJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ5PPPY?JJJJ5PPPJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYPPP5JJJJJYPPPY?JJJJY55YY555YJJY55PYY5PPYJJJY55PYY5P5YJJY5P5JJJ5P5JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ5PPP5YYYY5PPPPJJJJJ5P5J?YPPPJJJYPPPYJYPPPYJJ5PP5JJ5PPPJJJPPPYJJYP5JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ?YPPPYJJJJJ5PPPYJJJYPP5J?JPPPYJJJPPPJ??JPPPJ?YPPPJJ?YPP5JJ?5PPY??Y5JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJPPP5JJJJJJPPP5JJJJPPPY?J5PP5?JJ5PP5JJJ5PPYJJ5PPYJJJPPPJJJJ5PP5?Y5JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ5PPPYJJJJJPPPPJJJJJPPP5YYPPPYYJYPPPJJJ5P5YJ?YPP5JJJPP5JJJJJYPP5YYJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYY5555YJJJYY5555YJJJJY555JJ555YJJ5PP5YY55JJJJJPPP5YY5YJJJJJJ?YPP5JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ??YPP5JJJJJJJJ?5PPY?JJJJJJJYYJJ55YJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYPPPYJJJJJJJJYPPPYJJJJJJJ5PP5YYJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYYYYYJJJJJJJJYYYYYJJJJJJJJYYJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ?JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ???JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYYYYYYJJJJJJYYYYYYYJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYYYYYJJJJJJYYYYYJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ5PPP5JJJJJJJPPYYPPPJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJPPPP5JJJJJJ5PYJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ?YPPPY?JJJJY5YJ??JYJJJJJJJJJJJJJJJJJ5PJJJJJJJJJJ?Y5YPPP5JJJJJ5Y?JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ5PPPYJJJJ5YJJJY555JJJJJJYYY555JY55PPPYJJJJJJJJJJ5J?YPPP5JJ?Y5JJJJJY55YYY55JJJY555YJY555JJY555JJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ5PPPJ?J55JJJJJ5PP5JJJY5P5JJPPPJJ5PPPJJJJJJJJJJ?55JJJYPPP5?JPJJJJJ5P5J?5PP5JJJYPPPYY5PPPYY5PPPJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ5PPPJY5YJJJJJYPPPJJJ5PP5JYPP5JJJPPPY?JJJJJJJJJJPJJJJJYPPPY5Y?JJYPP5J?JPPPJJJJPPP5YJ5PP5YJ5PP5JJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ5PPP5YJJJJJJJPPPYJJYPPPYYYJJJJJ5PP5?JJJJJJJJJJ5YJJJJJJYPPP5JJJJPPPJ?JPPPY?J?YPPPJ?YPPPJ?YPPPJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJPPPYJJJJJJJJ5PP5JYJ5PPPJJJJYYJJPPPJYJJJJJJJJJY5JJJJJJJJYPPJJJJYPPPYY5PPPYYJJPPPJ?JPPPY?JPPP5YJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ5YJJJJJJJJJJYPP5YJJJ5PPP55YJJJJ5P5YJJJJJJJJYY55YJJJJJJJJ5YJJJJJ5PP5JYPP5YJJY55YJJY55YJJJ555YJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJYYYYYJJJYYYYYJJJJJYYYJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYYYJJJJJJJJJJJJJJJJJJJYYYYYYYJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJJYPPP5JJJYPPP5JJJJJ5PYJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYPPPYJJJJJJJJJJJJJJJJJJJPPPPYY5PP5YJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
JJJJJ?YPPPY?J?YPPPY?JJJ5YJJJJJJJJJJJJJJ?JJJJJJJJJJJJJJJJJJJJJJJJJJ?JJJJJ?JJJJJJJJJJJJJJJYPPY?JJJJ?JJJJJJJJJJJJJPPP5?J?JPPP5JJJJJJJJJJJ?JJJJJJJJJJJJJJJ
JJJJJJ5PPPJ?JYPPPPY?JY5YJJJJYYYY5YJJJJYY55YJY55YJJY555JJJJJJY5YYYY5YJJJYY55JJY55YJJJJJJYY5JJY5YYY5YJJJJJJJJJJJ5PPPJJJJ?5PPP5JJJJJY5YYY55JJYY55JJJY5YJJ
JJJJJJ5PPPJY5Y5PPPJJ5YJJJJ5PPJJJPP5JJJYPPPYY5PPPYY5PPPJJJJYPPYJJPPPYJJJ5PP5YY5PPPJJJJJJYJJJ5PPYJJ55JJJJJJJJJJYPPPY?JJJ?5PPP5JJJ5P5JJ5PP5JJYPPPY?J5PPJJ
JJJJJJPPP5Y5J?5PPPY5JJJJYPPPJJ?YPPPJJJPPP5YJ5PP5YJ5PP5JJJ5PPY??YPP5JJJJPPP5YJ5PP5JJJJJJJJJJ5PPP5JJJJJJJJJJJJJPPP5JJJJJJPPPPY?YPP5J?JPPPJJJ?YPP5JJJ5YJJ
JJJJJJPPPPYJJJPPPPYJJJJJPPPY?JJPPPYJ?YPPPJ?YPPPY?YPPPJJJYPP5?JYPPPJJJJ5PP5J?YPPPJJJJJJJJJJJJY5PPPYJJJJJJJJJJ5PPPJJJJ?J5PPPY?JPPPJ?J5PP5?JJJYPP5?J5YJJJ
JJJJJYPP5JJJJJPP5JJJJJJYPPPJJJ5PPYJJJPPPJ?JPPPY?JPPPYYJJ5PP5JYPPP5JJ?YPP5JJJPPPYYJJJJJJJJY5J?JYPPYJJJJJJJJJYPPP5?JJJYPP5YJJJYPPPYY5PPPJYJJJYPPPY5JJJJJ
JJJJJYPYJJJJJYPYJJJJJJJJYPPYY55YJJJJ5PPYJJYPP5JJJ5P5YJJJYPPP5J5PP5YJJ5PPYJJJ5PPYJJJJJJJJJYP5YYY5YJJJJJJJJYY5PPP5YY555YJJJJJJJ5PP5YYPP5YJJJJJPPPYJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ?YP5JJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJYPP5YYJJJJJJJJJJ
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJY5YJJJJJJJJJJJJ



"""
list_str = string.split()
for i in list_str:
    print(i)
    time.sleep(0.1)