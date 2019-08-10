import allure
import pytest

from page.buy_goods import BuyGoods

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
class TestBuyGoods:
    @allure.step(title='普通购物')
    def test_buy_goods(self,open_mobile):
        """测试购买商品"""
        buy=BuyGoods(open_mobile)
        # 进入个人中心
        allure.attach('个人中心', '进入个人中心')
        buy.my()
        # 我的余额
        my_old_money = buy.my_old_money()
        allure.attach('我的余额(购买前的)', f'购买前的余额:{my_old_money}')
        # 首页
        allure.attach('首页', '进入首页')
        buy.home_page()
        # 商品分类
        allure.attach('商品分类', '进入商品分类')
        buy.goods_class()
        # 点击电脑分类
        allure.attach('电脑分类', '点击电脑分类')
        buy.computer_class()
        # 点击笔记本分类
        allure.attach('笔记本分类', '点击笔记本分类')
        buy.notebook()
        # #点击笔记本
        allure.attach('笔记本', '随机选择一款笔记本')
        buy.select_notebook_goods()
        # 立即购买
        allure.attach('立即购买', '点击立即购买')
        buy.buy_button()
        # 确定
        allure.attach('确定', '点击确定(确定商品的数量和型号)')
        buy.confirm_button()
        # # 使用积分
        # buy.integral()
        # 使用余额
        allure.attach('余额', '使用余额')
        buy.balance()
        # 获取订单金额
        order_money = buy.order_money()
        allure.attach('订单金额', f'订单金额:{order_money}')
        # 提交订单
        allure.attach('提交订单', '点击提交订单')
        buy.submit()
        # 输入支付密码
        allure.attach('支付密码', '输入支付密码')
        buy.order_password()
        # 点击确定
        allure.attach('确定密码', '点击确定密码')
        buy.sure_button()
        # 后退
        buy.back()
        # 再次进入个人中心获取余额
        # 进入个人中心
        allure.attach('再次进入个人中心', '再次进入个人中心')
        buy.my_again()
        # 购买后的余额
        my_new_money = buy.my_new_money()
        allure.attach('购买后的余额', f'购买后的余额:{my_new_money}')
        #关闭手机
        open_mobile.quit()

        allure.attach('断言', f'购买前的余额:{my_old_money}-订单金额{order_money}=购买后的余额{my_new_money}')
        # 原来的余额减去订单金额等于现在的金额
        if (my_old_money - order_money) == my_new_money:
            assert 1
        else:
            print("有BUG了")

if __name__ == '__main__':
    pytest.main("-r test_buy_goods.py")
