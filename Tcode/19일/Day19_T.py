# # 문제1
# # 텍스트 파일을 이용해서 2004생이 몇명인지 찾아보시오.

# li = ['20181127', '19860303', '20000324', '19750119', '19900407', '19850511', '20090517', '19811214', '20120125', '19920308', '20040610', '19990310', '20171126', '20160727', '19751006', '19920823', '20060103', '20171208', '19990222', '19731206', '19960824', '19970902', '19780714', '19901002', '19970224', '20091107', '19730209', '19890601', '19951003', '20051022', '19770520', '20000206', '19711221', '19820526', '20080413', '20200104', '19780204', '20030524', '20040509', '19800225', '19820327', '20130610', '19880426', '19880421', '19850101', '20011205', '19940326', '20200104', '19750823', '19701226', '20190626', '20150819', '19720626', '19890910', '20081223', '19831028', '19910406', '20160118', '20150823', '20090925', '19970812', '19800123', '20151108', '20020109', '19820414', '19920804', '20000318', '19700717', '20150610', '19840907', '19991110', '20060611', '19891204', '20030319', '19700302', '20051213', '20020216', '20050403', '19831111', '19780720', '20051218', '20000920', '19991121', '19751108', '19941216', '19891023', '20181121', '20080207', '19840818', '20040525', '19961028', '19891121', '20040411', '20121113', '19900508', '20150813', '19880622', '19830312', '20040828', '20060304', '19861025', '19770428', '19940118', '19700809', '20030414', '19951004', '19930421', '20061015', '20160410', '20011022', '19980123', '19920507', '20070602', '19930414', '20181014', '19801105', '19900409', '19850217', '19910712', '19830314', '19960424', '20080223', '19880915', '20131213', '20150724', '20040504', '20120419', '20101202', '19951120', '19851116', '19740314', '20041201', '20060703', '20070407', '20080518', '20050222', '19760416', '20091111', '19761102', '19781024', '20011002', '19750217', '19971113', '19921026', '19860128', '20181227', '19770401', '19830509', '19720417', '19921125', '20010914', '20080105', '19901207', '20020612', '19780906', '20060401', '19880316', '19720521', '20121220', '19700107', '19840804', '19990428', '20100905', '20160817', '19781107', '20000927', '20070525', '20200824', '19990620', '20201125', '20080920', '19720326', '20140925', '20070828', '19711120', '20060227', '20120605', '20181121', '20001209', '20000123', '19991004', '19810918', '19970602', '19990219', '20170603', '19720420', '19910321', '20191010', '19800125', '20171026', '20030717', '19720423', '19780912', '20150603', '19830804', '20140521', '20111010', '20080209', '20160910', '19800926', '20020821', '19990203', '20080224', '19830627', '19781220', '20160815', '19930518', '19751124', '19861121', '19940522', '20040326', '19991007', '20190425', '19760526', '19851219', '20131221', '19740405', '20160524', '19930117', '19730915', '19840323', '19760926', '19780502', '19870209', '20031121', '20140627', '20030201', '20130304', '20170326', '19830320', '19970726', '19850905', '20110127', '19881228', '20080821', '19811106', '19850411', '20171220', '19930306', '19930222', '20121223', '19760414', '19940618', '19840721', '19730118', '19980815', '19700307', '20140311', '20200313', '20070217', '20100706', '19871215', '19770518', '19910114', '20030110', '19850401', '20130923', '20201107', '20041224', '19990706', '20191115', '20040707', '20000110', '19810319', '19870726', '20040405', '19990113', '19790924', '19960817', '20100414', '19920124', '20180705', '20050116', '20130924', '20121023', '19860904', '19750614', '19781023', '19831128', '19790621', '19910106', '19960601', '19700311', '20120802', '19780306', '20030114', '19970615', '19741112', '19800410', '19870923', '19711203', '20200824', '20030415', '19820901', '20000816', '19910224', '20051203', '19990712', '19701224', '19961024', '20081216', '19741103', '19730223', '19750626', '20201118', '20131115', '19850714', '20170906', '20120213', '19820408', '19871103', '20090206', '20160218', '20000201', '19870225', '19971207', '19750317', '19751223', '20110527', '19801128', '20090206', '19911108', '19710224', '20190805', '19820124', '19881210', '19801026', '19800123', '20150112', '20060411', '20090708', '19810628', '19791205', '20190819', '19750926', '19830212', '19971127', '20120712', '20101020', '19901002', '20190321', '19840915', '20050723', '20001213', '19861018', '19940626', '19841008', '19741220', '20080812', '20091204', '20160225', '19741127', '19910610', '20041211', '19900526', '20030514', '20040712', '19951217', '19970427', '19880621', '20130219', '19921003', '19720711', '19970609', '19700101', '20181125', '20190711', '20150313', '20140415', '20061102', '19730406', '19801218', '19860823', '19970205', '20070819', '19850309', '19870804', '19940817', '19850921', '19700801', '19851013', '19710428', '19980109', '20130403', '20190908', '19910504', '20201016', '19890401', '20090915', '20081012', '19711214', '19990617', '19860906', '20050820', '19961011', '19980414', '19750916', '20090127', '20150226', '19811015', '19841218', '19890320', '20051208', '19850216', '19920301', '19700404', '19940223', '19961021', '19851215', '19760902', '19771225', '20070415', '19790604', '20140718', '19920926', '19961101', '19790625', '19790911', '20160801', '19720211', '19810426', '19981201', '20100422', '20011109', '19920904', '20040607', '20130510', '20100922', '19790709', '20070626', '20040324', '20010327', '20180923', '20070628', '19850128', '19720507', '19880513', '19951207', '19991110', '19960905', '20071122', '20071221', '19741018', '20051213', '20091213', '19900505', '19850518', '19720409', '20040526', '19880918', '19970502', '19700922', '19830408', '19730607', '20100202', '19741025', '20060818', '20170602', '19971123', '19860601', '19860906', '20120904', '19920117', '19810603', '20090318', '19770923', '19850117', '19880114', '19850814', '19990509', '20111116', '19920721', '20020822', '19840621', '19930720', '19911006', '19850606', '20170624', '20010424', '19700423', '19721014', '19710219', '19700404', '19701001', '19920724', '19851108', '20010613', '20130816', '20081206', '20200704', '19840309', '19721020', '19861212', '20090502', '20040909', '20051205', '20120719', '20180402', '19940205', '20011117', '19971227', '19881009', '19751228', '19830705', '20030523', '20080507', '19881205', '19961101', '20041209', '19740916', '19970418', '20110928', '20130911', '19791009', '20190628', '19830626', '20131110', '19701118', '19791121', '19880625', '19880211', '20140601', '20121126', '19830407', '19930523', '19760802', '19870605', '20000402', '20190921', '19980722', '19951122', '20160812', '19700620', '19901013', '19880105', '19740502', '19761205', '20000207', '19940605', '19930627', '19780812', '19780221', '19940718', '19880221', '19950810', '20120325', '20100218', '19850322', '20130218', '19870918', '19790818', '20180111', '19730718', '20010522', '20171111', '20010407', '20150628', '19781019', '20050806', '19970802', '19901113', '20091108', '19930211', '19830506', '20121013', '20101127', '20070828', '20110206', '19750123', '20090711', '19760914', '19840322', '19700918', '20050928', '19780928', '19990722', '19880519', '20011022', '19910513', '19701108', '20161214', '20040827', '19751123', '19711212', '20170914', '20170121', '19991204', '19710819', '20140917', '20150917', '19820802', '19830406', '19930507', '20021123', '20150623', '20190911', '19721125', '19800404', '20130125', '20120911', '19710928', '19980327', '20161122', '20150718', '20071122', '20190524', '19890625', '19830728', '19950624', '20070808', '19830909', '19711116', '19700208', '19980823', '19991215', '20180920', '20010727', '19760704', '20100425', '19870704', '19800813', '19871109', '19940206', '20181127', '19790312', '19820505', '20160825', '19910427', '19850916', '20131124', '20160628', '20160217', '20080612', '19910320', '20180104', '20021113', '19980611', '19920109', '19941209', '20161020', '20130223', '19710828', '19810402', '20010225', '19740510', '19810825', '19900320', '19831220', '20061113', '20030224', '19890405', '19980603', '19870124', '20201212', '20060625', '20030909', '20160406', '19741014', '20030902', '20160121', '20110816', '20131223', '19940703', '19880127', '20200526', '19730727', '20190812', '20130708', '19990808', '20160802', '20040312', '19771028', '20090406', '19911201', '20010224', '20130828', '20100514', '19831023', '20091021', '19890212', '20051025', '20170207', '19730822', '19770620', '19710702', '20080108', '20041226', '19850220', '20010505', '19730101', '19830108', '19950714', '20021003', '19960303', '20030827', '20140318', '20061210', '20180713', '20120522', '19780712', '19870320', '19801017', '20071008', '19771002', '20111108', '20111114', '19700523', '20031115', '19990312', '19980228', '20160420', '19760713', '19741125', '19770427', '20151110', '19981219', '20050708', '19861021', '19800117', '19951116', '19971221', '20040514', '19751002', '20120108', '20020919', '20180107', '19960520', '19870227', '19720322', '20161126', '19940626', '19980420', '19971224', '19771224', '20200204', '20020221', '20190328', '19960301', '19970804', '20071201', '20110801', '19810715', '19980913', '20000106', '20020816', '20180813', '19990623', '19790814', '20201021', '20150919', '19800526', '20110319', '19970317', '19960106', '20060117', '20020901', '19940904', '19970326', '19890325', '20140704', '19871201', '19881115', '19820113', '20120316', '20011110', '19730405', '19950106', '19821004', '20080118', '19950509', '19990111', '19720203', '19930824', '19701121', '19740308', '20150916', '20060319', '19931025', '19980308', '19721207', '20140928', '19770225', '19910301', '19890706', '19991005', '20140920', '19891103', '19800221', '20190614', '20100605', '19840106', '20150124', '19781019', '20030711', '19810725', '20201219', '20020616', '19950412', '19710522', '19851213', '20000501', '19801102', '19940423', '19890218', '20070501', '20080217', '20060913', '20200416', '20010304', '20100319', '20150718', '19860419', '19950115', '19820221', '19820715', '20180104', '19801209', '20180628', '19750510', '20000921', '20181018', '19791206', '20140515', '19950902', '20171123', '19920116', '20070304', '19741221', '20160325', '19731204', '19750902', '19751116'
# , '20190703', '19700722', '20101123', '19751101', '20040525', '20070522', '19851116', '20041016', '20190715', '19881225', '19910612', '19720616', '20041106', '20200716', '19970722', '19730708', '19710823', '19730128', '19900819', '20070809', '19820802', '19870416', '19870221', '20121206', '19890411', '19911013', '20110406', '20141101', '19990624', '19761024', '20040627', '19720615', '19960407', '20130220', '20071110', '19800916', '19950916', '19950818', '19990303', '19711006', '19931111', '19720422', '19831128', '19790822', '20030115', '20150320', '19850821', '19811003', '19920604', '19930825', '20090207', '19780313', '19790828', '19751122', '19940906', '19900907', '20020618', '20040420', '20190311', '20200502', '19870727', '20050111', '19750503', '19900518', '19981119', '19760515', '19710104', '19970414', '19810718', '20080316', '19860305', '19720217', '20001124', '20050105', '20131226', '20110501', '19820625', '19990428', '20170214', '20021114', '19980404', '20050710', '20140123', '19870803', '20111119', '20060625', '19770612', '19870416', '20000209', '20080925', '20021220', '19840511', '20090925', '20150517', '19860923', '20151220', '19990801', '20070109', '20150321', '19920605', '19760212', '20091017', '19721215', '19851203', '20040506', '20010220', '19820127', '19761215', '19920523', '20020920', '20070302', '19941005', '19830323', '19741217', '20010519', '19790521', '19791117', '19750511', '19750224', '19930306', '19820213', '19780507', '19830208', '19700208', '20130203', '19711127', '19950109', '20170425', '20170405', '20050505', '19901218', '20020522', '19710921', '20200722', '19860107', '20170525', '19881019', '19710311', '20070910', '19710213', '19960727', '19820801', '19891019', '20060719', '20190919', '19700303', '19950505', '20070214', '20200212', '19970718', '19960425', '19890403', '19870317', '19780805', '20100502', '19930601', '19760401', '19930903', '19861105', '19751223', '19720307', '20040923', '19700228', '19981017', '20020228', '19941224', '20050422', '19820113']

