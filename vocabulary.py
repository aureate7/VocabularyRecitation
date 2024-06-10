import difflib
import random

# 词汇数据
vocab = {
    "Marine Insurance": "海运保险",
    "Free on Board (FOB)": "装运港船上交货",
    "Negotiable / Non-negotiable B/L": "可转让/不可转让提单",
    "Sales Confirmation": "销售确认书",
    "Delivery Time": "交货时间",
    "Terms of Payment": "付款条件",
    "Non-firm Offer": "虚盘",
    "Insurance Policy": "保险单",
    "Board of Directors": "董事会",
    "Memos and Minutes": "备忘录和会议记录",
    "Letter of Credit at Sight": "即期信用证",
    "Patent Agreement": "专利协议",
    "Non-fulfillment of Contract": "合同不履行",
    "All Risks": "一切险",
    "Failure in Entering into Contract": "不能签订合同",
    "Ocean B/L": "海运提单",
    "Negotiating Bank": "议付银行",
    "Clean Collection": "跟单托收",
    "Counter-offer": "还盘",
    "Counter-bid": "还价",
    "Current/Prevailing Price": "现价",
    "Durable Goods/Durables": "耐用品",
    "Fancy Goods": "花俏商品",
    "Gross Price": "毛价，总价",
    "Lead Time": "从订货到交货的间隔时间",
    "Offer Sheet": "报盘单",
    "Quotation Sheet": "报价单",
    "Retail Price": "零售价",
    "Rock-bottom Price": "最底价",
    "Make an Offer / a Quotation": "报盘/报价",
    "Offer Firm": "报实盘",
    "Quote a Price": "报价",
    "Credit Status": "资信状况",
    "Correspondent Bank": "往来行",
    "Publicity Brochure": "宣传小册子",
    "Down Payment": "预定金",
    "Find a Ready Sale/Market for": "畅销",
    "End-user": "最终用户",
    "Ex Works (EXW)": "工厂交货（价）",
    "Cost & Freight (CFR)": "成本加运费",
    "Cost, Insurance and Freight (CIF)": "成本加保险费运费",
    "Carriage & Insurance Paid to (CIP)": "运费保险费付至…",
    "Carriage Paid to (CPT)": "运费付至…",
    "Delivered At Frontier (DAF)": "边境交货",
    "Delivered Duty Paid (DDP)": "完税后交货",
    "Delivered Duty Unpaid (DDU)": "未完税交货",
    "Delivered Ex Quay (DEQ)": "目的港码头交货",
    "Delivered Ex Ship (DES)": "目的港船上交货",
    "Free Alongside Ship (FAS)": "船边交货",
    "Free Carrier (FCA)": "货交承运人",
    "Import License (I/L)": "进口许可证",
    "Mode of Payment": "付款方式",
    "Proforma Invoice (P/I)": "形式发票",
    "Prompt Shipment": "即期装运",
    "Regular Purchase": "定期购货",
    "Repeat Order": "重复订单，翻单",
    "Sales Contract (S/C)": "销售合同",
    "Trial Order": "试销订单",
    "Accept an Order": "接受订单/订货",
    "Acknowledge an Order": "（卖方）确认订单",
    "Arrive at / Come to an Agreement": "达成协议",
    "Book an Order": "接受订单/货",
    "Cancel an Order": "撤销订单/货",
    "Complete an Order": "处理订单，备货",
    "Confirm an Order": "（买方）确认订单",
    "Decline an Order": "谢绝订单",
    "Deliver an Order": "交付订货",
    "Draft a Contract": "起草合同",
    "Obtain Indemnity": "获得赔偿",
    "A Cover Note": "承保单",
    "A Marine Policy": "海洋运输保单",
    "A Floating Policy": "全额保单",
    "An Open Policy": "预约保单",
    "A Valued Policy": "定值保单",
    "Declaration Form": "启运通知书",
    "A Claims Form": "索赔申请书/表",
    "ETA (Estimated Time of Arrival)": "估计到达时间",
    "ETD (Estimated Time of Departure)": "估计离开时间",
    "Secure the Vessel": "弄到船只",
    "Cargo Capacity": "载货能力",
    "Charter Party": "租船合同",
    "Air Waybill": "空运提单",
    "Carrying Vessel": "运货船",
    "Direct Steamer": "直达船",
    "Dock Receipt": "码头收据",
    "Document of Title": "产权单证",
    "Freight Prepaid": "运费已付",
    "Freight to Collect": "运费到付",
    "General Cargo Vessel": "杂货船",
    "Negotiable Instrument": "可流通/转让票据",
    "Dispatch Money": "速遣费，快装费",
    "Freight Ton": "运费吨",
    "Measurement Ton": "尺码吨",
    "Weight Ton": "重量吨",
    "Weight Memo": "重量单",
    "Ocean Transportation": "海洋运输",
    "Full Container Load (FCL)": "整箱货",
    "Less than Container Load (LCL)": "拼箱货",
    "Bill of Lading (B/L)": "海运提单",
    "Top stow cargo": "堆顶货",
    "Total deadweight (TDW)": "总载重量",
    "Tracer": "(货物)查询单",
    "Tractor": "牵引车",
    "Trading limits": "航行范围",
    "Trailer": "拖车",
    "Transfer (equipment handover) charge": "设备租用费",
    "Transship (trans-ship)": "转船",
    "Transhipment (transshipment, trans-shipment)": "转船",
    "Transit cargo": "过境货物",
    "Transporter crane": "轨道式起重机",
    "Tray": "货盘",
    "Trim": "平舱",
    "Trim a ship": "调整船舶吃水",
    "Tug": "拖轮",
    "Turn round (around, or turnaround) time": "船舶周转时间",
    "Turn time": "等泊时间",
    "Tween deck": "二层甲板",
    "Twin hatch vessel": "双舱口船",
    "Two-way pallet": "两边开槽托盘",
    "Ultra large crude carrier (ULCC)": "超大型油轮",
    "Uncontainerable (uncontainerisable) cargo": "不适箱货",
    "Under deck shipment": "货舱运输",
    "Unit load": "成组运输",
    "Unitisation": "成组化",
    "Universal bulk carrier (UBC)": "通用散装货船",
    "Unload": "卸货",
    "Unmoor": "解揽",
    "Unseaworthiness": "不适航",
    "Utilization": "整箱货",
    "Valuation form": "货价单",
    "Valuation scale": "货价表",
    "Vehicle /train ferry": "汽车/火车渡轮",
    "Ventilated container": "通风集装箱",
    "Ventilation": "通风",
    "Ventilator": "通风器",
    "Vessel": "船舶，船方",
    "Vessel sharing agreement (V.S.A.)": "船舶共用协议",
    "Void filler": "填充物",
    "Voyage account": "航次报表",
    "Voyage (trip) charter": "航次租船",
    "Waybill": "货运单",
    "Weather permitting (w.p)": "天气允许",
    "Weather working day": "晴天工作日",
    "Weather-bound": "天气阻挠",
    "With effect from (w.e.f)": "自生效",
    "Weight cargo": "重量货",
    "Weight or measure (measurement) (W/M)": "重量/体积",
    "Weight rated cargo": "计重货物",
    "Well": "货井，井区",
    "Wharf": "码头",
    "Wharfage (charges)": "码头费",
    "When where ready on completion of discharge (w.w. r c.d.)": "何时何处还船",
    "Whether in berth or not (w.i.b.o.n.)": "无论靠泊与否",
    "Whether in free pratique or not (w.i.f.p.o.n.)": "无论是否通过检验",
    "Whether in port or not (w.i.p.o.n.)": "不论是否在港内",
    "White (clean, clean petroleum) products": "精炼油",
    "Wide laycan": "长销约期",
    "Workable (working) hatch": "可工作舱口",
    "Working day": "工作日",
    "Working day of 24 consecutive hours": "连续24小时工作日",
    "Working day of 24 hours": "24小时工作日",
    "Working time saved (w.t.s.)": "节省的装卸时间",
    "Yard (shipyard)": "造船厂",
    "International Civil Aviation Organization (ICAO)": "国际民用航空组织",
    "International Air Transport Association (IATA)": "国际航空运输协会",
    "Scheduled Airline": "定期航班",
    "Booking number": "订舱号码",
    "Vessel": "船名",
    "Voyage": "航次",
    "CY Closing DATE": "截柜日期，截关日",
    "Closing Date/Time": "截柜日期",
    "SI CUT OFF date/time": "截提单补料日期/时间",
    "Expiry date": "有效期限，到期日期",
    "Sailing date": "航行日期 / 船离开港口的日期",
    "ETA (ESTIMATED TIME OF ARRIVAL)": "预计到达时间，到港日",
    "ETD (ESTIMATED TIME OF DELIVERY)": "开船日",
    "ETC (ESTIMATED TIME OF CLOSING)": "截关日",
    "Port of loading (POL)": "装货港",
    "Loading port": "装货港",
    "From City": "起运地",
    "EXP (export)": "出口",
    "Final destination": "目的港，最终目的地",
    "Place of Delivery (POD) or To City": "目的地，交货地",
    "Port of discharge": "卸货港",
    "Discharge port": "卸货港",
    "Load Port": "装货港",
    "Dry": "干的/不含液体或湿气",
    "Quantity": "数量",
    "Cargo type": "货物种类",
    "Container number": "集装箱号码",
    "Container": "集装箱",
    "Specific cargo container": "特种货物集装箱",
    "Number of container": "货柜数量",
    "Container Size": "货柜尺寸",
    "CU.FT": "立方英尺",
    "Cont Status": "货柜状况",
    "Seal number": "封条号码",
    "Seal No": "封条号码",
    "Seal type": "封条类型",
    "Weight": "重量",
    "Gross weight": "总重（一般是含柜重和货重）",
    "Net Weight": "净重",
    "Actual weight": "实际重量，货车，集装箱等运输工具装载后的总重量",
    "International Civil Aviation Organization (ICAO)": "国际民用航空组织",
    "International Air Transport Association (IATA)": "国际航空运输协会",
    "Scheduled Airline": "定期航班",
    "Chartered Carrier": "包机运输",
    "Consolidation": "集中托运",
    "Air Express": "航空快递",
    "Air Waybill": "航空运单",
    "Master Air Waybill (MAWB)": "航空主运单",
    "House Air Waybill (HAWB)": "航空分运单",
    "Chargeable Weight": "计费重量",
    "High density cargo": "重货",
    "Low density cargo": "轻货",
    "Specific Commodity Rates (SCR)": "特种货物运价",
    "Commodity Classification Rates (CCR)": "等价货物运价",
    "General Cargo Rates (GCR)": "普通货物运价",
    "Unit Load Devices (ULD)": "集装设备",
    "Construction Rate": "比例运价",
    "Combination of Rate": "分段相加运价",
    "Valuation Charges": "声明价值费",
    "Declared value for Carriage": "运输声明价值",
    "No Value Declared (NVD)": "不要求声明价值",
    "Declared Value for Customs": "海关声明价值",
    "No customs valuation (NCV)": "无声明价值",
    "Railway transportation": "铁路运输",
    "Railway transport administration": "铁路运输管理",
    "Railway operation": "铁路运营",
    "Railway traffic organization": "铁路运输组织",
    "Quality control of railway transportation": "铁路运输质量管理",
    "Regulations for railway passenger traffic": "铁路旅客运输规程",
    "Regulations for railway freight traffic": "铁路货物运输规程",
    "Railway heavy haul traffic": "铁路重载运输",
    "Railway high speed traffic": "铁路高速运输",
    "Insured rail traffic": "铁路保险运输",
    "Value insured rail traffic": "铁路保价运输",
    "Railway military service": "铁路军事运输",
    "Railway passenger traffic": "铁路旅客运输",
    "Railway passenger traffic organization": "铁路客运组织",
    "Luggage": "行李",
    "Parcel": "包裹",
    "Public hall": "广厅",
    "Luggage office": "行李房",
    "Booking office": "售票处",
    "Waiting room": "候车室",
    "Overhead waiting hall": "高架火车厅",
    "Information office": "问讯处",
    "Passenger flow": "客流",
    "Through passenger flow": "直通客流",
    "Local passenger flow": "管内客流",
    "Suburban passenger flow": "市郊客流",
    "Passenger flow volume": "客流量",
    "Passenger flow investigation": "客流调查",
    "Passenger flow diagram": "客流图",
    "Number of passenger despatched": "旅客发送人数",
    "Number of passengers arrived": "旅客到达人数",
    "Number of passengers transported": "旅客运送人数",
    "Maximum number of passengers in peak hours": "旅客最高聚集人数",
    "Ticket": "车票",
    "Passenger ticket": "客票",
    "Fast extra ticket": "加快票",
    "Express extra ticket": "特快加快票",
    "Berth ticket": "卧铺票",
    "Platform ticket": "站台票",
    "Reduced-fare ticket": "减价票",
    "Student ticket": "学生票",
    "Child ticket": "小孩票",
    "Disabled army man ticket": "残废军人票",
    "Passenger ticket for international through traffic": "国际联运旅客车票",
    "Top stow cargo": "堆顶货",
    "Total deadweight (TDW)": "总载重量",
    "Tracer": "(货物)查询单",
    "Tractor": "牵引车",
    "Trading limits": "航行范围",
    "Trailer": "拖车",
    "Transfer (equipment handover) charge": "设备租用费",
    "Transship (trans-ship)": "转船",
    "Transhipment (transshipment, trans-shipment)": "转船",
    "Transit cargo": "过境货物",
    "Transporter crane": "轨道式起重机",
    "Tray": "货盘",
    "Trim": "平舱",
    "Trim a ship": "调整船舶吃水",
    "Tug": "拖轮",
    "Turn round (around, or turnaround) time": "船舶周转时间",
    "Turn time": "等泊时间",
    "Tween deck": "二层甲板",
    "Twin hatch vessel": "双舱口船",
    "Two-way pallet": "两边开槽托盘",
    "Ultra large crude carrier (ULCC)": "超大型油轮",
    "Uncontainerable (uncontainerisable) cargo": "不适箱货",
    "Under deck shipment": "货舱运输",
    "Unit load": "成组运输",
    "Unitisation": "成组化",
    "Universal bulk carrier (UBC)": "通用散装货船",
    "Unload": "卸货",
    "Unmoor": "解揽",
    "Unseaworthiness": "不适航",
    "Utilization": "整箱货",
    "Valuation form": "货价单",
    "Valuation scale": "货价表",
    "Vehicle /train ferry": "汽车/火车渡轮",
    "Ventilated container": "通风集装箱",
    "Ventilation": "通风",
    "Ventilator": "通风器",
    "Vessel": "船舶，船方",
    "Vessel sharing agreement (V.S.A.)": "船舶共用协议",
    "Void filler": "填充物",
    "Voyage account": "航次报表",
    "Voyage (trip) charter": "航次租船",
    "Waybill": "货运单",
    "Weather permitting (w.p)": "天气允许",
    "Weather working day": "晴天工作日",
    "Weather-bound": "天气阻挠",
    "With effect from (w.e.f)": "自生效",
    "Weight cargo": "重量货",
    "Weight or measure (measurement) (W/M)": "重量/体积",
    "Weight rated cargo": "计重货物",
    "Well": "货井，井区",
    "Wharf": "码头",
    "Wharfage (charges)": "码头费",
    "When where ready on completion of discharge (w.w. r c.d.)": "何时何处还船",
    "Whether in berth or not (w.i.b.o.n.)": "无论靠泊与否",
    "Whether in free pratique or not (w.i.f.p.o.n.)": "无论是否通过检验",
    "Whether in port or not (w.i.p.o.n.)": "不论是否在港内",
    "White (clean, clean petroleum) products": "精炼油",
    "Wide laycan": "长销约期",
    "Workable (working) hatch": "可工作舱口",
    "Working day": "工作日",
    "Working day of 24 consecutive hours": "连续24小时工作日",
    "Working day of 24 hours": "24小时工作日",
    "Working time saved (w.t.s.)": "节省的装卸时间",
    "Yard (shipyard)": "造船厂",
    "International Civil Aviation Organization (ICAO)": "国际民用航空组织",
    "International Air Transport Association (IATA)": "国际航空运输协会",
    "Scheduled Airline": "定期航班",
    "Goods": "商品",
    "Freight": "货运,货物",
    "Cargo": "货物，船货",
    "Transportation": "运输",
    "Transit": "运输",
    "Conveyance": "运输",
    "To transport": "运送",
    "To carry": "运送",
    "To convey": "运送",
    "Transportation business": "运输业",
    "Forwarding business": "运输业",
    "Carrying trade": "运输业",
    "A forwarding agent": "运输代理人",
    "A freight agent": "承运人",
    "A carrier": "承运人",
    "A shipping agent": "船务代理人",
    "Transportation by land": "陆上运输",
    "Transportation by sea": "海上运输",
    "Goods traffic": "货物运输",
    "Freight traffic": "货物运输",
    "Carriage of freights": "货物运输",
    "Carriage of goods": "货物运输",
    "Cargo boat": "货轮",
    "Freighter": "货轮",
    "Cargo steamer": "货轮",
    "Cargo carrier": "货轮",
    "Goods-train": "火车",
    "Freight-train": "火车",
    "Goods-van": "卡车",
    "Goods wagon": "卡车",
    "Freight car": "卡车",
    "Truck": "卡车",
    "Goods-office": "货运办公室",
    "Freight-department": "货运办公室",
    "Freight": "运费率",
    "Freight rates": "运费率",
    "Goods rate": "运费率",
    "Carriage charges": "运费",
    "Shipping expenses": "运费",
    "Express charges": "运费",
    "Cartage": "车费",
    "Portage": "车费",
    "Carriage prepaid": "运费预付",
    "Carriage paid": "运费预付",
    "Carriage forward": "运费到付",
    "Freight collect": "运费到付",
    "Carriage free": "运费免除",
    "Conference freight": "协定运费",
    "Freight rate": "协定运费",
    "Freight account": "运费清单"
}

