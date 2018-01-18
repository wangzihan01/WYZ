'''
首先需要先登录或者注册
'''
print('服务系统为你服务')
print('~'*30)
list_list = [{'name':'pass','passwd':'pass'}]
# 初始列表不可以空

while True:
	print('~'*30)
	print('1、登录','2、注册','3、退出')
	denglu_zhuce = int(input('请输入您所选择的功能序号'))
	
	def zhuce():
		# 创建一个函数
		name = input('输入您要注册的账户名')
		list_zhanghao = []
	  # 循环列表	
		for dictionary in list_list:
			# 将字典中健为name的值添加到列表中
			list_zhanghao.append(dictionary['name']) 
		if name in list_zhanghao:
			print('帐号已存在，请登录')
		elif name not in list_zhanghao:
			passwd = input('请输入您要注册的密码')
			# 创建的帐号密码保存到一个空字典中然后保存到list_list当中
			dic = {}
			dic['name'] = name
			dic['passwd'] = passwd
			list_list.append(dic)
			print('注册成功')
	# 登录
	def denglu():
		name = input('输入您的帐号')
		
		for dictionary in list_list:
			list_zhanghao = []
			list_zhanghao.append(dictionary['name'])
		if name not in list_zhanghao:
			print('没有这个帐号，请先注册')
		elif name in list_zhanghao:
			pswd = input('请输入密码')
			i = 0
			length = len(list_list)
			dic = {}
			while i <= length -1:
				dic = list_list[i] 
				if dic['name'] == name:
					zmima = dic['passwd']
					break
				else:
					i += 1
					dic = {}
			if pswd == zmima:
				print('欢迎登录')


			while True:
				print('*'*40)
				print('1、看电影，2、买车子 3、租房子,4、抓娃娃,5、ATM取款,6、返回上级')	
				denglu_zhuce = int(input('请输入上方的功能序号'))
				if denglu_zhuce == 1:
					print('本次电影有\n1、喜剧\n2、科幻\n3、恐怖\n4、灾难')
					name = int(input('请问您要看什么类型'))
					if name == 1:
						print('1、分手大师\n2、惊声尖笑\n3、喜剧之王')
						xi_ju = int(input('请问您要看什么喜剧'))
						if xi_ju == 1:
							print('分手大师:9:30分开始，请走第一号影房032座')
						elif xi_ju == 2:
							print('惊声尖笑:9:45分开始，请走第二号影房047座')
						elif xi_ju == 3:
							print('喜剧之王:10:00分开始,请走第三号影房101座')
					elif name == 2:
						print('1、超体\n2、变形金刚\n3、生化危机')
						ke_huan = int(input('请输入科幻电影名称'))
						if ke_huan == 1:
							print('超体:12:10分开始，请走四号影厅123座')
						elif ke_huan == 2:
							print('变形金刚:13:00分开始，请走五号影厅302座') 
						elif ke_huan == 3:
							print('生化危机:14:00分开始,请走六号影厅072座')
					elif name == 3:
						print('1、僵尸大战葫芦娃\n2、惊声尖叫\n3、死神来了')
						kong_bu = int(input('请输入恐怖电影名称'))
						if kong_bu == 1:
							print('僵尸大战葫芦哇:17:30分开始，请走七号影厅056座')
						elif kong_bu == 2:
							print('惊声尖叫:21:00分开始，请走八号影厅015座')
						elif kong_bu == 3:
							print('死神来了:22:00分开始,请走第八号影厅104座')
					elif name == 4:
						print('1、海啸\n2、猩球崛起\n3、丧尸黎明')
						zai_nan = int(input('输入灾难电影名称'))
						if zai_nan == 1:
							print('海啸: 15:30分开始，请走十二影厅032座')
						elif zai_nan == 2:
							print('猩球崛起:16:45分开始,请走十三影厅120座')
						elif zai_nan == 3:
							print('丧尸黎明:20:00分开始,请走十四影厅105座')
						else:
							print('没有')
				if denglu_zhuce == 2:
					print('车子的分类:\n1、豪车\n2、垃圾车\n')
					car = int(input('请问要什么类型的车子'))
					if car == 1:
						qian =500000000
						msld = 3200000
						lbjn = 5000000
						bl   = 2600000
						lh   = 1750000
						hm   = 6660000
						bjdwl= 10000000
						lsls = 20000000
						print('1、玛莎拉蒂    ￥3200000\n2、兰博基尼    ￥5000000\n3、宾利        ￥2600000\n4、路虎        ￥1750000\n5、悍马        ￥6660000\n6、布加迪威龙  ￥10000000\n7、劳斯莱斯    ￥20000000')
						car_car = int(input('请问想要什么车子呢？'))
						if car_car == 1:
							gou_mai = int(input('请付钱'))
							if gou_mai >= msld < qian:
								print('您已购买玛莎拉蒂:')
								print('~'*40)
								print('   像风一样出其不意')
								print('                 ——玛莎拉蒂')
							else:
								print('您的钱不够，下次在来吧')	
						elif car_car == 2:
							gou_mai = int(input('请付钱'))
							if gou_mai >= lbjn < qian:
								print('~'*40)
								print('您已购买兰博基尼:')
								print('   我习惯别人看我的尾灯')
								print('                     ——兰博基尼')
							else:
								print('您的钱不够，下次在来吧')
						elif car_car == 3:
							gou_mai = int(input('请付钱'))
							if gou_mai >= bl < qian:
								print('~'*40)
								print('您已购买宾利:')
								print('   两个座椅，决定一个世界')
								print('                       ——宾利')
							else:
								print('您的钱不够，下次再来吧')
						elif car_car == 4:
							gou_mai = int(input('请付钱'))
							if gou_mai >= lh < qian:
								print('~'*40)
								print('您已购买路虎:')
								print('   尊贵，上无止境.巅峰,从此入境')
								print('                             ——路虎')
							else:
								print('您的钱不够，下次再来吧')
						elif car_car == 5:
							gou_mai = int(input('请付钱'))
							if gou_mai >= hm < qian:
								print('~'*40)
								print('您已购买悍马:')
								print('   路的尽头，是悍马的起点')
								print('                       ——悍马')
							else:
								print('您的钱不够，下次再来吧')
						elif car_car == 6:
							gou_mai = int(input('请付钱'))
							if gou_mai >= bjdwl < qian:
								print('~'*40)
								print('您已购买布加迪威龙')
								print('   集合所有激情的传说')
								print('                   ——布加迪威龙')
							else:
								print('您的钱不够，下次再来吧')
						elif car_car == 7:
							gou_mai = int(input('请付钱'))
							if gou_mai >= lsls <qian:
								print('~'*40)
								print('您已够买劳斯莱斯')
								print('   开到60迈的公路上，唯一的噪音来自于他的电子表')
								print('                                             ——劳斯莱斯')
							else:
								print('您的钱不够，下次再来吧')
					elif car == 2:
						print('不是侮辱您，垃圾车我们不卖')
					
				if denglu_zhuce == 3:
					print('房子的价位:\n￥100,000\n￥300,000\n￥800,000\n￥200,000,0')
					money = int(input('请问您有多少钱?'))
					if money == 100000 or money <= 300000:
						print('您可以租4环半年的房费')
					elif money == 300000 or money <= 800000:
						print('您可以租二环的一年房费')
					elif money == 800000 or money <= 2000000:
						print('可以买房了为什么还要租？')
					elif money < 100000:
						print('别待了 住马路吧')
				if denglu_zhuce == 4:
					for i in range(0,5): 
						num = int(input('请输入你本次抓娃娃需要多少秒(1~60)'))
						if num > 30:
							print('时间到了，机器自动给你抓了')
						#continue
						print('你本次用了%d秒抓了一下'%num)
						continue

				# 银行取款系统
				if denglu_zhuce == 5:
					yname = input('请输入你的姓名')
					account = input('输入帐号')
					a = 1  # 取一个值
					while a <= 3:
						password = input('输入密码')
						if password == '******':
							need = input('输入取款金额')
							yuan = 600000  # 总金额
							shouxufei = int(need) * 0.001    # 手续费
							yue = int(yuan)-int(need)-int(shouxufei) # 余额
							print('姓名:%s \n卡号:%s \n原有金额:%s \n取款:%s \n手续费:%s \n余额:%s'%(yname,account,yuan,need,shouxufei,yue))
							break
						elif password != '123456':
							print('对不起您的密码有误，请重新输入')
							i +=1
							continue

				if denglu_zhuce == 6:
					print('您已返回上级指令,请登录或是注册')	
					break







        # 调用函数
			else:
				print('密码错误')
	if denglu_zhuce == 1:
		denglu()
	elif denglu_zhuce == 2:
		zhuce()
	elif denglu_zhuce == 3:
		print('欢迎再来')
		break