# a = 0
# for i in li:
#     if i[:4] == "2004" :
#         a += 1
# print("2004년생 {} 명".format(a))

# #문제2  
# # 주민등록번호를 이용해서 10명의 남녀 비율(명)을 구하세요.
# li = """170522-4185902
# 010403-4195574
# 860122-1466919
# 900127-2351114
# 961023-1167050
# 150107-4367190
# 050403-3806690
# 140808-3906302
# 980113-1575274
# 101103-4152319
# """

# w,m = 0,0

# for i in li.split("\n"):
#     if i[7] == "1" or i[7] == "3":
#         m += 1
#     elif i[7] == "2" or i[7] == "4":
#         w += 1
# print("남자: {}명\t여자 :{}명".format(m,w))

# #문제3 
# #텍스트 파일을 이용하여 전체 가격의 총합을 구하시오.
# li = [ "715000원", "322000원", "808000원", "70000원", "2000원", "608000원" ,"307000원", "878000원",
# "772000원", "38000원", "829000원", "360000원", "163000원", "148000원", "653000원", "595000원", 
# "134000원", "153000원", "243000원", "542000원", "10000원" ]

# su = 0
# for i in li:
#     # print(i[:-1])
#     su += int(i[:-1])
# print(su)


#함수
# #1. 긴코드 축약

