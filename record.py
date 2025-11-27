# 收支记录功能模块
def add_record(amount, type, category, date, note):
    """
    添加收支记录
    :param amount: 金额（数值型）
    :param type: 类型（收入/支出）
    :param category: 类别（如餐饮、工资、兼职等）
    :param date: 日期（格式：YYYY-MM-DD）
    :param note: 备注信息
    :return: 记录字典
    """
    record = {
        "amount": amount,
        "type": type,
        "category": category,
        "date": date,
        "note": note
    }
    print(f"✅ 收支记录添加成功：{record}")
    return record

# 测试代码
if __name__ == "__main__":
    add_record(200, "收入", "兼职", "2025-11-27", "家教课时费")
