import time
from common.base import Base





class BuyFavorableGoods(Base):
    """封装表现层"""
    my_loc = ("xpath", "//*[@text='我的']")  # 我的余额(个人中心)
    my_money_loc = ("id","com.tpshop.malls:id/balance_tv")  # 余额(个人中心)
    home_loc = ("xpath", "//*[@text='首页']")  # 首页
    promotion_loc = ("xpath", "//*[@text='商品促销']")#商品促销
    select_goods_loc = ("id", "com.tpshop.malls:id/product_pic_img")  #选择商品
    buy_button_loc = ("id", "com.tpshop.malls:id/promptly_buy_tv")  # 立即购买按钮
    confirm_button_loc = ("xpath", "//*[@text='确定']") # 确定数量按钮
    buyer_message_loc=("xpath", "//*[@text='(选填)请对本次交易说明']")#买家留言
    input_content_loc = ("id", "com.tpshop.malls:id/value_et")  # 留言内容
    message_button_loc = ("id", "com.tpshop.malls:id/ok_btn")  # 确定留言按钮
    integral_loc = ("id", "com.tpshop.malls:id/order_point_sth")  # 使用积分
    balance_loc = ("id", "com.tpshop.malls:id/order_balance_sth")  # 使用余额
    order_money_loc=("id","com.tpshop.malls:id/balance_fee_tv")#获取余额
    submit_loc = ("xpath", "//*[@text='提交订单']")  # 提交订单按钮
    order_password_loc = ("id", "com.tpshop.malls:id/pwd_et")  # 输入支付密码
    sure_button_loc = ("xpath", "//*[@text='确定']")  # 支付密码确定按钮
    order_num_loc = ("id", "com.tpshop.malls:id/order_sn_tv")  # 订单号


    """封装操作层"""
    def my (self):
        """进入个人中心"""
        self.click(self.my_loc)
    def my_old_money(self):
        """获取我的余额"""
        my_element=self.find_element(self.my_money_loc)
        my_money_1=my_element.get_attribute("text")
        my_money=float(my_money_1)
        return  my_money
    def home_page(self):
        """点击首页"""
        self.click(self.home_loc)
    def goods_promotion(self):
        """点击商品促销"""
        self.click(self.promotion_loc)
    def select_goods(self):
        """点击商品"""
        elements=self.find_elements(self.select_goods_loc)
        # 随机索引
        index = self.random_index()
        elements[index].click()

    def buy_button(self):
        """立即购买"""
        self.click(self.buy_button_loc)
    def confirm_button(self):
        """点击确定按钮"""
        self.click(self.confirm_button_loc)
        time.sleep(2)
        # 如果买过一次限购商品(就不能在购买了),就返回到商品列表随机选择商品
        try:
            text = self.all_toast("每人限购")
            if text:
                self.browser_back()
                self.browser_back()
                self.select_goods()
                self.buy_button()
                self.confirm_button()
            else:
                print("继续执行")
        except:
              print("继续执行")

    def integral(self):
        """点击使用积分"""
        self.click(self.integral_loc)
    def balance(self):
        """点击使用余额"""
        self.click(self.balance_loc)
    def order_money(self):
        """获取订单金额"""
        element=self.find_element(self.order_money_loc)
        order_money=element.get_attribute("text")
        money=order_money[1:]
        money=float(money)
        return money
    def submit(self):
        """点击提交订单按钮"""
        self.click(self.submit_loc)
    def order_password(self):
        """输入支付密码"""
        self.send_keys(self.order_password_loc,text=123456)
    def sure_button(self):
        """点击支付密码确定按钮"""
        self.click(self.sure_button_loc)
    def back(self):
        self.browser_back()
        self.browser_back()
        self.browser_back()
        self.browser_back()
    def my_again (self):
        """再次进入个人中心"""
        self.click(self.my_loc)
    def my_new_money(self):
        """获取我的余额"""
        self.click(self.my_money_loc)
        my_element=self.find_element(self.my_money_loc)
        my_money_2=my_element.get_attribute("text")
        my_money=float(my_money_2)
        return  my_money

if __name__ == '__main__':
    driver = open_mobile()
    buy = BuyFavorableGoods(driver)
    # 进入个人中心
    buy.my()
    # 我的余额
    my_old_money = buy.my_old_money()
    # 首页
    buy.home_page()
    # 商品促销
    buy.goods_promotion()
    # 樱桃
    buy.cherry_fruit()
    # 立即购买
    buy.buy_button()
    time.sleep(2)
    # 确定
    buy.confirm_button()
    # # 使用积分
    # buy.integral()
    # 使用余额
    buy.balance()
    # 获取订单金额
    order_money = buy.order_money()
    # 提交订单
    buy.submit()
    # 输入支付密码
    buy.order_password()
    # 点击确定
    buy.sure_button()
    # 后退
    buy.back()
    # 再次进入个人中心获取余额
    # 进入个人中心
    buy.my_again()
    # 我的余额
    my_new_money = buy.my_new_money()