# vocab = {
#     "Marine Insurance": "海运保险",
#     "Free on Board (FOB)": "装运港船上交货",
#     "Negotiable / Non-negotiable B/L": "可转让/不可转让提单",
#     "Sales Confirmation": "销售确认书",
#     "Delivery Time": "交货时间"
# }

def is_similar(answer, correct_answer, threshold=0.6):
    return difflib.SequenceMatcher(None, answer, correct_answer).ratio() > threshold

def check_answer(answer, correct_answers):
    for correct_answer in correct_answers:
        if is_similar(answer, correct_answer):
            return True
    return False

def quiz(vocab, mode, correct_words):
    correct_count = len(correct_words)
    total_words = len(vocab)
    vocab_items = list(vocab.items())
    wrong_items = []
    count = 0

    while vocab_items:
        english, chinese = random.choice(vocab_items)
        if english in correct_words:
            vocab_items.remove((english, chinese))
            continue

        correct_answers = [ans.strip() for ans in chinese.split('/')]

        if mode == 1:
            if random.choice([True, False]):
                # 给出英文，要求用户输入中文
                answer = input(f"请翻译成中文: {english} (输入-1提前结束, 输入0重置词典)\n")
                if answer == '-1':
                    print("结束游戏。")
                    return correct_words, wrong_items, count, True
                elif answer == '0':
                    print("重置词典。")
                    return set(), [], 0, False
                print(f"标准答案是: {chinese}")
                count += 1
                if check_answer(answer, correct_answers):
                    print("正确!")
                    correct_count += 1
                    correct_words.add(english)
                else:
                    print(f"错误")
                    wrong_items.append((english, chinese))
            else:
                # 给出中文，要求用户输入英文
                answer = input(f"请翻译成英文: {chinese} (输入-1提前结束, 输入0重置词典)\n")
                if answer == '-1':
                    print("结束游戏。")
                    return correct_words, wrong_items, count, True
                elif answer == '0':
                    print("重置词典。")
                    return set(), [], 0, False
                print(f"标准答案是: {english}")
                count += 1
                if answer.strip().lower() == english.lower():
                    print("正确!")
                    correct_count += 1
                    correct_words.add(english)
                else:
                    print(f"错误")
                    wrong_items.append((chinese, english))

        elif mode == 2:
            # 给出英文，要求用户输入中文
            answer = input(f"请翻译成中文: {english} (输入-1提前结束, 输入0重置词典)\n")
            if answer == '-1':
                print("结束游戏。")
                return correct_words, wrong_items, count, True
            elif answer == '0':
                print("重置词典。")
                return set(), [], 0, False
            print(f"标准答案是: {chinese}")
            count += 1
            if check_answer(answer, correct_answers):
                print("正确!")
                correct_count += 1
                correct_words.add(english)
            else:
                print(f"错误")
                wrong_items.append((english, chinese))

        elif mode == 3:
            # 给出中文，要求用户输入英文
            answer = input(f"请翻译成英文: {chinese} (输入-1提前结束, 输入0重置词典)\n")
            if answer == '-1':
                print("结束游戏。")
                return correct_words, wrong_items, count, True
            elif answer == '0':
                print("重置词典。")
                return set(), [], 0, False
            print(f"标准答案是: {english}")
            count += 1
            if answer.strip().lower() == english.lower():
                print("正确!")
                correct_count += 1
                correct_words.add(english)
            else:
                print(f"错误")
                wrong_items.append((chinese, english))

        elif mode == 4:
            # 选择模式
            if random.choice([True, False]):
                # 给出英文，选择中文
                options = [chinese]
                while len(options) < 4:
                    option = random.choice(list(vocab.values()))
                    if option not in options:
                        options.append(option)
                random.shuffle(options)
                print(f"请为以下英文选择正确的中文翻译: {english} (输入-1提前结束, 输入0重置词典)")
                for i, option in enumerate(options):
                    print(f"{i + 1}. {option}")
                answer = input("请选择正确的选项（输入数字）：")
                if answer == '-1':
                    print("结束游戏。")
                    return correct_words, wrong_items, count, True
                elif answer == '0':
                    print("重置词典。")
                    return set(), [], 0, False
                correct_option = options.index(chinese) + 1
                print(f"标准答案是: {correct_option}. {chinese}")
                count += 1
                if answer.isdigit() and int(answer) == correct_option:
                    print("正确!")
                    correct_count += 1
                    correct_words.add(english)
                else:
                    print("错误")
                    wrong_items.append((english, chinese))
            else:
                # 给出中文，选择英文
                options = [english]
                while len(options) < 4:
                    option = random.choice(list(vocab.keys()))
                    if option not in options:
                        options.append(option)
                random.shuffle(options)
                print(f"请为以下中文选择正确的英文翻译: {chinese} (输入-1提前结束, 输入0重置词典)")
                for i, option in enumerate(options):
                    print(f"{i + 1}. {option}")
                answer = input("请选择正确的选项（输入数字）：")
                if answer == '-1':
                    print("结束游戏。")
                    return correct_words, wrong_items, count, True
                elif answer == '0':
                    print("重置词典。")
                    return set(), [], 0, False
                correct_option = options.index(english) + 1
                print(f"标准答案是: {correct_option}. {english}")
                count += 1
                if answer.isdigit() and int(answer) == correct_option:
                    print("正确!")
                    correct_count += 1
                    correct_words.add(english)
                else:
                    print("错误")
                    wrong_items.append((chinese, english))

        vocab_items.remove((english, chinese))
        print(f"目前正确率: {correct_count}/{count} ({(correct_count / count) * 100:.2f}%)")
        print(f"进度: {count}/{total_words}")

        if count == total_words:
            break

    return correct_words, wrong_items, count, False

if __name__ == "__main__":
    correct_words = set()
    wrong_items = []
    count = 0
    while True:
        mode = input("请选择模式: 1 (随机), 2 (英文翻译为中文), 3 (中文翻译为英文), 4 (选择模式): ").strip()
        if mode in ['1', '2', '3', '4']:
            correct_words, wrong_items, count, exit_game = quiz(vocab, int(mode), correct_words)
            if count != 0:
                print(f"\n最终正确率: {len(correct_words)}/{count} ({(len(correct_words) / count) * 100:.2f}%)")
            if wrong_items:
                print("\n错题列表:")
                for item in wrong_items:
                    print(f"{item[0]} - {item[1]}")
            if exit_game:
                break
        else:
            print("无效的模式，请重新选择。")

