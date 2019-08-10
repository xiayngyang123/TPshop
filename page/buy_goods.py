
from common.base import Base,open_mobile



class BuyGoods(Base):
    """封装表现层"""
    my_loc = ("xpath", "//*[@text='我的']")  # 我的余额(个人中心)
    my_money_loc = ("id", "com.tpshop.malls:id/balance_tv")  # 余额(个人中心)
    home_loc = ("xpath", "//*[@text='首页']")  # 首页
    goods_class_loc = ("xpath", "//*[@text='分类']")#商品分类
    computer_class_loc = ("xpath", "//*[@text='电脑']")  #电脑分类
    notebook_loc = ("xpath", "//*[@text='笔记本']")  # 笔记本分类
    select_notebook_loc=("id","com.tpshop.malls:id/product_pic_img")#选择一个笔记本电脑
    buy_button_loc = ("id", "com.tpshop.malls:id/promptly_buy_tv")  # 立即购买按钮
    goods_num_loc=("id","com.tpshop.malls:id/product_spec_store_count_tv")#商品库存
    add_button_loc = ("id", "com.tpshop.malls:id/cart_plus_btn") #增加数量按钮
    confirm_button_loc = ("xpath", "//*[@text='确定']") # 确定数量按钮
    buyer_message_loc=("xpath", "//*[@text='(选填)请对本次交易说明']")#买家留言
    input_content_loc = ("id", "com.tpshop.malls:id/value_et")  # 留言内容
    message_button_loc = ("id", "com.tpshop.malls:id/ok_btn")  # 确定留言按钮
    integral_loc = ("id", "com.tpshop.malls:id/order_point_sth")  # 使用积分
    balance_loc = ("id", "com.tpshop.malls:id/order_balance_sth")  # 使用余额
    order_money_loc = ("id", "com.tpshop.malls:id/balance_fee_tv")  # 获取余额
    submit_loc = ("xpath", "//*[@text='提交订单']")  # 提交订单按钮
    order_password_loc = ("id", "com.tpshop.malls:id/pwd_et")  # 输入支付密码
    sure_button_loc = ("xpath", "//*[@text='确定']")  # 支付密码确定按钮
    order_num_loc = ("id", "com.tpshop.malls:id/order_sn_tv")  # 订单号
    my_balance_loc=("id", "com.tpshop.malls:id/balance_tv")#我的余额(个人中心)

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

    def goods_class(self):
        """点击商品分类"""
        self.click(self.goods_class_loc)

    def computer_class(self):
        """点击电脑分类"""
        self.click(self.computer_class_loc)

    def notebook(self):
         """点击笔记本分类"""
         self.click(self.notebook_loc)

    def select_notebook_goods(self):
        """选择一个笔记本"""
        elements=self.find_elements(self.select_notebook_loc)
        #随机索引
        index=self.random_index()
        elements[index].click()
    def buy_button(self):
        """立即购买"""
        self.click(self.buy_button_loc)

    def confirm_button(self):
        """点击确定按钮"""
        self.click(self.confirm_button_loc)

    def integral(self):
        """点击使用积分"""
        self.click(self.integral_loc)

    def balance(self):
        """点击使用余额"""
        self.click(self.balance_loc)

    def order_money(self):
        """获取订单金额"""
        element = self.find_element(self.order_money_loc)
        order_money = element.get_attribute("text")
        money = order_money[1:]
        money = float(money)
        return money

    def submit(self):
        """点击提交订单按钮"""
        self.click(self.submit_loc)

    def order_password(self):
        """输入支付密码"""
        self.send_keys(self.order_password_loc, text=123456)

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

    driver =open_mobile()
    buy = BuyGoods(driver)
    # 首页
    buy.home_page()
    #商品分类
    buy.goods_class()
    # 点击电脑分类
    buy.computer_class()
    # 点击笔记本分类
    buy.notebook()
    # #点击笔记本
    buy.select_notebook_goods()
    # 立即购买
    buy.buy_button()
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

