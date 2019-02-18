import datetime



# 计算两个日期之间的工作日数,非天数.
class WorkDays():

    l = ["2019-02-04", "2019-02-05", "2019-02-06", "2019-02-07", "2019-02-08"]

    def __init__(self, start_date, end_date, days_off=None):
        """days_off:休息日,默认周六日, 以0(星期一)开始,到6(星期天)结束, 传入tupple
        没有包含法定节假日,
        """
        self.start_date = start_date
        self.end_date = end_date
        self.days_off = days_off
        if self.start_date > self.end_date:
            self.start_date, self.end_date = self.end_date, self.start_date
        if days_off is None:
            self.days_off = 5, 6
        # 每周工作日列表
        self.days_work = [x for x in range(7) if x not in self.days_off]

    def workDays(self):
        """实现工作日的 iter, 从start_date 到 end_date , 如果在工作日内,yield 日期
        """
        # 还没排除法定节假日
        tag_date = self.start_date
        while True:
            if tag_date > self.end_date:
                break
            if tag_date.weekday() in self.days_work:
                if str(tag_date) not in self.l:
                    # print(tag_date)
                    yield tag_date
            tag_date += datetime.timedelta(days=1)

    def daysCount(self):
        """工作日统计,返回数字"""
        return len(list(self.workDays()))