# #선언
# def 인사():
#     print("안녕하세요")
#     print("반갑습니다")
#     print("다시만나요")

# #호출
# 인사()
# 인사()
# 인사()

# #2. 마법의 모자를 만들고 싶을때

# #선언
# def 마법모자(구멍):
#     print(구멍+1)

# #호출
# 마법모자(1)
# 마법모자(100)
# 마법모자(1000)

# # for문 + "안녕하세요" 3번 출력되게 함수 생성
# def 함수1(value,n):
#     for i in range(n):
#         print(value)

# 함수1("안녕하세요",3)

# TypeError 발생

# 함수1("안녕하세요")

#함수1("안녕하세요",3,3)

# #리턴
# a = input("값을 입력해주세요: ")
# print(a)


# #자료 없이 리턴
# #선언
# def 함수리턴1():
#     print("A위치 입니다.")
#     return 
#     print("B위치 입니다.")

# #호출
# print(함수리턴1())


# #자료와 함께 리턴
# # 선언
# def 함수리턴2():
#     return 100

# #호출
# print(함수리턴2())


# #자료없이 리턴후 출력(None)
# def 함수리턴3():
#     return

# #호출
# print(함수리턴3())


# #문제1 (for문)
# 시작 = int(input("수 입력: "))
# 끝 = int(input("수 입력: "))

# a = 0
# for i in range(시작,끝+1):
#     a += i
# print(a)

# #문제2
# def sum_1(시작,끝):
#     a = 0
#     for i in range(시작,끝+1):
#         a += i
#     print(a)

# sum_1(1,10)

# #문제3 (for문 + def + return)

# def sum_1(시작,끝):
#     a = 0
#     for i in range(시작,끝+1):
#         a += i
#     return a

# print(sum_1(1,10))


# #키워드 매개 변수
# def sum_1(시작=1,끝=100,증가=1):
#     a = 0
#     for i in range(시작,끝+1,증가):
#         a += i
#     return a

# print(sum_1())
# print(sum_1(끝=10))

# #문제4
# def 팩토리얼(a):
#     A = 1
#     for i in range(1,a+1):
#         A *= i
#     return A

# print(팩토리얼(5))

# #문제5
# def 약수1(a):
#     for i in range(1,a+1):
#         if a % i == 0:
#             print("{}은 약수 입니다.".format(i))

# 약수1(8)

# #약수 개수 
# def 약수2(a):
#     count = 0
#     for i in range(1,a+1):
#         if a % i == 0:
#             count += 1
#     return count

# print(약수2(8))

# #숙제1

# 1.약수 + 약수개수 = 함수

# 2.(약수 + 약수개수 = 함수) + 리턴








